# Cadrage de l'audit GRC — SantéConnect

> **Projet de démonstration pédagogique** — SantéConnect est une PME fictive.
> Les livrables reflètent une démarche GRC réelle adaptée à un contexte simulé.

> **Note méthodologique** — Dans le cadre de ce projet pédagogique,
> la collecte documentaire et les entretiens terrain sont simulés.
> Les sections correspondantes illustrent la démarche qu'un consultant
> appliquerait en contexte réel. Les constats et risques identifiés
> sont basés sur les caractéristiques fictives de SantéConnect.
---

## 1. Objectif et livrable

| | |
|--|--|
| **Objectif** | Audit GRC de la PME SantéConnect |
| **Livrable** | Fiche de gestion des risques en e-santé |
| **Méthode** | Analyse documentaire + interviews fictives + vérifications opérationnelles |

---

## 2. Périmètre

### Infrastructure et applications

| Asset | Type |
|-------|------|
| App Mobile B2C | Applicatif |
| WebApp B2C | Applicatif |
| Plateforme B2B | Applicatif |
| Hébergement (OVH HDS) | Infrastructure |
| APIs externes (CHU, laboratoires, Stripe) | Infrastructure |
| Équipement routage et sécurité | Infrastructure |

### Données traitées

| Catégorie | Exemples |
|-----------|----------|
| Données personnelles patients | Nom, email, numéro de sécurité sociale |
| Données de santé | Antécédents, ordonnances, résultats ECG |
| Données de paiement | CB pour abonnements premium |
| Données praticiens | Nom, spécialité, rattachement établissement |
| Authentification | Identifiants, tokens, clés API |
| Droits d'accès | RBAC, inventaire des comptes |
| Clôture et archivage | Données post-clôture de compte |

### Personnel

| Thème | Contenu |
|-------|---------|
| Rôles et responsabilités | RACI défini dans [Contexte SantéConnect](../semaine-0-fondamentaux/contexte-santeconnect.md) |
| Formation équipes opérationnelles | Législation, risques, MCS, authentification, durcissement, cloisonnement réseau, journalisation |
| Sensibilisation utilisateurs | Bonnes pratiques à l'arrivée et à intervalles réguliers (mails, affichage, intranet) |

---

## 3. Référentiels applicables

| Référentiel | Obligation | Périmètre |
|-------------|------------|-----------|
| **RGPD** | Obligatoire | Toutes données personnelles et de santé |
| **HDS** | Obligatoire | Hébergement de données de santé en France |
| **NIS2** | Applicable | Secteur santé — partenariat CHU, indépendamment de la taille |
| **ISO 27001** | Recommandée | Sécurité de l'information — référence de marché |
| **Code de Santé Publique** | Obligatoire | Secret médical + partage inter-praticiens + conservation |
| **RGS + PGSSI-S** | Applicable | Échanges sécurisés avec le CHU partenaire (établissement public) |

---

## 4. Collecte documentaire

| Document | Existant | Récupéré | Évaluation |
|----------|----------|----------|------------|
| Schéma informatique du réseau | | | |
| Politique de sécurité (PSSI) | | | |
| Procédures générales | | | |
| Procédures d'arrivée, départ, changement de fonction | | | |
| Procédure de gestion des incidents sécurité | | | |
| Procédure de contrôle et audit régulier | | | |
| Registre des traitements (RGPD) | | | |
| Politique de gestion des accès | | | |
| Inventaire exhaustif des comptes privilégiés | | | |
| PRA / PCA | | | |
| Politique de mise à jour des composants SI | | | |
| Journaux des composants critiques | | | |
| Politique de sauvegarde des composants critiques | | | |
| Analyse de risques formelle existante | | | |
| Attestations de suivi des formations sécurité | | | |
| Clauses sécurité dans contrats prestataires externes | | | |
| Autre (à préciser) | | | |

---

## 5. Interviews terrain

| Interlocuteur | Objectif |
|---------------|----------|
| PDG / COO | Vision stratégique, budget sécurité, appétence au risque |
| RSSI | Mesures techniques en place, incidents passés, monitoring |
| DPO | Conformité RGPD/HDS, registre des traitements, consentements |
| Responsable Produit | Privacy by design, security by design, gestion des consentements |
| DevOps | Chiffrement, sauvegardes, logs, gestion des accès techniques |
| Responsable RH | Procédures arrivée/départ, formations, clauses contractuelles |

> **Objectif des entretiens :** détecter les écarts entre ce qui est théoriquement prévu et ce qui est réellement appliqué.

---

## 6. Tests et vérifications opérationnelles

| Vérification | Méthode | Statut |
|--------------|---------|--------|
| Comptes actifs d'anciens employés | Revue IAM | |
| Droits d'accès (principe du moindre privilège) | Revue RBAC | |
| Sauvegardes fonctionnelles | Test de restauration | |
| 2FA activé sur tous les accès critiques | Vérification technique | |
| Logs actifs et exploitables | Revue des journaux | |
| Ports ouverts non nécessaires | Scan réseau | |
| Tokens / clés API exposés | Scanner de secrets | |
| Certification HDS OVH à jour | Vérification documentaire | |

---

## 7. Analyse des écarts et des risques

Comparaison **réel vs théorique** + évaluation du risque (Impact × Probabilité).

→ Voir [`fiche-risques-e-sante.md`](./fiche-risques-e-sante.md) pour la cartographie complète et la priorisation.

---

## 8. Rapport et plan d'action

Le livrable final est la **fiche de gestion des risques en e-santé** ([`fiche-risques-e-sante.md`](./fiche-risques-e-sante.md)), structurée en :

1. Cartographie des actifs avec niveau de criticité
2. Identification des menaces par asset
3. Top 5 des risques prioritaires
4. Recommandations actionnables priorisées
