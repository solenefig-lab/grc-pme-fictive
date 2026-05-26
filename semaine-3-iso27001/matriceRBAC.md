# Matrice RBAC (Role-Based Access Control)

## Objectif
Documenter les **droits d’accès** par rôle pour garantir :
- La **confidentialité** des données médicales (RGPD, HDS).
- Le **principe du moindre privilège** (ISO 27001 A.5.18).
- La **traçabilité** des accès (ISO 27001 A.5.15).
- **L’alignement avec les exigences métiers** de SantéConnect (ex : accès des praticiens à leurs patients uniquement).

## Périmètre
- **Rôles** : Internes (employés) + Externes (praticiens, sous-traitants comme OVH, Stripe).
- **Données** : Médicales, personnelles, paiement, marketing, RH, code source.
- **Ressources** : Applications (WebApp, Mobile), bases de données, dépôts Git, logs.
- **Exclusions** :
  - Les **accès physiques** (couverts par [A.7.1 à A.7.14](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-3-iso27001/SoA.md)).
  - Les **accès aux systèmes du CHU** (couverts par la [convention co-responsabilité CHU](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/note-co-responsabilite-chu.md)).

## Méthodologie
- **Niveau RBAC** : Niveau 1 (rôles métiers), qui permet à la fois une granularité suffisante pour séparer les accès aux données sensibles (ex : patients, praticiens, RH) et une maintenance adaptée par une petite équipe (RSSI temps partiel).
- **Classification des données** : Critique/Sensible/Standard (conforme à la [PSSI](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-3-iso27001/pssi.md)).
- **Lien avec les risques** : Chaque rôle est associé aux risques identifiés dans la [fiche-risques-e-sante.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-1-gouvernance/fiche-risques-e-sante.md).


## Matrice RBAC

| ID   | Rôle  | Catégorie de données | Classification | Ressources | Permission | MFA | Justification | Contrôle ISO 27001:2022 | Revue des accès | Preuves |
|------|--------------------|----------------------|-----------------|--------------------------|------------|-----|---------------|-----------------------------|------------------|---------|
| RBAC-01 | CEO | Données RH / Paie | Sensible | Suivi des contrats et promotions | L E | O | Autorisation dirigeant ; E limité aux propres données de l’entreprise (RGPD Art. 6) | A.5.18, A.8.5 | **Annuelle** | Logs d’accès |
| RBAC-02 | CEO | Données financières | Sensible | Données financières entreprises | L | O | Accès en lecture seule pour supervision | A.5.18 | **Annuelle** | Logs d’accès |
| RBAC-03 | RSSI | Logs techniques | Sensible | Logs Graylog | L A | O | Accès en lecture et administration pour surveillance (ISO A.8.15). Pas d’écriture pour préserver l’intégrité | A.8.15, A.8.16 | **Semestrielle** | Logs d’accès |
| RBAC-04 | RSSI | Infra OVH (console admin) | Critique | Configuration infrastructure | L E A | O | Accès admin complet pour gestion de l’infrastructure (ISO A.12.1). | A.8.9, A.8.15 | **Semestrielle** | Logs OVH + contrat |
| RBAC-05 | DPO | Registre des traitements | Sensible | Données métadonnées | L E | O | Gestion du registre des traitements (RGPD Art. 30) pour assurer la traçabilité des données (ISO A.5.12) et la conformité réglementaire (ISO A.12.4) | A.5.12, A.8.15 | **Semestrielle** | [Registre des traitements](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/registre-traitements/registre_traitement.md) |
| RBAC-06 | Dev Produit | Plateforme B2B praticiens | Sensible | Données praticiens | L E | O | Développement et maintenance (accès limité aux données métiers). | A.8.4, A.8.25 | **Annuelle** | Logs d’accès |
| RBAC-07 | Dev Produit | App Mobile / WebApp (admin) | Sensible | Code source | L E | O | Accès aux branches dev/test (pas de merge en production sans validation); **Note** : en cas de départ, la revue des accès Git et la validation des merges seront assurées par le RSSI en intérim, avec un recrutement prioritaire d’un 2ème dev | A.8.4, A.8.25 | **Annuelle** | Logs Git |
| RBAC-08 | Dev Produit | Logs techniques | Sensible | Logs Graylog | L | O | Besoin de debug ; pas d’écriture pour préserver l’intégrité des logs (ISO A.8.15). | A.8.15, A.8.16 | **Annuelle** | Logs d’accès |
| RBAC-09 | Dev Produit | Infra OVH (console admin) | Critique | Configuration infrastructure | - | - | Aucun accès (séparation des privilèges, ISO A.5.3). DevOps gère l’infra. | A.5.3, A.8.9 | **-** | - |
| RBAC-10 | RH | Données RH/Paie | Sensible | Données RH | L E S | O | Gestion des ressources humaines (RGPD Art. 6). S réservée au RH pour traçabilité. | A.6.1, A.6.2 | **Annuelle** | Logs d’accès |
| RBAC-11 | Comptabilité | Données financières | Sensible | Données financières | L E | O | Gestion financière (PCI-DSS via Stripe). E limitée aux données comptables | A.5.15, A.8.5 | **Annuelle** | Logs d’accès |
| RBAC-12 | Praticien B2B | Données patients | Critique | Données de santé | L X | O | Principe du moindre privilège ; L+X uniquement sur ses patients (HDS R.1112-7). Pas de S (traçabilité) | A.5.15, A.8.3 | **Semestrielle** | Logs d’accès + [Convention CHU](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/note-co-responsabilite-chu.md) |
| RBAC-13 | Laboratoires | Dossier médical | Critique | API CHU/labos | L E | O | Accès en Lecture + Écriture (ajout uniquement) via API HL7/FHIR pour déposer les résultats d’analyses (convention CHU + RGPD Art. 28). Pas de modification des données existantes (traçabilité HDS R.1112-7). | A.5.15, A.8.21, A.8.26 | **Semestrielle** | Logs API + [Convention CHU](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/note-co-responsabilite-chu.md) |
| RBAC-14 | Praticien B2B | Plateforme B2B praticiens | Sensible | Données praticiens | L E | O | Gestion de son profil et plannings | A.8.3, A.8.5 | **Annuelle** | Logs d’accès |
| RBAC-15 | Patient B2C | Gestion des comptes patients | Sensible | Ses coordonnées | L E | N | Accès aux données personnelles uniquement pour son propre compte (RGPD Art. 15). | A.5.18, A.8.3 | **Annuelle** | Logs d’accès |
| RBAC-16 | Patient B2C | Données patients | Critique | Données de santé | L | N | Droit d’accès (RGPD Art. 15). Lecture seule sur son dossier. | A.5.18, A.8.3 | **Annuelle** | Logs d’accès |
| RBAC-17 | Patient B2C | Données de paiement | Sensible | Données financières | L E | N | Gestion de son abonnement (PCI-DSS via Stripe) | A.8.5, A.8.24 | **Annuelle** | Logs d’accès |
| RBAC-18 | Compte de service API CHU | API CHU/labos | Critique | Données de santé | L | O | Accès en lecture seule (HL7/FHIR). Pas d’écriture (convention CHU). | A.5.15, A.8.21 | **Trimestrielle** | Logs API + [Convention CHU](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/note-co-responsabilite-chu.md) |
| RBAC-19 | Compte de service API Stripe | API Stripe | Sensible | Données financières | L E | O | Accès limité aux transactions (PCI-DSS). Pas d’accès aux données patients. | A.8.5, A.8.24 | **Trimestrielle** | Logs API + Contrat Stripe |
| RBAC-20 | OVH (Sous-traitant) | Données médicales | Critique | Sauvegardes, hébergement | L | O | Accès en lecture seule aux sauvegardes chiffrées (RGPD Art. 28, HDS). Pas d’écriture sur les données médicales. Contrat OVH + AIPD. | A.5.23, A.8.13, A.8.9 | **Trimestrielle** | Contrat OVH + [AIPD](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/aipd-synthetique.md) |

### Légende
| Permission | Signification | Exemple |
|------------|---------------|---------|
| **L** | Lecture | Consulter un dossier patient. |
| **E** | Écriture / Mise à jour | Modifier les coordonnées d’un patient. |
| **S** | Suppression | Supprimer un compte utilisateur. |
| **X** | Export / Téléchargement | Exporter une liste de patients (interdit pour les données médicales sauf exception). |
| **A** | Administration | Configurer les droits d’accès. |
| **-** | Aucun Accès | Aucun. |
 
Exemple : "Un praticien ne peut accéder qu’aux dossiers de ses patients (filtre par ID praticien)."

> Dans le cas HDS/RGPD, X (Export/Téléchargement) est pertinent sur les données médicales.

**MFA Requis** :
- **O** : Obligatoire (ex : accès aux données **Critiques/Sensibles**).
- **N** : Non obligatoire (ex : accès aux données **Standard**).

Note: MFA obligatoire pour les rôles internes et les accès aux données Critiques/Sensibles (conforme à la PSSI 2.1). Pour les patients B2C, MFA recommandé mais non obligatoire (équilibre UX/sécurité):
- Évite l’exclusion numérique des patients âgés (cible de SantéConnect).
- Respecte le principe de proportionnalité (RGPD Art. 5).

### Règles générales
- **Principe du moindre privilège** : Chaque rôle a **uniquement les accès nécessaires** à ses missions.
- **MFA obligatoire** pour les accès aux données **Critiques/Sensibles** (conforme à la [PSSI](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-3-iso27001/pssi.md)).
- **Revues trimestrielles** des habilitations (ISO 27001 A.5.15).

### Classification des données
| Classification | Exemples | Réglementation | Risque principal | Mesures de protection |
| --- | --- | --- | --- | --- |
| 🔴 Critique | Dossiers médicaux, ECG, données RH/paie | RGPD (Art. 9), HDS, Code Santé Public | Fuite de données sensibles (sanction jusqu’à 4% du CA) | Séparation par conception, MFA, OAuth2, Chiffrement AES-256 |
| 🟠 Sensible | Données personnelles (B2C/B2B), Logs IT, données R&D | RGPD (Art. 4–9), HDS | Usurpation d’identité, traçabilité compromise | MFA, OAuth2, Surveillance des accès, Chiffrement AES-256 |
| 🟡 Standard | Données utilisation site web | RGPD (Art. 5) | Accès non autorisé | Accès Least Privilege, Surveillance des flux |
 
### Fréquences de revue

| Fréquence | Rôles concernés | Justification |
| --- | --- | --- |
| Trimestrielle | Comptes de service (API CHU, API Stripe), OVH | Risque élevé : Accès externes + données critiques. Revue fréquente pour détecter les anomalies (ISO A.5.18 + HDS) |
| Semestrielle | RSSI, Praticien B2B, Laboratoires | Accès aux données critiques (médicales) ou rôles sensibles (ex : RSSI) |
| Annuelle | CEO, Dev Produit, RH, Comptabilité, Patients B2C | Risque modéré : Accès aux données sensibles ou standard. Revue annuelle suffisante pour une PME|

## Schéma de flux de données
Reprend et **enrichit le schéma 1.3** de la [fiche-risques-e-sante.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-1-gouvernance/fiche-risques-e-sante.md) avec :
- **Les rôles RBAC** (ex : Patient, Praticien B2B, Laboratoires, OVH).
- **Les permissions** (L, E, S, X, A) pour chaque flux.
- **Les interfaces d'accès** (API HL7/FHIR, WebApp, Console OVH, etc.).
- **Les ressources critiques** (dossiers médicaux, données paiement, logs).

```mermaid
flowchart TD
    %% ===== ACTEURS =====
    subgraph Acteurs Internes
        A["Patient B2C<br>(RBAC-15,16,17)"] -->|L - via WebApp| B["Dossier médical<br>Critique"]
        A -->|L E - via WebApp| C["Coordonnées<br>Sensible"]
        A -->|L E - via Stripe| D["Données paiement<br>Sensible"]

        E["Praticien B2B<br>(RBAC-12,14)"] -->|L X - via WebApp| B
        E -->|L E - via WebApp| F["Données praticiens<br>Sensible"]

        G["RSSI<br>(RBAC-03,04)"] -->|L A - via Graylog| H["Logs Graylog<br>Sensible"]
        G -->|L E A - via Console OVH| I["Infra OVH<br>Critique"]

        J["Dev Produit<br>(RBAC-06,07,08)"] -->|L E - via WebApp| F
        J -->|L E - via Git| K["Code source<br>Sensible"]
        J -->|L - via Graylog| H

        L2["RH<br>(RBAC-10)"] -->|L E S - via SIRH| M["Données RH/Paie<br>Sensible"]
        M2["Comptabilité<br>(RBAC-11)"] -->|L E - via Comptabilité| N["Données financières<br>Sensible"]
    end

    subgraph Acteurs Externes
        O["Laboratoires<br>(RBAC-13)"] -->|L E - via API HL7/FHIR| B
        P["API CHU<br>(RBAC-18)"] -->|L - via API HL7/FHIR| B
        Q["API Stripe<br>(RBAC-19)"] -->|L E - via API Stripe| D
        R["OVH<br>(RBAC-20)"] -->|L - via Console OVH| I
    end

    %% ===== LÉGENDE =====
    classDef critical fill:#ff6b6b,color:#fff,stroke:#c91818;
    classDef sensitive fill:#ffd166,color:#000,stroke:#ffaa00;
    classDef standard fill:#a5d8ff,color:#000,stroke:#1e90ff;

    class B,I critical;
    class C,D,F,H,K,M,N sensitive;
    classDef default fill:#f9f9f9,stroke:#333;



## Signatures

| Rôle | Nom | Date | Version | Dernière révision |
|------|-----|------|---------| ---------|
| RSSI | Claire ESPINOZA | 25.01.2024 | 1.0 | 25.01.2026 |
| DPO | Jeanne PETIT | 25.01.2024 | 1.0 | 25.01.2026 |
| CEO | Martin DUPONT | 25.01.2024 | 1.0 | 25.01.2026 |

Révision annuelle. 

**Note** : Les habilitations sont **révisées trimestriellement** par RSSI (ISO 27001 A.5.15).