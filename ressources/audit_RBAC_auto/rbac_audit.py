#!/usr/bin/env python3
"""
Script Python : Audit RBAC simplifié
- Vérifie les accès par rapport à une matrice RBAC (CSV).
- Génère un rapport des anomalies (CSV).

Intégration SIEM : non implémentée dans ce script (aucune dépendance
externe) - voir la section « Intégration SIEM » du README.
"""

# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Solène Figueiredo

import csv
import unicodedata
from datetime import datetime

# --- CONFIGURATION ---
RBAC_MATRIX_FILE = "MatriceRBAC.csv"
USERS_FILE = "users.csv"
USER_ACCESS_LOG_FILE = "user_access_log.csv"

# -----------------------------------------------------------------
# Heures d'ouverture autorisées
# Modifier ici les horaires si nécessaire.
# Format : HH:MM (24 heures)
# -----------------------------------------------------------------
BUSINESS_OPEN = "08:00"
BUSINESS_CLOSE = "18:00"

# -----------------------------------------------------------------
# Jours ouvrés (norme ISO : lundi=0 … dimanche=6)
# Un accès hors jours ouvrés déclenche le contrôle horaire.
# -----------------------------------------------------------------
WORKING_DAYS = {0, 1, 2, 3, 4}

# Libellés des jours (informationnel - messages d'anomalie)
DAY_NAMES = ["lundi", "mardi", "mercredi", "jeudi",
             "vendredi", "samedi", "dimanche"]

# -----------------------------------------------------------------
# Rôles exemptés du contrôle horaire
# Le contrôle horaire cible le personnel interne (heures de bureau).
# Sont exemptés : usage légitime à toute heure et fonctionnement 24/7.
# V2 possible : horaires par rôle + corroboration multi-signaux
# (fréquence des accès, localisation) — voir README.
# -----------------------------------------------------------------
HOUR_EXEMPT_ROLES = {
    "Patient B2C",                 # télémesure/usage à toute heure
    "Praticien B2B",                # astreintes, urgences
    "Laboratoires",                 # partenaire, flux 24/7
    "Compte de service API CHU",    # intégration continue
    "Compte de service API Stripe",  # transactions
    "OVH (Sous-traitant)",          # sauvegardes nocturnes
}

TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
REPORT_FILE = f"{TIMESTAMP}_rapport_anomalies.csv"

# --- FONCTIONS ---
def load_rbac_matrix(file_path: str) -> list:
    """
    Charge la matrice RBAC (CSV) : détection du séparateur, validation
    d'en-têtes, vocabulaire strict des permissions (L E S X A -) et du
    MFA (O/N), rejet des règles dupliquées (même Rôle/Ressources).

    Colonnes lues : ID, Rôle, Classification, Ressources, Permission
    (ou Permissions), MFA. Les autres colonnes (ex. Justification) sont
    ignorées. Vocabulaire inconnu ou structure ambiguë : arrêt
    (fail-closed) — un jeton non reconnu pourrait être interprété comme
    une autorisation, une valeur MFA imprévue désactiverait le contrôle
    sans signal, une règle dupliquée pourrait être contournée.
    """
    REQUIRED_COLUMNS = ["ID", "Rôle", "Classification", "Ressources", "MFA"]
    VALID_PERMISSIONS = {"L", "E", "S", "X", "A", "-"}
    matrix = []
    try:
        with open(file_path, mode="r", encoding="utf-8-sig") as f:
            first_line = f.readline().strip()
            f.seek(0)

            separator = "," if "," in first_line else ";"
            reader = csv.DictReader(f, delimiter=separator)

            if reader.fieldnames is None:
                raise ValueError("Fichier vide (aucun en-tête)")
            fieldnames = [field.strip() for field in reader.fieldnames]

            permission_col = None
            for candidate in ["Permission", "Permissions"]:
                if candidate in fieldnames:
                    permission_col = candidate
                    break
            if permission_col is None:
                raise ValueError(
                    f"Colonne 'Permission' introuvable. "
                    f"Colonnes disponibles : {fieldnames}"
                )
            missing = [c for c in REQUIRED_COLUMNS if c not in fieldnames]
            if missing:
                raise ValueError(
                    f"Colonne(s) obligatoire(s) absente(s) : {missing}. "
                    f"Colonnes attendues : {REQUIRED_COLUMNS} "
                    f"+ {permission_col}"
                )

            seen_rules = {}
            for line_num, row in enumerate(reader, start=2):
                if None in row or any(v is None for v in row.values()):
                    raise ValueError(
                        f"Ligne {line_num} : nombre de colonnes incorrect "
                        f"(attendu : {len(fieldnames)})"
                    )
                clean_row = {k.strip(): v.strip() for k, v in row.items()}

                permission_str = clean_row.get(permission_col, "")
                permissions = permission_str.split() if permission_str else []
                unknown = [t for t in permissions if t not in VALID_PERMISSIONS]
                if unknown:
                    raise ValueError(
                        f"Ligne {line_num} : jeton(s) de permission "
                        f"invalide(s) {unknown}. Vocabulaire autorisé : "
                        f"L E S X A - (ou - pour refus explicite)"
                    )

                mfa_value = clean_row.get("MFA", "")
                if mfa_value not in ("O", "N"):
                    raise ValueError(
                        f"Ligne {line_num} : valeur MFA invalide "
                        f"'{mfa_value}'. Vocabulaire autorisé : O/N"
                    )

                rule_key = (clean_row["Rôle"], clean_row["Ressources"])
                if rule_key in seen_rules:
                    raise ValueError(
                        f"Ligne {line_num} : règle dupliquée "
                        f"({clean_row['Rôle']} / {clean_row['Ressources']}), "
                        f"déjà définie ligne {seen_rules[rule_key]}"
                    )
                seen_rules[rule_key] = line_num

                clean_row["Permission"] = permissions
                matrix.append(clean_row)

    except FileNotFoundError:
        print(f"[ERREUR] Fichier introuvable : {file_path}. "
              f"Audit arrêté (fail-closed).")
        raise SystemExit(1)
    except Exception as e:
        print(f"[ERREUR] Lecture interrompue ({file_path}) : {e}. "
              f"Règles chargées avant l'erreur : {len(matrix)}. "
              f"Audit arrêté : une matrice partielle produirait "
              f"un rapport trompeur.")
        raise SystemExit(1)
    return matrix

def load_access_logs(file_path: str) -> list:
    """
    Charge les logs d'accès depuis un fichier CSV.
    Échec explicite (SystemExit) si le fichier est absent ou illisible :
    un audit ne s'exécute jamais sur des données incomplètes.
    """
    try:
        with open(file_path, mode="r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f, delimiter=";")
            if reader.fieldnames is None:
                raise ValueError("Fichier vide (aucun en-tête)")
            expected = ["timestamp", "user", "role", "resource",
                        "action", "mfa_enabled"]
            if [fn.strip() for fn in reader.fieldnames] != expected:
                raise ValueError(
                    f"En-tête invalide. Attendu : {expected}. "
                    f"Lu : {[fn.strip() for fn in reader.fieldnames]}"
                )
            expected_cols = len(reader.fieldnames)
            rows = []
            for line_num, row in enumerate(reader, start=2):
                if None in row or any(v is None for v in row.values()):
                    raise ValueError(
                        f"Ligne {line_num} : nombre de colonnes "
                        f"incorrect (attendu : {expected_cols})"
                    )
                rows.append({k.strip(): v.strip() for k, v in row.items()})
            return rows
    except FileNotFoundError:
        print(f"[ERREUR] Fichier introuvable : {file_path}. "
              f"Audit arrêté (fail-closed).")
        raise SystemExit(1)
    except Exception as e:
        print(f"[ERREUR] Lecture interrompue ({file_path}) : {e}. "
              f"Audit arrêté (fail-closed).")
        raise SystemExit(1)


def load_users(file_path: str) -> list:
    """
    Charge le référentiel des utilisateurs.
    Échec explicite (SystemExit) si le fichier est absent ou illisible.
    """
    try:
        with open(file_path, mode="r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f, delimiter=";")
            if reader.fieldnames is None:
                raise ValueError("Fichier vide (aucun en-tête)")
            expected = ["user_id", "user", "user_type", "role", "status"]
            if [fn.strip() for fn in reader.fieldnames] != expected:
                raise ValueError(
                    f"En-tête invalide. Attendu : {expected}. "
                    f"Lu : {[fn.strip() for fn in reader.fieldnames]}"
                )
            expected_cols = len(reader.fieldnames)
            rows = []
            seen_users = {}
            for line_num, row in enumerate(reader, start=2):
                if None in row or any(v is None for v in row.values()):
                    raise ValueError(
                        f"Ligne {line_num} : nombre de colonnes "
                        f"incorrect (attendu : {expected_cols})"
                    )
                clean = {k.strip(): v.strip() for k, v in row.items()}
                user_name = clean["user"]
                if user_name in seen_users:
                    raise ValueError(
                        f"Ligne {line_num} : utilisateur dupliqué "
                        f"'{user_name}', déjà défini ligne "
                        f"{seen_users[user_name]}. Un référentiel ambigu "
                        f"rend le statut dépendant de l'ordre des lignes"
                    )
                seen_users[user_name] = line_num
                rows.append(clean)
            return rows
    except FileNotFoundError:
        print(f"[ERREUR] Fichier introuvable : {file_path}. "
              f"Audit arrêté (fail-closed).")
        raise SystemExit(1)
    except Exception as e:
        print(f"[ERREUR] Lecture interrompue ({file_path}) : {e}. "
              f"Audit arrêté (fail-closed).")
        raise SystemExit(1)


def normalize_role(role: str) -> str:
    """
    Normalise la graphie d'un rôle pour comparaison fiable :
    NFKC (accents décomposés/recomposés) + espaces parasites + casse.
    """
    return unicodedata.normalize("NFKC", role).strip().casefold()

def check_roles_consistency(rbac_matrix: list, users: list) -> tuple:
    """
    Pré-contrôle : cohérence des rôles entre le référentiel IAM et la
    matrice RBAC (source de vérité). Retourne
    (orphan_iam, orphan_rbac, invalid_status).

    Comparaison STRICTE de la graphie (casse et accents compris) :
    la matrice est la source de vérité ; une graphie approximative est
    une donnée à corriger, pas à tolérer. La normalisation NFKC ne sert
    qu'à détecter la quasi-correspondance, citée dans le message d'arrêt.

    Un compte ACTIF dont le rôle est absent de la matrice bloque l'audit
    (saturation du rapport en NoMatchingRule, masquant les violations
    réelles). Les comptes INACTIFS sont exclus du contrôle bloquant
    (dé-provisionnement normal, couvert par le contrôle InactiveAccount).

    Le vocabulaire des statuts (Active/Inactive) est contrôlé : une valeur
    imprévue bloque l'audit (fail-closed), comme le vocabulaire des
    permissions de la matrice.
    """
    matrix_roles = [r["Rôle"] for r in rbac_matrix]
    iam_roles = {u["role"] for u in users}

    invalid_status = sorted({
        u["user"] for u in users
        if u["status"] not in ("Active", "Inactive")
    })
    orphan_iam = sorted({
        u["role"] for u in users
        if u["status"] == "Active" and u["role"] not in matrix_roles
    })
    orphan_rbac = sorted({
        r["Rôle"] for r in rbac_matrix if r["Rôle"] not in iam_roles
    })
    return orphan_iam, orphan_rbac, invalid_status

def check_user_role(log_entry: dict, users: list) -> dict | None:
    """
    Vérifie que le rôle déclaré dans le log
    correspond au rôle enregistré.
    """

    user = next(
        (
            u
            for u in users
            if u["user"] == log_entry["user"]
        ),
        None
    )

    if user is None:

        return {
            **log_entry,
            "compliant": False,
            "rbac_rule": "-",
            "control_type": "UnknownUser",
            "classification": "-",
            "severity": "high",
            "reason": "Utilisateur inconnu dans le référentiel IAM."
        }

    if user["status"] != "Active":

        return {
            **log_entry,
            "compliant": False,
            "rbac_rule": "-",
            "control_type": "InactiveAccount",
            "classification": "-",
            "severity": "high",
            "reason": "Compte utilisateur inactif."
        }

    if user["role"] != log_entry["role"]:

        return {
            **log_entry,
            "compliant": False,
            "rbac_rule": "-",
            "control_type": "RoleMismatch",
            "classification": "-",
            "severity": "critical",
            "reason": (
                f"Le rôle déclaré ({log_entry['role']}) "
                f"ne correspond pas au rôle enregistré "
                f"({user['role']})."
            )
        }

    return None

def check_access_compliance(log_entry: dict, rbac_matrix: list) -> list:
    """
    Contrôle 2 : conformité RBAC d'un accès.

    Retourne la liste des anomalies de l'entrée (zéro à trois) :
    1. action hors vocabulaire → MalformedValue (permissions non évaluables) ;
    2. valeur mfa_enabled invalide → MalformedValue (contrôle de qualité
       de la donnée, AVANT la recherche de règle) ;
    3. règle RBAC inexistante → NoMatchingRule (retour immédiat : la
       conformité MFA exige une règle) ;
    4. refus explicite → ExplicitDeny ;
    5. permissions → PermissionViolation ;
    6. MFA requis non activé → MFA (évalué seulement si la valeur est
       valide et la règle existe).
    """
    anomalies = []
    action_mapping = {
        "read": "L", "write": "E", "delete": "S",
        "admin": "A", "execute": "X",
    }
    user_role = log_entry["role"]
    resource = log_entry["resource"]
    action = log_entry["action"]
    raw_mfa = log_entry["mfa_enabled"].strip().lower()

    rbac_action = action_mapping.get(action)
    if rbac_action is None:
        anomalies.append({
            **log_entry,
            "compliant": False,
            "rbac_rule": "-",
            "control_type": "MalformedValue",
            "classification": "-",
            "severity": "high",
            "reason": (
                f"Action '{action}' hors vocabulaire "
                f"(attendu : read/write/delete/admin/execute). "
                f"Les permissions ne peuvent pas être évaluées — "
                f"source de log à corriger."
            ),
        })
    mfa_valid = raw_mfa in ("true", "false")
    if not mfa_valid:
        anomalies.append({
            **log_entry,
            "compliant": False,
            "rbac_rule": "-",
            "control_type": "MalformedValue",
            "classification": "-",
            "severity": "high",
            "reason": (
                f"Valeur 'mfa_enabled' invalide : '{log_entry['mfa_enabled']}'. "
                f"Attendu : True/False. La conformité MFA ne peut pas "
                f"être évaluée — source de log à corriger."
            ),
        })

    rule = next(
        (r for r in rbac_matrix
         if r["Rôle"] == user_role and r["Ressources"] == resource),
        None,
    )
    if rule is None:
        anomalies.append({
            **log_entry,
            "compliant": False,
            "rbac_rule": "N/A",
            "control_type": "NoMatchingRule",
            "classification": "N/A",
            "severity": "critical",
            "reason": (
                "Aucune règle RBAC définie pour ce rôle et cette ressource "
                "(refus implicite : défaut de couverture de la matrice)."
            ),
        })
        return anomalies

    permissions = rule["Permission"]
    if permissions == ["-"] or permissions == []:
        anomalies.append({
            **log_entry,
            "compliant": False,
            "rbac_rule": rule["ID"],
            "control_type": "ExplicitDeny",
            "classification": rule["Classification"],
            "severity": "critical",
            "reason": (
                f"Accès explicitement interdit par la politique RBAC "
                f"({rule['ID']})."
            ),
        })
    elif rbac_action is not None and rbac_action not in permissions:
        anomalies.append({
            **log_entry,
            "compliant": False,
            "rbac_rule": rule["ID"],
            "control_type": "PermissionViolation",
            "classification": rule["Classification"],
            "severity": "high",
            "reason": (
                f"Action '{action}' non autorisée "
                f"(permissions autorisées : {', '.join(permissions)})."
            ),
        })

    if mfa_valid and rule["MFA"] == "O" and raw_mfa != "true":
        anomalies.append({
            **log_entry,
            "compliant": False,
            "rbac_rule": rule["ID"],
            "control_type": "MFA",
            "classification": rule["Classification"],
            "severity": "medium",
            "reason": "MFA obligatoire mais non activé."
        })

    return anomalies

def check_business_hours(log_entry: dict) -> dict | None:
    """
    Vérifie si l'accès a eu lieu dans la fenêtre ouvrée : jours ouvrés
    (WORKING_DAYS) et horaires (BUSINESS_OPEN/CLOSE).

    L'horodatage est supposé en heure locale du site (gouvernance des
    journaux : un journal d'hébergeur en UTC doit être converti en amont
    — cf. README). Un horodatage invalide produit une anomalie
    MalformedValue : les logs sont la matière auditée, la valeur
    défectueuse est signalée sans rejeter le fichier ; le contrôle
    horaire est simplement non évaluable.
    """
    try:
        access_dt = datetime.fromisoformat(log_entry["timestamp"])
    except ValueError:
        return {
            **log_entry,
            "compliant": False,
            "rbac_rule": "-",
            "control_type": "MalformedValue",
            "classification": "-",
            "severity": "high",
            "reason": (
                f"Horodatage invalide : '{log_entry['timestamp']}'. "
                f"Le contrôle horaire ne peut pas être évalué — "
                f"source de log à corriger."
            ),
        }

    # Rôles exemptés : usage légitime à toute heure (mais un horodatage
    # invalide est signalé, cf. ci-dessus — la qualité de la donnée
    # se vérifie pour tous les rôles).
    if log_entry["role"] in HOUR_EXEMPT_ROLES:
        return None

    opening = datetime.strptime(BUSINESS_OPEN, "%H:%M").time()
    closing = datetime.strptime(BUSINESS_CLOSE, "%H:%M").time()
    out_of_hours = access_dt.time() < opening or access_dt.time() > closing
    out_of_days = access_dt.weekday() not in WORKING_DAYS

    if out_of_days or out_of_hours:
        if out_of_days:
            detail = f"jour non ouvré ({DAY_NAMES[access_dt.weekday()]})"
        else:
            detail = f"horaires {BUSINESS_OPEN} - {BUSINESS_CLOSE}"
        return {
            **log_entry,
            "compliant": False,
            "rbac_rule": "-",
            "control_type": "BusinessHours",
            "classification": "-",
            "severity": "medium",
            "reason": (
                f"Accès hors fenêtre ouvrée : {detail} — signal à "
                f"corroborer (fréquence des accès, autres signaux) "
                f"avant escalade."
            ),
        }

    return None

def generate_report(anomalies: list, output_file: str) -> None:
    """
    Génère un rapport CSV des anomalies — Y COMPRIS à 0 anomalie.
    Un « rien à signaler » non traçable n'est pas prouvable en audit :
    le rapport horodaté (même réduit à l'en-tête) constitue la preuve
    que l'audit a été exécuté et n'a rien détecté.
    """
    fieldnames = [
        "timestamp",
        "user",
        "role",
        "resource",
        "action",
        "mfa_enabled",
        "rbac_rule",
        "control_type",
        "classification",
        "reason",
        "severity"
    ]
    with open(output_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for anomaly in anomalies:
            writer.writerow({
                "timestamp": anomaly["timestamp"],
                "user": anomaly["user"],
                "role": anomaly["role"],
                "resource": anomaly["resource"],
                "action": anomaly["action"],
                "mfa_enabled": anomaly["mfa_enabled"],
                "rbac_rule": anomaly["rbac_rule"],
                "control_type": anomaly["control_type"],
                "classification": anomaly["classification"],
                "reason": anomaly["reason"],
                "severity": anomaly["severity"]
            })

    if anomalies:
        print(f"[SUCCESS] Rapport généré : {output_file} "
              f"({len(anomalies)} anomalie(s)).")
    else:
        print(f"[SUCCESS] Rapport généré : {output_file} "
              f"(0 anomalie — audit exécuté sans écart, "
              f"à conserver comme preuve d'exécution).")

# --- INTÉGRATION SIEM ---
# Non implémentée dans ce script (aucune dépendance externe, découplage
# voulu). Considérations et exigences d'une intégration Wazuh/Graylog :
# voir la section « Intégration SIEM » du README.

# --- MAIN ---
if __name__ == "__main__":

    print("=== [DEBUT] Audit RBAC ===")

    # 1. Charger la matrice RBAC et les logs
    rbac_matrix = load_rbac_matrix(RBAC_MATRIX_FILE)
    print(f"[INFO] Matrice RBAC chargée : {len(rbac_matrix)} règles.")
    if not rbac_matrix:
        print(f"[ERREUR] Matrice RBAC vide ou sans règle exploitable : "
              f"{RBAC_MATRIX_FILE}. Audit arrêté (fail-closed).")
        raise SystemExit(1)

    access_logs = load_access_logs(USER_ACCESS_LOG_FILE)
    print(f"[INFO] Logs d'accès chargés : {len(access_logs)} entrées.")
    if not access_logs:
        print(f"[ERREUR] Journal d'accès vide : {USER_ACCESS_LOG_FILE}. "
              f"Aucune entrée analysée — vérifier l'export ou la période. "
              f"Un rapport sans matière analysée ne prouve rien.")
        raise SystemExit(1)

    users = load_users(USERS_FILE)
    print(f"[INFO] Référentiel IAM chargé : {len(users)} utilisateurs.")
    if not users:
        print(f"[ERREUR] Référentiel IAM vide : {USERS_FILE}. "
              f"Aucune identité de référence — chaque accès serait "
              f"signalé UnknownUser, masquant les violations réelles. "
              f"Vérifier l'export.")
        raise SystemExit(1)

    # 2. Cohérence des rôles (fail-closed)
    orphan_iam, orphan_rbac, invalid_status = check_roles_consistency(rbac_matrix, users)
    if invalid_status:
        print(f"[ERREUR] Statut(s) invalide(s) dans le référentiel IAM : "
              f"{invalid_status}. Vocabulaire attendu : Active/Inactive. "
              f"Audit arrêté (fail-closed).")
        raise SystemExit(1)
    if orphan_iam:
        print(f"[ERREUR] Rôles des comptes ACTIFS absents de la matrice RBAC "
              f"(comparaison stricte) : {orphan_iam}")
        for role in orphan_iam:
            suggestion = next(
                (m for m in (r["Rôle"] for r in rbac_matrix)
                 if normalize_role(m) == normalize_role(role)),
                None
            )
            if suggestion:
                print(f"[ERREUR]   '{role}' : quasi-correspondance avec "
                      f"'{suggestion}' — corriger la graphie dans le "
                      f"référentiel ou la matrice.")
        print("[ERREUR] Audit arrêté : chaque accès de ces comptes produirait "
              "une anomalie NoMatchingRule et saturerait le rapport. "
              "Corriger la matrice ou le référentiel avant exécution.")
        raise SystemExit(1)
    if orphan_rbac:
        print(f"[AVERTISSEMENT] Rôles de la matrice sans utilisateur référencé : "
              f"{orphan_rbac}")

    # Exemption horaire silencieuse : un rôle exempté absent de la
    # matrice ne serait jamais exempté, sans aucun signal.
    unknown_exemptions = sorted(
        HOUR_EXEMPT_ROLES - {r["Rôle"] for r in rbac_matrix}
    )
    if unknown_exemptions:
        print(f"[AVERTISSEMENT] Rôles exemptés du contrôle horaire absents "
              f"de la matrice RBAC : {unknown_exemptions}. "
              f"L'exemption ne s'applique à aucun accès — adapter "
              f"HOUR_EXEMPT_ROLES à la matrice utilisée.")
        
    # 3. Vérifier chaque accès
    anomalies = []

    for log in access_logs:
        user_result = check_user_role(log, users)
        if user_result:
            anomalies.append(user_result)
            continue
        # Conformité RBAC : 0, 1, 2 ou 3 anomalies (contrôles indépendants)
        anomalies.extend(check_access_compliance(log, rbac_matrix))
        # Fenêtre horaire
        hours_result = check_business_hours(log)
        if hours_result:
            anomalies.append(hours_result)

    print(f"[INFO] {len(anomalies)} anomalie(s) détectée(s).")

    # 4. Générer le rapport
    generate_report(anomalies, REPORT_FILE)

    print("=== [FIN] Audit terminé ===")