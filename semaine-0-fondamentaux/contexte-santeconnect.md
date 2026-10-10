# SantéConnect – Fiche de présentation
**PME fictive spécialisée en e-santé cardiologique**

*Connecter patients et praticiens pour un suivi sécurisé et personnalisé.*

> ⚠️ **Projet de démonstration pédagogique** — SantéConnect est une PME fictive.
> Les livrables reflètent une démarche GRC réelle adaptée à un contexte simulé.

---

## 📌 Contexte et mission

- **Taille** : 15 employés (dont 3 devs, 1 RSSI à temps partiel, 1 Responsable Produit) + 1 DPO (externe, as-a-service)
- **Utilisateurs** : 80 patients + 20 praticiens (cardiologues, infirmiers, kinés)
- **Partenariat clé** : CHU Local – Service de Cardiologie
- **Hébergement** : OVH Health Data Hosting (certifié HDS) – Gravelines, France

**Valeurs fondatrices :**
| Valeur | Description |
|--------|-------------|
| Consentement éclairé | Opt-in explicite pour le partage de données (RGPD Art. 9) |
| Simplicité | UX adaptée aux seniors (public cible en cardiologie) |
| Sécurité by design | Chiffrement, traçabilité, hébergement France |

**Partenariat CHU :**
Échange de données (ex : résultats d'ECG) via API sécurisée standard **HL7/FHIR**.
→ **Enjeu GRC** : Rôles RGPD qualifiés par traitement (sous-traitance art. 28 ou co-responsabilité art. 26, cf. registre des traitements et convention CHU) ; chiffrement des flux.

---

## 🔍 Périmètre technique et fonctionnel

### 1. Infrastructure et applications

| Composant | Description | Enjeux GRC |
|-----------|-------------|------------|
| **App Mobile B2C** | Suivi cardiologique (poids, tension, rappels médicaments), coffre-fort médical (PDF ordonnances), messagerie sécurisée praticiens | Chiffrement données locales (AES-256), consentement granulaire |
| **WebApp B2C** | Version web de l'app (mêmes fonctionnalités) | Authentification forte (2FA), journalisation des accès |
| **Plateforme B2B** | Dossiers patients (droits par spécialité + consentement), agenda partagé, facturation | RBAC (rôles : médecin, infirmier, admin), traçabilité des accès |
| **Hébergement** | OVH Health Data Hosting (certifié HDS) – Gravelines, France | Vérification certification HDS, contrat sous-traitance RGPD |
| **APIs externes** | Laboratoires d'analyses, CHU Local, Stripe (paiements premium) | Sécurité APIs (OAuth2, logs), clauses RGPD avec chaque partenaire |

### 2. Données traitées

| Type de données | Exemples | Réglementation applicable | Risque principal |
|-----------------|----------|--------------------------|-----------------|
| Données personnelles | Nom, email, NIR | RGPD (Art. 4–9) | Usurpation d'identité |
| Données de santé | Antécédents cardiologiques, ordonnances, résultats ECG/analyses | RGPD (Art. 9) + HDS | Fuite de données sensibles (plafond de 20 M€ ou 4 % du CA mondial, le plus élevé (art. 83(5))) |
| Données de paiement | CB pour abonnements premium | PCI-DSS (via Stripe) | Fraude |
| Données praticiens | Nom, spécialité, rattachement établissement | RGPD | Accès non autorisé à des dossiers patients |

### 3. Processus métiers critiques

| Processus | Description | Réglementations concernées |
|-----------|-------------|---------------------------|
| Création de compte | Inscription en présentiel lors du contact avec le CHU (vérification d’identité, présentation du service, premier recueil du consentement), vérification du mobile par code, puis MFA | RGPD (Art. 5, 6, 9), PGSSI-S (identification électronique) |
| Partage de dossiers | Patient donne son consentement pour partager son dossier avec un praticien | RGPD (Art. 7, 9), Code Santé Public, HDS |
| Facturation premium | Paiement des abonnements via Stripe | PCI-DSS, RGPD (données de paiement) |
| Clôture de compte | Suppression ou archivage des données selon leur nature | RGPD (Art. 17) — voir section conservation ci-dessous |
| Support client | Réponses aux questions via email/tchat | RGPD (accès aux données par un tiers) |

---

## 🗂️ Gestion de la conservation des données (tension RGPD / CSP)

### Cadre légal applicable

| Article | Portée | Impact SantéConnect |
|---------|--------|-------------------|
| **RGPD Art. 17** | Droit à l'effacement sur demande du patient | S'applique aux données dont SantéConnect est responsable de traitement |
| **Art. R. 1112-7 CSP** | Conservation 20 ans des dossiers médicaux hospitaliers | S'applique aux données transmises par le CHU |
| **Art. L. 1111-8 CSP + R. 1111-10 CSP** | Obligation de certification HDS pour tout hébergeur | S'applique à OVH (hébergeur de SantéConnect) |
| **Art. R. 4127-45 (code de déontologie médicale)** | Conservation sous la responsabilité du médecin ; pas de durée légale fixe pour les libéraux (alignement recommandé sur R. 1112-7, 20 ans) | La responsabilité incombe au praticien, pas à SantéConnect |

### Solution : distinction par type de données

| Type de données | Origine | Rôle de SantéConnect | Durée de conservation | Solution Art. 17 RGPD |
|-----------------|---------|---------------------|----------------------|----------------------|
| Données transmises par le CHU | Dossier médical hospitalier | Qualifié par traitement (art. 28 ou 26, cf. semaine 2) | 20 ans (Art. R. 1112-7) | Archivage restreint : verrouillage de l'accès. La demande est relayée au CHU, responsable de ces données, que SantéConnect assiste. Le patient est informé de la conservation légale (20 ans). |
| Données créées dans l'app | Suivi personnel (tension, poids) | Responsable de traitement | 5 ans (recommandation CNIL) | Effacement possible après vérification d'absence de lien avec un dossier hospitalier |
| Données de compte | Email, identité | Responsable de traitement | 3 ans après clôture | Effacement complet après vérification des obligations légales (facturation) |
| Données praticiens libéraux | Dossiers patients stockés via app | Sous-traitant | 20 ans (alignement recommandé sur R. 1112-7, art. R. 4127-45) - responsabilité praticien | Contrat de sous-traitance + recommandation d'export avant clôture |

### Processus de clôture de compte

1. Le patient demande l'effacement via l'app
2. SantéConnect :
   - **Efface** les données créées dans l'app (notes personnelles, suivi)
   - **Archive** (sans accès) les données transmises par le CHU avec notification, sur instruction du CHU : *"Vos données hospitalières sont archivées pour respecter les obligations légales (20 ans). Vous pouvez demander un accès restreint via votre médecin."*
   - **Anonymise** les données de suivi après 5 ans (suppression des liens avec l'identité du patient)
   - **Transfère** les données CHU vers un stockage froid (OVH Archive) avec accès restreint, sur instruction du CHU

---

## ⚖️ Contexte réglementaire

| Référentiel | Obligation | Périmètre |
|-------------|------------|-----------|
| **RGPD** | Obligatoire | Toutes données personnelles et de santé |
| **HDS** | Obligatoire | Hébergement de données de santé en France |
| **NIS2** | Applicable | Secteur santé — Indirecte, supply chain via CHU (hors périmètre direct a priori) * |
| **ISO 27001** | Recommandée | Sécurité de l'information — référence de marché |
| **Code de Santé Publique** | Obligatoire | Secret médical + partage inter-praticiens + conservation |
| **RGS + PGSSI-S** | PGSSI-S : directe pour l’identification électronique des usagers ; indirecte pour les flux avec le CHU. RGS : indirecte | Flux HL7/FHIR avec le CHU (établissement public) ; référentiels PGSSI-S opposables à lister |

* SantéConnect n’entre a priori pas directement dans le périmètre NIS2 au regard de sa taille.
Toutefois, en tant que prestataire d’un établissement de santé, elle peut être concernée indirectement via des exigences de sécurité imposées par ses partenaires (logique de supply chain).

---

## 👥 Acteurs clés et responsabilités

### Rôles internes

| Rôle | Responsabilité GRC |
|------|--------------------|
| **Direction (PDG/COO)** | Valide les décisions stratégiques et le budget sécurité |
| **RSSI** | Pilote la sécurité technique et la conformité |
| **DPO** | Garant de la conformité RGPD/HDS — désignation volontaire (art. 37(4) RGPD), justifiée par la sensibilité des données et les exigences du CHU |
| **Responsable Produit** | Garant Privacy by Design et Security by Design dès la conception des fonctionnalités |
| **DevOps** | Implémente les mesures techniques (chiffrement, sauvegardes, logs) |

_Note : Direction = CEO ; Responsable Produit = Dev Produit ; DevOps = rôle tenu au sein des 3 devs._

### Acteurs externes

| Acteur | Rôle | Enjeu contractuel |
|--------|------|-------------------|
| **CHU Local** | Fournit des données médicales, impose des exigences de sécurité | Contrat de sous-traitance RGPD + clauses HL7/FHIR |
| **OVH** | Hébergeur certifié HDS | Vérification annuelle de la certification |
| **Stripe** | Paiements premium | Conformité PCI-DSS |
| **Praticiens libéraux** | Utilisateurs B2B — responsables de leurs dossiers patients | Contrat précisant les responsabilités de conservation |

### RACI – Responsabilités GRC

*R = Responsible (réalise) · A = Accountable (valide) · C = Consulted (est consulté) · I = Informed (est informé) · A/R = Accountable et Responsible*  
*Règles : un seul A par ligne, au moins un R, les acteurs externes (CHU, praticiens) en C ou I uniquement.*

| Processus / Tâche | Direction | RSSI | DPO | Resp. Produit | DevOps | CHU | Praticiens |
|-------------------|-----------|------|-----|---------------|--------|-----|------------|
| Définir la stratégie GRC | A | R | C | C | I | C | - |
| Désigner le DPO | A/R | C | - | - | I | - | - |
| Approuver le budget sécurité | A | R | C | C | I | - | - |
| Rédiger la PSSI | A | R | C | C | C | I | - |
| Mettre en place le chiffrement | I | A | I | C | R | - | - |
| Gérer les consentements patients | I | C | R | A | C | C | I |
| Notifier un incident (RGPD/NIS2) | A | R | R | I | C | C | I |
| Auditer les sous-traitants | I | A/R | C | I | C | - | - |
| Former les équipes à la sécurité | C | A/R | C | I | I | - | I |
| Gérer les accès (RBAC) | I | A | C | C | R | C | I |
| Valider les échanges avec le CHU | A/R | C | C | C | I | C | - |
| Tester les sauvegardes | I | A | I | - | R | - | - |
| Répondre à une demande RGPD (droit d'accès/suppression) | I | C | R | A | C | I | I |
| Définir les fonctionnalités (ex : coffre-fort médical) | C | C | C | A/R | I | C | C |
| Intégrer Privacy by Design | I | C | C | A/R | C | I | I |
| Valider Security by Design | I | A | C | R | C | I | I |
| Suivre les évolutions réglementaires | I | R | A/R | C | I | C | I |
| Gérer les demandes d'effacement (Art. 17 RGPD) | I | C | A | R | C | C | I |

---

## 🛠️ Outils et méthodologie

- **Approche** : « GRC comme produit », pragmatique, progressive, ancrée dans la réalité d'une PME ; chaque livrable est daté.
- **Cotation des risques** : grille 3×3 (Impact × Probabilité) ; formalisation inspirée d'EBIOS Risk Manager.
- **Référentiels** : RGPD et HDS (obligatoires), ISO 27001:2022 comme cadre de référence, NIS2 en lecture supply chain (CHU).
- **Outils** : Markdown versionné sous Git ; modèles Excel d'inventaire des actifs et autres [ressources](../ressources/README.md).

---

## 📎 Principaux documents associés

| Semaine | Livrable |
|---------|----------|
| [Semaine 1](../semaine-1-gouvernance/README.md) | [Fiche risques](../semaine-1-gouvernance/fiche-risques-e-sante.md) |
| [Semaine 2](../semaine-2-rgpd-hds/README.md) | [Audit RGPD-HDS](../semaine-2-rgpd-hds/checklist-audit-rgpd-hds.md) + [Registre des traitements](../semaine-2-rgpd-hds/registre-traitements/registre_traitement.md) |
| [Semaine 3](../semaine-3-iso27001/README.md) | [PSSI adaptée à la santé](../semaine-3-iso27001/pssi.md) |
| [Semaine 4](../semaine-4-nis2/README.md) | [Synthèse impact NIS2](../semaine-4-nis2/analyse-impact-nis2.md) + [Plan d'action](../semaine-4-nis2/plan_action_nis2.md) |
