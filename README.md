# GRC Fil Rouge — Démarche complète pour une HealthTech fictive

![Domaine](https://img.shields.io/badge/Domaine-GRC%20%7C%20Cybersécurité-purple)
![Secteur](https://img.shields.io/badge/Secteur-e--Santé-blue)
![Référentiels](https://img.shields.io/badge/Référentiels-RGPD%20%7C%20HDS%20%7C%20NIS2%20%7C%20ISO%2027001-red)
![Status](https://img.shields.io/badge/Status-En%20cours-orange)
![Niveau](https://img.shields.io/badge/Niveau-Junior%20GRC-yellow)

> ⚠️ **Projet de démonstration pédagogique** — basé sur une PME fictive
> (SantéConnect). Les livrables reflètent une démarche GRC réelle adaptée
> à un contexte simulé. Ils évoluent semaine après semaine au fil de la
> montée en compétences de l'auteure. La démarche s’appuie sur une logique inspirée d’EBIOS Risk Manager (formalisation complète en semaine 5).

# SantéConnect — Démarche GRC complète pour une HealthTech fictive

> Simuler la mise en place d'une démarche GRC complète pour une PME du domaine
> de la e-santé — de l'audit initial à l'impact NIS2 — pour démontrer des
> compétences en tant que consultante junior GRC et interface senior métier-IT.

---

## 🏥 SantéConnect en bref

SantéConnect est une PME fictive de 15 employés qui connecte patients et
médecins/praticiens pour améliorer le suivi, le partage d'informations et la
prise de rendez-vous tout au long du parcours de soin.

- **Utilisateurs :** 100 utilisateurs actifs (patients + praticiens)
- **Partenariat :** CHU local — spécialité cardiologie
- **Produits :** application mobile + WebApp patients / interface praticiens
- **Hébergement :** 100 % France
- **Valeurs fondatrices :** consentement éclairé, simplicité, sécurité

---

## 📂 Livrables
| Semaine | Thème | Livrable | Statut |
|---------|-------|----------|--------|
| [0](./semaine-0-fondamentaux/contexte-santeconnect.md) | Fondamentaux | [Présentation SantéConnect](./semaine-0-fondamentaux/contexte-santeconnect.md) | ✅ Complet |
| [1](./semaine-1-gouvernance/README.md) | Gouvernance & Risques | [Cadrage audit](./semaine-1-gouvernance/cadrage-audit.md) · [Fiche risques](./semaine-1-gouvernance/fiche-risques-e-sante.md) | ✅ Complet |
| 2 | RGPD & HDS | Audit RGPD-HDS + template registre | 🔄 En cours |
| 3 | ISO 27001 | PSSI adaptée à la santé | 🔄 En cours |
| 4 | NIS2 | Synthèse impact NIS2 + plan d'action | 🔄 En cours |

---

## 🛠️ Ressources réutilisables

Des outils conçus dans le cadre de ce projet, adaptables à toute PME :

| Outil | Public cible | Accès |
|-------|-------------|-------|
| Cartographie des actifs GRC: Version PME | Dirigeants, DPO, consultants junior | [📥 Télécharger](./ressources/grc-asset-inventory-template-pme.xlsx) |
| Cartographie des actifs GRC: Version Advanced | Équipes techniques, cabinets GRC | [📥 Télécharger](./ressources/grc-asset-inventory-template-pme-threats.xlsx) |

> Conçu avec une posture *"GRC comme produit"*, simple, progressif, ancré dans la réalité opérationnelle d'une PME.

----

## ⚖️ Référentiels mobilisés

| Référentiel | Obligation | Périmètre |
|-------------|------------|-----------|
| **RGPD** | Obligatoire | Toutes données personnelles et de santé |
| **HDS** | Obligatoire | Hébergement de données de santé en France |
| **NIS2** | Applicable | Secteur santé — indirectement via partenariat CHU |
| **ISO 27001** | Recommandée | Sécurité de l'information — référence de marché |
| **Code de Santé Publique** | Obligatoire | Secret médical + partage inter-praticiens |
| **RGS + PGSSI-S** | Applicable | Échanges sécurisés avec le CHU partenaire (établissement public) |

---


## 👩‍💻 À propos de l'auteure

**Solène Figueiredo**
Chef de Projet Cybersécurité | Ex-Renault – Déploiements internationaux (100 pays)
GRC · Risques · Transformation digitale · Interface IT-métier

Positionnement : interface entre technique, risques et décision métier, au
service de projets cybersécurité ancrés dans la réalité opérationnelle.

**Parcours :** 10 ans de pilotage de projets digitaux internationaux chez
Renault
> Campagnes simultanées dans plus de 100 pays (Twizy), programmes CRM
multi-marchés (ZOE), gestion de plateformes digitales sur 40 pays.
> Habituée aux environnements complexes : coordination d'équipes pluridisciplinaires,
enjeux business critiques, contraintes de délais et de qualité.

**Aujourd'hui :** spécialisation en cybersécurité avec un positionnement
opérationnel en GRC, gestion des risques et coordination de projets sécurité.

Capacités démontrées dans ce projet :
- Analyser des situations de sécurité (permissions, exposition, vulnérabilités)
- Identifier les risques associés (escalade de privilèges, fuite de données,
  mauvaises configurations)
- Formuler des recommandations actionnables (hardening, IAM, sensibilisation)
- Relier les risques aux exigences réglementaires (RGPD, NIS2, ISO 27001)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-solenefigueiredo-blue)](https://www.linkedin.com/in/solene-figueiredo/)
[![Portfolio](https://img.shields.io/badge/Portfolio-happygomotion.com-lightgrey)](https://www.happygomotion.com/fr/showcase)
