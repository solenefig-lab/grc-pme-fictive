# GRC Fil Rouge - Démarche complète pour une HealthTech fictive

![Domaine](https://img.shields.io/badge/Domaine-GRC%20%7C%20Cybersécurité-purple)
![Secteur](https://img.shields.io/badge/Secteur-e--Santé-blue)
![Référentiels](https://img.shields.io/badge/Référentiels-RGPD%20%7C%20HDS%20%7C%20ISO%2027001%20%7C%20NIS2%20%7C%20ReCyF-red)
![Méthode](https://img.shields.io/badge/Méthode-EBIOS%20Risk%20Manager-darkgreen)
![Outils](https://img.shields.io/badge/Outils-Python%20%7C%20Markdown%20%7C%20GitHub-lightgrey)
![Status](https://img.shields.io/badge/Status-En%20cours-orange)
![Niveau](https://img.shields.io/badge/Niveau-GRC%20Opérationnel%20PME-yellow)


## SantéConnect — Démarche structurée de mise en conformité et gestion des risques pour une HealthTech

> Chaque livrable documente des arbitrages méthodologiques réels : choix d'exclusions ISO 27001, positionnement NIS2 en logique supply chain,décision MFA patients calibrée RGPD Art. 5, modélisation RBAC pour RSSI temps partiel. 
> Une démarche calibrée PME, pas un exercice académique.

---

## Compétences démontrées

- **Analyse de risques ISO 27001** → Plan de traitement des risques (11 risques critiques, grille 3×3, contrôles liés)  
- **Conformité RGPD en contexte HDS** → AIPD D-002 + D-005, convention co-responsabilité CHU art. 26  
- **Exposition NIS2 supply chain** → Gap analysis, 1 risque critique identifié, PCA/PRA livré, feuille de route  
- **Modélisation EBIOS RM** → Cadrage systémique, 24 couples SR/OV, scénario compromission API CHU  
- **Automatisation audit RBAC** → Script Python autonome, 0 dépendance externe, rapport CSV horodaté  

Exemples d'arbitrage : 

| Enjeu métier | Analyse produite| Décision supportée|
| ------- | ------- | ------- |
|Protection données patients |AIPD + registre traitements | NIR repositionné donnée à protection renforcée - mesures différenciées D-002 vs D-001|
|Continuité service cardiologie |PCA/PRA | RTO 72h accepté, activation 4h pour API CHU - faisabilité vérifiée et documentée |
| Ressources limitées RSSI part-time | Plan traitement risques | Budget sécurité priorisé sur 11 risques critiques, 4 thèmes acceptés score ≤3|
|Accès praticiens/patients | Matrice RBAC | MFA patients B2C non obligatoire - arbitrage UX/inclusion numérique documenté RGPD Art. 5 |
| Partenaire CHU | Analyse supply chain NIS2 | Clauses contractuelles renforcées - délais alerte 4h ancrés convention co-responsabilité |

---

## 🏥 SantéConnect en bref

SantéConnect est une PME fictive de 15 employés qui connecte patients et
médecins/praticiens pour améliorer le suivi, le partage d'informations et la
prise de rendez-vous tout au long du parcours de soin.

- **Utilisateurs :** 100 utilisateurs actifs (80 patients + 20 praticiens)
- **Partenariat :** CHU local - spécialité cardiologie
- **Produits :** application mobile + WebApp patients / interface praticiens
- **Hébergement :** 100 % France
- **Valeurs fondatrices :** consentement éclairé, simplicité, sécurité

---

## 📂 Livrables
| Semaine | Thème | Livrable | Statut |
|---------|-------|----------|--------|
| [0](./semaine-0-fondamentaux/contexte-santeconnect.md) | Fondamentaux | [Présentation SantéConnect](./semaine-0-fondamentaux/contexte-santeconnect.md) | ✅ Complet |
| [1](./semaine-1-gouvernance/README.md) | Gouvernance & Risques | [Cadrage audit](./semaine-1-gouvernance/cadrage-audit.md) · [Fiche risques](./semaine-1-gouvernance/fiche-risques-e-sante.md) | ✅ Complet |
| [2](./semaine-2-rgpd-hds/README.md) | RGPD & HDS | [Registre des Traitements](./semaine-2-rgpd-hds/registre-traitements/registre_traitement.md) · [AIPD synthétique](./semaine-2-rgpd-hds/aipd-synthetique.md) · [Note de co-responsabilité](./semaine-2-rgpd-hds/note-co-responsabilite-chu.md) · [Synthèse clauses sous-traitants](./semaine-2-rgpd-hds/synthese-clauses-sous-traitants.md) · [Procédure incident et notification](./semaine-2-rgpd-hds/procedure-incident-notification.md) · [Checklist audit RGPD-HDS](./semaine-2-rgpd-hds/checklist-audit-rgpd-hds.md)| ✅ Complet |
| [3](./semaine-3-iso27001/README.md) | ISO 27001 | [PSSI](./semaine-3-iso27001/pssi.md) · [Tableau synthétique des contrôles ISO 27001](./semaine-3-iso27001/declaration-applicabilite.csv) · [Déclaration d'applicabilité synthètique (SOA)](./semaine-3-iso27001/SoA.md) · [Matrice RBAC](.//semaine-3-iso27001/matriceRBAC.md) · [Plan traitement des risques](./semaine-3-iso27001/plan-traitement-risques.md)  | ✅ Complet |
| [4](./semaine-4-nis2/README.md) | NIS2 | [Note de coresponsabilité mise à jour NIS2](./semaine-4-nis2/note-coresponsabilite-CHU-maj-nis2.md) · [Analyse Impact NIS2](./semaine-4-nis2/analyse-impact-nis2.md) · [Plan d'action](./semaine-4-nis2/plan_action_nis2.md)  · [PRA/PCA](./semaine-4-nis2/pra-pca.md)| ✅ Complet |
| [5](./semaine-5-ebios-rm/README.md) | EBIOS Risk Manager | [Atelier 1 - Cadrage et socle de sécurité](./semaine-5-ebios-rm/1-ebios-rm-santeconnect-cadrage.md) · [Atelier 2 - Sources de risque](./semaine-5-ebios-rm/2-sources-risque.md) · Scénario opérationnel - Compromission API CHU · Synthèse et plan d'action | 🔄 En cours |

---

## 🛠️ Bibliothèque de ressources GRC

Les livrables génériques produits dans le cadre de ce projet sont regroupés dans une bibliothèque de ressources réutilisables.

Elle rassemble des modèles, guides et outils pratiques inspirés des référentiels ISO 27001, RGPD, HDS et NIS2, conçus pour être adaptés à d'autres contextes, avec un focus particulier sur les PME e-santé.

➡️ **Consulter la bibliothèque complète :** [ressources/README.md](./ressources/README.md)


| Outil | Public cible | Accès |
|-------|-------------|-------|
| Cartographie des actifs GRC: Version PME | Dirigeants, DPO, consultants junior | [📥 Télécharger](./ressources/grc-asset-inventory-template-pme.xlsx) |
| Cartographie des actifs GRC: Version Advanced | Équipes techniques, cabinets GRC | [📥 Télécharger](./ressources/grc-asset-inventory-template-pme-threats.xlsx) |
| Vision base légale - Conformité RGPD-HDS | Responsables de PME sans expertise juridique| [Référentiel légal simplifié](./ressources/Referentiel_legal_simplifie.md) |
| ISO 27001:2022 - Contrôles priorisés PME e-santé | RSSI, DPO, consultants GRC | [📖 Consulter](./ressources/ISO%2027001_Liste_Controle.md) · [📥 Télécharger](./ressources/ISO27001_Liste-Controle.csv))  |
| Plan de Réponse aux Incidents (PRI) - Modèle PME e-santé | RSSI, DPO, dirigeants PME | [📖 Consulter](./ressources/plan_reponse_incidents.md) |
| Guide de conformité NIS2 Art. 21 & 23 pour PME e-santé et correspondance avec les contrôles ISO 27001:2022 | RSSI, DPO, dirigeants PME dans domaine e-santé | [📖 Consulter](./ressources/nis2_correspondances_ISO27001.md)|
|  Script Python d'audit RBAC + Génération de rapports d'anomalies | RSSI, équipes techniques, consultant GRC | [📥 Télécharger](./ressources/audit_RBAC_auto/rbac_audit.py) · [📖 Documentation](./ressources/audit_RBAC_auto/README.md) |


> Conçu avec une posture *"GRC comme produit"*, simple, progressif, ancré dans la réalité opérationnelle d'une PME.

----

## ⚖️ Référentiels mobilisés

| Référentiel | Obligation | Périmètre |
|-------------|------------|-----------|
| **RGPD** | Obligatoire | Toutes données personnelles et de santé |
| **HDS** | Obligatoire | Hébergement de données de santé en France |
| **NIS2** | Applicable | Secteur santé - indirectement via partenariat CHU |
| **ReCyF (ANSSI)** |Anticipée | Référentiel cible pré-transposition NIS2 française |
| **ISO 27001** | Recommandée | Sécurité de l'information - référence de marché |
| **Code de Santé Publique** | Obligatoire | Secret médical + partage inter-praticiens |
| **RGS + PGSSI-S** | Applicable | Échanges sécurisés avec le CHU partenaire (établissement public) |

---


## 👩‍💻 À propos de l'auteure

**Solène Figueiredo**
Consultante GRC | Conformité RGPD · Gestion des risques · Interface IT-Métier

Positionnement : interface entre technique, risques et décision métier, au
service de projets cybersécurité ancrés dans la réalité opérationnelle.

**Parcours :** 10 ans de pilotage de projets digitaux internationaux chez
Renault
> Campagnes simultanées dans plus de 100 pays (Twizy), programmes CRM
multi-marchés (ZOE), gestion de plateformes digitales sur 40 pays.
> Habituée aux environnements complexes : coordination d'équipes pluridisciplinaires,
enjeux business critiques, contraintes de délais et de qualité.

**Aujourd'hui :** Positionnement GRC fondé sur 10 ans de pilotage international data/IT, appliqué à la gouvernance, la gestion des risques et la conformité cyber.

Capacités démontrées dans ce projet :
- Structurer une démarche GRC complète pour une PME e-santé
- Produire des livrables opérationnels inspirés des pratiques de mission GRC en environnement professionnel (registre, AIPD, analyse de risques)
- Articuler conformité réglementaire et réalité opérationnelle PME
- Traduire les exigences RGPD-HDS en documents actionnables pour dirigeants et DPO

---

*Projet fictif à visée pédagogique - les livrables reflètent une démarche GRC réelle adaptée à un contexte simulé.*

---

## English Summary

**SantéConnect** is a fictional French HealthTech 
(15 employees, cardiology, hospital partnership) used 
as a case study to demonstrate a structured GRC approach.

**Deliverables cover:** GDPR · French Health Data 
Hosting (HDS) · ISO 27001:2022 · NIS2 · EBIOS RM

**Key outputs:**
- Risk treatment plan (11 critical risks, 3×3 grid)
- ISO 27001:2022 control mapping and applicability analysis  
- NIS2 supply chain gap analysis + action plan
- Business continuity plan (RTO 72h / RPO 24h)
- EBIOS RM threat modeling (24 source/objective pairs)
- Automated RBAC audit script (Python, no dependencies)

**Reusable resources** (CC BY 4.0) available in 
`/ressources` — adaptable to any SME context.

→ [Resource library](./ressources/README.md)

---

[![LinkedIn](https://img.shields.io/badge/LinkedIn-solenefigueiredo-blue)](https://www.linkedin.com/in/solene-figueiredo/)
