# Atelier 2 : Identification des Sources de Risque

> Document fictif - [Projet portfolio GRC](github.com/solenefig-lab/grc-pme-fictive) Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité. Le niveau de granularité illustre une cible de maturité, non l'état courant du marché TPE/PME santé.

---

## **Sommaire**

1. [Cadre et objectifs](#1-cadre-et-objectifs)
2. [Rappel des éléments clés de l'atelier 1](#2-rappel-des-éléments-clés-de-latelier-1)
3. [Identifier les sources de risque (SR) et les objectifs visés (OV)](#3-identifier-les-sources-de-risque-sr-et-les-objectifs-visés-ov)
4. [Cartographie des sources de risque](#4-cartographie-des-sources-de-risque)
5. [Priorisation SR/OV](#5-priorisation-srov)
6. [Signatures](#6-signatures)

---

## 1 Cadre et objectifs

### 1.1. Objectifs
Objectif principal : Anticipation cadre ReCyF (application française de NIS2) dans le cadre du partenariat avec CHU Fictif.

Objectifs de l'atelier "2. Identification des Sources de Risque" :

**Objectif :** dans le cadre du périmètre  et sur la base de la mission et des valeurs métiers definis pendant l'[atelier 1. Cadrage et socle de sécurité](./ebios-rm-santeconnect-cadrage.md), 
- identifier les personnes ou évènements (= Source de Risque, SR) et leurs objectifs (= Objectif Visé, OV), qui pourraient impacter négativement cette mission et ces valeurs métiers,   
- détailler les SR/OV identifiés, 
- les prioriser pour sélectionner ceux qui serviront de base aux scénarios stratégiques et opérationnels à construire dans les ateliers 3 et 4.

### 1.2 Participants

| Rôle | Nom | Responsabilté | 
| ----- | ----- | --------- | 
| CEO | Martin DUPONT | D |
| RSSI | Claire ESPINOZA | R |
| DPO | Jeanne PETIT | C |
| DevProduit | Stéphane ROY | C |
| Analyste indépendant CTI | Djibril MOUSSA | C | 


**Légende**: D = Décide, R = Responsable, C = Est Consulté

_Notes :_  
_- L'atelier 2 est mené sur la base du travail préparatoire mené par le RSSI avec le DevProduit, relu par la DPO et le spécialiste en analyse numérique._  
_- Dans le cadre de cet atelier, SantéConnect se fait accompagner  d'un consultant indépendant chevronné analyste Cyber Threat Intelligence (CTI ou spécialiste en analyse de menace numérique)) pour l'accompagner sur l’état de la menace dans le secteur de la santé et notamment l'identification des (groupes d') attaquants, leurs ressources et objectifs supposés, leurs modus operandi ainsi que des activités les plus exposées, la connaissance des dernières actualités et attaques cyber et la mise en contexte de la menace._ 
_- Cet investissement a été arbitré et validé par le CEO, notamment suite aux attaques cyber observés contre les CHUs français en 2023/24 [Article sur cyberattaque CHU Rouen](https://stm.cairn.info/revue-risques-et-qualite-en-milieu-de-soins-2022-1-page-23?lang=fr) 
_- Au quotidien, CHU Fictif en tant que partenaire SantéConnect partage veille cyber (notamment via bulletin ANSSI) et alertes sectorielles._  

### 1.3. Livrables

A la suite de cet atelier et sur la base de l'atelier 1. seront formalisés les éléments suivants :

- Identification des couples SR / OV,  
- Evaluation de ces couples et priorisation (couples prioritaires pour étude dans les ateliers suivants et secondaires pour surveillance attentive et possible étude ultérieure selon les ressources disponibles),  
- Cartographie des SR. 

_Note : la formalisation des livrables après l'atelier est mené par la RSSI._

---

## 2. Rappel des éléments clés de l’Atelier 1

Pour garantir la cohérence de l’analyse des risques, cette section rappelle les éléments fondateurs identifiés lors de [l’Atelier 1 : Cadrage et socle de sécurité](./ebios-rm-santeconnect-cadrage.md).

**Périmètre - Services critiques :**
API HL7/FHIR : Interface centrale pour l’échange de données médicales avec le CHU (ex : suivi cardiologique en temps réel).
Base de données D-002 : Stockage des données sensibles des patients (ordonnances, comptes-rendus d’analyses).

**Acteurs :**

Utilisateurs : 80 patients + 20 praticiens.
Partenaires : CHU Fictif (co-responsabilité RGPD/HDS), laboratoires, Stripe (paiements).

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


---

## 3. Identifier les sources de risque (SR) et les objectifs visés (OV)


### 3.1. Mission et valeurs métiers

Le rappel des valeurs métiers (VM) permet de mieux caractériser les SR à même de porter préjudice à la mission de SantéConnect, son secteur ou à la souveraineté nationale.

**Mission :** Assurer le suivi cardiologique global (poids, tension, rappels médicaux) des patients suivis au CHU, via une plateforme mobile et web sécurisée, pour améliorer leur prise en charge et réduire les hospitalisations de 20% d’ici 2027 (_note: cible fictive_), tout en garantissant la conformité HDS, RGPD, et la résilience des services critiques (API HL7/FHIR, données médicales).

**Valeurs Métiers**

| ID | Dénomination | Description | Type | Biens Support | Responsable métier |
| --- | --- | --------------- | --- | --- |  --- |
| VM1 | Suivi cardiologique | Suivi quotidien des indicateurs cardiologiques critiques (poids, tension artérielle) avec alertes automatisées en cas de valeurs anormales, et rappels de prise de médicaments pour améliorer l’observance thérapeutique | Processus | App mobile, Web app, API CHU, Données Médicales | CEO | 
| VM2 | Coffre-fort médical | Stockage sécurisé et conforme HDS des documents médicaux sensibles (ordonnances, comptes-rendus d’analyses) avec accès restreint (RBAC) et traçabilité (logs Graylog) | Stockage | App mobile, Web app, Données médicales | DPO |
| VM3 | Messagerie sécurisée | Messagerie chiffrée de bout en bout pour les échanges entre patients et praticiens ou praticiens entre eux, conforme à HDS (L.1111-8 CSP) et intégrée aux dossiers patients | Communication | App mobile, Web app | CEO | 


### 3.2. SR/OV par catégorie SR

L'objectif est ici d'identifier :  
- les SR pouvant de porter atteinte aux missions de SantéConnect ou visant des intérêts supérieurs (sectoriels, étatiques, etc.), SantéConnct devenant alors une cible intermédiaire ?  
- les OV pour chaque SR en termes d'effet attendu ?

| Source de risque | Objectif visé | Motivation | Ressources | VM Impactées | Pertinence | Priorisation |
| --- | --- | --- | --- | --- | --- | --- |
| Concurrent | Espionnage (vol de données patients, vol stack techno) | Obtenir avantage concurrentiel | Importantes (budget R&D) | VM1, VM2, VM3 | 🔴 | P1 |
| Concurrent | Influence (dénigrement) | Obtenir avantage concurrentiel | Significatives (réseaux sociaux) | VM3 | 🟡 | P2 |
| Concurrent | Entrave au fonctionnement | Obtenir avantage concurrentiel | Importantes (DDoS, sabotage) | VM1, VM2, VM3 | 🔴 | P1 |
| Personnel interne mécontent | Espionnage (vol de données) | Saboter l'entreprise | Maximales (accès admin) | VM2 | 🔴 | P1|
| Personnel interne mécontent | Influence (fuites internes) | Saboter la réputation | Maximales (accès admin) | VM3 | 🔴 | P1 |
| Personnel interne mécontent | Entrave au fonctionnement | Saboter le business | Maximales (accès admin) | VM1, VM2 | 🔴 | P1 |
| Personnel interne mécontent | Entrave au fonctionnement | Erreur humaine | Maximales (accès admin) | VM1 | 🟡 | P2 |
| Personnel interne mécontent | Lucratif (revente de données) | Gain financier | Maximales (accès admin) | VM2 | 🔴 | P1|
| Personnel externe malveillant | Espionnage (vol de données) | Saboter l'entreprise | Importantes (compétences techniques) | VM2 | 🔴 | P1 |
| Personnel externe malveillant | Influence (dénigrement) | Saboter la réputation | Significatives (réseaux sociaux) | VM3 | 🟡 | P2 |
| Personnel externe malveillant | Entrave au fonctionnement | Saboter le business | Importantes (DDoS, sabotage) | VM1, VM2 | 🔴 | P1 |
| Personnel externe malveillant | Lucratif (revente de données) | Gain financier | Significatives (accès limités) | VM2 | 🟡 | P2 |
| Organisation Criminelle | Espionnage (vol de données D-002) | Revente de données | Importantes (outils avancés, dark markets) | VM2 | 🔴 | P1 |
| Organisation Criminelle | Entrave (ransomware) | Extorsion (rançon) | Importantes (ransomware-as-a-service) | VM1, VM2 | 🔴 | P1 |
| Organisation Criminelle | Lucratif (exfiltration + chiffrement) | Double extorsion | Importantes (outils comme LockBit) | VM1, VM2 | 🔴 | P1 |
| Organisation Etatique | Espionnage | Surveillance sectorielle | Importantes (APT) | VM2 | 🟡 | P2 |
| Organisation Etatique | Influence | Déstabiliser le secteur santé | Importantes (APT) | VM3 | 🟡 | P2 |
| Organisation Terroriste | Influence | Déstabiliser/détruire | Importantes (cyberattaques) | VM1, VM2, VM3 | 🟡 | P2 |
| Organisation Terroriste | Entrave au fonctionnement | Déstabiliser/détruire | Importantes (cyberattaques) | VM1, VM2 | 🟡 | P2 |
| Hacktiviste | Influence (message politique) | Passer un message | Significatives (outils open-source) | VM3 | 🟢 | P3 |
| Hacktiviste | Entrave au fonctionnement | Démonstration de force | Significatives (DDoS) | VM1 | 🟢 | P3 |
| Officine spécialisée | Lucratif (services cybercriminels) | Gain financier | Importantes (expertise ciblée) | VM2 | 🟡 | P2|
| Jeune hacker (script kiddie) | Lucratif | Gain financier | Faibles (outils basiques) | VM2 | 🟢 | P3 |
| Jeune hacker (script kiddie) | Défi/amusement | Démontrer ses compétences | Faibles (outils basiques) | VM1 | 🟢 | P3 |


_Notes :_  
_- Une même SR peut avoir plusieurs objectifs visés différents, générant donc plusieurs couples SR/OV._   
_- Un objectif visé peut sortir du cadre du périmètre défini, qui devient un intermédiaire à l'OV final ou un risque collétaral via son exposition au risque._ 
_- Les ressources comprennent les capacités financières et matérielles, et le niveau de compétence sur les cyberattaques._
_- La cotation de la pertinence peut être enrichie et affinée ultérieurement si souhaité avec l'aide du spécialiste en analyse de manace numérique en détaillant pour chaque couple SR/OV : activité, modes opératoires, secteurs d'activité, arsenal d'attaque et faits d'armes._


**Cotation Pertinence**

L'évaluation de la pertinence d'un couple SR/OV se base sur la motivation et les ressources identifiées selon la matrice suivante :

| Ressources / Motivation | Faible | Significative | Importante | Maximale |
| -------- | -------- | -------- | -------- | -------- |
| Maximales | 🟡 Moyen | 🟡 Moyen | 🔴 Elevé | 🔴 Elevé |
| Importantes | 🟢 Faible | 🟡 Moyen | 🔴 Elevé | 🔴 Elevé |
| Significatives | 🟢 Faible | 🟢 Faible | 🟡 Moyen | 🔴 Elevé |
| Faibles | 🟢 Faible | 🟢 Faible | 🟡 Moyen | 🟡 Moyen |

**Cotation Priorisation**

L'évaluation de la pertinence d'un couple SR/OV se base sur la pertinence et le potential d'impact sur le business, la réputation ou les risques réglementaires.

| Priorisation | Justification | Action |
| -------- | -------- | -------- | 
| P1 | Activités critiques entravées ou arrêtées, réputation endommagée sur la durée, sanction financière ou arrêt service | Couple SR/OV à étudier dans les ateliers suivants |
| P2 | Activités critiques partiellement entravées , réputation endommagée sur le court terme, rappel à l'ordre | Couple SR/OV à étudier ultérieurement |
| P3 | Activités critiques non entravées ou arrêtées | Couple SR/OV à surveiller régulièrement |


---

## 4. cartographie des sources de risque

Les deux représentations des cartographies d'abord des sources de risque et puis des objectifs visés sont repésentés sous forme de tableau pour faciliter la sélection des couples SR/OV prioritaires et valoriser les résultats de l’atelier. 

#### 4.1. Cartographie par Source de Risque (SR)
*Objectif : Identifier les acteurs les plus pertinents pour SantéConnect.*

| Source de risque | Pertinence dominante | OV principaux (P1) | OV secondaires (P2) | Priorisation |
| --- | --- | --- | --- | --- |
| Organisation Criminelle | 🔴 Élevée | Entrave, Lucratif, Espionnage | — | P1 |
| Personnel interne mécontent | 🔴 Élevée | Espionnage, Entrave, Lucratif | — | P1 |
| Personnel externe malveillant | 🔴 / 🟡 Mixte | Espionnage, Entrave | Influence, Lucratif | P1 / P2 |
| Concurrent | 🔴 / 🟡 Mixte | Espionnage, Entrave | Influence | P1 / P2 |
| Organisation Étatique | 🟡 Moyenne | — | Espionnage, Influence | P2 |
| Organisation Terroriste | 🟡 Moyenne | — | Entrave, Influence | P2 |
| Officine spécialisée | 🟡 Moyenne | — | Lucratif | P2 |
| Hacktiviste | 🟢 Faible | — |


**Analyse** :
- Les **organisations criminelles** et le **personnel interne** sont les SR les plus critiques (🔴).
- *→ Priorité pour l’Atelier 3 : Scénarios ciblant ces acteurs.*

#### 4.2. Cartographie par Objectif Visé (OV)
*Objectif : Identifier les motivations les plus impactantes pour les VM.*

| Objectif visé | SR les plus pertinentes | VM exposées | Pertinence max | Priorisation |
| --- | --- | --- | --- | --- |
| Espionnage | Org. Criminelle, Interne, Concurrent | VM2 | 🔴 | P1 |
| Entrave au fonctionnement | Org. Criminelle, Interne, Concurrent | VM1, VM2 | 🔴 | P1 |
| Lucratif | Org. Criminelle, Interne | VM2 | 🔴 | P1 |
| Influence | Concurrent, Interne, Étatique | VM3 | 🔴 / 🟡 | P1 / P2 |
| Défi / Amusement | Script kiddie | VM1 | 🟢 | P3 |

**Analyse** :
- Les objectifs **Entrave** et **Lucratif** sont les plus pertinents (🔴).
- *→ Priorité pour l’Atelier 3 : Scénarios de ransomware et compromission d’API.*


---

## 5. Priorisation SR/OV

### 5.1. Couples SR/OV prioritaires (P1)
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

### 5.2. Objectif de l’Atelier 3

Construire 3 scénarios stratégiques pour :
- Tester la résilience (PCA/PRA, RTO 72h, RPO 24h).  
- Valider les contrôles ISO 27001 (A.5.29, A.8.13).  
- Préparer la conformité NIS2 (notification ANSSI sous 24h, Art. 23).  

_Notes :_
_-Les scénarios S4 (Exfiltration par admin) et S5 (Vol de données via partenaire) sont exclus de l’Atelier 3 mais pourront être étudiés ultérieurement (P2)._
_-Les fiches scénarios serviront de base pour la mise à jour du PRI et du Plan d’Action NIS2 (V2)._

### 5.3. Actions décidées avant Atelier 3

| Livrable | Description | Responsable | Échéance |
| --- | --- | --- | --- |
| Fiches scénarios (S1-S3) | Narratif + acteurs + impacts + preuves de conformité | RSSI | 10/07/2026 |
| Arbres des causes (S1-S3) | Causes racines et directes  | DevProduit | 10/07/2026 |
| Playbooks de réponse (S1-S3) | Procédures d’urgence (isolation, notification, restauration) | RSSI | 13/07/2026 |
| Matrice des preuves | Logs, rapports, sauvegardes (liens avec RGPD/HDS/NIS2) | DPO  | 13/07/2026 |

_Note : Ces livrables sont formalisés pour illustrer la démarche EBIOS RM ; dans le cadre du portfolio, seul le scénario S1 est développé (cf. 5.4)._

### 5.4. Note sur la démarche

Dans le cadre de ce portfolio, seul le scénario "Compromission API HL7/FHIR" sera développé dans l’Atelier 3.
Les deux autres scénarios prioritaires (Ransomware sur D-002 et Sabotage interne des sauvegardes) ne seront pas traités dans ce livrable, mais pourront faire l’objet d’une étude ultérieure (ex : extension du portfolio).

**Justification :**

Le scénario "Compromission API HL7/FHIR" couvre à lui seul :  
- Tous les gaps 🔴 (PCA/PRA).  
- 2 gaps 🟡 (Surveillance, Micro-segmentation).  
- VM1 et VM2 (critiques pour SantéConnect).  
- Les obligations NIS2 (Art. 21.c, 23) et HDS (L.1111-8 CSP).  

Il permet une démonstration complète de l’application d’EBIOS RM (de l’analyse des risques à la réponse incident), tout en restant focalisé et crédible pour une PME.

---

## 6. Signatures

| Rôle | Nom | Date | 
| ----- | ----- | ----- | 
| CEO | Martin DUPONT | 07/07/2026 |
| RSSI | Claire ESPINOZA | 07/07/2026 |
| DPO | Jeanne PETIT |07/07/2026 |
| DevProduit | Stéphane ROY | 07/07/2026 |
| Analyste indépendant CTI | Djibril MOUSSA | 07/07/2026 |

---

*Document produit dans le cadre du projet portfolio GRC - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*
*Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité.*