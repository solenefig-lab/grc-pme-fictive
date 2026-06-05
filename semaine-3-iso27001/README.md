## Semaine 3 - Sécurité de l'information - ISO 27001

### Objectif
**Traduire les exigences de conformité (RGPD-HDS) en contrôles ISO 27001 opérationnels** pour SantéConnect :
- **Structurer la gouvernance** via une **PSSI** adaptée aux contraintes d’une PME e-santé.
- **Évaluer et prioriser** les contrôles de sécurité via un **Statement of Applicability (SoA)**.
- **Préparer les artefacts opérationnels** (ex : matrice RBAC, registre des alertes) pour une mise en œuvre concrète.

---

### Livrables
   Livrable | Description | Statut |
 |---|---|---|
 | [`PSSI.md`](./pssi.md) | **Politique de Sécurité des Systèmes d’Information** : Cadre global pour la sécurité, incluant rôles (RACI), objectifs, et mesures prioritaires (ex : chiffrement, gestion des accès). | ✅ Complet |
 | [`SoA.md`](./SoA.md) | **Statement of Applicability** : Mapping complet des contrôles ISO 27001 (A.5 à A.8) appliqués à SantéConnect, avec justifications, états (Appliqué/Partiellement Appliqué) et CIAT. | ✅ Complet |
 | [`declaration-applicabilite.csv`](./declaration-applicabilite.csv) | **Tableau synthétique** des contrôles ISO 27001, avec statut, CIAT et documentation liée, au format CSV pour une intégration facile dans des outils de suivi. | ✅ Complet |
 | [`matriceRBAC.md`](./matriceRBAC.md) | Matrice des droits d’accès (rôles, permissions, ressources) pour une gestion fine des accès. | ✅ Complet|
 | [`plan-traitement-risques.md`](./plan-traitement-risques.md)| *Document ISO 27001 (cl. 6.1.3)* : Pour chaque risque identifié dans le SoA, **décision formelle** (Accepter / Réduire / Transférer / Éviter) + **actions concrètes** associées. Inclut : risques prioritaires, contrôles ISO 27001 liés, responsables, échéances, et indicateurs de suivi.| ✅ Complet  |

---

### Points méthodologiques clés

- **Approche pragmatique** : Le SoA et la PSSI sont **calibrés pour une PME e-santé** (ressources limitées, RSSI temps partiel).
- **Alignement RGPD-HDS** : Les contrôles ISO 27001 sont **priorisés** en fonction des risques identifiés dans la [Semaine 2](../semaine-2-rgpd-hds/) (ex : protection des données médicales, gestion des incidents).
- **Focus sur l’opérationnel** : Les contrôles **Partiellement Appliqués** (ex : A.5.25, A.8.12) sont accompagnés de **cibles de maturité** (ex : automatisation de la surveillance, déploiement DLP).
- **Collaboration avec le CHU** : Les mesures de sécurité tiennent compte des **exigences du partenariat** (ex : séparation des réseaux, redondance des données).

---

## Ressources associées

Ces artefacts sont **réutilisables pour toute PME** et illustrent une démarche ISO 27001 adaptée aux contraintes des petites structures :
 | Ressource | Description | Statut |
 |---|---|---|
 | [`ISO27001:2002_Liste_Controle.md`](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/ressources/ISO%2027001_Liste_Controle.md) | 93 contrôles ISO 27001:2022 regroupés, illustrés priorisés pour les PME e-santé, avec alignement HDS, RGPD et NIS2 par contrôle. | ✅ Complet |
  | **Registre des alertes** | *À venir*  - Artefact opérationnel pour le suivi des incidents. | 🔄 En cours |
 

---

## Prochaine étape

La **Semaine 4** traduira les contrôles ISO 27001 en **mesures NIS2**, avec un focus sur :
- L’**impact de NIS2** sur une PME e-santé (ex : résilience, reporting des incidents).
- La **conformité croisée** (RGPD + HDS + NIS2 + ISO 27001).
- Les **outils low-cost** pour automatiser la surveillance et la réponse aux incidents.

[Semaine 4 - Conformité NIS2](../semaine-4-nis2/README.md)
