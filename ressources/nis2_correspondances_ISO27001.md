# Exigences cyber des clients et partenaires : repères NIS2 et correspondances indicatives avec ISO 27001:2022

**Ce guide s’adresse aux PME e-santé et aux fournisseurs de services numériques intervenant auprès d’établissements de santé. Il aide à analyser les exigences de cybersécurité applicables, à distinguer les obligations réglementaires des exigences contractuelles et à préparer les mesures et preuves correspondantes.**

---

## Objet, limites et état vérifié

Ce guide présente les 10 domaines de l’art. 21(2) et l’art. 23 de la [directive NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj?locale=fr), avec des correspondances indicatives avec ISO 27001:2022 et des exemples de preuves.

> **Limites.** Ce document est un support pédagogique d’autoévaluation. Il ne constitue ni un avis juridique, ni un audit, ni une certification. Les mesures à mettre en œuvre dépendent de l’activité, des risques, du périmètre des systèmes, des textes applicables et des engagements contractuels de l’organisation.

> **État vérifié le 18/10/2026.** La loi française de transposition de NIS2 n’est ni adoptée ni publiée. L’ANSSI diffuse depuis le 17/03/2026 le ReCyF ([Référentiel Cyber France](https://messervices.cyber.gouv.fr/nis2#presentation)), un document de travail. Ce guide s’appuie sur la [directive (UE) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj?locale=fr). Le ReCyF n’est pas, à cette date, un ensemble de mesures obligatoires. Vérifier ce statut avant toute nouvelle diffusion.

L’ANSSI propose un outil de comparaison entre le ReCyF et d’autres référentiels, dont ISO 27001:2022 : [Outil de comparaison de référentiels](https://messervices.cyber.gouv.fr/nis2#exigences).   
Ces correspondances facilitent l’analyse des écarts, elles ne prouvent pas à elles seules la conformité NIS2.

---

## Comment utiliser ce guide

1. Qualifier l’applicabilité de NIS2 à votre entité (voir [Qualifier l’assujettissement](#qualifier-lassujettissement--êtes-vous-soumis-directement-à-nis2-)).
2. Identifier les exigences du client ou partenaire (contrat, annexe sécurité, questionnaire) et préciser, pour chacune, si elle est réglementaire ou contractuelle.
3. Vérifier, pour chaque domaine, les mesures déjà en place.
4. Rassembler les preuves et contrôler pour chacune sa date, son périmètre, son résultat et son responsable.
5. Consigner les écarts et formaliser un plan d’action priorisé.

---

## Qualifier l’assujettissement : êtes-vous soumis directement à NIS2 ?

Une PME n’est pas automatiquement soumise directement à NIS2 du seul fait qu’elle fournit un service numérique en santé. Son assujettissement ne peut pas non plus être exclu sur la seule base de son effectif. 
Trois questions, dans l’ordre :

1. **Secteur.** L’activité relève-t-elle d’un type d’entité listé dans les annexes de la directive (annexe I : secteurs hautement critiques, annexe II : autres secteurs critiques) ?
2. **Taille.** Si oui, l’entité atteint-elle au moins la taille d’une entreprise moyenne, liens avec d’autres entreprises compris ?
3. **Cas particuliers.** Sinon, l’un des cas de l’art. 2(2) à (4), applicables quelle que soit la taille, s’applique-t-il ?

| Art. | Ce que dit le texte | Conséquence pour l’analyse |
|---|---|---|
| **2(1)** | Entités d’un type listé aux annexes I ou II, constituant des entreprises moyennes au sens de la recommandation 2003/361/CE (définition européenne de la PME) ou dépassant ses plafonds, et fournissant leurs services ou exerçant leurs activités dans l’Union. | Les micro et petites entreprises sont en principe hors 2(1). Les liens avec d’autres entreprises (entreprises partenaires ou liées) peuvent modifier la taille retenue : l’effectif de l’entité seule ne suffit pas à conclure. |
| **2(2)** | Entités d’un type listé aux annexes I ou II, quelle que soit la taille, dans certains cas : fournisseurs de communications électroniques, de services de confiance, registres de noms de domaine de premier niveau et services DNS ; seul prestataire d’un service essentiel ; perturbation pouvant avoir un impact important sur la sécurité publique, la sûreté publique ou **la santé publique** ; risque systémique important ; importance critique nationale ou régionale ; certaines administrations publiques. | À apprécier au regard du texte exact et de sa mise en œuvre nationale. **Le cas « santé publique » mérite une analyse explicite pour un service e-santé.** |
| **2(3) et 2(4)** | 2(3) : entités critiques au titre de la directive (UE) 2022/2557. 2(4) : entités fournissant des services d’enregistrement de noms de domaine. Dans les deux cas, quelle que soit la taille. | Vérifier si l’organisation relève de l’un de ces cas. Le 2(4) est un cas particulier, pas une règle générale pour les PME. |

**Secteur d’activité.** Fournir un logiciel de santé ne suffit pas seul à qualifier un prestataire de soins de santé. 
 - Examiner l’activité réellement exercée au regard des annexes. 
 - Selon les services rendus, un fournisseur peut relever d’une autre catégorie : par exemple l’informatique en nuage ou les services gérés (annexe I), ou la fabrication de dispositifs médicaux (annexe II), si le logiciel est qualifié de dispositif médical au sens du règlement (UE) 2017/745. Cette qualification est à établir au cas par cas.  

**Conclusion de l’analyse.** Documenter les activités examinées, la taille et les liens avec d’autres entreprises, les catégories des annexes, les cas de l’art. 2(2) à (4) et les dispositions nationales. 
> Tant que cette analyse n’est pas faite, la conclusion est « à qualifier ». Ne conclure à l’absence d’obligation directe qu’après cette vérification. L’éventuelle obligation d’enregistrement ou de notification auprès de l’ANSSI dépendra de la transposition française.

---

## Exigences d’un client : réglementaire et contractuel

**Le lien entre le client et son fournisseur :** Une entité soumise à NIS2 doit gérer la sécurité de sa chaîne d’approvisionnement, y compris les relations avec ses fournisseurs directs (art. 21(2)(d) et 21(3)). 
C’est en pratique par le contrat que cette exigence atteint le fournisseur. Un client non assujetti peut imposer des exigences de même nature. 
Les exigences applicables à la PME découlent de ses obligations réglementaires directes et des engagements contractuels convenus avec son client.

Ces exigences peuvent couvrir les 10 domaines de l’art. 21(2), détaillés dans le tableau de la [section 1](#1-analyse-rapide-des-attentes-nis2) : risques, incidents, continuité, fournisseurs, développement, évaluation, hygiène et formation, cryptographie, accès et ressources humaines, authentification et communications.

**Deux régimes à ne pas confondre :**

- **Régime de l’art. 23 (entités qui y sont soumises).** 
    - Alerte précoce sans retard injustifié et au plus tard 24 heures après avoir eu connaissance d’un incident important, 
    - Notification d’incident au plus tard 72 heures,
    - Rapport final au plus tard un mois après la notification. 
Ces notifications s’adressent au centre de réponse aux incidents (CSIRT) ou à l’autorité compétente. Le texte prévoit aussi l’information des destinataires des services lorsque l’incident est susceptible de nuire à leur fourniture.

- **Exigences contractuelles.** Un client peut imposer à son fournisseur un délai d’alerte distinct, souvent plus court. 
*Exemple à confirmer avec le client : alerte sous 4 heures, informations complémentaires sous 24 heures. Ces délais sont illustratifs et ne sont pas ceux de l’art. 23.*

**Il est important que la PME :**
- analyse les écarts entre ses mesures et les exigences de son client, et prépare un plan d’action ;
- définisse le périmètre des services, systèmes, données et interfaces concernés ;
- établisse les rôles et responsabilités en son sein.

---

## Illustration : cas fictif SantéConnect

- [ISO 27001:2022 : contrôles regroupés par sous-catégorie pour les PME e-santé](./ISO27001_Liste_Controle.md)
- [SantéConnect et NIS2 (semaine 4)](../semaine-4-nis2/README.md)

---

## 1. Analyse rapide des attentes NIS2

Ce tableau constitue une grille de premier niveau. 
La présence d’un domaine dans ce tableau ne signifie pas qu’il est exigé de votre entité. Les exigences applicables sont à vérifier au regard des obligations réglementaires directes et des engagements contractuels. 
_Les exemples contractuels sont indicatifs : ils doivent être confirmés dans le contrat, l'annexe de sécurité ou le questionnaire du client._ 

|Domaine NIS2 | **Exemple d'exigence contractuelle** (à compléter avec les clauses contractuelles de votre partenaire) | Question d’autoévaluation |
| ----------- | ----------- | ----------- | 
| 21(2)(a) Politiques relatives à l'analyse des risques et à la sécurité des systèmes d'information | _Ex.: Politique de sécurité formalisée, exigences de sécurité applicables au service fourni_ | Avez-vous identifié vos principaux risques cyber et défini une politique de sécurité formalisée ? |
| 21(2)(b) Gestion des incidents  | _Ex.: délai alerte 4h, notification 24h (illustration, selon partenaire)_ | Savez-vous détecter, enregistrer, traiter et notifier un incident de sécurité, puis en tirer les enseignements ? |
| 21(2)(c) Continuité des activités, notamment gestion des sauvegardes, reprise des activités et gestion des crises |  _Ex.: objectifs de reprise convenus, tests de restauration ou de reprise selon les exigences du client_ | Pouvez-vous maintenir ou rétablir vos services après un incident majeur ? |
| 21(2)(d) Sécurité de la chaîne d'approvisionnement, y compris les aspects liés à la sécurité des relations entre l'entité et ses fournisseurs ou prestataires de services directs | _Ex.: clauses de sécurité fournisseurs, santé en France - exigences d'hébergement HDS lorsque pertinentes, modalités de notification des incidents_ | Avez-vous identifié les risques liés aux fournisseurs, hébergeurs et sous-traitants qui contribuent au service, et pouvez-vous les suivre ? |
| 21(2)(e) Sécurité de l'acquisition, du développement et de la maintenance des réseaux et des systèmes d'information, y compris le traitement et la divulgation des vulnérabilités | _Ex.: exigences de développement sécurisé, de correction des vulnérabilités et de maintenance définies pour le service:_ | Avez-vous intégré la sécurité dans vos projets, applications et infrastructures, y compris dans le traitement des vulnérabilités ? |
| 21(2)(f) Politiques et procédures pour évaluer l'efficacité des mesures de gestion des risques en matière de cybersécurité | _Ex.: communication des résultats de tests ou du suivi des actions correctives, selon les engagements convenus_ | Vérifiez-vous régulièrement que vos mesures de sécurité fonctionnent réellement et suivez-vous les corrections nécessaires ? |
| 21(2)(g) Pratiques de base en matière de cyberhygiène et formation à la cybersécurité | _Ex.: sensibilisation des collaborateurs et formation adaptée aux rôles_ | Vous assurez-vous que vos collaborateurs connaissent les risques cyber et appliquent les bonnes pratiques attendues ? |
| 21(2)(h) Politiques et procédures relatives à l'utilisation de la cryptographie et le cas échéant, du chiffrement | _Ex.: exigences de chiffrement des données et des communications selon leur sensibilité et les risques_ | Protégez-vous les données et les communications par des mesures cryptographiques adaptées aux risques ? |
| 21(2)(i) Sécurité des ressources humaines, politiques de contrôle d'accès et gestion des actifs | _Ex : règles d'habilitation, retrait des accès au départ d'un collaborateur, gestion des équipements confiés_ | Disposez-vous d'une gestion formalisée des actifs, droits d'accès et des habilitations tout au long du cycle de vie des collaborateurs, de leur arrivée à leur départ ? |
| 21(2)(j) Utilisation de solutions d'authentification à plusieurs facteurs ou d'authentification continue, de communications vocales, vidéo et textuelles sécurisées et de systèmes sécurisés de communication d'urgence au sein de l'entité, selon les besoins |  _Ex.: MFA sur les accès concernés, canaux de communication sécurisés et procédure de communication d'urgence_ | Sécurisez-vous les moyens d'authentification (p.ex. authentification renforcée), les communications et les canaux d'urgence selon les besoins ? |
| 23. Obligations d’information (notification des incidents importants) | _Ex.: délai contractuel d'alerte au client, interlocuteurs, informations initiales et modalités d'escalade_ | Savez-vous qui prévenir, dans quel délai et selon quelle procédure, en distinguant les obligations réglementaires applicables des engagements contractuels ? |

## 2. Correspondance ISO 27001:2022 et éléments de preuve

Le tableau ci-dessous propose une correspondance indicative entre les domaines de l’article 21(2) de la directive NIS2 et des contrôles d’ISO/IEC 27001:2022, avec des exemples de documents et de preuves d’exécution.  
Les niveaux proposés ici sont une appréciation éditoriale propre à ce guide, distincte de l'Outil de comparaison entre ReCyF et d'autres référentiels de l'ANSSI.  
Les intitulés des contrôles sont abrégés ou paraphrasés: se référer à la norme. Ce guide n’en reproduit pas le texte: [ISO/IEC 27001:2022](https://www.iso.org/fr/standard/27001).

**Une correspondance ne vaut ni conformité à NIS2 ni preuve d’efficacité des mesures.**  
L’évaluation dépend du périmètre, de la mise en œuvre effective et des preuves disponibles. Elle doit aussi prendre en compte les autres dispositions applicables de la directive, notamment la gouvernance (article 20), et ne pas se limiter aux articles 21 et 23.

|Domaine NIS2 | Contrôles (annexe A) ISO 27001:2022| Ex. documents | Ex. preuves d'exécution| Niveau de correspondance indicative via ISO 27001:2022 |
| ----------- | ----------- | ----------- | ----------- |  ----------- | 
| 21(2)(a) Politiques relatives à l'analyse des risques et à la sécurité des systèmes d'information | A.5.1 Politiques de sécurité de l’information, A.5.2 Rôles et responsabilités _+ Clauses 6.1.2 et 6.1.3 (appréciation et traitement des risques)_ | PSSI, méthodologie d'analyse de risques, cartographie des actifs | Analyse de risques mise à jour, compte-rendu de revue annuelle, plan de traitement des risques  | ● Elevé |
| 21(2)(b) Gestion des incidents  | A.5.24 à A.5.28 Gestion des Incidents, A.6.8 Signalement des événements liés à la sécurité de l’information, A.8.15 Journalisation, A.8.16 Activités de surveillance | Procédure de gestion des incidents, registre d'incidents | Ticket d'incident traité, exercice de gestion de crise, REX documenté  | ● Elevé|
| 21(2)(c) Continuité des activités |  A.5.29 Sécurité de l'information en cas de perturbation, A.5.30 Préparation des TIC à la continuité des activités, A.8.13 Sauvegarde des informations, A.8.14 Redondance des moyens de traitement de l’information | PCA, PRA, stratégie de sauvegarde | Compte-rendu de test PRA/PCA, journal de restauration de sauvegarde | ◐ Partiel |
| 21(2)(d) Sécurité de la chaîne d'approvisionnement | A.5.19 à A.5.23 Contrats et Conformité avec fournisseurs, sous-traitants et services cloud | Politique fournisseurs, contrats, registre sous-traitants | Revue annuelle fournisseur, évaluation de risque fournisseur (le cas échéant : éléments d'évaluation du fournisseur et certificats pertinents), attestations de certification, avec contrôle du périmètre et de la validité (ex. santé : certificat HDS) | ◐ Partiel |
| 21(2)(e) Sécurité de l'acquisition, du développement et de la maintenance des réseaux et des systèmes d'information | A.8.8 Gestion des vulnérabilités techniques, A.8.25 à A.8.33 Cycle de vie et développement | Politique de développement sécurisé, architecture cible | Revue de code, résultats de scans, gestion des vulnérabilités, pentests | ◐ Partiel |
| 21(2)(f) Politiques et procédures pour évaluer l'efficacité des mesures de gestion des risques en matière de cybersécurité | A.5.35 Revue indépendante, A.5.36 Conformité aux politiques, règles et normes en matière de sécurité de l'information, A.8.34 Protection des systèmes d’information pendant les tests d’audit _+ Clauses 9.1 (surveillance, mesure, analyse et évaluation), 9.2 (audit interne) et 9.3 (revue de direction)_ | Programme d'audit, procédure de contrôle | Rapports d'audit, résultats de tests techniques, suivi des actions correctives | ● Elevé |
| 21(2)(g) Pratiques de base en matière de cyberhygiène et formation à la cybersécurité | A.5.10 Utilisation acceptable des informations et autres actifs associés, A.6.3 Sensibilisation, éducation et formation à la sécurité de l'information, A.6.8 Signalement des événements liés à la sécurité de l’information, A.8.1 Terminaux utilisateurs, A.8.7 Protection contre les logiciels malveillants, A.8.8 Gestion des vulnérabilités techniques | Plan de sensibilisation, supports de formation | Feuilles d'émargement, statistiques e-learning, campagnes phishing | ◐ Partiel |
| 21(2)(h) Cryptographie et chiffrement | A.8.24. Utilisation de la cryptographie | Politique cryptographique | Paramétrage TLS, inventaire des certificats, rapports d'audit de configuration, gestion des clés | ● Elevé  |
| 21(2)(i) Sécurité des ressources humaines, politiques de contrôle d'accès et gestion des actifs | A.5.9 à A.5.14 Inventaire et gestion des actifs et de l’information, A.5.15 à A.5.18 Contrôle d’accès, gestion des identités, informations d’authentification, droits d’accès, A.6.1 à A.6.6 Vérification des antécédents, conditions d’emploi, sensibilisation et formation, processus disciplinaire, responsabilités après changement ou cessation d’emploi, accords de confidentialité | Politique d'habilitation, politique d’habilitation (par exemple matrice de rôles) | Revue périodique des accès, journaux d'attribution/retrait des droits, inventaire des actifs, procédure arrivée/départ, revue des droits | ◐ Partiel |
| 21(2)(j) Utilisation de solutions d'authentification à plusieurs facteurs ou d'authentification continue, de communications vocales, vidéo et textuelles sécurisées et de systèmes sécurisés de communication d'urgence au sein de l'entité, selon les besoins |  A.5.14 Transfert d’informations, A.5.17 Informations d’authentification, A.8.5 Authentification sécurisée, A.8.20 à A.8.22 Sécurité des réseaux, sécurité des services réseau, segmentation des réseaux |  Politique d'authentification, procédure de communication d’urgence | Configuration MFA vérifiée, paramètres des canaux sécurisés, résultats d’exercice | ○ À à approfondir |
| 23. Obligations d’information (notification des incidents importants) | A.5.5 Contacts avec les autorités, A.5.24 à A.5.27 Procédure de gestion des incidents et notification, A.5.31 Exigences légales, statutaires, réglementaires et contractuelles  | Procédure de notification, registre incidents | Historique des notifications, exercices de notification, REX | ◐ Partiel |


**Légende :**
- MFA : Multi-Factor Authentication
- PSSI : Politique de Sécurité du Système d'Information
- PRA : Plan de Continuité d'Activité 
- PCA : Plan de Reprise d'Activité
- REX : Retour d'Expérience
- SIEM : Security Information and Event Management
- Niveaux de correspondance indicative :
    - ● Elevé : les contrôles ISO cités présentent une correspondance directe avec une part importante du domaine NIS2 considéré.  
    - ◐ Partiel : les contrôles cités couvrent certains aspects du domaine, mais des compléments ou des vérifications sont nécessaires.
    - ○ À approfondir : les correspondances identifiées ne permettent pas, à elles seules, de couvrir suffisamment le domaine ; une analyse complémentaire est nécessaire.
    > Ces niveaux qualifient uniquement la correspondance proposée dans ce tableau. Ils ne mesurent ni le niveau de mise en œuvre des contrôles dans une organisation, ni sa conformité à NIS2. La présence d’un document ou d’une preuve ne suffit pas, à elle seule, à démontrer l’efficacité d’une mesure.

---

*Document produit dans le cadre du projet portfolio GRC - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*
*Ce document est une synthèse pédagogique. Il ne se substitue ni à une analyse adaptée au contexte de l’organisation, ni à un audit ou à un accompagnement juridique lorsque ceux-ci sont nécessaires.*

Version 2.0, date : 19/10/2026, Licence : CC BY 4.0, attribution Solène Figueiredo, projet grc-pme-fictive.