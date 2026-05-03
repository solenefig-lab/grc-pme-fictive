# Synthèse des clauses sous-traitants - SantéConnect
## RGPD art. 28

> **Document fictif** - Projet portfolio GRC (SantéConnect, PME e-santé fictive). Le niveau de granularité illustre une cible de maturité RGPD, non l'état courant du marché TPE/PME santé.

> **Note introductive** : alors que la Directive et la LIL rattachaient la sous-traitance principalement aux obligations de sécurité, le RGPD a instauré un régime autonome et complet des rapports responsables/sous-traitants, élargissant considérablement les devoirs contractuels du sous-traitant et le contrôle du responsable.

Ces clauses sont encadrées par le RGPD art. 28 et visent à garantir que le recours de SantéConnect à des sous-traitants n'affaiblisse pas la protection des données personnelles.

---

## Sous-traitants identifiés

| Sous-traitant | Type de service | Statut RGPD | Pays | Mécanisme de transfert (si hors UE) |
|---|---|---|---|---|
| OVH | Hébergement - certifié HDS | Sous-traitant | France | - |
| Stripe | Paiement | Sous-traitant | Irlande | Clauses Contractuelles Types (art. 46 RGPD) |
| Matomo | Analyse (cookies) | Sous-traitant **uniquement si Matomo Cloud** | Allemagne | - |

> **Note - Matomo** : Matomo en auto-hébergement n'est pas un sous-traitant. Seule la version SaaS (Matomo Cloud) est concernée par les clauses ci-dessous.

Ces contrats sont régis par le droit français. Tout litige sera soumis aux tribunaux compétents.

---

## Clauses contractuelles (RGPD art. 28.3)

### 1. Instruction documentée du responsable - Art. 28.3.a

Le sous-traitant s'engage à ne traiter les données à caractère personnel que sur instruction documentée du responsable du traitement, y compris en ce qui concerne les transferts vers un pays tiers ou une organisation internationale, à moins qu'il ne soit tenu d'y procéder en vertu du droit de l'Union ou du droit de l'État membre ; dans ce cas, le sous-traitant informe le responsable avant le traitement, sauf si le droit concerné interdit une telle information pour motifs d'intérêt public.

Les transferts vers des pays tiers doivent respecter les mécanismes prévus par le RGPD art. 46 (ex : Clauses Contractuelles Types de la Commission Européenne).

> **Cas particulier OVH - Données Médicales :**
> - Prise en compte de la co-responsabilité entre SantéConnect et CHU Fictif
> - Mise en œuvre de la solution technique de flux de données (API HL7/FHIR)
> - Séparation stricte et chiffrement des Données Médicales des autres données SantéConnect par conception

---

### 2. Confidentialité des personnes autorisées - Art. 28.3.b

Le sous-traitant veille à ce que les personnes autorisées à traiter les données personnelles s'engagent à respecter la confidentialité ou soient soumises à une obligation légale appropriée de confidentialité.

Le sous-traitant garantit que l'accès aux données n'est accordé qu'aux personnes ayant un besoin légitime (principe du moindre privilège - *least privilege*).

---

### 3. Mesures de sécurité - Art. 28.3.c + Art. 32

Le sous-traitant prend toutes les mesures requises en vertu de l'art. 32 du RGPD :

| Mesure | Détail |
|---|---|
| Contrôle d'accès | 2FA, audit annuel des droits (RBAC), journalisation des accès (logs 6 mois, 1 an si incident) |
| Chiffrement | TLS 1.3 (transit) + AES-256 (repos) |
| Données médicales | Séparation stricte par conception des autres données |

> **Cas particulier OVH** : séparation stricte des Données Médicales par conception + flux API HL7/FHIR sécurisé

> **Cas particulier Matomo** *(applicable uniquement si Matomo Cloud - version SaaS)* :
> - Solution analytics sans transfert hors UE, pas de cookie tiers
> - Audits réguliers des mécanismes de recueil du consentement + CMP horodaté

---

### 4. Conditions pour recourir à des sous-traitants secondaires - Art. 28.2 + 28.3.d

Le sous-traitant ne recrute pas d'autre sous-traitant sans autorisation écrite préalable (spécifique ou générale) de SantéConnect.

En cas d'autorisation générale, le sous-traitant informe SantéConnect de tout changement prévu (ajout ou remplacement), laissant à SantéConnect **15 jours** pour émettre des objections.

> **Exemple** : si Stripe sous-traite à AWS pour l'hébergement, SantéConnect doit autoriser par écrit ce sous-traitement secondaire.

---

### 5. Assistance pour l'exercice des droits des personnes concernées - Art. 28.3.e

Le sous-traitant aide SantéConnect à répondre aux demandes **sous 1 mois** (RGPD art. 12.3).

Droits couverts : accès, rectification, effacement ("droit à l'oubli"), portabilité, opposition, limitation du traitement.

> **Cas particulier OVH - Dossier Médical :**
> - Droits soumis à la réglementation CSP - non opposables au-delà des délais légaux d'archivage
> - Suspension du service : archivage restreint 20 ans, accès réservé au CHU (CSP art. R. 1112-7)
> - Archivage selon durée légale pour praticiens libéraux + outil d'export sécurisé (CSP art. R. 1111-10)

---

### 6. Assistance pour les obligations de sécurité, notification et analyses d'impact - Art. 28.3.f

Le sous-traitant assiste SantéConnect dans :

- La réalisation des AIPD pour les traitements à risque, notamment les Données Médicales (RGPD art. 35)
- La notification des violations à la CNIL (RGPD art. 33) **sous 48h** après prise de connaissance *(délai interne avant notification CNIL sous 72h)*
- La sécurisation des traitements *(cf. clause 3 - Mesures de sécurité)*

---

### 7. Effacement ou restitution des données en fin de prestation - Art. 28.3.g

À la fin du contrat, le sous-traitant supprime les données (effacement sécurisé selon la norme NIST SP 800-88) ou les restitue sur support chiffré. Une **certification de destruction** doit être fournie.

> **Cas particulier OVH** : transfert des données hébergées vers le CHU sous 30 jours (format HL7/FHIR chiffré) + outil d'export sécurisé pour les praticiens libéraux

---

### 8. Mise à disposition des informations pour contrôle - Art. 28.3.h

Le sous-traitant accepte des **audits annuels** (ou sur demande en cas d'incident) par SantéConnect ou un tiers indépendant.

Les audits sont à la charge de SantéConnect, sauf si un manquement est constaté (alors à la charge du sous-traitant).

> **Cas particulier OVH** : vérification annuelle de la conformité HDS/RGPD, conduite conjointement par SantéConnect et CHU Fictif ou un tiers indépendant
>
> **Cas particulier Stripe** : vérification annuelle de la conformité PCI-DSS Level 1

---

### 9. Obligation de signaler toute instruction illégale - Art. 28.3.i

Toute instruction illégale doit être signalée par écrit au DPO de SantéConnect (DPO As a Service - privacy@santeconnect.fr) **dans les 24h**, avec copie dans le registre des incidents.

---

### 10. Responsabilité du sous-traitant - Art. 28.10

Si un sous-traitant détermine lui-même les finalités et les moyens du traitement en violation du RGPD, il est requalifié en responsable de traitement pour ce traitement.

Le sous-traitant s'engage à **indemniser SantéConnect** en cas de sanction CNIL due à son manquement.

> **Exemple** : si Stripe décide unilatéralement de transférer des données de paiement vers les États-Unis sans mécanisme de transfert valide (art. 46 RGPD), Stripe devient responsable de traitement et engage sa responsabilité civile et réglementaire.

---

### 11. Durée du contrat et reconduction

- Durée initiale : **2 ans**, renouvelable par tacite reconduction
- Résiliation anticipée : préavis de **3 mois** en cas de manquement aux obligations RGPD

---

## Signatures

| Rôle | Nom | Date de signature | Révision |
|---|---|---|---|
| CEO SantéConnect | Martin DUPONT | 15/01/2024 | 15/01/2025 |
| DPO SantéConnect (As a Service) | Jeanne PETIT | 15/01/2024 | 15/01/2025 |
| Co-signataire - clauses Données Médicales (CHU Fictif) | Dr. Alice BEN-ALI | 15/01/2024 | 15/01/2025 |

---

*Document produit dans le cadre du projet portfolio GRC - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*

*Ce document est une synthèse pédagogique. Il ne se substitue pas à un accord juridique formalisé par un cabinet spécialisé.*
