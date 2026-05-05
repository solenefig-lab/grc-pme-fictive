# Politique de Sécurité des Systèmes d'Information (PSSI) - SantéConnect

> **Document produit dans le cadre du projet portfolio GRC** - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)
> Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité. Le niveau de granularité illustre une cible de maturité, non l'état courant du marché TPE/PME santé.

---

## 1. Contexte, objectifs et périmètre

### 1.1. Contexte

SantéConnect est une PME de 15 personnes spécialisée dans l'amélioration du suivi cardiologique des utilisateurs. Le service est proposé en partenariat avec le CHU Fictif et des praticiens libéraux (20 praticiens) pour 80 patients, constituant une population principalement âgée. Le cœur du service est le dossier médical, dont les données sont séparées par conception des autres données traitées.

### 1.2. Objectifs

Ce document porte le cadre de protection du Système d'Information (SI), en ligne avec les exigences de la norme ISO 27001:2022 (Annexe A), ainsi que les obligations liées à la réglementation des données personnelles (RGPD) et à l'hébergement des Données de Santé (HDS).

> **Note :** en situation réelle, la PSSI serait doublée d'une politique de sécurité plus opérationnelle.

Les enjeux sont les suivants :

- Maintien de la sécurité du SI 24/7
- Assurer la Confidentialité, Intégrité et Disponibilité des données (personnelles, médicales, contractuelles, RH, R&D, etc.)
- Veiller au respect des contraintes légales et réglementaires
- Sensibiliser et former les collaborateurs à la sécurité de l'information
- Connaître et mitiger les risques cyber
- Assurer la résilience du SI et documenter les incidents
- Instaurer une procédure fiable de détection et de gestion des fuites de données
- Garantir l'image de marque de SantéConnect

### 1.3. Périmètre

La PSSI est applicable à la totalité du système d'information de SantéConnect, incluant toutes les informations matérielles ou logicielles nécessaires à leur gestion (création, acquisition, traitement, stockage, diffusion, destruction, etc.) où qu'elles se trouvent.

La fiche risques e-santé explicite la gestion des risques, structurée en :

- Cartographie des actifs avec niveau de criticité
- Identification des menaces par asset
- Top 5 des risques prioritaires
- Recommandations actionnables priorisées

→ [fiche-risques-e-sante.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-1-gouvernance/fiche-risques-e-sante.md)

Les actifs sont répartis entre :

- **Infrastructure** : tout élément physique supportant les processus du SI et toute forme d'interconnexion des composants matériels et logiciels
- **Applicatif** : tout programme, API ou exécutable contribuant aux opérations sur les données
- **Données** : toute donnée stockée chez SantéConnect, au format papier ou numérique
- **Collaborateur** : toute personne impliquée dans le SI (salariés, sous-traitants, partenaires, stagiaires ou apprentis)

Les risques de sécurité principaux identifiés sont :

- Cyberattaques et tentatives d'intrusion
- Erreurs humaines ou mauvaises pratiques
- Vulnérabilités techniques et failles applicatives

### 1.4. Durée et versioning

| Champ | Valeur |
|---|---|
| Date de première émission | 15/02/2024 |
| Numéro de version | v1.0 |
| Révision | Annuelle |
| Audit de suivi | Annuel |

### 1.5. Gouvernance

RACI défini dans le cadrage audit → [contexte-santeconnect.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-0-fondamentaux/contexte-santeconnect.md)

| Rôle | Responsabilité |
|---|---|
| Direction (CEO) | Valide les décisions stratégiques et le budget sécurité |
| RSSI (salarié, temps partiel) | Pilote la sécurité technique et la conformité |
| DPO (service externe) | Garant de la conformité RGPD/HDS |
| Responsable Produit | Garant Privacy by Design et Security by Design |
| DevOps | Implémente les mesures techniques (chiffrement, sauvegardes, logs) |
| Responsables Métiers (RH, Comptabilité) | Garants de la protection des données de leur périmètre |
| Utilisateurs | Respect des règles de sécurité |

> **Note :** Partenaire co-responsable : CHU Fictif - cadre défini par convention art. 26 RGPD (cf. [note-co-responsabilite-chu.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/note-co-responsabilite-chu.md))

### 1.6. Classification des données

Plus de détails dans le Registre des Traitements → [registre_traitement.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/registre-traitements/registre_traitement.md)

#### 🔴 Critique

- **Données médicales** : soumises aux règles RGPD-HDS, séparation des autres données par conception
- **Données salariés (RH/paie)** : exigences contractuelles, soumises aux obligations fiscales et réglementaires

*Mesures : Séparation par conception, Authentification MFA, OAuth2, Chiffrement AES-256*

#### 🟠 Sensible

- **Données personnelles B2C** : public âgé, soumises aux règles RGPD
- **Données personnelles B2B** : praticiens ayant accès aux données médicales
- **Données R&D/Statistiques** : anonymisées, soumises à validation DPO si doute

*Mesures : Authentification MFA, OAuth2, Surveillance des accès et des flux, Chiffrement AES-256*

#### 🟡 Standard

- **Logs IT** : suivi et documentation encadrés - archivage 6 mois (1 an glissant si incident)
- **Données utilisation site web** : conservation 1 an (Matomo auto-hébergé)

*Mesures : Accès Least Privilege, Surveillance des accès et des flux*

---

## 2. Mesures opérationnelles

### 2.1. Règles de gestion des accès : authentification, gestion des identités et contrôle des accès

SantéConnect applique le principe du **moindre privilège (least privilege)** par défaut. Tout premier accès est soumis à une approbation explicite du RSSI.

**Révocation des accès** - procédure automatisée sous 24h ouvrées lors :

- Du départ d'un salarié, à la date du départ
- Du changement de poste d'un salarié, à la date effective du changement
- De la suppression d'un compte utilisateur B2C ou B2B, à la date de suppression

> **Note :** Un praticien B2B disposera d'un outil d'export sur les données dont il a les droits pendant 30 jours suivant la clôture de son compte.

**Revue des habilitations** - menée semestriellement par le RSSI (maintien, modification, suppression), et déclenchée sur demande si incident ou si +20 nouveaux utilisateurs sur un mois.

**Authentification renforcée** - Pour l'accès aux données sensibles et critiques : authentification MFA obligatoire.

> **Note méthodologique :** La fiche risques préconisait le 2FA sur accès critiques. La PSSI retient le terme MFA - plus évolutif - et étend le périmètre aux données sensibles au regard du risque d'accès indirect aux données médicales documenté en 1.6.

**APIs** - SantéConnect applique la norme **OAuth2** pour autoriser les connexions des applications sans divulguer de données personnelles, et une validation stricte des entrées/sorties sur toutes les APIs exposées selon les recommandations **OWASP API Security Top 10**.

**Documentation associée :**

- Matrice des droits d'accès (RBAC)
- Logs d'habilitation (maintien, modification, suppression)
- Preuve d'activation MFA sur données sensibles et critiques, OAuth2 sur APIs exposées
- Revue d'audit semestrielle ou ponctuelle (incident / seuil de nouveaux utilisateurs)

---

### 2.2. Politique de protection des données : classification, chiffrement et sauvegardes

Classification des données : cf. **1.6** et Registre des Traitements.

SantéConnect applique un **cloisonnement** : base de données dédiée aux données de santé, séparée des données d'identification, par conception et dans les clauses contractuelles avec les sous-traitants.

**Chiffrement**

| Contexte | Standard |
|---|---|
| Au repos | AES-256 |
| En transit | TLS 1.3 |

**Sauvegardes**

- **Données médicales** : sauvegardes quotidiennes sur stockage OVH HDS dédié, mode WORM (immuabilité). Test de restauration mensuel automatisé. Test approfondi trimestriel avec vérification d'intégrité complète et validation RSSI. En cas d'incident majeur, les données médicales originelles restent disponibles au CHU comme source de récupération d'urgence.
- **Données hors médicales** : sauvegardes mensuelles sur serveur dédié, test de copie mensuel.

**Archivage après clôture de compte**

| Catégorie | Durée | Référence |
|---|---|---|
| Dossier médical | 20 ans, archivage restreint | CSP art. R.1112-7 (CHU) / R.1111-10 (autres praticiens) |
| Données de paiement | 3 ans | - |
| Logs IT | 6 mois (1 an glissant si incident) | - |
| Données utilisation site web | 1 an | Matomo auto-hébergé |
| Données RH/paie | 5 ans après dernière paie / 5 ans après fin de contrat | - |
| Autres données | 5 ans après dernière activité | Suppression à clôture si non liées à un dossier CHU |

**Documentation associée :**

- Registre des Traitements
- Politique de protection des données interne
- Logs de sauvegarde et tests de restauration

---

### 2.3. Procédure de gestion des incidents : détection et réponses

Détail de la procédure pour les données personnelles → [procedure-incident-notification.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/procedure-incident-notification.md)

**Détection**

- **Alertes OVH HDS** : détection quasi temps réel des anomalies infrastructure (accès, flux réseau)
- **Logs applicatifs centralisés (Graylog)** : détection quasi temps réel des comportements suspects au niveau applicatif (accès inhabituels, requêtes API anormales)
- **Analyse des journaux d'événements** : revue hebdomadaire automatisée

**Réponse et coordination**

- Le RSSI notifie les équipes DevOps sous **4h** pour tout incident impliquant des données médicales, sous **24h** pour les autres incidents
- Coordination avec les sous-traitants (OVH, Stripe) par clause contractuelle art. 28
- Coordination avec le CHU par convention art. 26
- Procédure de notification CNIL (72h) et personnes concernées documentée - cf. lien ci-dessus

---

### 2.4. Plan de gestion de crise

Se référer à **2.3** pour les premières heures après détection : coordination des équipes et, le cas échéant, notification aux organismes extérieurs et personnes concernées.

**À la détection d'un incident :**

**Actions immédiates**

- Isolation des systèmes compromis (isolation réseau et désactivation des accès via console OVH) et documentation horodatée (source alerte, premier constat) : **dans l'heure**
- Notification et coordination des équipes concernées : cf. 2.3
- Réunion de crise pilotée par le RSSI, secondée par le DPO (As a Service) : évaluation de la nature, de l'étendue et de l'impact de l'incident

**Mesures de mitigation** - cible : 72h (24h pour données critiques)

- *Containment* : blocage des accès suspects (comptes, IP)
- *Éradication* : réinitialisation des credentials des comptes compromis et privilégiés, correction des vulnérabilités, suppression des malwares

**Mesures de récupération** - sous 72h

- Test de tous les systèmes
- Vérification de l'intégrité des sauvegardes et restauration

**Clôture**

- Audit post-incident pour confirmer le succès des mesures : J+7+1
- Retour d'expérience (RSSI, DPO, CEO, équipes concernées) : J+15
  - Rapport d'incident et documentation des preuves - conservation 5 ans
  - Mise à jour du registre des traitements et du registre des incidents
  - Mise à jour des procédures de gestion des incidents et de la PSSI

---

### 2.5. Mécanismes de continuité d'activité

SantéConnect fixe les objectifs suivants. Le CHU et les praticiens disposent des données patients par ailleurs, ce qui sécurise la continuité des soins pendant la restauration.

| Indicateur | Valeur |
|---|---|
| RTO (délai max de restauration) | 72h |
| RPO données critiques | 24h |
| RPO données sensibles | 48h |
| RPO autres données | 72h |

> **Conformité RGPD/HDS :** Même pour les données non critiques, SantéConnect doit garantir la disponibilité et l'intégrité des données qu'elle gère (historiques partagés, plannings) et pouvoir restaurer ses services sous 72h pour éviter une violation de la sécurité des données.

**PCA - Maintien des services critiques en fonctionnement**
*Validé par RSSI et CEO, supervision DPO*

En cas d'interruption majeure, la continuité des soins est assurée par le CHU qui dispose des données patients par ailleurs. SantéConnect maintient un accès en lecture seule aux données non médicales via interface web OVH sur environnement isolé. Déclenchement sur validation RSSI et CEO.

**PRA - Restauration après interruption majeure**
*Validé par RSSI et CEO, supervision DPO*

- Restaurer la dernière sauvegarde quotidienne pour les données critiques, mensuelle pour les autres
- Vérifier l'intégrité des données avant mise en production
- Conserver les logs de tests de restauration (preuve)

---

### 2.6. Sensibilisation des collaborateurs et bonnes pratiques de sécurité

Chaque collaborateur SantéConnect suit un **e-learning de sensibilisation** à la protection des données personnelles à son entrée dans l'entreprise (prestataire formateur sélectionné par RH sur validation DPO). Les collaborateurs ayant accès à des données sensibles suivent une **formation complémentaire** dédiée.

Des **affiches** sur les bonnes pratiques de sécurité sont affichées en salle de pause et à l'entrée. Un **dashboard de conformité** est visible sur la home page interne, avec un lien vers le rappel des bonnes pratiques et un test de connaissances.

Annuellement, RH, DPO et RSSI auditent les niveaux de conformité et révisent la politique de formation si jugé insuffisant.

**Documentation associée :**

- Plan de formation annuel (général + spécificités par métier)
- Preuves de présence aux formations et certifications pour métiers spécifiques
- Dashboard de conformité, site interne et affiche
- Audit annuel du plan de formation

---

## 3. Validation et déploiement de la PSSI

### Signatures

Atelier de validation PSSI : **20/01/2024** - Version émise le **15/02/2024**

| Rôle | Nom | Date de signature |
|---|---|---|
| CEO SantéConnect | Martin DUPONT | 20/01/2024 |
| DPO SantéConnect (As a Service) | Jeanne PETIT | 20/01/2024 |
| RSSI | Claire ESPINOZA | 20/01/2024 |
| RH | Bernard THOMAS | 20/01/2024 |
| Comptabilité | Géraldine DUMONT | 20/01/2024 |
| Développement Produit | Stéphane ROY | 20/01/2024 |

### Déploiement

- **Communication interne** : plan de formation + actions de sensibilisation + dashboard de suivi de conformité déployés sous 1 mois
- **Audit annuel PSSI** : piloté par CEO, DPO, RSSI et RH - sous 15 jours si incident
- **Revue de direction annuelle (ISO 27001 cl. 9.3)** : examen des indicateurs de performance sécurité, résultats d'audit et actions correctives - pilotée par CEO avec RSSI et DPO

---

*Document produit dans le cadre du projet portfolio GRC - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*
*Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité.*
