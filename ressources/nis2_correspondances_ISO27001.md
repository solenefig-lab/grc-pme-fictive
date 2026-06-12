# NIS2 Art. 21 et 23 : Guide de Conformité pour les PME e-Santé ayant engagé une démarche ISO 27001:2022

**Ce guide est fait pour vous si vous êtes une PME e-santé travaillant avec un CHU ou un hôpital. Il vous aide à comprendre ce que votre partenaire peut vous demander au titre de NIS2 et comment y répondre avec vos outils ISO 27001.**

---

> Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité. Le niveau de granularité illustre une cible de maturité, non l'état courant du marché TPE/PME santé.  

_Note de contexte réglementaire (juin 2026) : La transposition NIS2 en droit français n'est pas encore publiée. L'ANSSI met à disposition depuis le 17 mars 2026 le Référentiel Cyber France (ReCyF), document de travail correspondant au référentiel mentionné à l'article 14 du projet de loi Résilience. Les analyses et recommandations de ce livrable s'appuient sur la directive NIS2 (UE) 2022/2555 et anticipent le ReCyF comme référentiel cible, conformément à la posture recommandée par l'ANSSI pour les futurs assujettis._
> Pour plus de détails et une comparaison détaillée, l'ANSSI a mis à disposition un outil de comparaison des exigences NIS2 (RecYf) et ISO27001:2022 à but d'information : [Outil de comparaison de référentiels](https://messervices.cyber.gouv.fr/nis2#exigences)

---

**Liste des 10 domaines de l’Art. 21 plus Art. 23 NIS2  avec leur traduction en contrôles ISO 27001:2022 et exemples de mise en œuvre pour une PME dans le domaine de l'e-santé.**

**Important à noter :**
- **Hors périmètre NIS2 :** une PME française de p.ex. 15 personnes fournissant des services numériques dans le domaine de la e-santé n'est ni une entité essentielle ni importante au sens de NIS2 et n'a donc pas d'obligation directe.
    - Taille - seuils NIS2 (Art. 2(1)) : NIS2 ne crée pas d'obligation directe sur les fournisseurs de taille réduite - en revanche, la PME peut travailler avec une entité essentielle (p.ex. CHU) qui porte l'obligation de sécuriser sa chaîne via Art. 21(2).
        _- Une analyse spécifique du secteur, du rôle joué dans l'écosystème de santé et des éventuelles exceptions prévues par la directive reste nécessaire._
    - Secteur d’activité : un fournisseur de services numériques en santé n'est pas un prestataire de soins au sens de l'Annexe I NIS2. Elle ne figure pas non plus dans l'Annexe II (secteurs critiques).
    - Statut juridique : **vérifier si la PME répond ou non aux critères de taille et de secteur définis (Art. 2(1) + Art. 2(4)).**
        - Le cas échéant: pas d'obligation de notification vers l'ANSSI, pas d'obligation d'enregistrement sur MonEspaceNIS2, et aucun contrôle ANSSI direct ne peut lui être opposé.
-  **Périmètre applicable :** une PME peut être impactée indirectement via un **partenariat avec une Entité Essentielle ou Importante** et **des exigences contractuelles inspirées de NIS2, imposées par le partenaire** pour garantir la sécurité des données partagées et des systèmes interconnectés. Ces exigences couvrent :
    - Les mesures de gestion des risques et de sécurité (NIS2 Art. 21.a à 21.j), notamment :
        -   21.a : Politiques de sécurité et analyses de risques.
        -   21.c : Plans de continuité des activités (PCA/PRA).
        -   21.d : Sécurité de la chaîne d’approvisionnement (ex : évaluation des fournisseurs critiques (hébergeur HDS, SaaS, MSSP, etc.)).
        -   21.i et 21.j : Contrôle d’accès et surveillance continue.
    - La notification des incidents (NIS2 Art. 23), avec des délais contractuels adaptés (ex : alerte précoce sous 4h, notification sous 24h).
    - Dans ce cas, il est important que la PME :
        - Passe en revue, analyse les risques et écarts et prépare un plan d'action pour être en règle avec les clauses de coresponsabilité ou contractuelle du partenaire,
        - Définisse clairement Objet, Périmètre et Modalité Technique des Informations concernées, 
        - Etablisse clairement Rôle et Responsabilités au sein de l'entreprise.

_voir exemples :_  
_ - [ISO 27001:2022 – Contrôles regroupés par sous-catégorie pour les PME e-santé](https://github.com/solenefig-lab/grc-pme-fictive/blob/main/ressources/ISO%2027001_Liste_Controle.md)_  
_- [SantéConnecte et NIS2](https://github.com/solenefig-lab/grc-pme-fictive/tree/main/semaine-4-nis2)_

----

## Comment utiliser ce guide ?

1. Commencez par identifier les exigences contractuelles imposées par votre client ou partenaire.
2. Vérifiez pour chaque domaine si les mesures attendues sont déjà mises en œuvre dans votre organisation.
3. Rassemblez les documents et preuves démontrant leur application effective.
4. Identifiez les écarts éventuels et formalisez un plan d'action priorisé.

## 1. Analyse rapide des attentes NIS2

|Domaine NIS2 | Via contrat Partenaire (**à compléter avec les clauses contractuelles de votre partenaire**) | Thème Central |
| ----------- | ----------- | ----------- | 
| 21.a. Politiques de sécurité et analyses de risques | - | Avez-vous identifié vos principaux risques cyber et défini une politique de sécurité formalisée ? |
| 21.b. Plans d’intervention en cas d’incident  | _Ex : délai alerte 4h, notification 24h (selon partenaire)_ | Savez-vous détecter, enregistrer, traiter et notifier un incident de sécurité ? |
| 21.c. Plans de continuité des activités |  _Ex : PCA testé annuellement, RTO contractualisé_ | Pouvez-vous maintenir ou rétablir vos services après un incident majeur ? |
| 21.d. Sécurité de la chaîne d’approvisionnement | _Ex. exigences HDS, clauses fournisseurs_ | Évaluez-vous les risques liés à vos fournisseurs, hébergeurs et sous-traitants ? |
| 21.e. Sécurité dans l’acquisition, le développement et la maintenance des réseaux et des systèmes d’information | - | La sécurité est-elle intégrée dans vos projets, applications et infrastructures ? |
| 21.f. Evaluation de l’efficacité des mesures de gestion des risques liés à la cybersécurité | - | Vérifiez-vous régulièrement que vos mesures de sécurité fonctionnent réellement ? |
| 21.g. Formation à la sensibilisation, à l’hygiène et aux meilleures pratiques en matière de cybersécurité | - | Les collaborateurs connaissent-ils les risques cyber et les bonnes pratiques à appliquer ? |
| 21.h. Cryptographie et chiffrement | - | Les données sensibles sont-elles correctement chiffrées et protégées ? |
| 21.i. Procédures de contrôle d’accès, en particulier pour les employés ayant accès à des données sensibles | _Ex : liste des accès communiquée au partenaire sur demande_ | Disposez-vous d'une gestion formalisée des droits d'accès et des habilitations ? |
| 21.j. Authentification multifactorielle, surveillance continue et systèmes de communication sécurisés |  - | Les accès critiques sont-ils protégés par MFA et les événements de sécurité surveillés ? |
| 23. Gestion des incidents | _Ex : délai alerte 4h, notification 24h (selon partenaire), exigences contractuelles de remontée d'incident_ | Savez-vous qui prévenir, quand et selon quelle procédure en cas d'incident ? |

## 2. Correspondance ISO 27001:2022 et éléments de preuve

|Domaine NIS2 | ISO 27001:2022| Exemples de documents | Exemple de preuves d'exécution| Niveau de couverture via ISO 27001 |
| ----------- | ----------- | ----------- | ----------- |  ----------- | 
| 21.a. Politiques de sécurité et analyses de risques | A.5.1. Politiques de sécurité de l'information, A.6.1. Vérification des antécédents (_pour postes traitant des données sensibles_) | PSSI, méthodologie d'analyse de risques, cartographie des actifs | Analyse de risques mise à jour, compte-rendu de revue annuelle, plan de traitement des risques  | 🟢 |
| 21.b. Plans d’intervention en cas d’incident  | A.5.24. à A.5.27. Gestion des Incidents | Procédure de gestion des incidents, registre d'incidents | Ticket d'incident traité, exercice de gestion de crise, REX documenté  | 🟢 |
| 21.c. Plans de continuité des activités |  A.5.29 Sécurité de l'information en cas de perturbation, A.5.30. Préparation des TIC à la continuité des activités, A.8.13. Sauvegarde des informations| PCA, PRA, stratégie de sauvegarde | Compte-rendu de test PRA/PCA, journal de restauration de sauvegarde | 🟡 |
| 21.d. Sécurité de la chaîne d’approvisionnement | A.5.19. à A.5.23. Contrats et Conformité avec fournisseurs, sous-traitants et services cloud | Politique fournisseurs, contrats, registre sous-traitants | Revue annuelle fournisseur, évaluation de risque fournisseur, certificats HDS/ISO | 🟢 |
| 21.e. Sécurité dans l’acquisition, le développement et la maintenance des réseaux et des systèmes d’information | A.8.25 à A.8.30. Technologie: cycle de vie et développement | Politique de développement sécurisé, architecture cible | Revue de code, résultats de scans, gestion des vulnérabilités, pentests | 🟡 |
| 21.f. Evaluation de l’efficacité des mesures de gestion des risques liés à la cybersécurité | A.5.35 Revue indépendante, A.5.36. Conformité aux politiques, règles et normes en matière de sécurité de l'information, A.8.34 Tests et évaluation | Programme d'audit, procédure de contrôle | Rapports d'audit, résultats de tests techniques, suivi des actions correctives | 🟢 |
| 21.g. Formation à la sensibilisation, à l’hygiène et aux meilleures pratiques en matière de cybersécurité | A.6.3. Sensibilisation, éducation et formation à la sécurité de l'information | Plan de sensibilisation, supports de formation | Feuilles d'émargement, statistiques e-learning, campagnes phishing | 🟡 |
| 21.h. Cryptographie et chiffrement | A.8.24. Utilisation de la cryptographie | Politique cryptographique | Paramétrage TLS, inventaire des certificats, rapports d'audit de configuration | 🟢  |
| 21.i. Procédures de contrôle d’accès, en particulier pour les employés ayant accès à des données sensibles | A.5.9. à A.5.18. Organisationnel: Inventaire et Gestion Informations, Actifs et Identités , A.8.2. Droits d'Accés Privilégiés , A.8.3. Restriction d'accès à l'information, A.8.5. Authentification sécurisée | Politique d'habilitation, matrice RBAC | Revue périodique des accès, journaux d'attribution/retrait des droits, preuve MFA | 🟡 / 🔴 si pas matrice RBAC |
| 21.j. Authentification multifactorielle, surveillance continue et systèmes de communication sécurisés |  A.5.17 Informations d’authentification, A.8.5 Authentification sécurisée, A.8.20. Sécurité des réseaux |  Politique d'authentification, procédure de supervision | Journaux SIEM, alertes traitées, rapports MFA activé | 🟡 / 🔴 si absence surveillance continue |
| 23. Gestion des incidents | A.5.24. à A.5.27. Procédure de gestion des incidents et notification | Procédure de notification, registre incidents | Historique des notifications, exercices de notification, REX | 🟢 |


**Légende :**
- AIPD: analyse d'impact relative à la protection des données
- Matrice RBAC : Role-Based Access Control pour la gestion des autorisations
- MFA : Multi-Factor Authentication
- PSSI : Politique de Sécurité du Système d'Information
- PTR : Plan de Traitement des Risques
- PRA/PCA : Plan de Continuité et de Rétablissement de l'Activité
- RACI : Matrice des Responsabilités
- REX : Retour d'Expérience
- SIEM : Security Information and Event Management
- Symboles :
    - 🟢 Elevée : si la PME a implémenté ce(s) contrôles, elle a une bonne couverture théorique de la conformité NIS2 (à documenter et à réviser pour éviter les gaps)
    - 🟡 Modérée: si la PME a implémenté ce(s) contrôles, elle a une couverture moyenne de la conformité NIS2 et devra mettre en place des mesures supplémentaires
    - 🔴 Faible : la PME doit mener une analyse d'impact NIS2 plus poussée pour identifier les mesures à mettre en place et documenter

--

*Document produit dans le cadre du projet portfolio GRC - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*
*Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité.*