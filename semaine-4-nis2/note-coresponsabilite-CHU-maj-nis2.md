# Note de convention de co-responsabilité - CHU Fictif
## RGPD art. 26
## V2.0 - Intégration clauses NIS2 (Art. 21, 23) suite à analyse d'impact S4.

> **Document fictif** - Projet portfolio GRC - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)
> Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité. Le niveau de granularité illustre une cible de maturité, non l'état courant du marché TPE/PME santé.

_Note de contexte réglementaire - juin 2026 : La transposition NIS2 en droit français n'est pas encore publiée. L'ANSSI met à disposition depuis le 17 mars 2026 le Référentiel Cyber France (ReCyF), document de travail correspondant au référentiel mentionné à l'article 14 du projet de loi Résilience. Les analyses et recommandations de ce livrable s'appuient sur la directive NIS2 (UE) 2022/2555 et anticipent le ReCyF comme référentiel cible, conformément à la posture recommandée par l'ANSSI pour les futurs assujettis._

---

## **Sommaire**

0. [Objet et Périmètre](#objet-et-périmètre)
1. [Gestion des droits des personnes concernées](#1-gestion-des-droits-des-personnes-concernées)
2. [Mesures de sécurité](#2-mesures-de-sécurité)
3. [Contrat avec le sous-traitant OVH](#3-contrat-avec-le-sous-traitant-ovh)
4. [Procédure de notification d'incident](#4-procédure-de-notification-dincident)
5. [Fin de la coopération](#5-fin-de-la-coopération)
6. [Information sur les menaces](#6-information-sur-les-menaces)
7. [Clauses Spécifiques NIS2](#7-clauses-spécifiques-nis2)
8. [Clause de résiliation anticipée](#8-clause-de-résiliation-anticipée)
9. [Signatures](#signatures)



---

## Objet et périmètre

SantéConnect et le CHU Fictif définissent ensemble les finalités et les méthodes de traitement des données médicales personnelles des patients en cardiologie du CHU Fictif ayant donné leur consentement éclairé à l'utilisation de SantéConnect.

- **Référence registre** : fiches D-002 (Données de Santé) + D-005 (Interconnexion CHU)
- **Objet** : partage et synchronisation des dossiers médicaux hospitaliers entre SantéConnect et le CHU Partenaire, dans le cadre de la continuité de la prise en charge médicale
- **Modalité technique** : synchronisation en temps réel des données médicales via API HL7/FHIR sécurisée

En ligne avec le RGPD art. 26 et sous le contrôle du DPO de SantéConnect et du DPO du CHU Fictif, SantéConnect et CHU Fictif sont désignés co-responsables du traitement des données susmentionnées. Cette convention définit les rôles, responsabilités et obligations de chaque partie pour le traitement des données médicales partagées.

---

## 1. Gestion des droits des personnes concernées

### 1.1 Information et accès à la convention

- Information sur la convention de co-responsabilité dans les CGU de SantéConnect et lors de la présentation du service par le service de cardiologie du CHU Fictif.
- Mise à disposition de l'accord via les CGU de SantéConnect + affichage dans le service de cardiologie (RGPD art. 26.2).

### 1.2 Point de contact et répartition des rôles DPO

**Point de contact unique** : privacy@santeconnect.fr

Les personnes concernées peuvent également contacter à tout moment le DPO du CHU Fictif pour faire valoir leurs droits.

| Responsabilité | DPO compétent | Périmètre |
|----------------|---------------|-----------|
| Réception demandes + coordination | DPO As a Service | Point de contact unique |
| Transmission et réponse | DPO CHU Fictif | Données CHU |
| Mesures personnelles, coffre-fort médical, messagerie | DPO As a Service | Données SantéConnect |
| Dossier médical CHU | DPO CHU Fictif | Données CHU |

### 1.3 Droits spécifiques

- **Droit à la rectification et à l'effacement du Dossier Médical** : soumis à la réglementation CSP - non opposable au-delà des délais légaux d'archivage.
- **Suspension du service SantéConnect par la personne concernée** :
  - Archivage restreint du Dossier Médical : 20 ans, accès réservé au CHU (CSP art. R. 1112-7)
  - Archivage selon durée légale + archivage restreint pour les praticiens libéraux - SantéConnect met à disposition un outil d'export sécurisé (CSP art. R. 1111-10)
  - La clôture du compte SantéConnect n'entraîne pas l'archivage chez le CHU ou les praticiens tant que ceux-ci continuent à suivre la personne concernée.

---

## 2. Mesures de sécurité

| Type de mesure | Détail |
|---|---|
| Chiffrement des données | TLS 1.3 (transit) + AES-256 (repos) |
| Contrôle d'accès | 2FA, audit annuel des droits d'accès (RBAC), journalisation des accès (logs conservés 1 an glissant) |
| Contrôle des sous-traitants | Vérification annuelle de la conformité HDS/RGPD de OVH |
| Archivage et résiliation | Données CHU déplacées vers stockage froid (OVH Archive), accès restreint au CHU via API sécurisée. Transfert des données au CHU sous 30 jours en cas de résiliation (format HL7/FHIR chiffré) |
| Notification incident | Notification CNIL sous 72h (RGPD art. 33) + information des patients concernés (RGPD art. 34) |

---

## 3. Contrat avec le sous-traitant OVH

Hébergement des données SantéConnect : OVH, hébergé en France, certifié HDS, choix validé en accord avec le CHU Fictif. Le contrat de sous-traitance (RGPD art. 28) mentionne explicitement :

- La co-responsabilité du CHU Fictif sur les Données Médicales
- La solution technique de flux de données (API HL7/FHIR)
- La séparation des Données Médicales des autres données SantéConnect par conception

Un audit co-joint annuel de conformité RGPD-HDS, d'analyse des risques et de priorisation des mesures de remédiation est mené annuellement par SantéConnect et CHU Fictif.

---

## 4. Procédure de notification d'incident

SantéConnect et CHU Fictif s'engagent à :

- Notifier leur partenaire sous 4h après la découverte de l'incident
- SantéConnect notifie la CNIL sous 72h (RGPD art. 33) -le CHU notifie simultanément l’ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information) en tant qu'entité essentielle soumise à NIS2 si applicable.
- Mettre en œuvre conjointement toutes les mesures nécessaires pour analyser, mitiger et sécuriser dans les 72h :
  - **Responsables SantéConnect** : RSSI + DPO As a Service
  - **Responsables CHU Fictif** : Chef de Service Cardiologie + Département IT + DPO CHU Fictif
- Partage des coûts liés à la gestion de l'incident (notification aux patients, audits) au prorata de la responsabilité de chaque partie
- Mise à jour de l'AIPD SantéConnect dans les 15 jours, à charge de SantéConnect ; le CHU Fictif est notifié et dispose de 5 jours ouvrés pour formuler des observations.

---

## 5. Fin de la coopération

**Données :**

- Arrêt immédiat de l'utilisation des Données Médicales par SantéConnect
- Transfert des données hébergées OVH vers le CHU sous 30 jours (format HL7/FHIR chiffré) + outil d'export sécurisé pour les praticiens libéraux
- La clôture de l'accord n'entraîne pas l'archivage chez le CHU ou les praticiens tant que ceux-ci continuent à suivre la personne concernée

**Accès et flux :**

- Arrêt de l'accès au flux d'interconnexion par SantéConnect et le CHU sous 45 jours

> *Note - hors périmètre RGPD : les questions de propriété intellectuelle relatives à l'infrastructure et aux procédures de SantéConnect relèvent du contrat de partenariat commercial et non du présent accord.*

---

## 6. Information sur les menaces

SantéConnect et CHU Fictif s'engagent à :

- **Transmettre sans délai** toute alerte ou information relative à une menace cyber identifiée comme pertinente pour les données partagées ou les systèmes interconnectés, via e-mail (rssi@santeconnect.fr, DPO As a Service en copie : privacy@santeconnect.fr ; resp. DPO@CHU-Fictif.fr), selon les délais suivants :

| Niveau    | Classification PRI | Délai notification partenaire (RGPD) | Délai Contractuel CHU (Logique NIS2) |
|-----------|--------------------|------------|----------------------|
| Critique  | P1                 | 4h         | 4h             |
| Élevé     | P2                 | 4h         | 4h           |
| Modéré    | P3                 | 72h        | 24h              |
| Faible    | P4                 | 15 jours   | 72h | 


- Cette transmission inclura : une description de la menace, son niveau de criticité (référence : Grille de cotation 3×3 - *fiche-risques-e-sante.md*), et :
    - **Mettre en œuvre conjointement** toutes les mesures nécessaires pour analyser, mitiger et sécuriser dans les 72h pour les alertes de niveau **Critique** et **Elevé**:
    - **Responsables SantéConnect** : RSSI + DPO As a Service
    - **Responsables CHU Fictif** : Département IT + DPO CHU Fictif
Le délai le plus contraignant s'applique.

> *Référence niveaux de criticité : Grille de cotation Impact × Probabilité (3×3) - voir [fiche-risques-e-sante.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-1-gouvernance/fiche-risques-e-sante.md)*

---

## 7. Clauses Spécifiques NIS2

*Conformément à la Directive (UE) 2022/2555 (NIS2), le CHU Fictif, en tant qu’entité essentielle, impose à SantéConnect les mesures suivantes pour garantir la sécurité des données partagées et des systèmes interconnectés.*

###  7.1. Gestion des Incidents (Art. 23 NIS2)

- **Notification sous 24h** : SantéConnect s’engage à notifier le CHU **sous 24h** en cas d’incident impactant les données partagées ou les systèmes interconnectés, en plus de la notification à la CNIL (RGPD Art. 33).
- **Réponse conjointe** : Le CHU et SantéConnect collaboreront pour une **réponse sous 72h**, incluant :
  - L’analyse de la cause racine.
  - La mitigation des impacts.
  - La sécurisation des systèmes.
- **Partage des coûts** : Les coûts liés à la gestion de l’incident (ex : audits, notifications) seront partagés **au prorata de la responsabilité de chaque partie**.

La notification sous 4h (section 4) constitue l'alerte précoce ; la notification formelle sous 24h constitue la notification d'incident qualifiée.

### 7.2. Continuité des Activités (Art. 21 NIS2)

- **Tests annuels** : SantéConnect testera son **PCA/PRA** au moins une fois par an et fournira les preuves au CHU.
- **Activation sous 4h** : En cas d’incident critique, le déclenchement de la procédure PCA/PRA sera activé **sous 4h**.

### 7.3. Sécurité des Chaînes d’Approvisionnement (Art. 21(2) NIS2)

- **Conformité des sous-traitants** : SantéConnect garantit que ses sous-traitants (ex : OVH) respectent les **exigences NIS2**, notamment :
  - Sécurité physique et logique (HDS R.1111-8 et L.1111-8).
  - Notification des incidents sous 24h.
- **Audit annuel conjoint** : Un audit sera réalisé chaque année pour vérifier la conformité des sous-traitants.

### 7.4. Sécurité des Réseaux et des Systèmes (Art. 21 NIS2)

- **Segmentation réseau** : SantéConnect maintiendra une **segmentation réseau** (DMZ pour les APIs) pour isoler les données partagées.
- **Chiffrement** : Les données seront **chiffrées en transit (TLS 1.3) et au repos (AES-256)**.
- **Audits semestriels** : Les configurations réseau et de sécurité seront auditées **tous les 6 mois**.

### 7.5. Tests de Sécurité (Art. 21 NIS2)

- **Tests de pénétration** : SantéConnect réalisera des **tests de pénétration annuels** sur ses applications critiques (APIs, App Mobile) et fournira les rapports au CHU.
- **Correction des vulnérabilités** : Les vulnérabilités critiques seront corrigées **sous 30 jours**.

### 7.6. Formation et Sensibilisation (Art. 21 NIS2)

- **Formation NIS2** : SantéConnect formera son équipe aux **exigences NIS2** (ex : gestion des incidents, continuité) et fournira les preuves de formation au CHU.
- **Sensibilisation annuelle** : Une session annuelle sera organisée pour rappeler les bonnes pratiques (ex : détection des phishings).

---

## 8. Clause de résiliation anticipée

Chaque partie peut résilier cet accord avec un préavis de 3 mois, en cas de :

- Manquement grave aux obligations RGPD/HDS
- Changement de législation rendant l'accord non conforme
- Faillite ou cessation d'activité d'une des parties

---

## 9. Révision de l'accord

- Révision annuelle à date anniversaire de signature
- Révision sous 1 mois en cas de : changement de finalité du traitement, évolution de la nature des Données Médicales, évolution réglementaire, évolution des activités de SantéConnect

Accord conclu pour une durée indéterminée à compter du 15/01/2024, révisable annuellement.

---

## Signatures
Version: V2.0 - 02/06/2026 (ajout section 7 : Clauses Spécifiques NIS2 et révision sections 4 et 6)
Révision : 15/02/2027

| Rôle | Nom | Date de signature | Version 2.0 |
|---|---|---|---|
| CEO SantéConnect | Martin DUPONT | 15/01/2024 | 02/06/2026 |
| DPO SantéConnect (As a Service) | Jeanne PETIT | 15/01/2024 | 02/06/2026 |
| Chef du Service Cardiologie CHU Fictif | Dr. Alice BEN-ALI | 15/01/2024 | 02/06/2026 |
| DPO CHU Fictif | Jérôme LEPEUVE | 15/01/2024 | 02/06/2026 |

---

*Document produit dans le cadre du projet portfolio GRC - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*
*Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité.*