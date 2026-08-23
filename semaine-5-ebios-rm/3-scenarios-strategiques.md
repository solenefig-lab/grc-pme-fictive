
# Atelier 3 - Scénarios stratégiques

> Document fictif - [Projet portfolio GRC](github.com/solenefig-lab/grc-pme-fictive) Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité. Le niveau de granularité illustre une cible de maturité, non l'état courant du marché TPE/PME santé.

---

## **Sommaire**

1. [Cadre et objectifs](#1-cadre-et-objectifs)
2. [Rappel des éléments clés de l'atelier 1 et 2](#2-rappel-des-éléments-clés-de-latelier-1-et-latelier-2)
3. [Parties prenantes (PP)](#3-parties-prenantes-pp)
4. [Scénarios stratégiques](#4-scénarios-stratégiques)
5. [Mesures de sécurité retenues pour l'écosystème](#5-mesures-de-sécurité-retenues-pour-lécosystème)
6. [Signatures](#6-signatures)

___

## 1. Cadre et Objectifs

### 1.1 Objectif

**Objectif principal :** Anticipation cadre ReCyF (application française de NIS2) dans le cadre du partenariat avec CHU Fictif (obligations spécifiques à SantéConnect comme sous-traitant de services essentiels).

Objectif de l'atelier 3 - Scénarios stratégiques
- Cartographier l’écosysteme de SantéConnect et les chemins d’attaque, pour répondre à cette question : par où passerait l’attaquant ?
- Relier les attaques globales aux parties prenantes. 
- Tester la résilience.
- Valider les conformités (contrôles ISO 27001 (A.5.29, A.8.13) et Recyf (notification ANSSI sous 24h, Art. 23)) .

_Notes :_  
_- Dans le cadre de ce portfolio, seul le scénario "Compromission API HL7/FHIR" (S1) sera développé dans l’Atelier 4._  
_- Les fiches scénarios serviront de base pour la mise à jour du PRI et du Plan d’Action NIS2 (V2)._


### 1.2. Les participants à l'atelier 

| Rôle | Nom | Responsabilité | 
| ----- | ----- | --------- | 
| CEO | Martin DUPONT | D |
| RSSI | Claire ESPINOZA | R |
| DPO | Jeanne PETIT | C |
| DevProduit | Stéphane ROY | C |
| Analyste indépendant CTI | Djibril MOUSSA | C | 

**Légende**: D = Décide, R = Responsable, C = Est Consulté

_Notes :_   
_- SantéConnect fait appel de nouveau au même analyste indépendant CTI que pour l'atelier 2 [Sources de Risque](./2-sources-risque.md) afin de garantir la cohérence et continuité de la démarche EBIOS RM engagée, mais avec une nouvelle mission (lien avec veille sectoriel, validation scenarii et enrichissement des preuves)._   


### 1.3. Livrables

1. Cartographie des Parties Prenantes et niveau de dangerosité
2. Scénarios stratégiques : principaux chemins d'attaque
3. Mesures de sécurité retenues pour l'écosystème
 
___

## 2. Rappel des éléments clés de l’Atelier 1 et l'Atelier 2

### 2.1. Atelier 1 : Cadrage et socle de sécurité

Pour garantir la cohérence de l’analyse des risques, cette section rappelle les éléments fondateurs identifiés lors de [l’Atelier 1 : Cadrage et socle de sécurité](./ebios-rm-santeconnect-cadrage.md).

**Périmètre - Services critiques :**
- API HL7/FHIR : Interface centrale pour l’échange de données médicales avec le CHU (ex : suivi cardiologique en temps réel).
- Base de données D-002 : Stockage des données sensibles des patients (ordonnances, comptes-rendus d’analyses).

**Acteurs :**
- Utilisateurs : 80 patients + 20 praticiens. 
- Partenaires : CHU Fictif (co-responsabilité RGPD/HDS), laboratoires, Stripe (paiements).

**Actifs critiques :**

| Actif | Description | Sensibilité | Propriétaire | Lien avec les VM |
| --- | --- | --- | --- | --- |
| API HL7/FHIR | Échange de données médicales avec le CHU (suivi cardiologique, alertes). | Critique | DevProduit (Stéphane) | VM1, VM2 |
| Base D-002 | Données médicales des patients (ordonnances, analyses). | Critique | DPO (Jeanne) | VM2 |
| Clés API | Accès aux services externes (CHU, laboratoires). | Critique | RSSI (Claire) | VM1, VM2 |
| App Mobile/WebApp | Interfaces utilisateurs pour le suivi cardiologique et la messagerie. | Sensible | DevProduit (Stéphane) | VM1, VM2, VM3 |
| Logs Graylog | Traçabilité des accès et des événements sécurité. | Sensible | RSSI (Claire) | VM2, VM3 |

**Menaces initiales identifiées :**
Les menaces ci-dessous ont été priorisées lors de l’Atelier 1 comme ayant un impact potentiel majeur sur les VM1 (Suivi cardiologique) et VM2 (Coffre-fort médical) :

- Compromission de l’API HL7/FHIR :
      - Impact : Indisponibilité du suivi cardiologique (VM1) + fuite de données médicales (VM2).
      - Cause racine : Vulnérabilités non patchées (ex : CVE-2023-28856) ou manque de micro-segmentation.
      - Lien avec NIS2 : Perturbation d’un service essentiel (via supply chain CHU) → obligation de notification sous 24h (Art. 23).
- Attaque par ransomware :
      - Impact : Chiffrement de la base D-002 → indisponibilité des données (VM1, VM2) + extorsion.
      - Cause racine : Sauvegardes non testées ou RPO/RTO non respectés.

- Fuite de données (D-002) :
      - Impact : Non-conformité HDS/RGPD → amende (4% du CA) + perte de confiance.
      - Cause racine : Accès non autorisés (RBAC mal configuré) ou logs non surveillés.
- Lien avec les gaps NIS2 (S4) : 
      - Gap 🔴 PCA/PRA : Scénarios de compromission de l’API ou ransomware testent la résilience (RTO 72h, RPO 24h).
      - Gap 🟡 Surveillance : Détection des attaques via Wazuh/Graylog (intégration des IOCs MISP).
      - Gap 🟡 Micro-segmentation : Limiter la propagation latérale en cas de compromission.


### 2.2. Atelier 2 : Sources de risque

**Couples SR/OV prioritaires (P1)**

**Critères :** 
Pertinence 🔴   
+ impact sur VM1 (Suivi cardiologique) et VM2 (Coffre-fort médical)   
+ lien avec les gaps NIS2 (PCA/PRA, Surveillance, Micro-segmentation).  

| Source de Risque | Objectif Visé | VM Impactées | Gaps NIS2 couverts | Scénario Atelier 3 |
| --- | --- | --- | --- | --- |
| Organisation Criminelle | Lucratif/Entrave | VM1, VM2 | PCA/PRA, Surveillance, Micro-seg | Compromission API HL7/FHIR |
| Organisation Criminelle | Lucratif (ransomware) | VM1, VM2 | PCA/PRA, Sauvegardes | Ransomware sur D-002 |
| Personnel interne mécontent | Entrave (sabotage sauvegardes) | VM1, VM2 | PCA/PRA, RBAC | Sabotage interne des sauvegardes |

**Justification :**  
- Ces 3 scénarios couvrent tous les gaps 🔴 (PCA/PRA) et 2 gaps 🟡 (Surveillance, Micro-segmentation).  
- Ils impactent directement VM1 et VM2, critiques pour SantéConnect.  
- Ils sont réalistes pour une PME santé (attaques observées sur les CHU en 2023/24).  

___

## 3. Parties prenantes (PP)

### 3.1. Cartographie des PP et évaluation niveau de dangerosité

`Est défini comme Partie Prenante toute Entité Externe ou Interne qui a un intérêt dans SantéConnect ou qui peut influencer sa sécurité, et sur les quels SantéConnect ne peut pas imposer des mesures de sécurité, sauf via contrats ou obligations légales.`

_Notes :_  
_- La RSSI, avec l'aide analyste CTI, est  responsable de la première sélection et de la priorisation des catégories de PP à évaluer dans cet atelier._  
_- Il a été choisi de distinguer les PP selon leur nature, Externe à SantéConnect et Interne, car il est probable que les mesures de sécurité soient contractualisées différemment._  
_- Les PP qui pourront également être considérées comme des sources de risque sont ici étudiées uniquement en tant que PP._  
_- Le prestataire d'hébergement OVH est à la fois un Bien Support en tant qu'infrastructure critique pour SantéConnect et une Partie Prenante car prestataire avec obligations contractuelles et réglementaires._


| ID | Nature | Type | Description | Exposition (Dépendance et Pénétration) | Fiabilité Cyber (Mâturité et Confiance)  | 
| --- |--------- | --------- | --------- | --------- | --------- | 
| PP01 | Externe | Clients B2C | Patientèle cardiologie | Utilisation terminaux propres via API SantéConnect : aucun lien ; accés utilisateur. | En général, faible connaissance cyber et mesures sécurité (friction) ; intentions probablement positives par rapport au service (amélioration de leur suivi cardiologique). |
| PP02 | Externe | Clients B2B | Médecins, praticiens | Utilisation terminaux propres avec accés administrateur métier ; accés utilisateur | Mode réactif avec prise en compte certaines mesure ; intentions supposées neutres par rapport au service. |
| PP03 | Externe | Partenaire | CHU Fictif | Partenaire clef : lien SI important et non substituable ; accés via API | Politique existante et intégrée ; intérêt pleinement compatible en tant que partenaire. |
| PP04 | Externe | Prestataire | Hébergeur : OVH Cloud | Indispensable pour hébergement données santé mais substituable ; hébergement donnée de santé | Obligations réglementaires et contractuelles fortes de sécurité ; Intérêt business et réputationnel, probablement positif |
| PP05 | Externe | Prestataire | Solution paiement : Stripe | Utile pour paiement mais substituable ; accès via API paiement | Obligations réglementaires et contractuelles fortes de sécurité ; Intérêt business et réputationnel, probablement positif |
| PP06 | Externe | Prestataire | Solution analytique web : Matomo | Utile pour données d'analyse mais substituable ; accès via API paiement | Obligations réglementaires et contractuelles fortes de sécurité ; Intérêt business et réputationnel, probablement positif |
| PP07 | Interne | Direction | CEO SantéConnect | Décisionnaire mais possible substitution ; accés limités aux données entreprises | Politique existante mais gaps encore existants ; alignement fort intérêt SantéConnect |
| PP08 | Interne | Equipe Technique | RSSI, DevOps | Indispensable pour cycle de vie SI mais possible substitution ; accés administrateurs possibles et accès physiques | Politique existante mais gaps encore existants ; intentions supposées neutres. | 
| PP09 | Interne | Equipe Métier | DevProduit, Comptabilité, RH | Utilisation via API : utile mais substituable ; accés utilisateur, possible accès physique | Mode réactif principalement avec sensibilisation politique de sécurité ; intentions supposées neutres. | 
| PP10 | Interne | Support Client | Helpdesk | Utilisation via API : utile mais substituable ; accés utilisateur et pas d'accés aux serveurs et terminaux sensibles | Mode réactif principalement avec sensibilisation politique de sécurité  ; intentions supposées neutres. | 

**Légende**:
- Exposition :  
      - Dépendance : évaluation du lien avec le Système d'Information (SI) de la PP pour la réalisation de la mission de SantéConnect ;  
      - Pénétration : pas d'accés au SI ou avec terminaux et/ ou privilège utilisateurs, accès avec privilèges administrateurs à terminaux utilisateurs et/ou accès physiques aux bureaux Santé Connect ; accès administrateurs possibles à des serveurs métiers (base de données, serveur web, serveur application ...) ; accès administrateurs à infrastructure SI (p.ex. firewall, switchs) ou physique aux salles serveurs.  
- Fiabilité Cyber :  
      - Mâturité Cyber : capacité réaction incertaine avec application mesures sécurité ponctuelles éventuelles; mode réactif avec prise en compte règle d'hygiène et règlementation ; mode réactif principalement mais politique de sécurité existante et quelques mesures préventives ; politique de management du risque intégrée et pro-active.  
      - Confiance : intentions PP non connues ; supposées neutres ; connues et probablement positives ; connues et pleinement compatibles.

**Evaluation niveau de dangerosité des Parties Prenantes**

| ID | Nature | Type | Description | Exposition : Dépendance | Exposition : Pénétration | Fiabilité Cyber : Mâturité | Fiabilité Cyber : Confiance | Niveau de dangerosité | 
| --- |--------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| PP01 | Externe | Clients B2C | Patientèle cardiologie | 1 | 1 | 1 | 3 | **0,6** |
| PP02 | Externe | Clients B2B | Médecins, praticiens | 1 | 3 | 2 | 2 | **0,8** |
| PP03 | Externe | Partenaire | CHU Fictif | 4 | 3 | 4 | 4 | **0,8** |
| PP04 | Externe | Prestataire | Hébergeur : OVH Cloud | 3 | 4 | 4 | 3 | **1** |
| PP05 | Externe | Prestataire | Solution paiement : Stripe | 2 | 3 | 4 | 3 | **0,5** |
| PP06 | Externe | Prestataire | Solution analytique web : Matomo | 2 | 3 | 4 | 3 | **0,5** |
| PP07 | Interne | Direction | CEO SantéConnect | 3 | 3 | 3 | 4 | **0,5** |
| PP08 | Interne | Equipe Technique | RSSI, DevOps | 3 | 4 | 3 | 3 | **1,3** |
| PP09 | Interne | Equipe Métier | DevProduit, Comptabilité, RH | 2 | 3 | 2 | 2 | **1,5**|
| PP10 | Interne | Support Client | Helpdesk | 2 | 2 | 2 | 2 | **1** |


**Légende**: 
- Niveaux d'exposition :
  - Dependance : aucun lien (1), lien utile (2), indispensable mais possible substitution (3), indispensable et non substituable (4) ;
  - Pénétration : accès utilisateurs (1), administrateurs sur terminaux utilisateurs (2), privilège administrateur "métier" (3), privilège "administrateur" sur infrastructure (4) :
    - Mâturité par rapport aux mesures de sécurité cyber : incertain (1) ; réactif avec application quelques mesures (2) ; réactif principalement avec politique existante (3) ; politique existante et intégrée (4).
    - Confiance que leurs intentions et intérêts convergent avec SantéConnect : inconnu (1), neutre (2), probablement positif (3), convergent (4).
- Niveau de dangerosité est calculé par `Exposition (Dépendance * Pénétration) / Fiabilité Cyber (Mâturité * Confiance)` (source méthodologique [FICHE METHODE 5 – Atelier 3](https://messervices.cyber.gouv.fr/documents-guides/Fiche_methode-Construire_lestimation_de_la_dangerosite_des_parties_prenantes_de_l_ecosysteme-atelier_3.pdf))

### 3.2. Représentation des PP selon niveau de dangerosité

**Définition des seuils :**
- Hors périmètre (< 0,5) : niveau de menace jugé négligeable.
- Zone de veille ( < 0,8): niveau de menace faible et acceptable, possible veille sur les PP sans prises en compte dans les scénarios stratégiques ;
- Zone de contrôle (< 2 ): niveau de menace tolérée et sous contrôle, vigilance particulière envers les PP concernés avec objectif à terme de réduction du risque ;
- Zone de danger ( 2+ ): niveau de menace très élevé et difficilement acceptable, mesures prioritaires pour faire baisser le niveau de dangerosité.

_Note : la gouvernance projet sous la responsabilité RSSI, avec aide analyste CT et validation direction, a fixé les PP à inclure à la limite de la zone de contrôle l'Equipe Technique de SantéConnect et le CHU Fictif et les solutions de paiement et analytique pour la zone de veille. Pour une PME de la taille de SantéConnect et dans un secteur aussi réglementé que la santé, au vu également des caractéristiques des différrentes PP, aucune n'est inclus dans le périmètre de la zone de danger._

| Hors périmètre | <span style="color:grey">Zone de veille</span> | <span style="color:orange">Zone de contrôle</span> | <span style="color:red">Zone de danger</span> |
| --------- | --------- | --------- | --------- |
|  | Solution de paiement, solution analytique web ; Patientèle cardiologie | Médecins praticiens, CHU Fictif, Hébergeur | |
| | Direction SantéConnect | Helpdesk, Equipe Métier, Equipe Technique  |  |


Sont inclus dans le périmètre d'appréciation des risques les PP dans la zone de contrôle, à savoir :
- PP Externe : Médecins praticiens, CHU Fictif, Hébergeur ;
- PP Interne : Helpdesk, Equipe Métier, Equipe Technique.

Après discussion entre les participants à l'atelier sont retenus comme PP critiques : CHU Fictif et Equipe Technique. 
Bien dans la zone de contrôle n'ont pas été retenus :
- L'hébergeur OVH est certifié HDS, soumis à des contraintes réglementaires et contractuelles forte ;
- Les médecins practiciens dont l'accés est limité à leurs propres données ;
- Les équipes helpdesk et métier qui n'ont pas d'accés admin sur les éléments d'infrastructure ni sur les données sensibles.

___

## 4. Scénarios stratégiques 

Objectif : explorer les chemins d'un attaquant (SR) pour atteindre son objectif (OV), notamment en utilisant quelles parties prenantes (PP) et actif. 

_Notes :_ 
_- Sont représentés les chemins d'attaque jugés les plus pertinents au regard des vulnérabilités identifiées et des PP critiques._  
_- Le niveau de gravité est directement issu de la cotation réalisé dans [L'Atelier 1](./1-ebios-rm-santeconnect-cadrage.md)._  
_- Dans la fiche de risques est utilisé une matrice 3 * 3 (probabilité * impact) pour évaluer les risques; ici la cotation se fait sur une base 4 et ajoute donc un seuil supplémentaire de gravité._

**Cotation de la gravité de l'impact**

| Echelle | Conséquences | Seuil de déclenchement |
| --- | --------- | --------- |
| G4 -  Critique | La survie de la société est menacée. | Indisponibilité de services critiques (dossier médical) > 24h (proche du RTO de 72h); RGPD/HDS : Toute fuite de données de santé ou falsification dès le premier patient = sanction maximale; NIS2 : Les incidents impactant la supply chain (CHU) doivent être notifiés sous 24h (Art. 23). | 
| G3 - Grave | La société va devoir fonctionner en mode très dégradé pour surmonter l'impact. | Indisponibilité coffre-fort > 24h; Falsification > 1 patient ou 1 praticien |
| G2 - Significative | La société va rencontrer quelques difficultés. | Indisponibilité messagerie (autres canaux disponibles) > 24h ; Fuite de données (hors médical) > 2 patients; perte traçabilité > 1 patient ou praticien |
| G1 - Mineure | Aucun impact opérationnel sur les performances ou la sécurité des biens et des personnes. | - |


**Ex. de logique d'enchaînement :**

`SR → exploite PP (vecteur d'entrée) → atteint actif critique → impact sur valeur métier (VM)`

Les scénarios sélectionnés se basent sur les [couples prioritaire SR/OV identifiés lors de [l'Atelier 2](#22-atelier-2--sources-de-risque) et intégrent les [PP prioritaires](#32-représentation-des-pp-selon-niveau-de-dangerosité).

| ID | Source de Risque | Vecteur d'entrée (PP) | Actif critique atteint | Impact VM | Gravité |
| -- |------------ | ------- | ------- | ------- | ------- | 
| S1 | Organisation Criminelle | CHU Fictif (API vulnérable) | Compromission API HL7/FHIR → Clés API → Base D-002 → App Mobile/WebApp | VM1 (indisponibilité suivi cardiologie), VM2 (fuite données dossier médical) | Critique (G4) |
| S2 | Organisation Criminelle | Equipe technique (phishing, cred stuffing) | Accès console OVH  → Dossier Médical (D-002): ransomware | VM1 (indisponibilité), VM2 (indisponibilité) | Critique (G4) |
| S3 | Personnel interne mécontent | Equipe Technique (accès admin) | Accès admin direct → Console OVH  → Sauvegarde WORM: sabotage | VM1, VM2 | Critique (G4) |


**S1: Compromission de l’API HL7/FHIR via le CHU Fictif**

Ce scénario est aligné sur les attaques récentes contre les CHU (ex : cyberattaque CHU Rouen 2023). 

Chemin d'attaque :  
- Exploitation : Une organisation criminelle (ex : LockBit, actif en 2023-2024) exploite une faille non patchée dans l’API HL7/FHIR du CHU  
→ Mouvement latéral : L'attaquant exploite les tokens d'authentification de la session API active pour accéder aux données de D-002  
→ Exfiltration : Vol de données médicales via l’App Mobile/WebApp  
→ Indisponibilité : L’API est rendue indisponible, bloquant le suivi cardiologique en temps réel

PP impliquée : CHU Fictif (PP03) → Vecteur d’entrée via l’API vulnérable  
Autre PP possible : Équipe Technique (PP08) → Accès administrateur aux clés API et logs (fait l'objet du Scénario S2)

**S2: Ransomware sur la base D-002 (dossier médical) via l’hébergeur OVH**
L'organisation criminelle rend indisponible les données via chiffrement et demande une rançon.

Chemin d'attaque :
Exploitation : L'attaquant utilise l'ingénierie sociale
→ Campagne phishing : vol des identifiants Équipe Technique
→ Contournement MFA : SIM swapping ou MFA fatigue pour franchir l'authentification à deux facteurs
→ Usurpation d'identité : accès à la console OVH avec les droits admin obtenus
→ Chiffrement : la base D-002 est chiffrée, rendant les données médicales inaccessibles
→ Extorsion : demande de rançon en échange de la clé de déchiffrement

PP impliquée : Equipe Technique → Vecteur d'entrée via campagne ingénierie sociale.  
Autre PP possibles : 
- Hébergeur OVH → Vecteur d’entrée via un accès administrateur compromis  
- CHU Fictif → Vecteur d’entrée via un accès administrateur compromis
_Note : Ces vecteurs sont jugés moins probables au regard des contrôles contractuels en place._


**S3 : Sabotage interne des sauvegardes**
Un membre de l'équipe technique décide de saboter intentionnellement SantéConnect en supprimant les sauvegardes.

Chemin d'attaque :
- Accès abusif : L’employé utilise ses droits administrateurs sur console OVH   
→ Effacement : Les sauvegardes WORM sont effacées, rendant la restauration impossible.

PP impliquée : Equipe Technique → Vecteur d'entrée via abus de droits
___

## 5. Mesures de sécurité retenues pour l'écosystème

### 5.1. Tableau des mesures de sécurité

| PP | Chemin d'attaque | Vulnérabilité | Mesures de sécurité | ISO 27001 | Risque Résiduel |
| ------- | ------- | ------- | ------- | ------- | ------- | 
| CHU Fictif | Compromission API HL7/FHIR → Clés API → Base D-002 → App Mobile/WebApp | APIs mal configurées ou mal patchés | Mettre à jour contractuelle CHU (clause sécurité API), Tester PCA/PRA et Configurer des alertes dans Wazuh/Graylog et Micro-segmentation | A.5.29-30, A.8.13 et A.5.17, A.8.5, A.8.20 | G3 - Grave |
| Equipe technique (phishing, cred stuffing) | Accès console OVH  → Dossier Médical (D-002): ransomware | Absence d'alertes sur comportements anormaux console OVH (Wazuh/Graylog non configuré sur cet accès) | Tester PCA/PRA, Finaliser et tester automatisation revue RBAC | A.5.9-18, A.8.2-3, A.8.5 | G2 - Significative |
| Equipe Technique (accès admin) | Accès admin direct → Console OVH  → Sauvegarde WORM: sabotage | Revues RBAC non automatisées et Surveillance continue non formalisée | Finaliser et tester automatisation revue RBAC et Configurer des alertes dans Wazuh/Graylog |  A.5.9-18, A.8.2-3, A.8.5 et A.5.17, A.8.5, A.8.20 | G3 - Grave|

_Notes :_  
_- Les risques, mesures de sécurité et contrôles sont basés sur [Plan d'action NIS2](../semaine-4-nis2/plan_action_nis2.md). Depuis le [PRA/PCA](../semaine-4-nis2/pra-pca.md) a été documenté et validé._  
_- Les tests de résilience (PRA/PCA), l'automatisation et configuration des alertes devraient permettre une plus grande réactivité aux menaces (notamment coupure accès jugé compromis) et basculer vers scénarios de crise, mais SantéConnect est dépendant du CHU Fictif sur son API._
_- Dans S3, la dépendance au facteur humain reste élevé._



### 5.2. Actions décidées à l'issue de l'Atelier 3

Rappel de la feuille de route [plan d'action NIS 2](../semaine-4-nis2/plan_action_nis2.md)


```mermaid
gantt
    title Feuille de Route — Plan d'Action NIS2
    dateFormat  YYYY-MM-DD
    section Priorité Critique
    Tester bascule automatique OVH (API HL7/FHIR, Base D-002) :a1, 2026-06-22, 8d
    Tester restauration sauvegardes OVH (RPO=0) :a2, 2026-06-22, 8d
    section Priorité Élevée
    Documenter schéma isolation APIs/bases :b1, 2026-06-23, 22d
    Documenter implémentation TLS 1.3 :b2, 2026-06-23, 22d
    Automatiser revues RBAC :b3, 2026-07-16, 30d
    Configurer alertes Wazuh/Graylog :b4, 2026-08-16, 30d
    section Priorité Moyenne
    Sélectionner formation NIS2 :c1, 2026-09-01, 30d
    section Cible 2027
    Automatiser alertes (Wazuh+Graylog+MIG) :d1, 2027-01-01, 180d
    Sélectionner et implémenter EDR :d2, 2027-01-01, 180d
 ```

| Livrable | Description | Responsable | Statut (échéance mise à jour si pertinent)|
| --------- | --------- | --------- | --------- | 
| Mise à jour clause contractuelle CHU | Ajout clause sécurité API | CEO | Nouveau (23/07/2026) |
| Planning test résilience opérationnelle | Mise en place planning et contrôle réalisation tests PCA/PRA (mensuel : sauvegarde, trimestriel : simulation panne, annuel : simulation crise) | RSSI | Nouveau (23/07/2026) |
| Automatisation revue RBAC | Documentation code, test et implémentation dans outils existants | DevOps | Livré (16/07/2026) |
| Micro-segmentation | Documenter schéma isolation APIs/bases | RSSI | Livré (23/06/2026) |
| Surveillance continue | Configurer alertes Wazuh/Graylog | DevOps | A faire (16/08/2026) |
| Surveillance continue | Automatiser alertes (Wazuh+Graylog+MIG) | DevOps | Cible : janvier 2027 |


___


## 6. Signatures

| Rôle | Nom | Date | 
| ----- | ----- | ----- | 
| CEO | Martin DUPONT | 16/07/2026 |
| RSSI | Claire ESPINOZA | 16/07/2026 |
| DPO | Jeanne PETIT |16/07/2026 |
| DevProduit | Stéphane ROY | 16/07/2026 |
| Analyste indépendant CTI | Djibril MOUSSA | 16/07/2026 |

---

*Document produit dans le cadre du projet portfolio GRC - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*
*Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité.*