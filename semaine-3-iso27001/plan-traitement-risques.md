# Plan de traitement des risques - ISO 27001:2022

> **Document produit dans le cadre du projet portfolio GRC** - [grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)  
> Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité. Le niveau de granularité illustre une cible de maturité, non l'état courant du marché TPE/PME santé.  
> Ce document illustre comment une PME e-santé peut aligner sa gestion des risques sur ses enjeux métiers (conformité RGPD/HDS, résilience opérationnelle) avec des ressources limitées.

---

## 1. Cadrage
### 1.1. Périmètre
Le périmètre est celui défini dans [Gouvernance: cadrage audit](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-1-gouvernance/cadrage-audit.md) pour les infrastructures et applications, données traitées et le personnel.

Plus de détails sont disponibles sur:
- la cartographie des actifs et l'identification des menaces dans la [Fiche de gestion des risques e-santé](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-1-gouvernance/fiche-risques-e-sante.md).
- la cartographie des données (conforme RGPD) dans le [Registre des traitements](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/registre-traitements/registre_traitement.md).
- la liste des contrôles pour la gestion du système de l'information dans la [Déclaration d'applicabilité](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-3-iso27001/declaration-applicabilite.csv).
- la politique de système d'information dans [Politique de Sécurité des Systèmes d'Information](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-3-iso27001/pssi.md)

> **Conformité ISO 27001:2022**  
> Ce document répond aux exigences suivantes :
> - **6.1.3** : Traitement des risques (méthodologie + actions documentées).
> - **6.1.4** : Acceptation des risques résiduels (seuils définis).
> - **A.5.30** : Préparation à la gestion des incidents (lien avec le PCA/PRA).
> - **A.12.4** : Enregistrement des activités (logs Graylog).

### 1.2. Objectif

Objectif: Identifier, évaluer et traiter les risques pour 
- garantir la conformité RGPD/HDS, 
- sécuriser les données médicales critiques de SantéConnect, 
- permettre un pilotage budgétaire sans surcoût (budget < 10k€/an).
- prioriser les actions** avec un budget maîtrisé (< 10k€/an).
- prouver la conformité aux audits et aux partenaires

Structure: risque global, adapté pour petite structure + accent mis sur sécurisation données médicales renforcées

Le cycle de gestion des risques s'appuie sur la norme ISO 27005 s’appuie sur un cycle de gestion du risque composé de plusieurs étapes clés : Définition du contexte, Identification des risques, Analyse et évaluation, Traitement des risques, Acceptation des risques résiduels, Suivi et réévaluation réguliers.
Ce cadre permet de garantir une prise de décision cohérente, alignée avec les objectifs métiers.

### 1.3. Parties prenantes

|  **Rôle**               | **Responsabilité**                         | **Implication dans le PTR**                     |
|------------------------|------------------------------------------------|-----------------------------------------------|
| **CEO** | Valider les arbitrages **budget/risque** et allouer les ressources.    | Approbation du plan, suivi trimestriel.       |
| **RSSI** | Piloter la **mise en œuvre** des mesures et le **suivi des risques**.      | Rédaction du plan, suivi mensuel.  |
| **DPO**   | Garantir la **conformité RGPD/HDS** et valider les mesures liées aux données.   | Revue des risques liés aux données personnelles. |
| **Responsable Produit** | Intégrer les **exigences de sécurité** dans les fonctionnalités (Privacy by Design). | Collaboration sur les risques liés au code. |
| **DevOps** | Appliquer les **mesures techniques** (ex : RBAC, sauvegardes).                  | Mise en œuvre des contrôles.     |

---

## 2. Synthèse Exécutive

**Objectifs clés** :
- **Réduire les risques critiques** (score ≥ 6) à un niveau acceptable (≤ 4) d’ici **6 mois**.
- **Maintenir les risques modérés** (score ≤ 5) sous contrôle avec des **mesures compensatoires**.
- **Transférer les risques** aux tiers certifiés (OVH, Stripe, CHU) via des **contrats conformes**.
- **Prouver la conformité** aux audits et partenaires (ex : CHU, patients, autorités de santé).


### Synthèse des Actions Prioritaires (Section 4.1)


| Risque | ID | Score | Mesure Clé | Budget | Échéance | Impact Attendu | Responsable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APIs mal configurées | R-API-01 | 9 | Déploiement d’un WAF + rotation des clés API | Élevé (>5k€) | 1 mois | Réduction du score à 4 | RSSI |
| Usurpation d’identité | R-DON-01 | 9 | Formation anti-phishing + MFA systématique | Moyen (1-5k€) | 2 mois | Réduction du score à 3 | DPO  + RSSI |
| Absence de TLS | R-DON-02 | 9 | Chiffrement TLS 1.3 + audit des transactions (contrôle compensatoire : TLS délégué à Stripe) | Moyen (1-5k€) | 1 mois | Réduction du score à 3 | DevOps |
| Injection SQL/Ransomware | R-DON-03 | 6 | Protection contre les malwares + sauvegardes chiffrées | Moyen (1-5k€) | 3 mois | Réduction du score à 4 | DevOps|
| Applications grand public | R-APP-01 | 6 | Audit de sécurité + tests de pénétration | Élevé (>5k€) | 2 mois | Réduction du score à 4 | DevOps |
| Plateforme B2B : accès non restreint | R-PLAT-01 | 6 | Matrice RBAC révisée + restriction des accès au code source | Faible (<1k€) | 1 mois | Réduction du score à 3 | RSSI |
| Interconnexion CHU | R-INT-01 | 6 | Segmentation réseau + revue des contrats CHU | Moyen (1-5k€) | 2 mois | Réduction du score à 4 | RSSI |
| Délai de notification des violations | R-GOV-02 | 6 | Procédure de notification (72h) + tests semestriels | Faible (<1k€) | 2 mois | Réduction du score à 3 | RSSI |
| Vulnérabilités non patchées | R-ISO-02 | 6 | Automatisation des correctifs + tests d’intrusion annuels | Moyen (1-5k€) | 3 mois | Réduction du score à 4 | DevOps  |
| Absence de procédure de réponse aux incidents | R-NIS2-02 | 6 | Rédiger la procédure + former l’équipe | Faible (<1k€) | 2 mois | Réduction du score à 3 | RSSI |
| Données PII exposées via App Mobile | R-DON-04 | 6 | Audit de l’App Mobile + chiffrement des données locales | Moyen (1-5k€) | 3 mois | Réduction du score à 4 | DevOps | 

_Note : Les estimations budgétaires sont indicatives et basées sur des ordres de grandeur marché PME (sources : grilles tarifaires publiques éditeurs, benchmarks ANSSI PME). Un chiffrage précis nécessite une consultation fournisseurs et une évaluation du temps interne DevOps/RSSI._


### Bilan des Risques


 | **Section** | **Nombre de Risques** | **Score Moyen** | **Budget** | **Statut** |
 |--------------------|-----------------------|-----------------|------------|------------|
 | **4.1 À Réduire** | 11 | 7.3 | _chiffrage précis via consultation / évaluation_| **Priorité absolue** |
 | **4.2 Acceptés** | 7 | 3.4 | 0 € | Contrôlés par des mesures existantes |
 | **4.3 Transférés** | 2 | 2.5 | 0 € | Délégés à des tiers certifiés (OVH, Stripe, CHU) |
 | **4.4 Regroupés** | ~35 | ≤ 3 | 0 € | Risques maîtrisés (sensibilisation, maintenance, contrats) |



### Points Clés pour la Direction

1. **Priorité aux risques score ≥ 6** :
   - **8 risques critiques** nécessitent une action immédiate (ex : R-API-01, R-DON-01).
   - **Budget** à valider pour couvrir ces risques.

2. **Risques transférés** :
   - **OVH, Stripe, et le CHU** portent une partie des risques (ex : sécurité physique, chiffrement TLS).
   - **Vérifier les contrats** (Art. 28 RGPD, HDS, PCI-DSS) pour s’assurer que les tiers maintiennent leurs certifications.

3. **Conformité réglementaire** :
   - Le PTR est **aligné sur RGPD, HDS, et NIS2**.
   - **Preuves** : Contrats signés, certifications tiers, et rapports d’audit.

4. **Suivi et Amélioration Continue** :
   - **Tableau de bord mensuel** pour suivre les KPIs (ex : % d’APIs protégées, délai de notification).
   - **Revue trimestrielle** avec la direction pour ajuster les priorités.


### Prochaines Étapes
1. **Validation du budget** par le CEO (Martin DUPONT) pour les risques critiques (Section 4.1).
2. **Priorisation des actions** :
   - Commencer par les risques **score 9** (R-API-01, R-DON-01, R-DON-02).
   - Étaler les coûts sur **6 mois** si nécessaire.
3. **Signature du PTR** par le **CEO, DPO, et RSSI** pour engagement formel.
4. **Mise en œuvre** :
   - **Mois 1** : Déploiement du WAF (R-API-01) + Chiffrement TLS (R-DON-02).
   - **Mois 2** : Formation anti-phishing (R-DON-01) + Segmentation réseau (R-NIS2-01).

---

## 3. Méthodologie et Justifications

### 3.1. Méthode d’Identification des Risques

Objectif : Lister les risques pertinents pour le périmètre défini.

Sources utilisées :
- la cartographie des actifs et l'identification des menaces dans la [Fiche de gestion des risques e-santé](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-1-gouvernance/fiche-risques-e-sante.md).
- la cartographie des données (conforme RGPD) dans le [Registre des traitements](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/registre-traitements/registre_traitement.md).
- la liste des contrôles pour la gestion du système de l'information dans la [Déclaration d'applicabilité](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-3-iso27001/declaration-applicabilite.csv).
- la politique de système d'information dans [Politique de Sécurité des Systèmes d'Information](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-3-iso27001/pssi.md)
- Réglementations : voire récapitulatif ci-dessous
- Retours terrain (pré-supposés dans le cadre de ce portfolio): Incidents passés, audits, feedbacks métiers.

**Risques réglementaires :**

| Réglementation | Risques Typiques pour SantéConnect | Source |
| --- | --- | --- |
| RGPD | Accès non autorisé aux données personnelles, fuite de données, non-respect des droits des patients (Art. 15-17). | [Art. 5, 32, 33-34](https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32016R0679) |
| HDS | Accès non autorisé aux données de santé, perte de traçabilité, non-conformité des sous-traitants. | [R. 1111-10, R. 1112-7](https://www.legifrance.gouv.fr/) |
| ISO 27001:2022 | Risques liés aux contrôles de l’Annexe A (ex : A.5.15, A.8.3, A.12.4). | [Annexe A](https://www.iso.org/standard/54534.html) |
| NIS2 | Risques liés à la résilience (PCA/PRA non testé, incidents non détectés). | [Directive NIS2](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive) |

Exhaustivité : Tous les risques liés aux actifs critiques sont identifiés.
Pertinence : Les risques sont spécifiques à SantéConnect (ex : SPOF sur le dev produit).

### 3.2. Critères d'évaluation des risques de sécurité de l'information

Grille de cotation, aligné sur ISO 27005 : Score (1 à 9) = Impact (1 à 3) * Probabilité (1 à 3)

_Note: Les scores reflètent les risques bruts (avant mesures existantes). Le risque résiduel est évalué après application des contrôles et documenté dans la colonne dédiée._

#### Critères d'évaluation de l'impact

| Score | Niveau | Définition |
|-------|--------|------------|
| 1 | Faible | Conséquence limitée, sans effet sur le fonctionnement |
| 2 | Modéré | Perturbation partielle, impact métier limité |
| 3 | Critique | Conséquence importante, effet négatif sur le bon fonctionnement |

#### Critères d'évaluation de la probabilité

| Score | Niveau | Critères objectifs |
|-------|--------|--------------------|
| 1 | Faible | Accès interne uniquement + contrôles forts en place |
| 2 | Modérée | Exposé Internet OU contrôles partiels / supposés |
| 3 | Élevée | Exposé Internet + contrôles faibles ou absents |



### 3.3. Critères d'acceptabilité des risques de sécurité de l'information


| Niveau | Score (Impact × Probabilité) | Seuil d'acceptation |
|--------|------------------------------|-------------------|
| 🟢 Faible | 1 – 2 | Risque acceptable (surveillance): mpact faible (ex : fuite de données non sensibles) ou probabilité faible (ex : attaque ciblée improbable) |
| 🟠 Modéré | 3 – 5 | Risque acceptable sous conditions (mesures compensatoires) |
| 🔴 Haut | 6 – 9 | Risque inacceptable (à traiter en priorité): impact critique (ex : sanction RGPD, perte de données médicales) ou probabilité élevée (ex : accès non contrôlé).|

Pour la gestion des risques, la norme ISO 27001 décrit quatre actions possibles : 
- **Traiter** le risque avec des contrôles de sécurité qui réduisent la probabilité qu'il se produise 
- **Éviter** le risque en empêchant les circonstances où il pourrait se produire 
- **Transférer** le risque avec un tiers (c'est-à-dire, externaliser les efforts de sécurité à une autre entreprise, souscrire une assurance, etc.) 
- **Accepter** le risque car le coût d'y remédier est supérieur aux dommages potentiels 

---

## 4. Plan de Traitement des Risques

### 4.1. Risques à Réduire (Score ≥ 6)


| ID | Impact | Probabilité | Score | Responsable | Indicateur de suivi |
| --- | --- | --- | --- | --- | --- |
| R-API-01 | 3 | 3 | 9 | RSSI | % d'APIs protégées par WAF (suivi hebdo) + Nombre de clés API rotées/mois. |
| R-APP-01 | 3 | 2 | 6 | DevOps | % d'applications auditées (suivi mensuel) + Nombre de vulnérabilités critiques corrigées/semaine. |
| R-PLAT-01 | 3 | 2 | 6 | RSSI | % des accès conformes à la matrice RBAC (suivi hebdo) + Nombre d’accès au code source restreints. |
| R-INT-01 | 3 | 2 | 6 | RSSI | % d’interconnexions segmentées (suivi mensuel) + Nombre de contrats CHU revus. |
| R-DON-01 | 3 | 3 | 9 | RSSI  | % d’employés formés au phishing (suivi mensuel) + % d’accès sensibles protégés par MFA (suivi hebdo). |
| R-DON-02 | 3 | 3 | 9 | DevOps | % de transactions chiffrées en TLS 1.3 (suivi hebdo) + Nombre d’audits de sécurité réalisés. |
| R-DON-03 | 3 | 2 | 6 | DevOps  | Nombre de vulnérabilités critiques corrigées/semaine + % de sauvegardes testées/mois. |
| R-DON-04 | 3 | 2 | 6 | DevOps | % de données sensibles protégées dans l’App Mobile + Nombre d’audits de sécurité | Données PII sensibles exposées via App Mobile (A.8.1, A.8.12, A.8.20, A.8.26). |
| R-GOV-02 | 3 | 2 | 6 | RSSI | % d’incidents notifiés dans les délais (suivi trimestriel) + Nombre de tests de procédure réussis. |  
| R-ISO-02 | 3 | 2 | 6 | DevOps | % de vulnérabilités critiques corrigées sous 30 jours + Nombre de tests d’intrusion réalisés | Vulnérabilités non patchées (A.8.8) + Absence de tests d’intrusion (A.8.29). |
| R-NIS2-02 | 3 | 2 | 6 | RSSI | % d’incidents traités dans les délais (suivi mensuel) + Nombre de vulnérabilités gérées | Absence de procédure de réponse aux incidents (A.5.25) + Vulnérabilités non gérées (A.8.8). |


_Note : R-DON-02: Contrôle compensatoire partiel avec chiffrement TLS délégué à Stripe (PCI-DSS Req. 4)._

### 4.2. Risques Acceptés (Score ≤ 5)

Risques contrôlés par des mesures existantes


| ID   | Impact | Probabilité | Score | Responsable       | Indicateur de suivi | Justification d'acceptation |
|-----------|------------|-----------------|----------|------------------------|-------------------------|--------------------------------|
| R-DB-01   | 2          | 2               | 4        | RSSI | % de données sensibles masquées (suivi trimestriel) + Vérification annuelle de la certification HDS | Contrôle transféré partiellement à OVH (certifié HDS). Risque résiduel acceptable car OVH porte la responsabilité légale. |
| R-GOV-01  | 3          | 1               | 3        | DPO  | % de traitements documentés (suivi mensuel) + Nombre de PIA validés | Risque contrôlé par livrable S2 (registre des traitements existant). Mise à jour trimestrielle requise. |
| R-DON-10  | 1          | 2               | 2        | DPO   | Aucune                 | Données volontairement publiques (obligation légale ou métier). Risque faible et accepté car conforme à la finalité déclarée (RGPD Art. 5.1.b). |
| R-ISO-01 | 3 | 1 | 3 | RSSI | % de la politique de sécurité finalisée | Absence de politique de sécurité (A.5.1) + Accès non autorisé (A.5.15, A.5.16, A.5.17, A.5.18). Risque contrôlé car politique en cours de rédaction. |
| R-ISO-03  | 2          | 2               | 4        | RSSI  | % d’accès revus (suivi trimestriel) + Nombre de configurations auditées | Contrôle partiel en place (matrice RBAC, configurations OVH documentées). Revues des accès réalisées annuellement. |
| R-NIS2-01 | 2          | 2               | 4        | RSSI | % de réseaux segmentés (suivi trimestriel) + Nombre d’alertes EDR/mois | Contrôle partiel en place (Graylog, pare-feu). Supervision basique existante, mais détection des intrusions à améliorer. |
| R-GOV-03 | 2 | 2 | 4 | Juridique + RSSI | % de contrats conformes RGPD Art. 28 | Responsabilités sécurité non définies (A.5.3) + Contrats sous-traitants non conformes (A.5.21, A.5.22, A.5.31). |
| R-HDS-01 | 2 | 2 | 4 | RSSI | % de données de santé chiffrées au repos + Vérification annuelle de la certification HDS | Hébergement non certifié HDS (A.5.21) + Données santé non chiffrées (A.8.11, A.8.13, A.8.20). |


### 4.3. Risques Transférés/Évités
Risques dont le contrôle est entièrement porté par un tiers avec contrat en place


| ID   | Risque | Décision | Moyen de transfert/évitement| Propriétaire | Référence contractuelle |
|-----------|------------|--------------|----------------------------------|------------------|-----------------------------|
| R-HDS-02  | Accès physique non contrôlé aux serveurs | **Transféré** | Sécurité physique **entièrement déléguée à OVH** (certifié HDS, R. 1111-10). | RSSI  | Contrat OVH Art. 28 RGPD + Certification HDS (R. 1111-10) + Convention de co-responsabilité |
| T-020    | Transfert de données hors UE non conforme | **Transféré** | Transfert **délégué à OVH/Stripe** (clauses SCC ou BCR en place). | RSSI  | Contrat OVH Art. 44-49 RGPD + Contrat Stripe (PCI-DSS Req. 12) + Clauses Contractuelles Standard (SCC) |

### 4.4 Regroupement des Risques (Score ≤ 3)


|**Thème** | **Contrôles couverts (ISO 27001:2022)** | **Score type** | **Justification** | **Responsable de surveillance** |
|-----------|----------------------------------------|----------------|------------------|--------------------------------|
| **Sensibilisation et formation** | A.6.3 Sensibilisation, éducation et formation à la sécurité de l'information | 1-2 | Formation annuelle obligatoire + tests de phishing trimestriels. **Risque résiduel faible** (employés sensibilisés). | DPO |
| **Maintenance et correctifs** | A.8.8 Gestion des vulnérabilités techniques, A.8.32 Gestion du changement | 2-3 | Correctifs appliqués sous **30 jours** + tests d’intrusion annuels. **Risque résiduel faible** pour une PME. | DevOps |
| **Contrats et conformité** | A.5.21 Gestion de la sécurité de l'information dans la chaîne d'approvisionnement des TIC, A.5.22 Surveillance, examen et gestion des changements des services fournisseurs, A.5.31 Exigences légales, réglementaires et contractuelles | 2 | Contrats RGPD Art. 28 signés avec tous les sous-traitants (OVH, Stripe, CHU). **Risque résiduel faible**. | Juridique + RSSI |
| **Sauvegardes et continuité** | A.8.13 Sauvegarde des informations (hors données médicales critiques, déjà couvertes en 4.1), A.5.30 Préparation des TIC à la continuité des activités  | 2-3 | Sauvegardes **automatiques et testées trimestriellement**. **Risque résiduel faible** (PCA/PRA basique en place). | DevOps  |

----

## 5. Risques par Thème ISO 27001:2022
Le mapping détaillé risques/contrôles est disponible en Annexe 7 (Matrice Complète des Risques).

----

## 6. Revue et validation

### 6.1 Validation et Approbation

Objectif : Obtenir l’engagement formel de la direction (ISO 27001:2022, clause 5.1) et valider l’adéquation du PTR avec la PSSI, le SoA, et les objectifs métiers de SantéConnect.

| Critère | Justification | Preuve |
| --- | --- | --- |
| Revue par la direction | Le plan a été présenté et validé par le CEO (Martin DUPONT) lors de l’atelier du 15/02/2025. | PV de revue de direction signé |
| Ressources allouées | Budget validé pour les mesures prioritaires (Section 4.1) + 0.5 FTE (DevOps) pour la maintenance de Graylog et les sauvegardes. | Décision budgétaire signée par le CEO |
| Intégration au SMSI | Le PTR est lié à la PSSI (mesures A.5.15, A.8.21, etc.) et au SoA (10 contrôles prioritaires). | Références croisées dans PSSI et SoA/Déclaration d'applicabilité. |
| Cohérence réglementaire | Alignement avec RGPD (Art. 30, 32, 33-34), HDS (R. 1111-10, R. 1112-7), et NIS2 (Obj. 3, 8, 10, 12, 20). | Matrice de conformité réglementaire |

### 6.2 Suivi et Revue

Objectif : Assurer l’efficacité des mesures et leur mise à jour continue (ISO 27001:2022, clause 9.1 - Surveillance, mesure, analyse et évaluation).

| Critère | Justification | Preuve |
| --- | --- | --- |
| Fréquence de revue | Trimestrielle pour les risques critiques (score ≥ 6) et annuelle pour les autres. | Calendrier intégré dans Suivi Plan Traitement des Risques. |
| Indicateurs | Mesure de l’efficacité via des KPIs (ex : % d’APIs protégées par WAF, délai moyen de notification des incidents). | Tableau de bord dans Suivi Plan Traitement des Risques. |
| Amélioration continue | Mise à jour du PTR en cas de : Nouveaux risques (ex : nouveau fournisseur, changement réglementaire),Évolution du contexte (ex : augmentation du volume de données sensibles), Incidents (ex : faille de sécurité détectée). | Historique des versions  |
| Audit interne  | Vérification semestrielle de l’application des mesures par le RSSI.      | Rapport d’audit 2026  |

### 6.3 Signatures

Historique des validations :

| Version | Date | Description | Lien |
| --- | --- | --- | --- |
| V1.0 | 20/03/2024 | Version initiale (atelier de validation). | [v1.0.md] |
| V1.1 | 15/02/2025 | Intégration des retours de la direction. | [v1.1.md] |
| Révision annuelle | 21/02/2026 | Revue annuelle complète. | [revision-2026.md] |

Signataires :

| Rôle | Nom | V1.0 | V1.1 | Révision 2026 |
| --- | --- | --- | --- | --- |
| CEO SantéConnect | Martin DUPONT | 20/03/2024 | 15/02/2025 | 21/02/2026 |
| DPO SantéConnect (As a Service) | Jeanne PETIT | 20/03/2024 | 15/02/2025 | 21/02/2026 |
| RSSI | Claire ESPINOZA | 20/03/2024 | 15/02/2025 | 21/02/2026 |

---

## 7. Annexe
### Matrice Complète des Risques

| ID        | Catégorie   | Risque                                                                                                                | Référence source                                                                           | Actif / Processus                                             | Contrôle ISO 27001:2022                                                                                                                                                                                                                                                 | Réglementation                                                                         |
| --------- | ----------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| R-DON-02  | Données     | Fuite de données : Écoute clandestine (absence TLS) + Transactions Stripe (fraude)                                    | Fiche risques (FR-14, FR-15) + Matrice RBAC (RBAC-17, RBAC-19)                             | Données paiement (T-003)                                      | A.5.14 Transfert d'informations ; A.8.20 Sécurité des réseaux ; A.8.21 Sécurité des services réseaux ; A.8.25 Cycle de vie du développement sécurisé                                                                                                                    | RGPD Art. 5, 32, 33, 34 · NIS2 Obj. 3, 8, 9, 10, 12, 20 · PCI-DSS Req. 4, 6, 7, 10, 11 |
| R-DON-03  | Données     | Injection SQL/XSS + Ransomware (chiffrement données santé)                                                            | Fiche risques (FR-16, FR-17)                                                               | Données santé (D-002)                                         | A.8.7 Protection contre les logiciels malveillants ; A.8.13 Sauvegarde des informations ; A.8.26 Exigences de sécurité des applications ; A.8.28 Codage sécurisé ; A.8.29 Tests de sécurité en développement et en réception                                            | RGPD Art. 5, 9, 32, 33, 34, 90 · NIS2 Obj. 8, 10, 12, 20                               |
| R-DON-04  | Données     | Données PII sensibles exposées via App Mobile + ciblées par hackers                                                   | Fiche risques (FR-18)                                                                      | Données personnelles/santé (D-002)                            | A.8.1 Dispositifs terminaux utilisateurs ; A.8.12 Prévention des fuites de données ; A.8.20 Sécurité des réseaux ; A.8.26 Exigences de sécurité des applications                                                                                                        | RGPD Art. 5, 9, 28, 32, 33, 34 · NIS2 Obj. 8, 10, 12, 20                               |
| R-DON-10  | Données     | Données PII disponibles publiquement (annuaires, web)                                                                 | Fiche risques (FR-21)                                                                      | Données praticiens                                            | A.5.9 Inventaire des informations ; A.5.10 Utilisation acceptable des informations et autres ressources associées ; A.8.3 Restriction d'accès à l'information                                                                                                           | RGPD Art. 5                                                                            |
| R-GOV-01  | Gouvernance | Absence de registre des traitements (RGPD Art. 30) + Absence de PIA (RGPD Art. 35)                                    | PSSI (PSSI-4) + RGPD Art. 30, 35                                                           | Registre des traitements, Données santé (D-002)               | A.5.31 Exigences légales, réglementaires et contractuelles ; A.5.33 Protection des documents ; A.5.36 Conformité aux politiques, règles et normes en matière de sécurité de l'information                                                                               | RGPD Art. 30, 35 · HDS                                                                 |
| R-GOV-02  | Gouvernance | Délai de notification des violations (RGPD Art. 33-34) + Absence de procédure de gestion des incidents (NIS2 Obj. 12) | PSSI (PSSI-5) + RGPD Art. 33-34, NIS2 Obj. 12                                              | Données personnelles/santé                                    | A.5.25 Évaluation et décision relatives aux événements de sécurité de l'information ; A.5.27 Leçons tirées des incidents de sécurité de l'information ; A.5.29 Sécurité de l'information en cas de perturbation ; A.5.37 Procédures opérationnelles documentées         | RGPD Art. 33-34 · HDS R.1112-7 · NIS2 Obj. 12                                          |
| R-GOV-03  | Gouvernance | Responsabilités sécurité non définies (CEO/RH) + Contrats sous-traitants non conformes (RGPD Art. 28)                 | PSSI (PSSI-4) + Matrice RBAC (RBAC-01, RBAC-02, RBAC-10) + RGPD Art. 28                    | Données financières, RH/Paie, Fournisseurs (OVH, Stripe, CHU) | A.5.3 Séparation des tâches ; A.5.21 Gestion de la sécurité de l'information dans la chaîne d'approvisionnement des TIC ; A.5.22 Surveillance, examen et gestion des changements des services fournisseurs ; A.5.31 Exigences légales, réglementaires et contractuelles | RGPD Art. 24, 28 · ISO 27001:2022                                                      |
| R-HDS-01  | HDS         | Hébergement non certifié HDS (OVH) + Données santé non chiffrées au repos                                             | HDS R.1111-10, R.1112-8 + PSSI (PSSI-6)                                                    | Hébergement OVH, Base de données (D-002)                      | A.5.21 Gestion de la sécurité de l'information dans la chaîne d'approvisionnement des TIC ; A.8.11 Masquage des données ; A.8.13 Sauvegarde des informations ; A.8.20 Sécurité des réseaux                                                                              | HDS R.1111-10, R.1112-8 · RGPD Art. 32                                                 |
| R-HDS-02  | HDS         | Accès physique non contrôlé aux serveurs + Journalisation incomplète des accès aux données santé                      | HDS R.1112-8, R.1112-7 + PSSI (PSSI-5)                                                     | Serveurs OVH, Logs (Graylog), Données santé (D-002)           | A.7.3 Sécurisation des bureaux, des salles et des installations ; A.7.4 Surveillance de la sécurité physique ; A.7.8 Implantation et protection des équipements ; A.8.15 Enregistrement                                                                                 | HDS R.1112-8, R.1112-7 · RGPD Art. 5, 32                                               |
| R-ISO-01  | ISO 27001   | Absence de politique de sécurité (A.5.1) + Accès non autorisé aux données d'authentification (RBAC incomplet)         | ISO 27001:2022 (A.5.1) + Matrice RBAC (RBAC-03, RBAC-04, RBAC-08, RBAC-09) + PSSI (PSSI-8) | Accès administrateurs, Tous les actifs                        | A.5.15 Contrôle d'accès ; A.5.16 Gestion des identités ; A.5.17 Informations d'authentification ; A.5.18 Droits d'accès ; A.5.3 Séparation des tâches                                                                                                                   | ISO 27001:2022 · RGPD Art. 5, 32                                                       |
| R-ISO-02  | ISO 27001   | Vulnérabilités non patchées (A.8.8) + Absence de tests d'intrusion                                                    | ISO 27001:2022 (A.8.8) + PSSI (PSSI-9)                                                     | Serveurs, applications, APIs                                  | A.8.8 Gestion des vulnérabilités techniques ; A.8.29 Tests de sécurité en développement et en réception ; A.8.16 Activités de surveillance ; A.8.32 Gestion du changement                                                                                               | ISO 27001:2022 · RGPD Art. 32 · NIS2 Obj. 10, 20                                       |
| R-ISO-03  | ISO 27001   | Revues des accès non réalisées (A.5.18) + Configuration infrastructure non sécurisée (OVH)                            | ISO 27001:2022 (A.5.18) + Matrice RBAC (RBAC-04, RBAC-20) + PSSI (PSSI-6)                  | Infrastructure OVH, Tous les accès (RBAC)                     | A.5.18 Droits d'accès ; A.8.9 Gestion de la configuration ; A.8.20 Sécurité des réseaux ; A.8.22 Séparation des réseaux                                                                                                                                                 | ISO 27001:2022 · HDS R.1112-8 · NIS2 Obj. 3                                            |
| R-NIS2-01 | NIS2        | Absence de détection des intrusions + Absence de supervision 24/7 + Absence de segmentation réseau                    | NIS2 Obj. 20, Obj. 3 + PSSI (PSSI-10)                                                      | Réseau, serveurs, APIs, WebApp, App Mobile                    | A.8.16 Activités de surveillance ; A.8.20 Sécurité des réseaux ; A.8.22 Séparation des réseaux ; A.5.7 Renseignements sur les menaces                                                                                                                                   | NIS2 Obj. 3, 20 · ISO 27001:2022                                                       |
| R-NIS2-02 | NIS2        | Absence de procédure de réponse aux incidents + Vulnérabilités non gérées                                             | NIS2 Obj. 12, Obj. 10 + PSSI (PSSI-9, PSSI-10)                                             | Tous les systèmes, Serveurs, applications                     | A.5.25 Évaluation et décision relatives aux événements de sécurité de l'information ; A.5.27 Leçons tirées des incidents de sécurité de l'information ; A.8.8 Gestion des vulnérabilités techniques ; A.8.16 Activités de surveillance                                  | NIS2 Obj. 10, 12 · ISO 27001:2022                                                      |
| T-020     | Juridique   | Transfert de données hors UE non conforme                                                                             | RGPD Art. 44-49 + PSSI (PSSI-10)                                                           | Données personnelles/santé (si applicable)                    | A.5.14 Transfert d'informations ; A.5.21 Gestion de la sécurité de l'information dans la chaîne d'approvisionnement des TIC ; A.5.31 Exigences légales, réglementaires et contractuelles                                                                                | RGPD Art. 44-49 · ISO 27001:2022                                                       |

### Livrables et documentations liées

| Document | Lien | Description | Référence dans le PTR |
| --- | --- | --- | --- |
| Cadrage Audit | [cadrage-audit.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-1-gouvernance/cadrage-audit.md) | Périmètre des infrastructures, applications, données traitées et personnel. | Section 1.1 (Périmètre) |
| Fiche de Gestion des Risques e-Santé | [fiche-risques-e-sante.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-1-gouvernance/fiche-risques-e-sante.md) | Cartographie des actifs et identification des menaces. | Sections 1.1, 3.1, 7 (Matrice Complète) |
| Registre des Traitements | [registre_traitement.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/registre-traitements/registre_traitement.md) | Cartographie des données (conforme RGPD). | Sections 1.1, 3.1, 4.2 (R-GOV-01) |
| Déclaration d'Applicabilité (SoA) | [declaration-applicabilite.csv](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-3-iso27001/declaration-applicabilite.csv) | Liste des contrôles ISO 27001:2022 appliqués ou non. | Sections 1.1, 3.1, 4.1, 4.2, 4.3 |
| Politique de Sécurité des Systèmes d'Information (PSSI) | [pssi.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-3-iso27001/pssi.md) | Politique de sécurité globale. | Sections 1.1, 3.1, 6.1 |
| PV de Revue de Direction | [pv-revue-direction.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/plan-traitement-risques/pv-revue-direction.md) | Preuve de validation du PTR par la direction. | Section 6.1 |
| Tableau de Bord de Suivi | [suivi.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/plan-traitement-risques/suivi.md) | Suivi des KPIs et statut des mesures. | Section 6.2 |
| Rapport d'Audit Interne 2026 | [audit-interne-2026.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/plan-traitement-risques/audit-interne-2026.md) | Résultats des vérifications semestrielles. | Section 6.2 |
| Convention CHU | [convention-chu.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/note-co-responsabilite-chu.md) | Accord de co-responsabilité avec le CHU pour les interconnexions. | Sections 4.1 (R-INT-01), 4.3 |
| Contrat OVH | [contrat-ovh.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/synthese-clauses-sous-traitants.md) | Contrat incluant les clauses RGPD Art. 28 et HDS. | Sections 4.1 (R-HDS-01), 4.3 |
| Contrat Stripe | [contrat-stripe.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/synthese-clauses-sous-traitants.md) | Contrat incluant les clauses PCI-DSS et RGPD Art. 28. | Sections 4.1 (R-DON-02), 4.3 |
| Matrice de Conformité Réglementaire | Conformité réglementaire: voir section 3.1| Alignement avec RGPD, HDS, et NIS2. | Section 3.1 |
