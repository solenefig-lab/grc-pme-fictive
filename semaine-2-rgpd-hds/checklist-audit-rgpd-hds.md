# Checklist audit RGPD-HDS - SantéConnect

> **Document fictif** - Projet portfolio GRC (SantéConnect, PME e-santé fictive). Le niveau de granularité illustre une cible de maturité RGPD, non l'état courant du marché TPE/PME santé.

Cette checklist s'appuie sur les livrables suivants : registre D-001→D-010, AIPD, note de convention de co-responsabilité CHU, synthèse des clauses sous-traitants.

---

## Modalités d'utilisation

| | |
|---|---|
| **Fréquence** | Annuelle - janvier |
| **Pilotage** | CEO SantéConnect + RSSI |
| **Validation** | DPO As a Service (Jeanne Petit) |
| **Premier audit** | Janvier 2025 |

---

## Partie 1 - Checklist RGPD

### 1. Évaluation du niveau de sécurité des données personnelles
*(Source : guide CNIL "La sécurité des données personnelles")*

- [ ] Sensibilisation des salariés manipulant les données et charte informatique
- [ ] Politique de gestion des accès : authentification, habilitation, logs et gestion des incidents
- [ ] Sécurisation de l'infrastructure : postes de travail, informatique mobile, réseau interne, serveurs
- [ ] Sécurisation de l'applicatif : sites web, app B2C, app B2B
- [ ] Politique de gestion des sauvegardes (continuité d'activité), sécurisation de l'archivage, maintenance et destruction des données
- [ ] Politique de gestion de la sous-traitance
- [ ] Gestion sécurisée des échanges avec d'autres organismes
- [ ] Protection des locaux
- [ ] Encadrement du développement informatique
- [ ] Utilisation du chiffrement

---

### 2. Conformité RGPD

**Respect des principes de traitement des données :**
- [ ] Base légale documentée par traitement (consentement / exécution du contrat / intérêt légitime)
- [ ] Finalité déterminée, explicite et légitime
- [ ] Minimisation des données collectées
- [ ] Exactitude et mise à jour des données
- [ ] Durées de conservation et suppressions documentées
- [ ] Registre des traitements à jour (D-001→D-010)

**Gestion des droits des personnes concernées :**
- [ ] Droit d'accès
- [ ] Droit de rectification
- [ ] Droit à l'effacement
- [ ] Droit à la restriction du traitement
- [ ] Droit d'opposition
- [ ] Droit à la portabilité
- [ ] Délai de réponse respecté (1 mois - RGPD art. 12.3)
- [ ] Transparence du traitement documentée dans les CGU

**Mesures de confidentialité et protection des données :**
- [ ] Mesures techniques en place (chiffrement, contrôle d'accès, logs)
- [ ] Mesures organisationnelles documentées (procédures, formation)
- [ ] AIPD réalisée et à jour *(nécessaire - données de santé art. 35)*
- [ ] DPO désigné et opérationnel *(nécessaire - données de santé à grande échelle)*
- [ ] Politique de gestion des incidents documentée
- [ ] Procédure de notification CNIL opérationnelle (art. 33-34)

**Gestion des transferts et partages de données :**
- [ ] Accord formel sous-traitants conforme art. 28 (OVH, Stripe, Matomo si SaaS)
- [ ] Transferts limités à la zone EEE ou couverts par mécanisme art. 46 (CCT)
- [ ] Convention de co-responsabilité CHU à jour *(nécessaire - art. 26)*

---

## Partie 2 - Checklist HDS

*(Référentiel : L.1111-8 CSP + certification ANS)*

- [ ] Révision annuelle du contrat d'hébergement OVH
- [ ] Vérification annuelle du certificat HDS OVH - valide, à jour, périmètre conforme *(activités 1-4 et 6 - L.1111-8 CSP)*
- [ ] Administration et exploitation du SI de SantéConnect conformes aux exigences HDS - procédures documentées *(activité 5 - L.1111-8 CSP)*
- [ ] Données de santé cloisonnées des autres données par conception (séparation base de données + chiffrement AES-256)
- [ ] PRA/PCA documenté et testé *(cf. semaine 3 - ISO 27001)*
- [ ] Audit annuel conjoint de conformité HDS/RGPD conduit avec le co-responsable CHU Fictif

---

*Document produit dans le cadre du projet portfolio GRC - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*
*Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité.*
