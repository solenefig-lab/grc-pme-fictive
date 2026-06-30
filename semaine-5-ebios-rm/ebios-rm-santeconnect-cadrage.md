# Atelier 1 : Cadrage et socle de sécurité

> Document fictif - Projet portfolio GRC - github.com/solenefig-lab/grc-pme-fictive Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité. Le niveau de granularité illustre une cible de maturité, non l'état courant du marché TPE/PME santé.

---

## **Sommaire**

1. [Cadre et objectifs](#1-cadre-et-objectifs)
2. [Périmètre métier et technique](#2-périmètre-métier-et-technique)
3. [Evènements redoutés et niveau de gravité](#3-evènements-redoutés-et-niveau-de-gravité)
4. [Socle de sécurité](#4-socle-de-sécurité)
5. [Signatures](#5-signatures)

---

## 1. Cadre et objectifs

### 1.1. Objectifs

Objectif principal : Anticipation cadre ReCyF (application française de NIS2) dans le cadre du partenariat avec CHU Fictif.

Objectifs de l'atelier "1. Cadrage et socle de sécurité" :
- Définir le cadre, le périmètre métier et techniques
- Identifier les évènements redoutés associés
- Identifier le socle de sécurité
- Assurer la conformité avec les référentiels avec les référentiels de sécurité numérique

_Note de contexte réglementaire (juin 2026) : La transposition NIS2 en droit français n'est pas encore publiée. L'ANSSI met à disposition depuis le 17 mars 2026 le Référentiel Cyber France (ReCyF), document de travail correspondant au référentiel mentionné à l'article 14 du projet de loi Résilience. Les analyses et recommandations de ce livrable s'appuient sur la directive NIS2 (UE) 2022/2555 et anticipent le ReCyF comme référentiel cible, conformément à la posture recommandée par l'ANSSI pour les futurs assujettis._


### 1.2. Participants

| Rôle | Nom | 1. Cadrage | 2. Sources de risques | 3. Scénarios stratégiques |
| ----- | ----- | ----- | ----- | ----- |
| CEO | Martin DUPONT | D | D | D |
| RSSI | Claire ESPINOZA | R |R | R|
| DPO | Jeanne PETIT |C | C | C |
| DevProduit | Stéphane ROY | C| C |C |



### 1.3. Cadre temporel

**Cadre temporel du cadrage :** 6 mois (juin 2026 - décembre 2026), avec réévaluation trimestrielle.

Justification :
- Aligné avec contraintes légales (RGPD et ISO 27001 : audit annuel + publication CefCys attendu d'ici fin 2026)
- Prise en compte besoin stabilité et ressources limitées

**Facteur de réévaluation anticipé :**
- Incident critique ou élevé, 
- Changement périmètre, 
- Nouvelle exigence contractuelle CHU.


### 1.4. Planning ateliers EBIOS RM:
- Atelier 1. Cadrage : 1/2 journée (29/06/2026)
- Atelier 2. Sources de Risque : 2 1/2 journées (6/07/2026 et 7/07/2026)
- Atelier 3. Scénarios stratégiques : 2 1/2  (15/07/2026 et 16/07/2026)
- Atelier 4. Scenarios operationnels et 5. Traitement du risque : à planifier à partir du 16/08/2026.

_Note : le planning des 3 premiers ateliers peut être avancé avant 14/07/2026 si besoin, mais doit être réalisé avant les principaux congés d'août._

### 1.5. Documentation de référence

- [Contexte SantéConnect](../semaine-0-fondamentaux/contexte-santeconnect.md)
- [Cadrage Audit](../semaine-1-gouvernance/cadrage-audit.md)
- [Fiche Risques](../semaine-1-gouvernance/fiche-risques-e-sante.md)
- [Politique de Sécurité des Systèmes d'Information](../semaine-3-iso27001/pssi.md)
- [Déclaration d'applicabilité ISO 27001](../semaine-3-iso27001/SoA.md)
- [Plan d'action NIS2](../semaine-4-nis2/plan_action_nis2.md)

---

## 2. Périmètre métier et technique

### 2.1. Mission

**Assurer le suivi cardiologique global** (poids, tension, rappels médicaux) des patients suivis au CHU, via une plateforme mobile et web sécurisée, pour améliorer leur prise en charge et réduire les hospitalisations de 20% d’ici 2027 (_note: cible fictive_), tout en garantissant la conformité HDS, RGPD, et la résilience des services critiques (API HL7/FHIR, données médicales).


### 2.2. Valeurs métiers (VM)

| ID | Dénomination | Description | Type | Biens Support | Responsable métier |
| --- | --- | --------------- | --- | --- |  --- |
| VM1 | Suivi cardiologique | Suivi quotidien des indicateurs cardiologiques critiques (poids, tension artérielle) avec alertes automatisées en cas de valeurs anormales, et rappels de prise de médicaments pour améliorer l’observance thérapeutique | Processus | App mobile, Web app, API CHU, Données Médicales | CEO | 
| VM2 | Coffre-fort médical | Stockage sécurisé et conforme HDS des documents médicaux sensibles (ordonnances, comptes-rendus d’analyses) avec accès restreint (RBAC) et traçabilité (logs Graylog) | Stockage | App mobile, Web app, Données médicales | DPO |
| VM3 | Messagerie sécurisée | Messagerie chiffrée de bout en bout pour les échanges entre patients et praticiens ou praticiens entre eux, conforme à HDS (L.1111-8 CSP) et intégrée aux dossiers patients | Communication | App mobile, Web app | CEO | 


### 2.3. Biens supports
- **Inclus** :
  - App mobile (B2C), 
  - Web app (B2B), 
  - Interconnexion CHU : API HL7/FHIR, 
  - Traitement Données médicales, 
  - Logs (Graylog), 
  - Sauvegardes (WORM).
- **Exclus** :
  - Infrastructure réseau interne du CHU.

### 2.4 Parties prenantes

| Acteur          | Rôle                          | Niveau d'influence |
|-----------------|-------------------------------|--------------------|
| CHU             | Fournisseur de données (API)  | **Critique**       |
| OVH             | Hébergeur HDS                 | **Élevé**          |
| Stripe          | Fournisseur solution paiement | **Moyen**          |
| Patients        | Utilisateurs finaux          | **Moyen**           |
| Praticiens      | Utilisateurs B2B              | **Élevé**          |
| Laboratoires    | Utilisateur B2B restreint     | **Faible**          |

_Note :_  
_- ceci est une première ébauche des parties prenantes pour compléter la description du périmètre de l'objet étudié,_
_- son niveau d'influence correspond à sa capacité à impacter les valeurs métiers, négativement ou non._
_- l'un des objectifs de l'atelier 3 est la cartographie de menace numérique de l’écosystème, où apparait l’ensemble des parties prenantes d’intérêt et leur niveau de menace par rapport à l'objet étudié,_
_- une partie prenante a un niveau de menace critique quand elle peut devenir un vecteur d'attaque fort, par ex. dû à son accés priviliégié à l'objet étudié, à sa vulnérabilité ou son exposition._

---

## 3. Evènements redoutés et niveau de gravité

### 3.1. Cotation de la gravité de l'impact 

_Note : Dans la fiche de risques est utilisé une matrice 3 * 3 (probabilité * impact) pour évaluer les risques; ici la cotation se fait sur une base 4 et ajoute donc un seuil supplémentaire de gravité._


| Echelle | Conséquences | Seuil de déclenchement |
| --- | --------- | --------- |
| G4 -  Critique | La survie de la société est menacée. | Indisponibilité de services critiques (dossier médical) > 24h (proche du RTO de 72h); RGPD/HDS : Toute fuite de données de santé ou falsification dès le premier patient = sanction maximale; NIS2 : Les incidents impactant la supply chain (CHU) doivent être notifiés sous 24h (Art. 23). | 
| G3 - Grave | La société va devoir fonctionner en mode très dégradé pour surmonter l'impact. | Indisponibilité coffre-fort > 24h; Falsification > 1 patient ou 1 praticien |
| G2 - Significative | La société va rencontrer quelques difficultés. | Indisponibilité messagerie (autres canaux disponibles) > 24h ; Fuite de données (hors médical) > 2 patients; perte traçabilité > 1 patient ou praticien |
| G1 - Mineure | Aucun impact opérationnel sur les performances ou la sécurité des biens et des personnes. | - |


### 3.2.Recensement des principaux événements redoutés (ER)

_Note : Dans l'atelier de cadrage, les ER sont identifiés du point de vue de la société, en-dehors de tout scénario d’attaque; ils pourront être actualisés du point de vue de l'attaquant dans l'atelier 3 (élaboration des scénarios stratégiques)._


| Valeur Métier | Evènement Redouté | Impacts | Gravité |
| --- | --------- | --------- | --- | 
| VM1 - Suivi Cardiologie | Indisponibilité du dossier médical > 24 heures | Impacts sur la mission et le service de SantéConnect ; Impacts sur la santé des patients ; Impacts sur l'image et la confiance ; Impacts sur les clauses contractuelles CHU | G4 |
| VM1 - Suivi Cardiologie | Fuite de données médicales (Base D-002 du registre des traitements) > 1 patient | Impacts sur la mission et le service de SantéConnect ; Impacts sur la confidentialité des données patients (RGPD) ; Impacts sur l'image et la confiance ; Impacts sur les clauses contractuelles CHU | G4 |
| VM1 - Suivi Cardiologie | Falsification données médicales > 1 patient | Impacts sur la mission et le service de SantéConnect ; Impacts sur la santé des patients ; Impacts sur l'image et la confiance ; Impacts juridiques | G4 |
| VM1 - Suivi Cardiologie | Perte de traçabilité des mesures de suivi (tensions, poids = mesures de suivi courant, impact médical moins immédiat que les données du coffre-fort médical) > 1 patient | Impacts sur la mission et le service de SantéConnect ; Impacts sur la santé des patients ; Impacts sur l'image et la confiance | G2 |
| VM2 - Coffre-fort médical | Indisponibilité du coffre-fort > 24 heures | Impacts sur la mission et le service de SantéConnect ; Impacts sur la santé des patients ; Impacts sur l'image et la confiance | G3 |
| VM2 - Coffre-fort médical | Fuite des données stockées > 1 patient | Impacts sur la mission et le service de SantéConnect ; Impacts sur la santé des patients ; Impacts sur l'image et la confiance ; Impacts juridiques (RGPD) | G4 |
| VM2 - Coffre-fort médical | Falsification des données stockées > 1 patient | Impacts sur la mission et le service de SantéConnect ; Impacts sur la santé des patients ; Impacts sur l'image et la confiance ; Impacts juridiques (RGPD) | G4 |
| VM3 - Messagerie sécurisée | Interruption du service > 24 heures | Impacts sur la mission et le service de SantéConnect ; Impacts sur la santé des patients ; Impacts sur l'image et la confiance | G2 |
| VM3 - Messagerie sécurisée | Fuite des messages > 2 praticiens | Impacts sur la mission et le service de SantéConnect ; Impacts sur la confidentialité des patients ; Impacts sur l'image et la confiance | G2 |
| VM3 - Messagerie sécurisée | Perte de traçabilité des messages > 2 praticiens| Impacts sur la mission et le service de SantéConnect ;  Impacts sur l'image et la confiance | G1 |
| VM3 - Messagerie sécurisée | Falsification des messages > 1 praticien | Impacts sur la mission et le service de SantéConnect ;  Impacts sur l'image et la confiance  ; Impact sur la santé des patients ; Impacts juridiques | G3 |


---

## 4. Socle de sécurité

### 4.1. Liste référentiels applicables

| Réglementation | Applicabilité | Etat d'application | Lien avec les VM | Documentation lié |
|----------------|---------------|------------------| ------------------| ------------------| 
| **RGPD**       | Directe       | ✅ Conforme | VM1, VM2 (données santé = Art. 9) | [AIPD synthétique](../semaine-2-rgpd-hds/aipd-synthetique.md)|
| **HDS**        | Directe       | ✅ Conforme | VM1, VM2, VM3 (L.1111-8 CSP) | [AIPD synthétique](../semaine-2-rgpd-hds/aipd-synthetique.md)|
| **NIS2**       | Indirecte (supply chain) | 🟡 Partiel |VM1 (API CHU = Art. 21) | [Plan d'action NIS2](../semaine-4-nis2/plan_action_nis2.md) |
| **ISO 27001**  | Volontaire     | 🟡 Partiel | Toutes (SoA S3) | [PSSI](../semaine-3-iso27001/pssi.md)|


### 4.2. Inventaire des écarts

_Note : actualisation des écarts identifiés dans la Déclaration d'Applicabilité ISO 27001 et le plan d'action NIS2; les mesures déjà mises en œuvre constituent le socle de sécurité, qui sera éprouvé dans les ateliers suivants d'appréciation des risques._
 
| Type référentiel | Nom référentiel | État d'application | Écart | Justification |
| --- | --- | --- | --- | --- |
| Réglementation | NIS2 | 🟡 Appliqué avec restrictions | PCA/PRA non testé | PCA/PRA existant mais non testé en conditions réelles (RTO 72h, RPO 24h). |
| Réglementation | NIS2 | 🟡 Appliqué avec restrictions | Micro-segmentation non documentée | Segmentation réseau existante (DMZ pour APIs), en cours de documentation. |
| Réglementation | NIS2 | 🟡 Appliqué avec restrictions | Preuves de formation NIS2 manquantes | La revue des formations existantes sur le marché est prévue mais non encore priorisée dans le planning RH. |
| Norme | ISO 27001:2022 | 🟡 Appliqué avec restrictions | A.5.29-30, A.8.13 : PCA/PRA non testé | PCA/PRA existant mais non testé en conditions réelles (RTO 72h, RPO 24h).  |
| Norme | ISO 27001:2022 | 🟡 Appliqué avec restrictions | A.8.22 Séparation des réseaux | Séparation physique/logique avec le CHU en cours de documentation. |
| Norme | ISO 27001:2022 | 🟡 Appliqué avec restrictions | A.5.9-18, A.8.2-3, A.8.5 : Revues RBAC non automatisées | Script Python RBAC existant mais intégration avec Wazuh/Graylog non finalisée. |
| Norme | ISO 27001:2022 | 🟡 Appliqué avec restrictions | A.5.17, A.8.5, A.8.20 : Surveillance continue non formalisée | Configuration Wazuh/Graylog: procédure de surveillance non encore documentée. |
| Norme | ISO 27001:2022 | 🟡 Appliqué avec restrictions |  A.6.3  : Preuves de formation NIS2 manquantes | La revue des formations existantes sur le marché est prévue mais non encore priorisée dans le planning RH. |
| Norme | ISO 27001:2022 | 🔴 Non appliqué | A.6.4 Processus disciplinaire | N.I. (Non Implémenté) : Pas de processus disciplinaire spécifique aux incidents de sécurité. |
| Norme | ISO 27001:2022 | 🔴 Non appliqué | A.7.11 Utilitaires de support | N.A. (Non Applicable) : Gestion des utilités déléguée au bailleur. |
| Norme | ISO 27001:2022 | 🟡 Appliqué avec restrictions | A.5.3 Séparation des tâches | Procédures non formalisées pour les données sensibles. |
| Norme | ISO 27001:2022 | 🟡 Appliqué avec restrictions | A.5.15 Contrôle d’accès | Matrice RBAC incomplète: inclure comptes techniques, comptes de secours, accès de crise. |
| Norme | ISO 27001:2022 | 🟡 Appliqué avec restrictions | A.5.25 Évaluation des événements | Surveillance non automatisée (Wazuh/Graylog): procédure de surveillance non encore documentée. |
| Norme | ISO 27001:2022 | 🟡 Appliqué avec restrictions | A.8.12 Prévention des fuites de données | Aucun outil DLP déployé. |
| Norme | ISO 27001:2022 | 🟡 Appliqué avec restrictions | A.8.23 Filtrage web | Étendre la liste noire et déployer un filtre web centralisé.  |
| Norme | ISO 27001:2022 | 🟡 Appliqué avec restrictions | A.8.32 Gestion du changement | Revues d’impact non formalisées avant déploiement. |

---

## 5. Signatures

| Rôle | Nom | Date | 
| ----- | ----- | ----- | 
| CEO | Martin DUPONT | 29/06/2026 |
| RSSI | Claire ESPINOZA | 29/06/2026 |
| DPO | Jeanne PETIT |29/06/2026 |
| DevProduit | Stéphane ROY | 29/06/2026 |

---

*Document produit dans le cadre du projet portfolio GRC - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*
*Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité.*