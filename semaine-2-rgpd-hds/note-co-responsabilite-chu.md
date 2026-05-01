# Note de convention de co-responsabilité — CHU Fictif
## RGPD art. 26

> **Document fictif** — Projet portfolio GRC (SantéConnect, PME e-santé fictive). Le niveau de granularité illustre une cible de maturité RGPD, non l'état courant du marché TPE/PME santé.

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
|---|---|---|
| Réception demandes + coordination | DPO As a Service (privacy@santeconnect.fr) | Point de contact unique officiel — notification systématique au DPO CHU |
| Transmission et réponse | DPO CHU Fictif (DPO@CHU-Fictif.fr) | Réception des demandes transmises par DPO As a Service |
| Mesures personnelles, coffre-fort médical, messagerie (hébergés OVH) | DPO As a Service | Données accessibles via SantéConnect |
| Dossier médical CHU, analyses, ordonnances, dossiers praticiens libéraux | DPO CHU Fictif | Données créées et gérées au service cardiologie du CHU |

### 1.3 Droits spécifiques

- **Droit à la rectification et à l'effacement** du Dossier Médical : soumis à la réglementation CSP — non opposable au-delà des délais légaux d'archivage.
- **Suspension du service SantéConnect** par la personne concernée :
  - Archivage restreint du Dossier Médical : 20 ans, accès réservé au CHU (CSP art. R. 1112-7)
  - Archivage selon durée légale + archivage restreint pour les praticiens libéraux — SantéConnect met à disposition un outil d'export sécurisé (CSP art. R. 1111-10)
  - La clôture du compte SantéConnect n'entraîne pas l'archivage chez le CHU ou les praticiens tant que ceux-ci continuent à suivre la personne concernée.

---

## 2. Mesures de sécurité

| Type de mesure | Détail |
|---|---|
| Chiffrement des données | TLS 1.3 (transit) + AES-256 (repos) |
| Contrôle d'accès | 2FA, audit annuel des droits d'accès (RBAC), journalisation des accès (logs conservés 6 mois, 1 an si incident) |
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

1. **Notifier leur partenaire sous 4h** après la découverte de l'incident
2. **SantéConnect notifie la CNIL sous 72h** (RGPD art. 33) — le CHU notifie simultanément sa propre autorité de contrôle compétente si applicable
3. **Mettre en œuvre conjointement** toutes les mesures nécessaires pour analyser, mitiger et sécuriser dans les 72h :
   - Responsables SantéConnect : CEO + Service IT/Support + DPO As a Service
   - Responsables CHU Fictif : Chef de Service Cardiologie + Département IT + DPO CHU Fictif
4. **Partage des coûts** liés à la gestion de l'incident (notification aux patients, audits) au prorata de la responsabilité de chaque partie
5. **Mise à jour de l'AIPD SantéConnect** dans les 15 jours, à charge de SantéConnect; le CHU Fictif est notifié et dispose de 5 jours ouvrés pour formuler des observations.

---

## 5. Fin de la coopération

À la fin de l'accord entre SantéConnect et CHU Fictif :

**Sort des données :**
- Arrêt immédiat de l'utilisation des Données Médicales par SantéConnect
- Transfert des données hébergées OVH vers le CHU sous 30 jours (format HL7/FHIR chiffré) + outil d'export sécurisé pour les praticiens libéraux
- La clôture de l'accord n'entraîne pas l'archivage chez le CHU ou les praticiens tant que ceux-ci continuent à suivre la personne concernée

**Accès et flux :**
- Arrêt de l'accès au flux d'interconnexion par SantéConnect et le CHU sous 45 jours

> **Note — hors périmètre RGPD** : les questions de propriété intellectuelle relatives à l'infrastructure et aux procédures de SantéConnect relèvent du contrat de partenariat commercial et non du présent accord.

---

## 6. Clause de résiliation anticipée

Chaque partie peut résilier cet accord avec un préavis de 3 mois, en cas de :

- Manquement grave aux obligations RGPD/HDS
- Changement de législation rendant l'accord non conforme
- Faillite ou cessation d'activité d'une des parties

---

## 7. Révision de l'accord

- Révision annuelle à date anniversaire de signature
- Révision sous 1 mois en cas de : changement de finalité du traitement, évolution de la nature des Données Médicales, évolution réglementaire, évolution des activités de SantéConnect

**Accord conclu pour une durée indéterminée à compter du 15/01/2024, révisable annuellement.**

---

## Signatures

| Rôle | Nom | Date de signature | Révision |
|---|---|---|---|
| CEO SantéConnect | Martin DUPONT | 15/01/2024 | 15/01/2025 |
| DPO SantéConnect (As a Service) | Jeanne PETIT | 15/01/2024 | 15/01/2025 |
| Chef du Service Cardiologie CHU Fictif | Dr. Alice BEN-ALI | 15/01/2024 | 15/01/2025 |
| DPO CHU Fictif | Jérôme LEPEUVE | 15/01/2024 | 15/01/2025 |

---

*Document produit dans le cadre du projet portfolio GRC — [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*  
*Ce document est une synthèse pédagogique. Il ne se substitue pas à un accord juridique formalisé par un cabinet spécialisé.*
