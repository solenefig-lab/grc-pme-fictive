# Registre des Traitements — SantéConnect

> **Projet de démonstration pédagogique** — SantéConnect est une PME fictive. Les livrables reflètent une démarche GRC réelle adaptée à un contexte simulé. Le niveau de granularité illustre une cible de maturité RGPD, non l'état courant du marché TPE/PME santé.

---

## 1. Objectif et livrable

| | |
|---|---|
| **Objectif** | Registre des Traitements RGPD de la PME SantéConnect |
| **Livrable** | Registre des Traitements et fiche associée pour chaque type de traitement |
| **Méthode** | Analyse documentaire + interviews fictives + vérifications opérationnelles |

---

## 2. Périmètre — Données traitées

| Réf. | Nom du traitement | Finalité | Données sensibles |
|---|---|---|---|
| D-001 | Gestion des comptes patients | Création et gestion des comptes utilisateurs (patients) pour l'accès aux services SantéConnect, incluant l'authentification et la récupération de mot de passe. | Non |
| D-002 | Données de santé | Suivi cardiologique (incl. affichage dossier CHU, coffre-fort médical, messagerie praticien) pour patients ayant donné leur consentement éclairé, rétractable à tout moment + NIR | **Oui** |
| D-003 | Données de paiement (abonnements premium) | Gestion des abonnements premium, incluant la collecte des paiements, la facturation et le suivi des transactions. | Non |
| D-004 | Données praticiens B2B | Identification et gestion des comptes praticiens sur la plateforme B2B | Non |
| D-005 | Échanges avec le CHU | Continuité de la prise en charge médicale du patient via partage du dossier médical avec le CHU partenaire | **Oui** |
| D-006 | Support client | Gestion des plaintes et retours clients sur accès et utilisation service, à l'exclusion de toute donnée de santé (sous réserve de cloisonnement technique garanti) | Non |
| D-007 | Gestion RH et Paie | Gestion des contrats, de la paie et des congés — calcul des rémunérations et versements aux organismes sociaux | Non |
| D-008 | Logs IT et gestion des accès | Suivi sécurité, accès et journalisation (sans accès aux données de santé par conception) | Non |
| D-009 | Statistiques / R&D | Amélioration du service et analyse statistique des parcours de soins cardiologiques en vue d'extension géographique, sur données agrégées/anonymisées | Non |
| D-010 | Analyses d'audience du site web marketing | Mesure de fréquentation et comportement des visiteurs du site marketing, sur consentement (RGPD art. 6.1.a) | Non |

---

## 3. Référentiels applicables

| Référentiel | Base légale | Périmètre |
|---|---|---|
| RGPD | Art. 6.1.a | Consentement |
| RGPD | Art. 6.1.b | Exécution du contrat |
| RGPD | Art. 6.1.c | Obligation légale |
| RGPD | Art. 6.1.f | Intérêt légitime (ex. sécurité des systèmes) |
| RGPD | Art. 9.2.a | Données sensibles — consentement explicite |
| RGPD | Art. 9.2.g | Motifs d'intérêt public important |
| RGPD | Art. 9.2.h | Nécessité pour les soins |
| RGPD | Art. 9.2.j | Recherche scientifique, statistiques ou archivage d'intérêt public (avec pseudonymisation obligatoire) |
| RGPD | Art. 17 | Droit à l'effacement — révocation des droits d'accès |
| RGPD | Art. 26 | Co-responsabilité de traitement |
| RGPD | Art. 28 | Contrat de sous-traitance |
| RGPD | Art. 33 | Notification CNIL en cas d'incident (72h) |
| RGPD | Art. 34 | Notification des personnes concernées en cas d'incident |
| CSP | Art. R-1111-10 | Obligation de conservation des données de santé — praticiens libéraux |
| CSP | Art. R-1112-7 | Obligation de conservation des données de santé — établissements hospitaliers |
| HDS | — | Hébergement des données de santé (certification OVH) |
| PCI-DSS | — | Sécurité des moyens de paiement (via Stripe) |
| Loi I&L | Art. 25 | Donnée à protection renforcée (NIR) — usage strictement limité aux obligations sociales et fiscales |

---

## 4. Structure des fichiers

```
registre-traitements/
├── registre_traitement.md          ← ce fichier
├── liste-des-traitements.csv
├── D-001_gestion-comptes-patients.csv
├── D-002_donnees-sante.csv
├── D-003_donnees-paiement.csv
├── D-004_donnees-praticiens.csv
├── D-005_echanges-chu.csv
├── D-006_support-client.csv
├── D-007_gestion-rh-paie.csv
├── D-008_logs-it.csv
├── D-009_stats-rd.csv
└── D-010_audience-site-web.csv
```

---

*Dernière mise à jour : avril 2024 — Validation DPO : DPO As A Service*
