# **Semaine 4 - Conformité NIS2 et Résilience Opérationnelle**

**Objectif principal** :
**Opérationnaliser les exigences NIS2 contractuelles du CHU** en **procédures de résilience** (PCA/PRA) et en **feuille de route de mise en conformité** pour SantéConnect, avec un focus sur :
- La **résilience** (PCA/PRA, continuité des services critiques).
- La **gestion des incidents** (délais contractuels CHU : 4h/24h/72h).
- L’**automatisation low-cost** des contrôles (ex : revues RBAC, surveillance).


---

## **Livrables**

   **Livrable** | **Description** | **Statut** |
 |--------------|----------------|------------|
 | [note-coresponsabilite-CHU-maj-nis2.md](note-coresponsabilite-CHU-maj-nis2.md) | Convention de co-responsabilité RGPD/HDS **mise à jour avec les clauses NIS2** (Art. 21 et 23), incluant les engagements du CHU et de SantéConnect. | ✅ Complet | 
 | [analyse-impact-nis2.md](./analyse-impact-nis2.md) | **Gap analysis NIS2** : Tableau comparatif des **10 domaines de l’Art. 21** et **Art. 23** vs. les contrôles ISO 27001:2022 existants, avec **priorisation des gaps** (🔴/🟡) . | ✅ Complet |
 | [pca-pra-santeconnect.md](./pra-pca.md) | **Plan de Continuité et de Reprise d’Activité** : Procédures pour maintenir/restaurer les services critiques (API HL7/FHIR, Base D-002) en cas d’incident, avec **RTO/RPO** alignés sur les exigences du CHU (ex : activation sous 4h). | ✅ Complet |
 | [plan-action-nis2.md](./plan_action_nis2.md) | **Feuille de route** pour combler les gaps NIS2 : Actions concrètes (ex : automatiser les revues RBAC, tester le PCA/PRA), **échéances**, et **responsables**. | ✅ Complet |



---

## **Points Méthodologiques Clés**

1. **Approche pragmatique pour une PME** :
   - Les **mesures NIS2** sont **adaptées aux ressources limitées** de SantéConnect (ex : scripts Python pour les revues RBAC, Wazuh/Graylog pour la surveillance).
   - **Focus sur l’essentiel** : Priorisation des gaps **critiques** (🔴) pour respecter les **exigences contractuelles du CHU**.

2. **Alignement multi-réglementaire** :
   - **NIS2** (via CHU) : PCA/PRA, notification sous 24h.
   - **HDS** : Notification sous 24h à l’ANS, chiffrement AES-256.
   - **RGPD** : Notification sous 72h à la CNIL, protection des données.
   - **ISO 27001:2022** : Contrôles A.5.29-30 (PCA/PRA), A.8.13 (sauvegardes).

3. **Collaboration avec le CHU** :
   - Les **clauses contractuelles** du CHU (inspirées de NIS2) sont **intégrées dans les livrables** (ex : délais de 4h pour l’activation du PCA/PRA).
   - **Preuves de conformité** : Rapports de tests, logs, contrats OVH (HDS).

4. **Automatisation low-cost** :
   - Utilisation d’**outils open-source** (Wazuh, Graylog, Python) pour **réduire les coûts** tout en respectant les exigences.

---

## **Ressources Associées (Réutilisables)**
Ces artefacts sont **réutilisables pour toute PME e-santé** et illustrent une démarche **NIS2 + ISO 27001** adaptée aux contraintes des petites structures :

 | **Ressource** | **Description** | **Statut** |
 |---------------|----------------|------------|
 | [nis2_correspondances_ISO27001.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/ressources/nis2_correspondances_ISO27001.md) | Guide de conformité NIS2 Art. 21 & 23 pour PME e-santé : analyse rapide des attentes par domaine, correspondance avec les contrôles ISO 27001:2022, exemples de documents et preuves d'exécution attendues. | ✅ Complet  |
 | **template-pca-pra-pme.md** | **Modèle générique de PCA/PRA** pour une PME, incluant des **RTO/RPO réalistes**, des **procédures types**, et des **liens vers les réglementations** (NIS2, HDS, RGPD). |🔄 En cours |
  |[audit_RBAC_auto/README.md](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/ressources/audit_RBAC_auto/README.md) | **Script Python** pour **automatiser les revues d’habilitation** (RBAC) : Vérifie les **droits d’accès**, Génère un **rapport hebdomadaire** des accès suspects, Exemple d’intégration SIEM (Wazuh/Graylog) fourni en commentaire. |   ✅ Complet  |


---

## **Prochaine Étape : Semaine 5 - EBIOS Risk Manager (EBIOS RM)**

Les **gaps résiduels identifiés** (micro-segmentation, surveillance continue) **alimenteront les scénarios de risque de l’analyse EBIOS RM**.
Cette analyse permettra de prioriser les risques liés à la chaîne d’approvisionnement (ex : OVH, CHU) et aux incidents critiques (ex : fuite de données, indisponibilité des services), en alignement avec les exigences **NIS2, HDS, RGPD et ISO 27001**.
