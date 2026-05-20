
# Déclaration d'applicabilité (SoA en anglais) - ISO 27001:2022

> **Document produit dans le cadre du projet portfolio GRC** - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)
> Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité. Le niveau de granularité illustre une cible de maturité, non l'état courant du marché TPE/PME santé.

---

## 1. Contexte et périmètre
### 1.1. Contexte

SantéConnect est une PME de 15 personnes spécialisée dans l'amélioration du suivi cardiologique des utilisateurs. Le service est proposé en partenariat avec le CHU Fictif et des praticiens libéraux (20 praticiens) pour 80 patients, constituant une population principalement âgée. Le cœur du service est le dossier médical, dont les données sont séparées par conception des autres données traitées.

### 1.2. Périmètre

La déclaration d'applicabilité concerne la totalité du système d'information de SantéConnect, incluant toutes les informations matérielles ou logicielles nécessaires à leur gestion (création, acquisition, traitement, stockage, diffusion, destruction, etc.) où qu'elles se trouvent.



### 1.3. Approche
Elle est basée sur la cartographie des actifs et l'analyses de risques ['Fiche Risques e-santé'](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-1-gouvernance/fiche-risques-e-sante.md), et référentiel réglementaire ['Contexte SantéConnect'](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-0-fondamentaux/contexte-santeconnect.md) et la politique de sécurité des systèmes d'information (./pssi.md) pour comprendre quels contrôles sont nécessaires et comment ils sont appliqués.


### 1.4. Durée et versioning

| Champ | Valeur |
|---|---|
| Date de première émission | 15/02/2024 |
| Numéro de version | v1.2 |
| Révision | Annuelle |
| Audit de suivi | Annuel |


| Rôle | Responsabilité |
|---|---|
| Direction (CEO) | Valide la première version et les revues annuelles |
| RSSI (salarié, temps partiel) | Valide première version et revues annuelles, responsable du contrôle des versions et changement|
| DPO (service externe) | Garant de la conformité RGPD/HDS |

---

## 2. Note méthodologique
La déclaration d'applicabilité repose sur la revue des 93 contrôles de l'Annexe A de la norme ISO 27001:2022,regroupé en contrôles organisationnels, des personnes, physiques et technologiques. Pour chaque contrôle, il est mentionné:
- le type de contrôle,
- si dans le système de management de la sécurité de l'information, le contrôle est: Inclus / Exclus (car non applicable) / Exclus (car non implémenté),
- la justification du statut du contrôle,
- son application si inclus: Appliqué ou Partiellement Appliqué,
- son rôle en termes C I A T sur la sécurité de l'information: Confidentialité Intégrité Disponibilité (Availability) et Traçabilité pour refléter les obligations spécifiques du secteur santé (HDS, RGPD art. 30),
- les preuves de documentations liées.


Note: Certains documents référencés sont présupposés existants dans le contexte SantéConnect (ex : plan des locaux, registres internes). Seuls les artefacts clés de la démarche GRC sont produits dans ce portfolio.

---

## 3. Synthèse chiffrée

   **Catégorie**          | **Nombre** | **Détails**                                                                                     |
 |------------------------|------------|-------------------------------------------------------------------------------------------------|
 | **Contrôles inclus**   | 91         | Tous les contrôles sauf **A.6.4** (Processus disciplinaire) et **A.7.11** (Utilitaires de support). |
 | **Contrôles exclus**   | 2          | A.6.4 (N.I.), A.7.11 (N.A.).                                                                     |
 | **Répartition par état** |            |                                                                                                 |
 | - **Appliqué**          | 23        | Ex : A.5.1, A.5.2, A.5.4, A.5.19, A.5.20, A.5.24, A.5.26, A.5.28, A.5.34, A.6.1, A.6.2, A.8.24 |
 | - **Partiellement Appliqué** | 68  | Majorité des contrôles, notamment ceux liés aux **ressources limitées de la PME**.               |
                                                          


### **Répartition par thème**
 | **Thème**          | **Inclus** | **Exclus** | **Appliqué** | **Partiellement Appliqué** |
 |--------------------|-----------|------------|--------------|-----------------------------|
 | **Organisationnel** | 37        | 0          | 12           | 25                          |
 | **Personnes**      | 7         | 1          | 5            | 2                           |
 | **Physiques**      | 13        | 1          | 2            | 11                           |
 | **Technologie**    | 34        | 0          | 4            | 30                           |

---

## 4. Contrôles exclus — justifications

   **Contrôle**               | **Type d'exclusion** | **Justification**                                                                                     |
 |----------------------------|----------------------|-------------------------------------------------------------------------------------------------------|
 | **A.6.4 Processus disciplinaire** | N.I. (Non Implémenté) | SantéConnect ne formalise pas actuellement de processus disciplinaire spécifique aux incidents de sécurité. En cas de manquement avéré, la société porte plainte et applique les sanctions prévues dans les contrats de travail. |
 | **A.7.11 Utilitaires de support** | N.A. (Non Applicable) | SantéConnect, locataire d’un espace tertiaire, délègue la gestion des utilités (électricité, climatisation) au bailleur. Les données critiques étant hébergées chez OVH (HDS), une interruption des utilités dans les locaux n’impacte pas la disponibilité des données médicales. |

---

## 5. Points d'attention et plan de remédiation

Ci-dessous un résumé des contrôles "Partiellement Appliqué" et les actions prévues (plus de détails sera donné dans un plan de traitement des risques [à venir]).
Les 10 contrôles listés ci-dessous ont été identifiés comme **prioritaires** car ils :
- **Impactent directement la conformité RGPD/HDS** (ex : gestion des accès, sauvegardes, prévention des fuites).
- **Présentent des risques élevés** pour une PME e-santé (ex : perte de données médicales, accès non autorisés).
- **Sont partiellement appliqués** mais critiques pour la sécurité et la résilience de SantéConnect.
- **Ont des actions concrètes et réalisables** à court/moyen terme (ex : finalisation de la matrice RBAC, déploiement d’outils DLP).


 |**Contrôle** | **Risque associé** | **Actions prévues** | **Cible de maturité** |
 |--------------|-------------------|--------------------|-----------------------|
 | **A.5.3 Séparation des tâches** | Risque de conflits d’intérêts ou d’erreurs humaines (petite structure). | Formaliser les procédures de séparation des tâches pour les données sensibles. | Automatisation des contrôles croisés via des outils de workflow. |
 | **A.5.15 Contrôle d’accès** | Accès non autorisé aux données sensibles (médicales). | Finaliser la **matrice RBAC** et automatiser les revues d’habilitation. | Déploiement d’un outil IAM (Identity and Access Management). |
 | **A.5.16 Gestion des identités** | Risque d’intrusion ou de fuite de données. | Compléter les **logs d’habilitation** et finaliser la matrice RBAC. | Intégration avec un SIEM pour une surveillance centralisée. |
 | **A.5.25 Évaluation des événements** | Détection tardive des incidents. | Automatiser la **surveillance des accès et flux** (ex : déploiement de Wazuh). | Dashboard automatisé pour la détection proactive. |
 | **A.8.12 Prévention des fuites de données** | Fuite de données sensibles. | Déployer un **outil DLP** (Data Loss Prevention) pour surveiller les flux sortants. | Automatisation complète du DLP. |
| **A.8.13 Sauvegarde des informations** | Perte de données critiques (médicales). | **Tester les sauvegardes** (RPO 24h, RTO 72h) et documenter les procédures de restauration. | Automatisation des tests de restauration. |
 | **A.8.20 Sécurité des réseaux** | Attaques réseau (ex : intrusion, DDoS). | **Segmenter davantage le réseau** (ex : isolation complète des données médicales). | Déploiement d’un NGFW (Next-Gen Firewall). |
 | **A.8.22 Séparation des réseaux** | Contamination entre réseaux (ex : CHU et PME). | **Documenter la séparation physique/logique** avec le CHU. | Audit annuel de la séparation des réseaux. |
 | **A.8.23 Filtrage web** | Accès à des sites malveillants. | **Étendre la liste noire** et déployer un filtre web centralisé. | Intégration d’un proxy sécurisé. |
 | **A.8.32 Gestion du changement** | Changements non contrôlés impactant la sécurité. | **Formaliser les revues d’impact** avant déploiement. | Automatisation des tests de non-régression. |

---

## 6. Lien vers le CSV

Cette déclaration s'appuie sur la revue complètedes 93 contrôles disponibles dans le document CSV de Déclaration d'Applicabilité ([declaration-applicabilite.csv](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-3-iso27001/declaration-applicabilite.csv)).

---

### Signatures

Atelier de validation V1.0: **20/01/2024** 

Atelier de validation V1.1: **15/02/2025**

Révision annuelle : **21/02/2026**

| Rôle | Nom | V1.0 | V1.1 |
|---|---|---|---|
| CEO SantéConnect | Martin DUPONT | 20/01/2024 | 15/02/2025 |
| DPO SantéConnect (As a Service) | Jeanne PETIT | 20/01/2024 | 15/02/2025 |
| RSSI | Claire ESPINOZA | 20/01/2024 | 15/02/2025 |

---

*Document produit dans le cadre du projet portfolio GRC - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*
*Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité.*
