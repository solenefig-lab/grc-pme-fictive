# 📚 Bibliothèque de ressources GRC pour PME

Cette bibliothèque rassemble des modèles, guides et outils pratiques issus du projet [grc-pme-fictive](../README.md) et conçues pour être réutilisables et adaptables à d'autres contextes, avec un focus particulier sur les PME e-santé.

Elle s'adresse aux :

- RSSI
- DPO
- consultants GRC
- dirigeants de PME
- étudiants

## Principes

Les ressources publiées dans ce dépôt sont conçues pour être :

- réutilisables
- adaptables
- documentées
- alignées sur les référentiels applicables lorsque cela est pertinent

Elles constituent des modèles de travail et doivent être adaptées au contexte de chaque organisation.

**Licence**

- Documentation (.md, .csv, .xlsx) : [CC-BY-4.0](./LICENSE-CC-BY-4.0).
- Code (rbac_audit.py) : [MIT](./LICENSE-MIT)
- Attribution souhaitée : Solène Figueiredo

> 🔄 **En cours** - cette section s'enrichit au fil des semaines du projet.


---

## Templates disponibles

L'objectif de cette bibliothèque est de transformer des exigences de gouvernance, conformité et cybersécurité en livrables directement exploitables par une PME.


| Ressource           | Format   | Sujet              | Public    |
| ------------------- | -------- | ------------------ | --------- |
| [Inventaire d'actifs](#1-cartographie-des-actifs-grc---template-pme)| XLSX     | Gestion des actifs | PME       |
| [Inventaire d'actifs (Advanced)](#2-cartographie-des-actifs-grc---template-advanced) | XLSX | Gestion des actifs + Threat Intel | Technique |
| [Référentiel légal simplifié](#3-référentiel-légal-simplifié---rgpd--hds) | MD | RGPD / HDS | DPO |
| [ISO 27001 priorisé](#4-iso-270012022---contrôles-priorisés-pour-pme-e-santé)  | MD / CSV | Gouvernance        | RSSI      |
| [PRI](#5-plan-de-réponse-aux-incidents-pri---modèle-pme-e-santé)  | MD       | Incident Response  | RSSI      |
| [NIS2 ↔ ISO 27001](#6-nis2-art-21--23---guide-de-conformité-pme-e-santé-iso-270012022)    | MD       | Conformité NIS2     | RSSI      |
| [Audit RBAC - Script Python](#7-audit-rbac---script-python)          | Python   | IAM                | Technique |


### 1. Cartographie des actifs GRC - Template PME
**Fichier :** `grc-asset-inventory-template-pme.xlsx`

Outil d'inventaire et de priorisation des risques pour une petite PME,
sans prérequis technique.

| Onglet | Contenu |
|--------|---------|
| Mode d'emploi | Démarche globale, sommaire, disclaimer |
| 1. Inventaire des actifs | Cartographie + scoring automatique (Impact × Probabilité) |
| 2. Grille de scoring | Critères d'impact, probabilité, décisions de traitement |
| 3. Mapping des risques | Top risques identifiés + décision + priorité |

**Public cible :** Dirigeants PME, DPO, consultants GRC junior  
**Approche :** Inspirée du NIST CSF (People · Process · Technology),
adaptée au contexte PME - posture *"GRC comme produit"*

[📥 Télécharger](./grc-asset-inventory-template-pme.xlsx)

---

### 2. Cartographie des actifs GRC - Template Advanced
**Fichier :** `grc-asset-inventory-template-pme-threats.xlsx`

Même outil enrichi d'un mapping des tactiques MITRE ATT&CK -
pour aller jusqu'à l'analyse des menaces.

| Onglet | Contenu |
|--------|---------|
| Mode d'emploi | Démarche globale, sommaire, disclaimer |
| 1. Inventaire des actifs | Cartographie + scoring automatique |
| 2. Grille de scoring | Critères + décisions de traitement |
| 3. Mapping des risques (Advanced) | Top risques + décision + priorité + Tactique MITRE ATT&CK par vecteur d'attaque |


**Public cible :** Équipes techniques, RSSI, cabinets GRC  
**Différenciateur :** Combine scoring PME accessible et référentiel
threat intelligence MITRE ATT&CK

[📥 Télécharger](./grc-asset-inventory-template-pme-threats.xlsx)

---

### 3. Référentiel légal simplifié - RGPD / HDS
**Fichier :** `Referentiel_legal_simplifie.md`

Synthèse des obligations légales applicables aux PME e-santé françaises :
RGPD, HDS (L.1111-8 CSP), Code de la Santé Publique, RGS, PGSSI-S.
Conçu comme entrée rapide pour DPO, dirigeants et consultants junior.

**Public cible :** DPO, dirigeants PME, consultants GRC junior  
**Contexte :** aligné RGPD art. 28/32/33

[📖 Consulter](./Referentiel_legal_simplifie.md)

---

### 4. ISO 27001:2022 - Contrôles priorisés pour PME e-santé
**Fichier :** `ISO27001_Liste-Controle.md` *(+ version CSV disponible)*

93 contrôles ISO 27001:2022 priorisés pour les PME e-santé, avec
alignement HDS, RGPD et NIS2 par contrôle. 

| Colonne | Contenu |
|---------|---------|
| Thème | Organisationnel / Personnes / Physiques / Technologie |
| Contrôle | Référence ISO 27001:2022 + intitulé |
| Sous-catégorie | Regroupement métier (ex : Gouvernance, Sauvegardes, IAM) |
| Priorité PME | 🟢 Basique / 🟡 Intermédiaire / 🔴 Avancé |
| Liens | Alignement HDS / RGPD / NIS2 par contrôle |

**Public cible :** RSSI, DPO, consultants GRC, dirigeants PME  
**Approche :** Phase 1 → contrôles 🟢 (80% des risques, 20% de l'effort).
Sources : ANSSI, CNIL, NIST SP 800-63B.

[📖 Consulter](./ISO27001_Liste-Controle.md)
[📥 Télécharger CSV](./ISO27001_Liste-Controle.csv)

---
### 5. Plan de Réponse aux Incidents (PRI) - Modèle PME e-santé
**Fichier :** `plan_reponse_incidents.md`

Modèle opérationnel de réponse aux incidents aligné ISO 27001:2022,
RGPD, HDS et NIS2. Couvre la classification des incidents, les rôles,
les playbooks (ransomware, fuite de données, phishing), le registre
des incidents et les templates REX.

| Section | Contenu |
|---------|---------|
| Personnalisation rapide | Table de correspondance SantéConnect → votre PME |
| Classification P1→P4 | Sévérité, délais légaux, responsables |
| Playbooks | Ransomware, fuite PII/Santé, phishing réussi |
| Annexes | Obligations réglementaires, registre incidents, REX |

**Public cible :** RSSI, DPO, dirigeants PME  
**Alignement :** ISO 27001:2022 (A.5.24→A.5.27), RGPD Art. 33-34,
HDS R.1112-7, NIS2 Art. 21-23

[📖 Consulter](./plan_reponse_incidents.md)

-----
### 6. NIS2 Art. 21 & 23 - Guide de conformité PME e-santé (ISO 27001:2022)
**Fichier PME :** `nis2_correspondances_ISO27001.md`

Guide pratique pour les PME e-santé travaillant avec un CHU ou un hôpital. Comprendre ce que votre partenaire peut exiger au titre de NIS2, évaluer votre couverture via vos contrôles ISO 27001:2022 existants, et identifier les preuves d'exécution attendues. 

| Section | Contenu |
|---------|---------|
| Analyse rapide des attentes par domaine Art. 21 + Art. 23 | Table des domaines → thème central |
| Correspondance ISO avec exemples de documents et preuves | Correspondances, documentation et couverture |


**Public cible :** RSSI, DPO, dirigeants PME dans domaine e-santé  
**Alignement :** ISO 27001:2022, NIS2 Art. 21-23

[📖 Consulter](./nis2_correspondances_ISO27001.md)

---

### 7. Audit RBAC - Script Python

**Fichier :** `audit_RBAC_auto/rbac_audit.py`

Script Python autonome pour auditer les droits d'accès (RBAC) et détecter les anomalies.
Compare une matrice RBAC, un référentiel utilisateurs et des logs d'accès pour générer un rapport CSV horodaté.

| Fichier | Contenu |
|---------|---------|
| `rbac_audit.py` | Script principal |
| `MatriceRBAC.csv` | Matrice des règles RBAC |
| `users.csv` | Référentiel utilisateurs (user → rôle) |
| `user_access_log.csv` | Logs d'accès (format : `timestamp;user;role;resource;action;mfa_enabled`) |
| `YYYYMMDD_HHMMSS_rapport_anomalies.csv` | Rapport généré |

**Public cible :** RSSI, équipes techniques, consultants GRC  
**Différenciateur :** Audit automatisé des droits RBAC avec génération de rapports horodatés, zéro dépendance externe.

📥 [Télécharger le script](./audit_RBAC_auto/rbac_audit.py) · 📖 [Documentation](./audit_RBAC_auto/README.md)

---


> 💡 **Ces ressources évoluent** avec le projet - elles reflètent
> une montée en compétences progressive et documentée.
> Retours et suggestions bienvenus via
> [Issues GitHub](../../../issues).
