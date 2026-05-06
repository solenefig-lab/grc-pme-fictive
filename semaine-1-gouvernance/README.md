# Semaine 1 - Gouvernance & Gestion des risques

> **Cas d'étude :** SantéConnect, PME e-santé fictive. Les livrables reflètent une démarche GRC réelle adaptée aux contraintes d'une PME de 15 personnes.

---

## Objectif

Poser les bases de l'audit GRC : gouvernance, cartographie des actifs et évaluation des risques pour prioriser les actions sécurité dès le départ.

---

## Points méthodologiques clés

- **Matrice de risques 3×3** - dimensionnée et lisible pour une petite PME e-santé, sans surcharge méthodologique.
- **Identification des 5 risques prioritaires** à traiter en premier.
- **Arbitrage clé** : Risque accepté sur l'interconnexion avec le CHU (exposition externe, pivot vers CHU, systèmes tiers non maîtrisés) - justifié par l'indépendance des systèmes historiques vis-à-vis de l'infrastructure PME, compensé par chiffrement BDD, authentification renforcée et contrôle des flux.

---

## Livrables

| Fichier | Description |
|---|---|
| [`cadrage-audit.md`](./cadrage-audit.md) | Document de cadrage de l'audit GRC |
| [`fiche-risques-e-sante.md`](./fiche-risques-e-sante.md) | Fiche de gestion des risques |

---

## 🛠️ Ressources associées

Ces templates sont issus de ce projet et réutilisables pour toute PME souhaitant produire un premier état des lieux de ses actifs et risques :

- [**Cartographie des actifs GRC - Version PME**](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/ressources/grc-asset-inventory-template-pme.xlsx) - Inventaire des actifs, grille de scoring 3×3, mapping des risques, accessible sans expertise technique.
- [**Cartographie des actifs GRC - Version Advanced**](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/ressources/grc-asset-inventory-template-pme-threats.xlsx) - Même outil avec mapping des tactiques MITRE ATT&CK, orienté équipes techniques et cabinets GRC.

---

## ➡️ Prochaine étape

La semaine 2 s'appuie sur la cartographie des actifs et l'analyse de risques pour structurer la conformité RGPD-HDS : registre des traitements, AIPD et procédure de gestion des incidents.

→ [Semaine 2 - Audit RGPD-HDS](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/semaine-2-rgpd-hds/README.md)
