#!/usr/bin/env python3
"""
Script Python : Audit RBAC simplifié
- Vérifie les accès par rapport à une matrice RBAC (CSV).
- Génère un rapport des anomalies (CSV).
- Note : Intégration Wazuh/Graylog en commentaire (non testée).
"""

import csv
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

TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
REPORT_FILE = f"{TIMESTAMP}_rapport_anomalies.csv"

# --- FONCTIONS ---
def load_rbac_matrix(file_path: str) -> list:
    """Charge la matrice RBAC depuis un fichier CSV (version ultra-robuste)."""
    matrix = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as f:
            # Lire la première ligne pour vérifier les noms de colonnes
            first_line = f.readline().strip()
            f.seek(0)  # Retour au début du fichier

            # Détecter le séparateur (virgule ou point-virgule)
            separator = "," if "," in first_line else ";"

            reader = csv.DictReader(f, delimiter=separator)

            # Nettoyer les noms de colonnes (supprimer les espaces et normaliser)
            fieldnames = [field.strip() for field in reader.fieldnames]

            # Trouver la colonne Permission (ou équivalent)
            permission_col = None
            for candidate in ["Permission", "Permissions", "Permission "]:
                if candidate.strip() in fieldnames:
                    permission_col = candidate.strip()
                    break

            if not permission_col:
                raise ValueError(
                    f"Colonne 'Permission' introuvable dans le CSV. "
                    f"Colonnes disponibles : {fieldnames}"
                )

            for row in reader:
                # Nettoyer les clés du dictionnaire (supprimer les espaces)
                clean_row = {k.strip(): v.strip() for k, v in row.items()}

                # Récupérer les permissions
                permission_str = clean_row.get(permission_col, "")
                permissions = permission_str.split() if permission_str else []

                # Ajouter à la matrice
                clean_row["Permission"] = permissions
                matrix.append(clean_row)

    except FileNotFoundError:
        print(f"[ERREUR] Fichier introuvable : {file_path}")
    except Exception as e:
        print(f"[ERREUR] Erreur lors de la lecture du CSV : {e}")

    return matrix

def load_access_logs(file_path: str) -> list:
    """Charge les logs d'accès depuis un fichier CSV."""
    logs = []
    with open(file_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            clean_row = {k.strip(): v.strip() for k, v in row.items()}
            logs.append(clean_row)
    return logs

def load_users(file_path: str) -> list:
    """Charge le référentiel des utilisateurs."""

    users = []

    with open(file_path, mode="r", encoding="utf-8") as f:

        reader = csv.DictReader(f, delimiter=";")

        for row in reader:
            users.append(
                {k.strip(): v.strip() for k, v in row.items()}
            )

    return users

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

def check_access_compliance(log_entry: dict, rbac_matrix: list) -> dict:

    action_mapping = {
        "read": "L",
        "write": "E",
        "delete": "S",
        "admin": "A",
        "execute": "X"
    }

    user_role = log_entry["role"]
    resource = log_entry["resource"]
    action = log_entry["action"]
    mfa_enabled = log_entry["mfa_enabled"] == "True"

    rbac_action = action_mapping.get(action, action)

    rule = next(
        (
            r for r in rbac_matrix
            if r["Rôle"] == user_role
            and r["Ressources"] == resource
        ),
        None
    )

    if rule is None:
        return {
            **log_entry,
            "compliant": False,
            "rbac_rule": "N/A",
            "control_type": "NoMatchingRule",
            "classification": "N/A",
            "severity": "medium",
            "reason": "Aucune règle RBAC définie pour ce rôle et cette ressource."
        }

    permissions = rule["Permission"]

    # Cas d'un refus explicite dans la matrice
    if permissions == ["-"] or permissions == []:
        return {
            **log_entry,
            "compliant": False,
            "rbac_rule": rule["ID"],
            "control_type": "ExplicitDeny",
            "classification": rule["Classification"],
            "severity": "critical",
            "reason": (
                f"Accès explicitement interdit par la politique RBAC "
                f"({rule['ID']})."
            )
        }

    if rbac_action not in permissions:
        return {
            **log_entry,
            "compliant": False,
            "rbac_rule": rule["ID"],
            "control_type": "PermissionViolation",
            "classification": rule["Classification"],
            "severity": "high",
            "reason": (
                f"Action '{action}' non autorisée "
                f"(permissions autorisées : {', '.join(permissions)})."
            )
        }

    if rule["MFA"] == "O" and not mfa_enabled:
        return {
            **log_entry,
            "compliant": False,
            "rbac_rule": rule["ID"],
            "control_type": "MFA",
            "classification": rule["Classification"],
            "severity": "medium",
            "reason": "MFA obligatoire mais non activé."
        }

    return {
        **log_entry,
        "compliant": True,
        "rbac_rule": rule["ID"],
        "reason": "Accès conforme"
    }

def check_business_hours(log_entry: dict) -> dict | None:
    """
    Vérifie si l'accès a eu lieu pendant les heures autorisées.

    Retourne :
        None si l'accès est conforme.
        Un dictionnaire d'anomalie sinon.
    """

    access_time = datetime.fromisoformat(
        log_entry["timestamp"]
    ).time()

    opening = datetime.strptime(BUSINESS_OPEN, "%H:%M").time()
    closing = datetime.strptime(BUSINESS_CLOSE, "%H:%M").time()

    if access_time < opening or access_time > closing:
        return {
            **log_entry,
            "compliant": False,
            "rbac_rule": "-",
            "control_type": "BusinessHours",
            "classification": "-",
            "severity": "medium",
            "reason": (
                f"Accès en dehors des heures autorisées "
                f"({BUSINESS_OPEN} - {BUSINESS_CLOSE})"
            )
        }

    return None

def generate_report(anomalies: list, output_file: str) -> None:
    """Génère un rapport CSV des anomalies."""
    if not anomalies:
        print("[INFO] Aucune anomalie détectée.")
        return
    
    # Générer un nom de fichier avec timestamp si non fourni
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{timestamp}_rapport_anomalies.csv"

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
        writer = csv.DictWriter(f, fieldnames=fieldnames)
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
    print(f"[SUCCESS] Rapport généré : {output_file}")

# --- INTÉGRATION WAZUH/GRAYLOG (ILLUSTRATION SEULEMENT) ---
"""
Note : Pour intégrer avec Wazuh ou Graylog, utiliser leur API REST.
Exemple de structure pour envoyer une alerte (non testé) :

1. Wazuh :
   - URL : http://<wazuh-server>:55000/elastalert
   - Méthode : POST
   - Headers : {"Content-Type": "application/json"}
   - Body :
     {
         "timestamp": "2026-06-25T10:00:00",
         "rule": {"id": "rbac_violation", "description": "Accès non conforme RBAC"},
         "data": {
             "user": "bob",
             "role": "Dev Produit",
             "resource": "Infra OVH (console admin)",
             "action": "write",
             "reason": "Action 'write' non autorisée (autorisées: [])"
         }
     }

2. Graylog :
   - URL : http://<graylog-server>:9000/api/labs/alerts
   - Méthode : POST
   - Headers : {"Content-Type": "application/json", "X-Requested-By": "rbac-audit-script"}
   - Body : Similaire à Wazuh, avec adaptation selon le schema Graylog.

Script d'intégration basique (non testé) :
---
import requests

def send_to_siem(alert: dict, siem_url: str, api_key: str = None) -> bool:
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    try:
        response = requests.post(siem_url, headers=headers, json=alert, timeout=5)
        return response.status_code in [200, 201]
    except requests.RequestException as e:
        print(f"[ERREUR] Échec envoi au SIEM : {e}")
        return False

# Exemple d'utilisation :
# send_to_siem(alert, "http://localhost:55000/elastalert")
"""

# --- MAIN ---
if __name__ == "__main__":

    print("=== [DEBUT] Audit RBAC ===")

    # 1. Charger la matrice RBAC et les logs
    rbac_matrix = load_rbac_matrix(RBAC_MATRIX_FILE)
    print(f"[INFO] Matrice RBAC chargée : {len(rbac_matrix)} règles.")

    access_logs = load_access_logs(USER_ACCESS_LOG_FILE)
    print(f"[INFO] Logs d'accès chargés : {len(access_logs)} entrées.")

    users = load_users(USERS_FILE)
    print(f"[INFO] Référentiel IAM chargé : {len(users)} utilisateurs.")

    # 2. Vérifier chaque accès
    anomalies = []

    for log in access_logs:
        # Vérification User == Role
        user_result = check_user_role(log, users)

        if user_result:
            anomalies.append(user_result)
            continue
        # Vérification RBAC
        result = check_access_compliance(log, rbac_matrix)

        if not result["compliant"]:
            anomalies.append(result)

        # Vérification des heures d'ouverture
        hours_result = check_business_hours(log)

        if hours_result:
            anomalies.append(hours_result)

    print(f"[INFO] {len(anomalies)} anomalies détectées.")

    # 3. Générer le rapport
    generate_report(anomalies, REPORT_FILE)

    print("=== [FIN] Audit terminé ===")