# Procédure de gestion des incidents et notification CNIL - SantéConnect

> **Document fictif** — Projet portfolio GRC (SantéConnect, PME e-santé fictive). Le niveau de granularité illustre une cible de maturité RGPD, non l'état courant du marché TPE/PME santé.
>
> Document signé par Martin Dupont, CEO SantéConnect, le 15/01/2024. Validé par DPO As a Service (Jeanne Petit), le 10/04/2024.

---

## 1. Contexte

Ce document réfère aux obligations RGPD art. 33 et 34 : notification de violation de données personnelles à la CNIL et information aux personnes concernées.

**Définition — violation de données personnelles :**
Constitue une violation de données personnelles tout traitement de données ayant subi, de manière accidentelle ou illicite, une perte de **DISPONIBILITÉ**, d'**INTÉGRITÉ** ou de **CONFIDENTIALITÉ**.

Toute violation de données personnelles nécessite la constitution d'une **documentation interne** portant sur :
- La nature, les méthodes et le volume de la violation
- Les mesures de sécurité préalables
- Les procédures menées et mesures appliquées suite à la violation, y compris la notification aux personnes concernées le cas échéant

> **Note** : en cas de cyberattaque, une plainte est à déposer au commissariat ou à la gendarmerie en parallèle de la notification CNIL.

**Procédure de notification CNIL :**

| Étape | Délai | Modalité |
|---|---|---|
| Notification initiale | Dans les 72h suivant la constatation (le plus tôt possible) | Via téléservice CNIL, par le responsable de traitement |
| Justification du dépassement | Si délai 72h dépassé | À documenter obligatoirement |
| Notifications complémentaires | Dès disponibilité d'informations supplémentaires | Via téléservice CNIL |
| Retour CNIL | Variable | Ex. clôture ou obligation d'information aux personnes concernées |

---

## 2. Procédure en cas de violation de données personnelles

### 2.1 Violation de données personnelles — hors données sensibles

1. **Horodater** la constatation de la violation et documenter : nature et volume des données concernées, nature et nombre de personnes concernées, méthode utilisée si connue.
2. **Mobiliser sous 24h** les responsables SantéConnect (CEO + Service IT/Support + DPO As a Service) pour analyser, documenter et sécuriser (remédiation / mitigation / suspension).
3. **Décider sous 48h** de la nécessité d'informer les personnes concernées selon les critères section 4.1 — décision CEO avec validation DPO As a Service.
4. **Notifier la CNIL sous 72h** (cf. section 3).
5. **Étude approfondie** de la violation pour prioriser de nouvelles mesures de sécurisation — mise à jour AIPD dans les 15 jours.
6. **Mise à jour de la notification CNIL** le cas échéant.

---

### 2.2 Cas particulier — violation de données sensibles

*(Données Médicales — cf. fiches de traitement D-002 et D-005)*

La procédure détaillée est définie dans la **convention de co-responsabilité avec CHU Fictif** (RGPD art. 26). Synthèse :

| Étape | Délai | Responsable |
|---|---|---|
| Notification inter-partenaires | Sous 4h après découverte | SantéConnect → CHU Fictif |
| Notification CNIL | Sous 72h (RGPD art. 33) | SantéConnect |
| Notification autorité CHU | Simultanément si applicable | CHU Fictif |
| Mise en œuvre mesures conjointes | Dans les 72h | CEO + IT/Support + DPO (SC) + Chef Cardiologie + IT + DPO (CHU) |
| Partage des coûts | Au prorata de la responsabilité | SantéConnect + CHU Fictif |
| Mise à jour AIPD | Sous 15 jours | SantéConnect — notification CHU Fictif pour observations (5 jours ouvrés) |

---

## 3. Notification CNIL

> **Note** : il est obligatoire d'utiliser le [téléservice de notification de violation de données personnelles de la CNIL](https://notifications.cnil.fr/notifications/index). Le template ci-dessous liste les principales catégories à préparer en amont — pour documentation interne uniquement.

### 3.1 Type de notification et identification

- Type : Complète / Initiale / Complémentaire
- Identification de l'organisme responsable du traitement concerné et coordonnées des responsables
- Le cas échéant : identification des autres organismes impliqués (ex : CHU Fictif en co-responsabilité)

### 3.2 Nature de la violation

| Champ | Contenu à documenter |
|---|---|
| Horodatage | Début / fin si terminée — "en cours" le cas échéant |
| Prise de connaissance | Date et heure de constatation |
| Nature | Perte de confidentialité / intégrité / disponibilité |
| Origine et cause(s) | Descriptif de la violation et cause identifiée |
| Données concernées | Nature, volume, catégorie de personnes, nombre |
| Mesures préalables | Mesures de sécurité en place avant la violation |
| Impact potentiel | Sur les données selon la nature de la violation |
| Préjudice personnes | Estimation du niveau de gravité pour les personnes concernées |
| Mesures appliquées | Techniques et organisationnelles suite à la violation |
| Communication personnes | Oui / Non mais prévue (date) / Non (risque faible / mesures empêchant lecture / accès coupé / effort disproportionné) / Non déterminé |
| Notifications transfrontalières | Le cas échéant |

---

## 4. Information aux personnes concernées

### 4.1 Critères d'information

La notification aux personnes concernées est déclenchée dans les cas suivants :

- **Préjudice potentiel jugé important** : données médicales, données bancaires, ou nombre significatif de personnes concernées au regard de la population totale traitée
- **Impossibilité d'appliquer des mesures** empêchant la lecture et la réutilisation des données (perte de confidentialité ou d'intégrité)
- **Impossibilité d'empêcher la répétition** de la violation

> **Note — effort disproportionné** : si la notification individuelle demandait des efforts disproportionnés, SantéConnect se réserve le droit d'avoir recours à une information publique via le journal local et des affiches au service de cardiologie du CHU Fictif.

**Délais :**
- Décision d'informer : sous 48h suite à la constatation
- Communication aux personnes concernées : sous 72h suite à la décision

> Pour les violations impliquant des données médicales → voir procédure 2.2 — notification conjointe avec CHU Fictif.

---

### 4.2 Template — courriel d'information aux personnes concernées

---

**De :** martin.dupont@santeconnect.fr

**Objet :** Important — Vos Données Personnelles

---

Cher(e) `[CIVILITÉ]` `[PRÉNOM]` `[NOM]`,

Nous souhaitons vous informer d'une récente violation de données qui a compromis certaines de vos informations personnelles. Plus précisément : `[DESCRIPTION DE LA VIOLATION — ex. : accès non autorisé à votre dossier médical / fuite de vos données de connexion]`.

Nos équipes de sécurité informatique ont rapidement pris les mesures nécessaires pour remédier à la situation et ont renforcé les mesures de protection afin d'éviter que cela ne se reproduise. Nous avons signalé cet incident à l'autorité de protection des données compétente en France (CNIL).

**Données concernées :**
`[LISTE DES DONNÉES CONCERNÉES]`

**Données non concernées :**
`[LISTE DES DONNÉES NON CONCERNÉES]`

Nous vous recommandons d'être vigilant face à toute communication inhabituelle mentionnant vos informations personnelles ainsi que face à toute activité suspecte. Les données impliquées dans cette violation pourraient être utilisées pour rendre des messages malveillants plus crédibles. Si vous recevez des messages ou appels inattendus — notamment des demandes d'informations personnelles ou vous incitant à agir — veuillez vérifier leur authenticité avant toute action.

Pour toute question ou assistance, contactez notre DPO : privacy@santeconnect.fr ou au 06.07.07.06.

Nous vous prions d'accepter nos excuses et vous assurons que SantéConnect prend très au sérieux la protection de vos données personnelles.

Veuillez agréer l'expression de nos salutations distinguées,

**Martin DUPONT**
Directeur SantéConnect

---

*Conformément à la réglementation applicable en matière de protection des données à caractère personnel, notamment les dispositions de la loi « Informatique et Libertés » du 6 janvier 1978 modifiée et du Règlement général sur la Protection des Données (Règlement UE 2016/679), vous disposez d'un droit d'accès, de rectification, d'effacement, d'opposition et de limitation du traitement de vos données personnelles. Pour plus d'informations, consultez la politique de confidentialité de SantéConnect dans les CGU de notre site web ou application.*

*SantéConnect — 123 Chemin du Bois, 00000 Fictif. `[NUMÉRO D'ENREGISTREMENT ENTREPRISE]`*

---

*Document produit dans le cadre du projet portfolio GRC — [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*
*Ce document est une synthèse pédagogique. Il ne se substitue pas à un avis juridique.*
