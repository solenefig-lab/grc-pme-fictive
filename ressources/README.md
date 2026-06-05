# Ressources — GRC Fil Rouge

> 🔄 **En cours** — cette section s'enrichit au fil des semaines du projet.

Les ressources publiées ici sont issues du projet
[grc-pme-fictive](../README.md) et conçues pour être
**réutilisables par toute PME**, indépendamment du contexte SantéConnect.

---

## 📦 Templates disponibles

### 1. Cartographie des actifs GRC — Version PME
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
adaptée au contexte PME — posture *"GRC comme produit"*

[📥 Télécharger](./grc-asset-inventory-template-pme.xlsx)

---

### 2. Cartographie des actifs GRC — Version Advanced
**Fichier :** `grc-asset-inventory-template-pme-threats.xlsx`

Même outil enrichi d'un mapping des tactiques MITRE ATT&CK —
pour aller jusqu'à l'analyse des menaces.

| Onglet | Contenu |
|--------|---------|
| Mode d'emploi | Démarche globale, sommaire, disclaimer |
| 1. Inventaire des actifs | Cartographie + scoring automatique |
| 2. Grille de scoring | Critères + décisions de traitement |
| 3. Mapping des risques | Top risques + décision + priorité |
| 4. Mapping Risques (Advanced) | + Tactiques MITRE ATT&CK par vecteur d'attaque |

**Public cible :** Équipes techniques, RSSI, cabinets GRC
**Différenciateur :** Combine scoring PME accessible et référentiel
threat intelligence MITRE ATT&CK

[📥 Télécharger](./grc-asset-inventory-template-pme-threats.xlsx)

---

### 3. Référentiel légal simplifié — RGPD / HDS
**Fichier :** `Referentiel_legal_simplifie.md`

Synthèse des obligations légales applicables aux PME e-santé françaises :
RGPD, HDS (L.1111-8 CSP), Code de la Santé Publique, RGS, PGSSI-S.
Conçu comme entrée rapide pour DPO, dirigeants et consultants junior.

**Public cible :** DPO, dirigeants PME, consultants GRC junior
**Contexte :** Produit en Semaine 2 du projet — aligné RGPD art. 28/32/33

[📖 Consulter](./Referentiel_legal_simplifie.md)

---

### 4. ISO 27001:2022 — Contrôles priorisés pour PME e-santé
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
### 5. Plan de Réponse aux Incidents (PRI) — Modèle PME e-santé
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

## 🔄 À venir

| Semaine | Ressource prévue |
|---------|-----------------|
| Semaine 4 | Checklist NIS2 — impact pour PME prestataire |

---

> 💡 **Ces ressources évoluent** avec le projet — elles reflètent
> une montée en compétences progressive et documentée.
> Retours et suggestions bienvenus via
> [Issues GitHub](../../../issues).
