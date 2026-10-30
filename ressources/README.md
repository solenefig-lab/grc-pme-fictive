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

Synthèse pédagogique des principales obligations réglementaires applicables aux PME françaises de l’e-santé : protection des données personnelles et de santé (RGPD), hébergement de données de santé (HDS), conservation des dossiers médicaux, identification nationale de santé (INS), sécurité des services numériques en santé et sécurité des paiements par carte (PCI DSS).

Le document présente les bases juridiques, les obligations structurantes, les risques de non-conformité et les premières vérifications à mener, avec des références réglementaires et des actions assorties de preuves attendues.

**Public cible :** Dirigeants de PME e-santé, DPO et professionnels du pilotage GRC.

**Contexte :** Sensibilisation et cadrage initial de la conformité RGPD-HDS, support d’orientation pour identifier les obligations applicables et prioriser les vérifications, à adapter au contexte de chaque organisation.

[📖 Consulter](./Referentiel_legal_simplifie.md)

---

### 4. ISO 27001:2022 - Contrôles priorisés pour PME e-santé
**Fichiers :** `ISO27001_Liste-Controle.md` et `ISO27001_Liste-Controle.csv`

Les 93 contrôles de l'annexe A (ISO 27001:2022), regroupés en 16 sous-catégories
thématiques (de la gouvernance à la veille) et priorisés pour une PME e-santé
éditrice hébergée chez un hébergeur certifié. Chaque ligne porte des renvois
lorsque pertinents aux exigences RGPD, NIS2 et HDS.

| Colonne | Contenu |
|---------|---------|
| Thème | Organisationnel / Personnes / Physiques / Technologie |
| Contrôle | Référence ISO 27001:2022 + intitulé (abrégé ou paraphrasé) |
| Sous-catégorie | Regroupement métier (ex : Gouvernance et rôles, IAM, Continuité et résilience) |
| Effort | ○ Faible / ◐ Moyen / ● Élevé : coût et complexité du contrôle complet, cotation qualitative |
| Phase | Ordre de traitement : 1 = exigible dès la mise en service (loi ou contrat), 2 = consolidation, 3 = maturité |
| Références | Renvois RGPD / NIS2 / HDS, lorsque pertinents |

**Le `+`** : contrôle exigible dès sa phase sous une version minimale, complétée ensuite (tableau des versions minimales dans le document).

**Formats :** le MD se lit par sous-catégorie ; le CSV, trié par contrôle, se filtre dans un tableur.
**Public cible :** RSSI, DPO, consultants GRC, dirigeants de PME e-santé.
**Avertissement :** document d'entrée, pas un audit ; les correspondances réglementaires sont indicatives et ne constituent pas un avis juridique.

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
CSP L. 1111-8-2, NIS2 Art. 21-23

[📖 Consulter](./plan_reponse_incidents.md)

-----
### 6. Exigences cyber des clients et partenaires : repères NIS2 et correspondances indicatives avec ISO 27001:2022
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
