# Référentiel légal simplifié - Conformité RGPD-HDS

> **Ce document est une entrée, pas un audit.** Il est conçu pour donner une vision claire aux responsables de PME sans expertise juridique des réglementations applicables, des données concernées et des actions prioritaires à mener.

---

## Recommandations stratégiques - Ordre de travail conseillé

1. **Cartographier les traitements et les données** : Identifier les données collectées, les finalités, les personnes concernées, les accès, les flux, les durées de conservation et les responsabilités de chaque acteur.  
_Livrable : registre des traitements et cartographie des flux._

2. **Déterminer les bases juridiques** : Pour chaque traitement de données de santé, vérifier la base de l'article 6, l'exception de l'article 9 et, si nécessaire, les dispositions françaises spécifiques à la recherche ou aux activités de soins.  
_Livrable : matrice traitements × bases juridiques × conditions applicables._

3. **Vérifier l'hébergement et les fournisseurs** : Déterminer le périmètre HDS, vérifier les activités couvertes par les certificats, les contrats, les sous-traitants ultérieurs, les sauvegardes, le lieu de stockage (UE ou EEE exclusivement, R.1111-9-1 CSP) et les accès à distance depuis des pays tiers (traités comme des transferts).  
_Livrable : registre des fournisseurs et dossier de preuves HDS._

4. **Évaluer le besoin d'AIPD (Analyse d'Impact relative à la Protection des Données) et de DPO (Délégué à la Protection des Données)** : Examiner les risques, le caractère sensible des données, les personnes concernées, l'échelle et les traitements envisagés. Documenter la décision, y compris lorsque l'AIPD ou la désignation d'un DPO n'est pas obligatoire.  
_Livrable : décision motivée sur l'AIPD et le DPO, avec les éléments justificatifs._

5. **Mettre en œuvre les mesures de sécurité** : Vérifier les habilitations, l'authentification multifacteur, la journalisation, les sauvegardes, les tests de restauration, les mises à jour et la procédure de gestion des violations.  
_Livrable : plan d'action priorisé, responsables, échéances et preuves de réalisation._

6. **Formation** : Sensibiliser les équipes aux risques de sécurité et aux obligations RGPD.  
_Livrable : plan de sensibilisation et registre des formations (preuve d'accomplissement)._

> **Note - Hébergement Cloud** : en cas de recours à un Cloud (_ex. : AWS, Azure, OVH_) pour héberger des données de santé pour le compte de tiers, appliquer l'article R.1111-9-1 CSP (en vigueur depuis le 26/09/2026, créé par le décret n° 2026-209 du 24/03/2026).
> - **Stockage** : exclusivement sur le territoire d'un État membre de l'UE ou partie à l'accord sur l'EEE. Cette règle ne comporte pas de dérogation : les garanties de l'art. 46 RGPD (CCT, BCR) ne permettent pas de stocker hors UE/EEE.  
> - **Transfert, y compris accès à distance** (par l'hébergeur ou l'un de ses sous-traitants) vers un pays tiers : possible avec une décision d'adéquation (art. 45 RGPD) ou, à défaut, avec les garanties appropriées de l'art. 46, à condition que les personnes disposent de droits opposables et de voies de droit effectives.  
> - **Contrat d'hébergement** (L.1111-8, I) : en l'absence de décision d'adéquation, il mentionne cette absence et décrit précisément les garanties et mesures complémentaires.  
> - **À vérifier** : lieux de stockage des données et des sauvegardes, pays d'administration et de support de l'hébergeur et de ses sous-traitants.  
>
> **Note - DPO** : évaluer l'obligation de désigner un DPO au regard de l'article 37 du RGPD, notamment de la nature des activités de base et de l'échelle des traitements. En l'absence d'obligation, apprécier l'intérêt d'une désignation volontaire ou d'un accompagnement spécialisé.

**Contrôles de premier niveau : action vérifiable / preuve attendue**

| Sujet	| Action vérifiable	| Preuve attendue |
| ---- | -------------- | -------------- |
| Droits des personnes | Tester une demande d'accès de bout en bout | Réponse dans le délai, trace de la procédure |
| HDS	| Vérifier que le certificat couvre les prestations réellement utilisées	| Certificat, périmètre et date de validité |
| Localisation | Vérifier les lieux de stockage (données et sauvegardes) et les accès à distance depuis des pays tiers (administration, support, sous-traitants) | Contrat d'hébergement, liste des lieux et pays d'accès, mention de l'absence de décision d'adéquation et des garanties le cas échéant |
| Sous-traitance	| Vérifier les contrats et la chaîne de sous-traitance	| Contrats, annexes RGPD, liste des sous-traitants ultérieurs |
| AIPD	| Évaluer le risque et justifier la décision de réaliser ou non une AIPD	| Analyse documentée, AIPD si requise |
| Violations	| Tester le processus d'escalade et de notification	| Procédure, contacts, journal des incidents |
| Sécurité	| Vérifier les mesures techniques et leur efficacité	| Paramétrages, journaux, tests de restauration et suivi des actions |

---

## Tableau de référence

Ce référentiel couvre les obligations structurantes d'une PME e-santé. La co-responsabilité (RGPD art. 26) et les garanties spécifiques des partenariats publics sont hors périmètre de ce référentiel et à qualifier avec le DPO.

| Texte ou référentiel | Nature | Focus | Données concernées | Obligation concrète | Risque si non-conformité |
|---|---|---|---|---|---|
| **RGPD - Art. 6 et liés** | Loi | Juridique | Données personnelles (nom, email, identifiants…) | Définir une finalité déterminée, explicite et légitime, puis identifier et documenter la base légale au titre de l'art. 6 : consentement, contrat, obligation légale, intérêts vitaux, mission d'intérêt public ou intérêts légitimes. Vérifier que les conditions de la base retenue sont remplies. | Amende RGPD, palier 83(5) - voir légende + perte de confiance + responsabilité civile + interdiction de traitement possible selon la gravité |
| **RGPD - Art. 9 et liés** | Loi | Juridique + Métier (Santé) | Données de santé (dossier médical, ECG, ordonnances…) | Identifier une base légale au titre de l'art. 6 **et** une exception autorisant le traitement au titre de l'art. 9. Le consentement explicite n'est requis que lorsque le régime retenu l'exige. Vérifier les conditions particulières applicables aux soins, à la recherche ou à la gestion des services de santé. | Amende RGPD, palier 83(5) - voir légende |
| **RGPD - Art. 12-22** | Loi | Juridique | Données des personnes concernées | Garantir l'exercice des droits (accès, rectification, effacement, portabilité, opposition) avec réponse dans un délai d'un mois, prolongeable de deux mois pour les demandes complexes ou nombreuses si la personne en est informée dans le premier mois (art. 12(3)), information claire des personnes. Accès au dossier médical : vérifier les délais propres prévus par le CSP. | Amende RGPD, palier 83(5) - voir légende |
| **RGPD - Art. 28 et liés** | Loi | Juridique | Données personnelles et de santé | Contrat écrit avec chaque sous-traitant comportant les clauses de l'art. 28(3), garanties suffisantes, instructions documentées, maîtrise des sous-traitants ultérieurs. | Amende RGPD, palier 83(4) - voir légende |
| **RGPD - Art. 30** | Loi | Juridique | Tous traitements | Tenir et mettre à jour le registre des traitements (responsables et sous-traitants). | Amende RGPD, palier 83(4) - voir légende |
| **RGPD - Art. 32 et liés** | Loi | Juridique | Données personnelles et de santé | Mesures de sécurité adaptées au risque : chiffrement, MFA, journalisation, sauvegardes, tests. | Amende RGPD, palier 83(4) - voir légende |
| **RGPD - Art. 33-34** | Loi | Juridique | Données personnelles et de santé | Documenter toute violation, évaluer le risque, notifier la CNIL **sous 72 h** lorsque la notification est requise, informer les personnes en cas de risque élevé, sauf exception applicable. | Amende RGPD, palier 83(4) - voir légende |
| **RGPD - Art. 35** | Loi | Juridique | Traitements à haut risque | Réaliser une AIPD pour les traitements à haut risque - les données de santé à grande échelle sont en principe concernées, documenter la décision même si l'AIPD n'est pas requise. | Amende RGPD, palier 83(4) - voir légende |
| **RGPD - Art. 37** | Loi | Juridique | Activités de base de l'organisme | Évaluer l'obligation de désignation d'un DPO (art. 37(1)(c) : activités de base consistant en un traitement à grande échelle de données art. 9) - voir note dédiée, documenter la décision. | Amende RGPD, palier 83(4) - voir légende |
| **RGPD - Art. 44-49** | Loi | Juridique | Données personnelles et de santé transférées hors EEE | Tout transfert vers un pays tiers, y compris par accès à distance, respecte le chapitre V : une décision d'adéquation, des garanties appropriées ou, à titre exceptionnel, une dérogation (art. 49, à ne pas utiliser pour des transferts récurrents). Pour les données de santé hébergées, appliquer en plus R.1111-9-1 CSP : stockage exclusivement UE/EEE, transfert encadré par le contrat d'hébergement (voir note Cloud). | Amende RGPD, palier 83(5) - voir légende |
| **LIL art. 30 + décret n° 2019-341 / CSP L.1111-8-1 + R.1111-8-1 et s.** | Loi | Juridique | NIR - numéro de sécurité sociale (NIR ou NIA) | **Hors santé** : usage du NIR limité aux responsables et finalités du décret n° 2019-341. **En santé, cadre distinct** : le référencement des données de santé s'appuie sur l'INS (matricule INS, NIR ou NIA, + traits d'identité), vérifié via le téléservice INSi, obligatoire depuis le 01/01/2021, finalités sanitaires et médico-sociales. | Amende administrative CNIL (RGPD art. 83), usage hors finalités autorisées : sanctions pénales possibles (art. 226-16 et s. Code pénal). |
| **CSP - R.1112-7** | Loi | Métier (Santé) | Dossier patient des établissements de santé | Conservation : 20 ans après le dernier séjour ou la dernière consultation externe, prorogé jusqu'au 28e anniversaire du patient si le terme de 20 ans est antérieur, 10 ans à compter du décès s'il survient moins de 10 ans après le dernier passage, suspension des délais en cas de recours. Ensuite, l'élimination du dossier suit les conditions de l'article (décision du directeur, avis du médecin DIM, visa des archives selon les établissements). | Responsabilité civile + sanctions ordinales pour les professionnels concernés |
| **CSP - R.4127-45 (réd. décret n° 2026-691)** | Loi | Métier (Santé) | Dossier médical tenu par les **médecins** (y compris libéraux) | Conservation pendant les **mêmes durées que les établissements de santé** (renvoi à R.1112-7 : 20 ans / 28e anniversaire / décès - voir ligne ci-dessus). Hors périmètre : autres professions de santé (infirmiers, pharmaciens…) - durées propres à vérifier. Documenter les durées retenues et les modalités de suppression/archivage. | Sanctions déontologiques (Conseil de l'Ordre) + responsabilité civile |
| **CSP - L.1111-8 + R.1111-8 et s. (HDS) - volet hébergeur** | Certification légale | Technique | Données de santé à caractère personnel hébergées sur support numérique | Soumis à certification dès lors que l'activité relève du champ HDS (L.1111-8, R.1111-8-8, R.1111-9) : certificat délivré par un organisme certificateur accrédité COFRAC, sur le référentiel édité par l'ANS, validité 3 ans, audits de surveillance annuels. R.1111-9 vise notamment l'infrastructure physique ou virtuelle, l'administration et l'exploitation, et la sauvegarde : vérifier que le certificat couvre les activités réellement exercées. Stockage exclusivement sur le territoire d'un État membre de l'UE ou partie à l'accord EEE (R.1111-9-1, en vigueur depuis le 26/09/2026). | **L.1115-1 CSP : 3 ans d'emprisonnement et 45 000 € d'amende** (prestation d'hébergement sans certificat) |
| **CSP - L.1111-8 + R.1111-8 et s. (HDS) - volet client** | Certification légale | Technique | Données de santé confiées à un hébergeur | S'assurer que l'hébergeur est certifié et que les **activités couvertes par le certificat** incluent les prestations réellement utilisées (R.1111-8-8), contrat d'hébergement contenant les clauses minimales de **R.1111-11** (article modifié le 26/09/2026, se référer à la version en vigueur) : notamment périmètre du certificat, lieux d'hébergement, modalités de signalement des violations, référent pour les incidents, restitution et destruction des données à la fin. Localisation : stockage exclusivement UE/EEE (R.1111-9-1). Si la prestation de l'hébergeur ou d'un sous-traitant implique un transfert, y compris un accès à distance, vers un pays tiers : décision d'adéquation (art. 45 RGPD) ou garanties de l'art. 46, dans ce second cas, le contrat d'hébergement mentionne l'absence de décision d'adéquation et décrit les garanties. | Exposition RGPD (art. 28/32 - CNIL) + risque contractuel |
| **PGSSI-S - référentiels de L.1470-5 CSP** | Référentiels approuvés par arrêté | Technique | Données de santé échangées, identification électronique | Les services numériques en santé destinés à être utilisés par les personnes mentionnées aux 1° et 2° de L.1470-1 CSP doivent être conformes aux référentiels d'interopérabilité, de sécurité et d'éthique élaborés par le GIP de L.1111-24 (ANS) et approuvés par arrêté (L.1470-5). Vérifier si le service est visé par L.1470-1 (1° et 2°), puis identifier les référentiels applicables à chaque intégration (ex. : référentiel d'accès des professionnels au DMP, arrêté du 26/10/2023). Ne pas supposer qu'ils s'appliquent indistinctement à toute PME. | Non-conformité à une obligation légale (L.1470-5), exigence du partenaire santé, conditions d'accès aux services nationaux (DMP, Mon espace santé) |
| **RGS (ordonnance n° 2005-1516 du 8 décembre 2005)** | Référentiel d'État | Technique | Échanges électroniques avec les autorités administratives | Le RGS vise la sécurité des échanges électroniques des autorités administratives. Une PME privée n'y est pas soumise directement, un partenaire public (ex. établissement public de santé) peut l'imposer par contrat. Relever dans le contrat ou l'annexe sécurité les niveaux exigés. | Risque contractuel |
| **PCI-DSS** | Norme contractuelle | Technique | Données de paiement (CB, tokens) | Référentiel de sécurité de l'écosystème des paiements par carte, opposé via les réseaux de paiement et l'acquéreur (pas une loi). Si le paiement est entièrement externalisé vers un prestataire certifié, évaluer l'éligibilité au **SAQ A** (Self-Assessment Questionnaire A) selon les critères en vigueur et l'architecture réelle. Vérifier le périmètre résiduel, les responsabilités et les exigences de l'acquéreur. | Pénalités contractuelles par transaction (réseaux cartes), résiliation par l'acquéreur, responsabilité en cas de fuite de données CB |

**Légende sanctions RGPD (art. 83)** : 
- palier 83(5) = 20 M€ ou 4 % du CA mondial, le plus élevé (bases légales, données art. 9, droits des personnes art. 12-22, transferts art. 44-49),  
- palier 83(4) = 10 M€ ou 2 %, le plus élevé (sous-traitance art. 28, registre art. 30, sécurité art. 32, violations art. 33-34, AIPD, DPO). Une faille de sécurité peut aussi être sanctionnée au titre des principes de l'art. 5 : palier 83(5).

**Références en date du 20/10/2026** : Ce référentiel doit être revérifié à chaque révision réglementaire.  
- [RGPD](https://www.cnil.fr/fr/reglement-europeen-protection-donnees) : Règlement (UE) 2016/679 du Parlement européen et du Conseil du 27 avril 2016,  
- [LIL](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000038886929) : Loi n° 78-17 du 6 janvier 1978 relative à l'informatique, aux fichiers et aux libertés, en vigueur depuis le 2 juin 2019,  
- [Décret n° 2019-341](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000038396526) : Décret n° 2019-341 du 19 avril 2019 relatif à la mise en œuvre de traitements comportant l'usage du numéro d'inscription au répertoire national d'identification des personnes physiques ou nécessitant la consultation de ce répertoire,  
- [CSP](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072665/2026-10-20) : Code de la santé publique, version consolidée consultée le 20/10/2026,  
- [CSP - article R.1111-9-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053720788) : Hébergement de données de santé, localisation du stockage et transferts, créé par le décret n° 2026-209 du 24 mars 2026, en vigueur depuis le 26 septembre 2026,  
- [Décret n° 2026-691](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054541620) : Décret n° 2026-691 du 27 juillet 2026 portant modification du code de déontologie médicale,  
- [Référentiel INS](https://esante.gouv.fr/produits-services/referentiel-ins) : Référentiels et déploiement de l'Identité Nationale de Santé (INS), utilisation de l'INS pour référencer les données de santé est obligatoire depuis le 1er janvier 2021,  
- [HDS](https://esante.gouv.fr/produits-services/hds) : Certification Hébergeur de Données de Santé,  
- [RGS](https://www.numerique.gouv.fr/offre-accompagnement/reference-securite-rgs/) : Référentiel général de sécurité, fondé sur ordonnance du 8 décembre 2005 (n° 2005-1516),  
- [PGSSI-S](https://esante.gouv.fr/securite/politique-generale-de-securite-des-systemes-d-information-de-sante) : Politique générale de sécurité des systèmes d'information de santé,  
- [Référentiel de sécurité et d'interopérabilité relatif à l'accès des professionnels au dossier médical partagé](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048368244) : Arrêté du 26 octobre 2023 portant approbation du référentiel de sécurité et d'interopérabilité relatif à l'accès des professionnels au dossier médical partagé (DMP),  
- [PCI-DSS](https://www.pcisecuritystandards.org/fr/standards/pci-dss/) : Base de référence des exigences techniques et opérationnelles conçues pour protéger les données des comptes de paiement, dernière version = PCI DSS v4.0.1, Juin 2024.

---

*Document produit dans le cadre du projet portfolio GRC - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*
*Ce document est une synthèse pédagogique. Il ne se substitue ni à une analyse adaptée au contexte de l'organisation, ni à un audit ou à un accompagnement juridique lorsque ceux-ci sont nécessaires.* 

Version 2.0, date : 20/10/2026, Licence : CC BY 4.0, attribution Solène Figueiredo, projet grc-pme-fictive.
