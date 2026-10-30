# ISO 27001:2022 - Contrôles regroupés par sous-catégorie pour les PME e-santé

> Alignement RGPD/NIS2/HDS et priorisation pratique.  
> Ce document est une entrée, pas un audit. Il est conçu pour donner une vision claire aux responsables de PME sans expertise juridique ni expertise normative des contrôles ISO 27001:2022, des informations concernées et des actions prioritaires à mener. Les correspondances réglementaires citées sont indicatives et ne constituent pas un avis juridique.
> Ce document ne reproduit pas la norme : il cite les références des contrôles et propose des explications et exemples rédigés indépendamment. Pour les libellés officiels et la guidance d'implémentation, se référer à l'ISO 27001:2022.

## **Objectif**

Cette liste recense les 93 contrôles de l'annexe A de l'ISO/IEC 27001:2022 :
- **Regroupés en 16 sous-catégories**, ordonnées de la gouvernance à la veille.
- Présentés en **deux formats complémentaires** : ce document, à lire par sous-catégorie, et le CSV associé, trié par contrôle, à filtrer dans un tableur.
- Avec, sur chaque ligne, des renvois lorsque pertinents aux **exigences RGPD, NIS2 et HDS**.
- Et **deux axes de priorisation** : l'Effort (coût et complexité du contrôle complet) et la Phase (ordre de traitement : la phase 1 regroupe ce que la loi ou le contrat rend exigible dès la mise en service).

---

## **Méthodologie**
1. **Classement par sous-catégorie** :
Logique (16 sous-catégories thématiques de la gouvernance à la veille): 
Gouvernance et rôles → Ressources humaines →  Sécurité physique →  Gestion des actifs et classification →  Gestion des accès et identités (IAM) →  Protection des données et échanges → Maintenance et correctifs → Sécurité réseau → Sécurité des postes → Développement sécurisé → Surveillance et journalisation → Gestion des incidents → Continuité et résilience → Contrats et conformité → Audit → Veille et contacts externes


2. **Priorisation** :
Deux dimensions indépendantes structurent le tableau : l'Effort (ce que coûte le contrôle) et la Phase (quand le traiter).  
Elles ne se déduisent pas l'une de l'autre : un contrôle lourd peut être exigé dès la phase 1, dans une version minimale.
- **Effort PME** : _Les seuils de coût et de charge sont à calibrer par PME selon sa taille, la grille ci-dessous correspond à une PME de 10 à 50 salariés._ 
   - ○ Faible : réalisable en interne, sans compétence rare ni budget externe. 
   - ◐ Moyen : quelques jours internes ou prestation ponctuelle. 
   - ● Élevé : budget externe significatif, compétence rare ou chantier pluriannuel.
- **Phase recommandée** : _Phases calibrées pour une PME éditrice hébergée chez un hébergeur certifié. Pour d'autres profils, revoir la répartition selon les caractéristiques._
   - Phase **1** - socle : exigences légales et contractuelles sans délai (continuité, sauvegarde, gestion des accès, réponse aux incidents) + gains rapides.
      - Recoupe environ les deux tiers des contrôles (cf. [répartition par phase](#feuille-de-route-suggérée-profil-éditeur-hébergé)). Une PME non régulée aurait une phase 1 plus courte.
      - Horizon indicatif : 6 à 12 mois pour une PME partant de zéro. 
      - Critère de passage en phase 2 : chaque contrôle de phase 1 dispose d'une preuve datée (périmètre, responsable) démontrant sa mise en œuvre, et les six 1+ ont leur version minimale documentée.
   - Phase **2** - consolidation: ajouter les contrôles en fonction des ressources disponibles.
      - Horizon indicatif 12 mois.
      - Critère de passage en phase 3  : chaque contrôle de phase 2 dispose d'une preuve datée (périmètre, responsable) démontrant sa mise en œuvre, un premier audit interne (A.5.36) a été réalisé, et la version minimale du 2+ (A.8.25) est documentée.
   - Phase **3** - maturité : contrôles attendus par les acteurs les plus exigeants (clients grands comptes, assureurs, audits de certification).


3. **Alignement réglementaire** :
- **RGPD** : Contrôles liés à la **protection des données personnelles** (p.ex. A.5.13 Étiquetage des informations, A.8.10 Suppression d’informations).
- **NIS2** : Contrôles liés à la **résilience et la cybersécurité critique** (p.ex. A.5.29 Sécurité en cas de perturbation, A.8.16 Surveillance).  
   _- Renvois NIS2 : granularité volontairement limitée au niveau de l'article. Correspondances détaillées et indicatives : cf. [Repères NIS2 et correspondances indicatives avec ISO 27001:2022](./nis2_correspondances_ISO27001.md). La transposition nationale reste à vérifier._
   _- Les intitulés de contrôles sont abrégés ou paraphrasés : se référer au texte officiel de la norme._  
   _- NIS2 impose ses obligations aux entités assujetties. Une PME non assujettie peut néanmoins se voir imposer des exigences par contrat, au titre de la sécurité de la chaîne d'approvisionnement exigée de ses clients assujettis (Art. 21(2)(d)), p. ex. une PME e-santé partenaire d'un CHU. Vérifier le statut de transposition en France avant d'opposer les délais._
- **HDS** : Contrôles liés à la **sécurité des données de santé** (p.ex. A.8.13 Sauvegarde, A.5.15 Contrôle d’accès).
   - Partage des responsabilités HDS : la qualification des activités relève du texte, le partage entre acteurs du contrat.
   - Les six activités HDS définies par CSP R.1111-9 : 1. sites physiques, 2. infrastructure matérielle, 3. infrastructure virtuelle, 4. plateforme d'hébergement d'application, 5. administration et exploitation du SI, 6. sauvegarde.
   - La certification de l'hébergeur ne dit pas qui porte quoi. 
   - Attention - selon l'ANS (juillet 2026) : publication visée en octobre 2026, application en décembre 2026. L'arrêté d'approbation reste à vérifier à la date de publication de ce document. A noter :
      - A.5.23 (Sécurité des services cloud) : dans le référentiel HDS v2.1, le contrat d'hébergement doit indiquer l'absence de soumission à des lois extra-UE ou les informations de tout transfert (un accès distant compte comme un transfert).
   - Périmètre des renvois HDS de ce tableau : seuls les objets directement identifiables du dispositif HDS portent un renvoi (contrôle d'accès, chiffrement, traçabilité, sauvegarde, disponibilité, chaîne de sous-traitance, documentation, sensibilisation, audit de certification). 
      - D'autres contrôles (p.ex. classification et inventaire des données, sécurité des postes, protection contre les logiciels malveillants, contrôle des logiciels et durcissement, environnements de test, sécurité du développement, stockage, maintenance) participent à la sécurité des données de santé sans que ce document n'affirme d'exigence HDS spécifique : à traiter dans l'analyse de risques et selon le partage de responsabilités de chaque acteur. 

4. **Exemples concrets** :
Chaque contrôle est illustré par un **cas d’usage e-santé/PME** pour faciliter l’appropriation.

5. **Prouver** : 
Un contrôle est mis en œuvre quand il existe une preuve datée, avec périmètre et responsable, démontrant la mise en œuvre et son efficacité, p.ex. un enregistrement de test de restauration daté, une revue des accès signée avec écarts suivis, un rapport de formation avec participants et évaluation. 
**Un document seul (une procédure, une politique) démontre l'intention, pas le résultat** : il ne suffit pas. 

---

## **Utilisation recommandée**

Ce tableau est également disponible en format CSV pour permettre filtrage et tri (p.ex. par sous-catégorie): [Liste Contrôles ISO 27001:2022](./ISO27001_Liste-Controle.csv).

*Note :*  
*- L'applicabilité de chaque contrôle dépend du contexte, une SoA argumente les exclusions.*  
*- En renseignant pour chaque contrôle un statut Inclus / Exclu et sa justification, ce tableau peut servir de point de départ à une déclaration d'applicabilité (SoA) ISO 27001:2022. L'état de mise en œuvre (en place / partiel / planifié) se suit séparément, dans votre plan de traitement, il ne relève pas de la déclaration d'applicabilité.*

---

## Feuille de route suggérée (profil éditeur hébergé)

**Avant de signer avec un hébergeur HDS** : points de vérification pour une PME cliente
- Périmètre HDS :  Le certificat couvre-t-il le service réellement utilisé et les activités nécessaires ?
- Contrôle d'accès : Les accès administrateurs sont-ils limités, nominatifs et revus ? 
- Traçabilité : Les accès et interventions d'administration sont-ils journalisés ?
- Chiffrement : Quelles protections sont mises en œuvre au repos et en transit, et qui gère les clés ?
- Sauvegardes : Qui sauvegarde, où, à quelle fréquence et avec quels tests de restauration ?
- Disponibilité : Quels engagements contractuels et dispositifs de continuité sont prévus ?
- Sous-traitance : Quels sous-traitants interviennent, pour quelles prestations et dans quels pays ?
- Localisation et transferts : Où les données sont-elles hébergées ? Existe-t-il des accès distants ou des transferts vers des pays tiers ?
- Réversibilité : Comment récupérer les données dans un format exploitable à la fin du contrat ?
- Gouvernance et documentation : Les responsabilités, engagements de sécurité et procédures d'incident sont-ils documentés ?
- Personnel : Les personnes intervenant sur le service sont-elles compétentes et sensibilisées ?

**Répartition par phase**

| Phase | Nombre de contrôles | Liste |
| ---- | ----- | --------------- |
| Phase 1 - socle | 61 contrôles (dont 6 contrôles en version 1+ : A.5.21, A.5.29, A.5.30, A.7.3, A.8.12, A.8.31) | A.5.1, A.5.2, A.5.3, A.5.5, A.5.9, A.5.10, A.5.11, A.5.12, A.5.14, A.5.15, A.5.16, A.5.17, A.5.18, A.5.19, A.5.20, A.5.21, A.5.22, A.5.23, A.5.24, A.5.25, A.5.26, A.5.28, A.5.29, A.5.30, A.5.31, A.5.33, A.5.34, A.5.37, A.6.1, A.6.2, A.6.5, A.6.6, A.6.7, A.6.8, A.7.1, A.7.2, A.7.3, A.7.5, A.7.6, A.7.7, A.7.8, A.7.10, A.7.14, A.8.1, A.8.2, A.8.3, A.8.5, A.8.7, A.8.8, A.8.10, A.8.12, A.8.13, A.8.15, A.8.17, A.8.19, A.8.20, A.8.24, A.8.26, A.8.30, A.8.31, A.8.33 |
| Phase 2 - consolidation | 28 contrôles (dont 1 en version 2+ : A.8.25) | A.5.4, A.5.6, A.5.7, A.5.8, A.5.13, A.5.27, A.5.36, A.6.3, A.7.4, A.7.9, A.7.11, A.7.12, A.7.13, A.8.4, A.8.6, A.8.9, A.8.11, A.8.16, A.8.18, A.8.21, A.8.22, A.8.23, A.8.25, A.8.27, A.8.28, A.8.29, A.8.32, A.8.34 |
| Phase 3 - maturité | 4 contrôles | A.5.32, A.5.35, A.6.4, A.8.14 |

En fin de phase 1, la PME a : un plan de réponse aux incidents prêt à être appliqué avec ses délais de notification, des sauvegardes chiffrées dont une restauration testée et datée, des accès revus et journalisés, une chaîne de sous-traitance contractualisée, et une preuve vérifiable pour chaque contrôle du socle. 

Certains contrôles peuvent s'appliquer sur plusieurs phases selon leur profondeur.
Notation `+`: contrôle exigible dès cette phase sous une version minimale, complété ensuite (cf. tableau des versions minimales). 
Notation indépendante de l'Effort : l'Effort mesure le contrôle complet (la cible). La version minimale est une étape intermédiaire, nécessairement moins coûteuse.
P.ex. la sécurité du code est couverte en phase 1 sur les exigences et environnements, et la phase 2 couvre le cycle complet. 

| Contrôle | Phase | Version minimale | Complet en |
| --- | --- | --- | --- |
| A.5.29 | 1+ | PCA documenté et approuvé (scénarios, rôles, contacts, priorités de reprise) | 2 (exercice PCA daté, revu) |
| A.5.30 | 1+ | RTO/RPO définis + une restauration testée et datée par an | 2 (test de bascule) |
| A.5.21 | 1+ | Vérification annuelle de la certification HDS (validité, périmètre) + sous-traitants identifiés | 2 (processus de surveillance fournisseurs) |
| A.8.31 | 1+ | Cloisonnement logique de la production, données fictives en dev/test | 3 (serveurs dédiés — coût matériel, exception justifiée) |
| A.8.12 | 1+ | Inventaire et journalisation des exports de données | 2 (DLP) |
| A.7.3 | 1+ | Verrouillage des locaux, local technique fermé à clé | 3 (caméras, contrôle d'accès électronique — acté) |
| A.8.25 | 2+ | Revue de code des modifications sensibles + scan automatisé dans la CI | 3 (revue systématique) |
| A.8.14 | conditionnel | Si un RTO contractuel l'exige : redondance dès la phase concernée | 3 sinon |

___


| Thème| Contrôle  | Sous-catégorie  | Courte explication  | Court exemple | Effort PME | Phase conseillée | Références RGPD/NIS2/HDS|
| --------------- | -------------------------- | ----- | ----- | ------------- | ---------- | ---------------- | --- |
| - | - | **Gouvernance et rôles**| -| -  | - | -  | - |
| Organisationnel | A.5.1 Politiques de sécurité de l'information| Gouvernance et rôles | Définir, faire approuver par la direction et communiquer une politique de sécurité.  | PSSI validée par le dirigeant, diffusée aux salariés et revue chaque année. | ◐ | **1** | RGPD (Art. 24, 32), NIS2 (Art. 21), HDS (documentation et gouvernance)  |
| Organisationnel | A.5.2 Rôles et responsabilités | Gouvernance et rôles | Attribuer et documenter les rôles de sécurité (direction, RSSI, DPO, équipes techniques). | Matrice RACI : qui décide, qui exécute, qui est informé en cas d'incident.| ○ | **1** | RGPD (Art. 24, 37-39), NIS2 (Art. 20) |
| Organisationnel | A.5.3 Séparation des tâches | Gouvernance et rôles | Éviter les conflits d'intérêts ou les erreurs en séparant les responsabilités critiques. | Chez un éditeur, celui qui déploie en production ne valide pas seul ses propres changements ; celui qui gère les comptes ne s'attribue pas seul un accès administrateur. | ○ | **1** | RGPD (Art. 32) |
| Organisationnel | A.5.4 Responsabilités de la direction| Gouvernance et rôles | La direction exige l'application de la politique et alloue les ressources nécessaires.  | Revue annuelle de direction avec arbitrage du budget sécurité. | ◐ | **2** | RGPD (Art. 24), NIS2 (Art. 20)|
| Organisationnel | A.5.8 Sécurité dans la gestion de projet| Gouvernance et rôles | Intégrer la sécurité dès la phase de conception des projets. | Inclure une analyse de risques cyber dans le cahier des charges d'un nouveau logiciel de dossier patient.  | ◐ | **2** | Aucune |
| Organisationnel | A.5.10 Utilisation acceptable| Gouvernance et rôles | Définir des règles claires sur l'usage des ressources (IT, données).| Charte informatique interdisant l'usage de clés USB personnelles pour transférer des données patients.  | ◐ | **1** | RGPD (Art. 32) |
| Organisationnel | A.5.36 Conformité aux politiques  | Gouvernance et rôles | Vérifier que les politiques de sécurité sont respectées.  | Organiser des audits internes pour vérifier l'application de la charte informatique. | ◐ | **2** | RGPD (Art. 24) |
| Organisationnel | A.5.37 Procédures opérationnelles documentées| Gouvernance et rôles | Documenter les procédures critiques pour assurer la traçabilité.  | Rédiger une procédure pour la gestion des mots de passe ou des sauvegardes. | ◐ | **1** | HDS (documentation et gouvernance)|
| - | - | **Ressources humaines** | -| -  | - | -  | - |
| Personnes | A.6.1 Vérification des antécédents| Ressources humaines| Vérifier les candidats avant embauche, dans la limite de la loi, selon la sensibilité du poste. | Vérification des références et des diplômes pour les postes accédant à des données de santé. | ◐ | **1** | RGPD (Art. 5, 32) |
| Personnes | A.6.2 Conditions d'emploi| Ressources humaines| Inclure les responsabilités de sécurité dans les contrats de travail.  | Clause de confidentialité et de respect de la charte informatique dans chaque contrat. | ○  | **1** | RGPD (Art. 28-29, 32) |
| Personnes | A.6.3 Sensibilisation et formation| Ressources humaines| Former les employés aux bonnes pratiques de sécurité.  | Organiser une formation annuelle sur la cybersécurité avec des cas pratiques (p.ex. phishing). | ◐ | **2** | RGPD (Art. 39), NIS2 (Art. 21), HDS (sensibilisation du personnel)  |
| Personnes | A.6.4 Processus disciplinaire| Ressources humaines| Prévoir des sanctions proportionnées en cas de manquement à la politique de sécurité.| Procédure disciplinaire proportionnée, intégrée au contrat de travail ou au règlement intérieur si l'effectif le requiert (50 salariés et plus). | ◐ | **3** | RGPD (Art. 32)  |
| Personnes | A.6.5 Responsabilités après la fin du contrat| Ressources humaines| Maintenir les obligations de confidentialité après le départ ou le changement de poste. | Révocation des accès, restitution du matériel, rappel de la confidentialité au départ. | ○  | **1** | RGPD (Art. 32) |
| Personnes | A.6.6 Accords de confidentialité  | Ressources humaines| Faire signer des engagements de confidentialité aux salariés et aux tiers.| NDA pour les prestataires et clause de confidentialité pour les salariés. | ○  | **1** | RGPD (Art. 28, 32)|
| Personnes | A.6.7 Télétravail | Ressources humaines| Sécuriser les accès à distance.  | Imposer l'usage d'un VPN et d'un ordinateur dédié (pas de BYOD) pour le télétravail. | ◐ | **1** | RGPD (Art. 32), NIS2 (Art. 21)|
| - | - | **Sécurité physique**| _Profil éditeur hébergé : ces contrôles portent sur vos locaux, vos postes et votre local technique. L'infrastructure distante (sites, serveurs, climatisation, alimentation) relève des garanties de votre hébergeur, vérifiez-les via la checklist « Avant de signer » plutôt que dans ce bloc_ | -  | - | -  | - |
| Physiques | A.7.1 Périmètres de sécurité physique| Sécurité physique  | Définir les zones à protéger (bureaux, salle technique) et leurs barrières.  | Plan des locaux avec zones publiques, restreintes et sensibles.| ○ | **1** | RGPD (Art. 32), HDS (sécurité physique des sites : hébergeur, selon contrat) |
| Physiques | A.7.2 Entrées physiques | Sécurité physique  | Contrôler l'accès aux locaux : badges, accueil, registre des visiteurs.| Badge pour les salariés, visiteurs enregistrés et accompagnés. | ◐ | **1** | RGPD (Art. 32), HDS (sécurité physique des sites : hébergeur, selon contrat) |
| Physiques | A.7.3 Sécurisation des locaux| Sécurité physique  | Protéger les bureaux et installations contre les intrusions. | Version minimale : verrouillage des locaux et local technique fermé à clé. Complet : caméras et contrôle d'accès électronique.  | ◐ | **1+** | RGPD (Art. 32), HDS (sécurité physique des sites : hébergeur, selon contrat) |
| Physiques | A.7.4 Surveillance physique | Sécurité physique | Détecter les accès non autorisés aux zones sensibles. | Alarme intrusion et caméras sur les locaux de la PME, journal des entrées/sorties. Salles serveurs : chez l'hébergeur HDS, selon contrat. | ○ | **2** | NIS2 (Art. 21) |
| Physiques | A.7.5 Protection contre les menaces physiques| Sécurité physique  | Protéger contre les risques (incendie, inondation, etc.). | Détecteurs de fumée et extincteurs dans les bureaux et le local technique, l'infrastructure distante relève des garanties de l'hébergeur. | ◐ | **1** | RGPD (Art. 32)|
| Physiques | A.7.6 Travail en zones sécurisées | Sécurité physique  | Limiter l'accès aux zones sensibles aux personnes autorisées.| Accès au local technique et aux armoires réseau limité aux personnes autorisées, la salle serveurs distante relève de l'hébergeur. | ○ | **1** | RGPD (Art. 32) |
| Physiques | A.7.7 Bureau dégagé et écran propre  | Sécurité physique  | Éviter les fuites d'informations via des documents visibles. | Imposer de verrouiller les écrans en cas d'absence et de ranger les documents sensibles.  | ○ | **1** | RGPD (Art. 32) |
| Physiques | A.7.8 Implantation des équipements| Sécurité physique  | Placer les équipements de manière sécurisée.| Ranger les équipements dans un local technique verrouillé et ventilé, l'implantation des serveurs hébergés relève de l'hébergeur. | ◐ | **1** | HDS (sécurité physique des sites : hébergeur, selon contrat) |
| Physiques | A.7.9 Sécurité des actifs hors site  | Sécurité physique  | Protéger les équipements en déplacement. | Chiffrer les disques durs des ordinateurs portables et activer le verrouillage automatique.  | ◐ | **2** | RGPD (Art. 32), HDS (chiffrement des données de santé)|
| Physiques | A.7.11 Services supports| Sécurité physique  | S'assurer que électricité, climatisation et télécoms ne compromettent pas les services critiques.  | Si les données critiques sont chez un hébergeur certifié, vérifier ses garanties plutôt que les équipements des bureaux.| ◐ | **2** | NIS2 (Art. 21), HDS (disponibilité de l'infrastructure, selon contrat) |
| Physiques | A.7.12 Sécurité du câblage| Sécurité physique  | Protéger les câbles réseau contre les interceptations ou dommages.| Faire passer les câbles dans des gaines sécurisées. | ◐ | **2** | NIS2 (Art. 21), HDS (sécurité physique des sites : hébergeur, selon contrat) |
| - | - | **Gestion des actifs et classification** | -| -  | - | -  | - |
| Organisationnel | A.5.9 Inventaire des informations | Gestion des actifs et classification  | Recenser les informations et supports détenus, avec localisation et responsable. | Cartographie des fichiers, bases et applications contenant des données de santé, avec responsable et localisation identifiés. | ◐ | **1** | RGPD (Art. 30) |
| Organisationnel | A.5.11 Retour des actifs| Gestion des actifs et classification  | S'assurer que les actifs (clés, badges, équipements) sont retournés en fin de contrat.  | Récupérer les badges d'accès et les ordinateurs portables des employés partants.  | ○ | **1** | RGPD (Art. 32) |
| Organisationnel | A.5.12 Classification des informations  | Gestion des actifs et classification  | Classer les informations selon leur sensibilité pour appliquer des protections adaptées.| Trois niveaux (critique, sensible, standard) avec mesures associées. | ◐ | **1** | RGPD (Art. 9, 32) |
| Organisationnel | A.5.13 Étiquetage des informations| Gestion des actifs et classification  | Étiqueter les informations selon leur sensibilité.| Marquer les dossiers patients avec des étiquettes « Confidentiel - RGPD ».| ◐ | **2** | RGPD (Art. 32) |
| Organisationnel | A.5.33 Protection des enregistrements| Gestion des actifs et classification  | Protéger les enregistrements (documents, dossiers, fichiers) contre la divulgation, la modification, la suppression ou la perte non autorisées. | Dossiers patients archivés en accès restreint, intégrité vérifiée à la restitution ; armoires verrouillées pour le papier, chiffrement pour les fichiers sensibles.| ◐ | **1** | RGPD (Art. 32) |
| Physiques | A.7.10 Supports de stockage  | Gestion des actifs et classification  | Sécuriser et gérer les supports de stockage.| Interdire l'usage de clés USB non chiffrées pour stocker des données patients. | ○ | **1** | RGPD (Art. 32)|
| Physiques | A.7.13 Maintenance des équipements| Gestion des actifs et classification  | Maintenir les équipements en bon état de fonctionnement.  | Faire maintenir le local technique et l'onduleur des bureaux, la maintenance de l'infrastructure hébergée est contractualisée avec l'hébergeur.  | ○ | **2** | RGPD (Art. 32) |
| Physiques | A.7.14 Élimination sécurisée des équipements | Gestion des actifs et classification  | Effacer les données avant de se débarrasser des équipements. | Fin de vie d'un équipement : commande ATA Secure Erase pour HDD et SSD SATA, effacement NVMe (Format/Sanitize) pour SSD NVMe, destruction de la clé pour disque chiffré dès la première utilisation. À défaut, prestataire de destruction certifié. | ◐ | **1** | RGPD (Art. 32) |
| Technologie | A.8.10 Suppression d'informations | Gestion des actifs et classification | Effacer les données de manière sécurisée. | Procédure de suppression des informations : quoi supprimer (fin de rétention, demande d'effacement, Art. 17 RGPD), quand, avec quelle preuve datée. Sauvegardes immuables (WORM) : suppression effective à l'expiration de leur rétention, contrainte documentée. Effacement des supports : cf. A.7.14. | ○ | **1** | RGPD (Art. 17) |
| - | - | **Gestion des accès et identités (IAM)** | -| -  | - | -  | - |
| Organisationnel | A.5.15 Contrôle d'accès | Gestion des accès et identités (IAM)  | Limiter l'accès aux informations et actifs aux personnes autorisées, conformément à la politique de contrôle d'accès.| Restreindre l'accès aux dossiers patients aux seuls praticiens concernés, avec revue périodique des droits.| ○ | **1** | RGPD (Art. 29, 32), HDS (contrôle d'accès)|
| Organisationnel | A.5.16 Gestion des identités | Gestion des accès et identités (IAM)  | Créer, modifier et supprimer les identités numériques de manière sécurisée.  | Utiliser un annuaire LDAP pour gérer les comptes utilisateurs et leurs droits. | ◐ | **1** | RGPD (Art. 32), HDS (contrôle d'accès)  |
| Organisationnel | A.5.17 Informations d'authentification | Gestion des accès et identités (IAM) | Protéger les informations d'authentification (mots de passe, clés, certificats) contre tout accès non autorisé. | Utiliser des mots de passe robustes (12+ caractères, gestionnaire de mots de passe) et désactiver la rotation périodique automatique sauf en cas de fuite (approche recommandée ANSSI et NIST, d'autres approches existent). Privilégier le MFA pour les accès sensibles que la PME contrôle : plateforme praticiens, accès administrateurs, outils internes. | ◐ | **1** | ANSSI (Reco MFA et mots de passe), CNIL (Reco mots de passe 2022), NIST SP 800-63B, RGPD (Art. 32), NIS2 (Art. 21) |
| Organisationnel | A.5.18 Droits d'accès| Gestion des accès et identités (IAM)  | Accorder des droits minimaux nécessaires (principe du moindre privilège). | L'équipe support accède aux comptes utilisateurs en lecture seule, sans accès aux dossiers patients. | ○ | **1** | RGPD (Art. 29), HDS (contrôle d'accès) |
| Technologie  | A.8.2 Droits d'accès privilégiés  | Gestion des accès et identités (IAM)  | Limiter, valider et journaliser les comptes à privilèges (administration, infrastructure).| Comptes administrateurs nominatifs, accès temporaire pour les actions sensibles, authentification renforcée.| ○ | **1** | RGPD (Art. 32), NIS2 (Art. 21), HDS (contrôle d'accès) |
| Technologie  | A.8.3 Restriction d'accès| Gestion des accès et identités (IAM)  | Limiter l'accès aux informations sensibles. | Configurer des ACL sur les dossiers partagés.  | ○ | **1** | RGPD (Art. 29), HDS (contrôle d'accès)|
| Technologie  | A.8.5 Authentification sécurisée  | Gestion des accès et identités (IAM)  | Choisir des méthodes d'authentification adaptées au risque : multifacteur pour les accès sensibles.| Mot de passe plus second facteur pour les accès aux données de santé, temporisation après échecs. | ◐ | **1** | RGPD (Art. 32), NIS2 (Art. 21), HDS (contrôle d'accès)|
| Technologie  | A.8.18 Utilisation de programmes privilégiés | Gestion des accès et identités (IAM)  | Contrôler l'usage des outils administratifs.| Limiter l'usage de sudo aux administrateurs et journaliser les commandes. | ◐ | **2** | RGPD (Art. 32), HDS (traçabilité des accès)|
| - | - | **Protection des données et échanges**| -| -  | - | -  | - |
| Organisationnel | A.5.14 Transfert d'informations| Protection des données et échanges | Sécuriser les transferts de données (chiffrement, protocoles).| Échanger les données de santé via une API sécurisée (TLS, authentification mutuelle mTLS ou jetons signés type OAuth2, sous contrat avec le partenaire).| ◐ | **1** | RGPD (Art. 32, 44), HDS (chiffrement des données de santé) |
| Technologie  | A.8.11 Masquage des données  | Protection des données et échanges | Masquer les données sensibles dans les environnements non production.  | Remplacer les identifiants patients par des pseudonymes dans les bases de test, la réidentification reste possible : les données restent des données personnelles. | ◐ | **2** | RGPD (Art. 4, 5, 25) |
| Technologie  | A.8.12 Prévention des fuites | Protection des données et échanges | Empêcher les fuites accidentelles ou malveillantes. | Version minimale : inventaire et journalisation des exports de données. Complet : DLP bloquant l'envoi de données patients par e-mail. | ● | **1+** | RGPD (Art. 32)|
| Technologie  | A.8.24 Utilisation de la cryptographie  | Protection des données et échanges | Définir et appliquer le chiffrement des données au repos et en transit, et gérer les clés.| Chiffrement des bases et des sauvegardes, TLS pour les flux, clés stockées à part et accès restreint.| ◐ | **1** | RGPD (Art. 32), NIS2 (Art. 21), HDS (chiffrement des données de santé)|
| Technologie  | A.8.33 Informations de test  | Protection des données et échanges | Protéger les données de test. | Utiliser des données fictives ou anonymisées. Pseudonymisation ≠ anonymisation.| ◐ | **1** | RGPD (Art. 25, 32) |
| - | - | **Maintenance et correctifs** | -| -  | - | -  | - |
| Technologie  | A.8.8 Gestion des vulnérabilités  | Maintenance et correctifs  | Identifier et corriger les vulnérabilités logicielles. | Fixer un délai de correction par criticité (par exemple critique : 30 jours) dans une politique de gestion des correctifs, et le suivre.| ○ | **1** | RGPD (Art. 32), NIS2 (Art. 21)|
| Technologie  | A.8.9 Gestion de la configuration | Maintenance et correctifs  | Maintenir une configuration sécurisée. | Tenir une configuration de référence validée (systèmes durcis, services désactivés par défaut), contrôlée régulièrement. | ○ | **2** | RGPD (Art. 32) |
| Technologie  | A.8.32 Gestion du changement | Maintenance et correctifs  | Contrôler les modifications des systèmes.| Documenter et valider les changements via GitLab ou Jira. | ○ | **2** | NIS2 (Art. 21)  |
| - | - | **Sécurité réseau**| -| -  | - | -  | - |
| Technologie  | A.8.20 Sécurité des réseaux  | Sécurité réseau | Protéger les réseaux contre les intrusions. | Configurer un pare-feu (p.ex. pfSense) pour filtrer le trafic.| ○ | **1** | RGPD (Art. 32), NIS2 (Art. 21)|
| Technologie  | A.8.21 Sécurité des services réseau  | Sécurité réseau | Sécuriser les services exposés.  | Ne pas exposer de services hérités non indispensables (ex. Telnet, FTP) sur les interfaces réseau. | ○ | **2** | NIS2 (Art. 21)  |
| Technologie  | A.8.22 Séparation des réseaux| Sécurité réseau | Isoler les réseaux sensibles. | Créer des VLANs séparés pour les postes, le Wi-Fi invités et l'environnement de démonstration; la production est isolée chez l'hébergeur HDS, selon le périmètre contractuel   | ○ | **2** | NIS2 (Art. 21) |
| Technologie  | A.8.23 Filtrage web  | Sécurité réseau | Bloquer l'accès à des sites malveillants.| Utiliser un proxy avec filtrage URL (p.ex. Squid). | ○ | **2** | RGPD (Art. 32), NIS2 (Art. 21)|
| - | - | **Sécurité des postes** | -| -  | - | -  | - |
| Technologie  | A.8.1 Dispositifs terminaux  | Sécurité des postes| Sécuriser les ordinateurs, tablettes et smartphones.| Installer un antivirus et un pare-feu sur tous les postes de travail.| ◐ | **1** | RGPD (Art. 32) |
| Technologie  | A.8.7 Protection contre les malwares | Sécurité des postes| Protéger contre les virus, ransomwares, etc.| Déployer une solution antivirus centralisée.| ◐ | **1** | RGPD (Art. 32) |
| Technologie  | A.8.19 Installation de logiciels  | Sécurité des postes| Contrôler les installations logicielles. | Bloquer l'installation de logiciels non approuvés via une GPO. | ○ | **1** | RGPD (Art. 32) |
| - | - | **Développement sécurisé** | -| -  | - | -  | - |
| Technologie  | A.8.4 Accès au code source| Développement sécurisé  | Contrôler l'accès au code source.| Utiliser Git avec des droits d'accès différenciés.  | ○ | **2** | RGPD (Art. 32), NIS2 (Art. 21)|
| Technologie  | A.8.25 Cycle de vie du développement sécurisé| Développement sécurisé  | Intégrer la sécurité à toutes les étapes.| Version minimale : revue de code des modifications sensibles (authentification, données de santé, permissions), scan automatisé dans la CI. Complet : revue systématique, exigences, tests, gestion des dépendances. | ● | **2+** | RGPD (Art. 25), NIS2 (Art. 21)|
| Technologie  | A.8.26 Exigences de sécurité des applications| Développement sécurisé  | Définir des exigences de sécurité pour les applications.  | Exiger un chiffrement TLS pour toute application manipulant des données patients. | ◐ | **1** | RGPD (Art. 32), HDS (chiffrement des données de santé)|
| Technologie  | A.8.27 Principes d'architecture sécurisée | Développement sécurisé  | Concevoir des systèmes avec la sécurité en tête.  | Appliquer le principe de défense en profondeur.| ◐ | **2** | RGPD (Art. 25), NIS2 (Art. 21)|
| Technologie  | A.8.28 Codage sécurisé  | Développement sécurisé  | Éviter les vulnérabilités courantes.| Former les développeurs aux bonnes pratiques OWASP. | ◐ | **2** | RGPD (Art. 25), NIS2 (Art. 21)|
| Technologie  | A.8.29 Tests de sécurité| Développement sécurisé  | Tester la sécurité des applications.| Réaliser des pentests avant la mise en production.  | ● | **2** | RGPD (Art. 32), NIS2 (Art. 21)|
| Technologie  | A.8.31 Séparation des environnements | Développement sécurisé  | Isoler les environnements (dev, test, prod).| Version minimale : cloisonnement logique de la production, données fictives en dev/test. Complet : serveurs dédiés pour chaque environnement.| ◐ | **1+** | RGPD (Art. 25)|
| - | - | **Surveillance et journalisation** | -| -  | - | -  | - |
| Technologie  | A.8.6 Gestion des capacités  | Surveillance et journalisation| S'assurer que les systèmes ont les ressources nécessaires.| Surveiller l'utilisation CPU/mémoire des serveurs.  | ○ | **2** | NIS2 (Art. 21)  |
| Technologie | A.8.15 Enregistrement (logs) | Surveillance et journalisation | Conserver des traces des activités pour analyse ou audit. | Démarche progressive : journalisation applicative des accès d'abord (durée de rétention définie et justifiée), centralisation SIEM ensuite. | ◐ | **1** | RGPD (Art. 32), NIS2 (Art. 21), HDS (traçabilité des accès) |
| Technologie  | A.8.16 Activités de surveillance  | Surveillance et journalisation| Surveiller les systèmes pour détecter les anomalies.| Configurer des alertes pour : accès hors plage horaire aux données médicales, requêtes HL7/FHIR anormales, ou échecs répétés d'authentification sur les systèmes critiques. | ◐ | **2** | RGPD (Art. 32), NIS2 (Art. 21)|
| Technologie  | A.8.17 Synchronisation de l'horloge  | Surveillance et journalisation| Synchroniser les horloges pour une traçabilité fiable (horodatage fiable au service de la journalisation). | Utiliser NTP pour synchroniser tous les équipements.| ○ | **1** | RGPD (Art. 32), NIS2 (Art. 21)|
| - | - | **Gestion des incidents**  | -| -  | - | -  | - |
| Organisationnel | A.5.24 Planification de la gestion des incidents| Gestion des incidents| Préparer des procédures, rôles et canaux de signalement avant l'incident. | Plan de réponse aux incidents avec classification et contacts d'astreinte.| ◐ | **1** | RGPD (Art. 33-34), NIS2 (Art. 21, 23) |
| Organisationnel | A.5.25 Évaluation et décision sur les événements de sécurité  | Gestion des incidents| Évaluer chaque événement de sécurité signalé et décider : incident à traiter, événement à surveiller ou faux positif. Décision documentée.| Triage des signalements : un phishing signalé est classé et priorisé selon une grille définie, décision consignée.| ◐ | **1** | RGPD (Art. 33-34), NIS2 (Art. 21)|
| Organisationnel | A.5.26 Réponse aux incidents | Gestion des incidents| Appliquer la procédure : isoler, analyser, corriger, notifier, restaurer. | Isoler le système compromis, notifier l'autorité et le partenaire dans les délais applicables.  | ◐ | **1** | RGPD (Art. 33-34), NIS2 (Art. 21, 23) |
| Organisationnel | A.5.27 Leçons tirées des incidents| Gestion des incidents| Documenter et partager les enseignements tirés des incidents (s'active au premier incident significatif).| Créer un rapport interne avec les causes racines et les actions correctives.| ◐ | **2** | RGPD (Art. 33), NIS2 (Art. 21)|
| Organisationnel | A.5.28 Collecte de preuves| Gestion des incidents| Conserver les traces utiles à l'analyse et aux obligations de notification.  | Sauvegarder les journaux horodatés avant toute remise en état d'un système. | ◐ | **1** | RGPD (Art. 33), NIS2 (Art. 21), HDS (traçabilité des accès) |
| Personnes | A.6.8 Signalement des événements de sécurité | Gestion des incidents| Offrir un canal simple pour signaler tout événement suspect. | Adresse e-mail ou bouton de signalement, sans reproche pour un signalement de bonne foi.  | ◐ | **1** | RGPD (Art. 33), NIS2 (Art. 21, 23)|
| - | - | **Continuité et résilience**  | -| -  | - | -  | - |
| Organisationnel | A.5.29 Sécurité en cas de perturbation  | Continuité et résilience| Préparer des plans pour maintenir la sécurité en cas de crise.| Version minimale : PCA documenté et approuvé (scénarios, rôles, contacts, priorités de reprise). Complet : PCA testé lors d'un exercice daté, puis revu. | ● | **1+** | NIS2 (Art. 21) |
| Organisationnel | A.5.30 Préparation TIC à la continuité  | Continuité et résilience| S'assurer que les systèmes IT critiques peuvent être rétablis rapidement. | Version minimale : RTO/RPO définis pour les systèmes critiques et une restauration testée et datée par an. Complet : restauration complète sur un environnement propre, dans le cadre d'un exercice de crise. La bascule sur infrastructure de secours relève de A.8.14. | ● | **1+** | NIS2 (Art. 21), HDS (sauvegarde externalisée) |
| Technologie  | A.8.13 Sauvegarde des informations| Continuité et résilience| Sauvegarder régulièrement les données critiques.  | Sauvegarde chiffrée quotidienne + test de restauration daté.| ◐ | **1** | RGPD (Art. 32), HDS (sauvegarde externalisée) |
| Technologie  | A.8.14 Redondance des installations  | Continuité et résilience| Assurer la disponibilité des systèmes critiques.  | Redondance des composants critiques chez l'hébergeur, à activer si le RTO contractuel l'exige. | ● | **3** | NIS2 (Art. 21), HDS (disponibilité de l'infrastructure, selon contrat)|
| - | - | **Contrats et conformité** | -| -  | - | -  | - |
| Organisationnel | A.5.19 Sécurité dans les relations avec les fournisseurs| Contrats et conformité  | Définir les exigences de sécurité vis-à-vis des fournisseurs ayant accès aux informations.| Liste des fournisseurs, données accessibles, exigences minimales. | ◐ | **1** | RGPD (Art. 28), NIS2 (Art. 21), HDS (chaîne de sous-traitance) |
| Organisationnel | A.5.20 Sécurité dans les accords avec les fournisseurs  | Contrats et conformité  | Inclure des clauses de sécurité dans chaque contrat fournisseur.  | Contrat avec clauses de confidentialité, notification d'incident et droit d'audit.| ◐ | **1** | RGPD (Art. 28), NIS2 (Art. 21), HDS (chaîne de sous-traitance) |
| Organisationnel | A.5.21 Chaîne d'approvisionnement TIC | Contrats et conformité | Évaluer et surveiller la sécurité des fournisseurs IT. | Version minimale : vérifier chaque année la certification HDS de l'hébergeur (validité, périmètre) et ses sous-traitants. Complet : processus de surveillance des fournisseurs IT (grille, clauses, revue annuelle). | ● | **1+** | RGPD (Art. 28), NIS2 (Art. 21), HDS (chaîne de sous-traitance) |
| Organisationnel | A.5.22 Surveillance des services fournisseurs| Contrats et conformité  | Surveiller les performances et la sécurité des services externalisés.  | Auditer annuellement le fournisseur de sauvegarde pour vérifier la conformité RGPD.  | ◐ | **1** | RGPD (Art. 28), NIS2 (Art. 21)|
| Organisationnel | A.5.23 Sécurité des services cloud| Contrats et conformité  | Encadrer l'usage du cloud : choix du fournisseur, localisation, responsabilités partagées.| Vérifier la certification HDS de l'hébergeur et la localisation des données dans l'UE ou l'EEE. | ◐ | **1** | RGPD (Art. 28, 44), NIS2 (Art. 21), HDS (chaîne de sous-traitance) |
| Organisationnel | A.5.31 Exigences légales et contractuelles| Contrats et conformité  | Respecter les obligations légales (RGPD, HDS, etc.).| Vérifier que les contrats avec les sous-traitants incluent des clauses de confidentialité.| ◐ | **1** | RGPD (Art. 28), HDS (documentation et gouvernance) |
| Organisationnel | A.5.32 Droits de propriété intellectuelle | Contrats et conformité  | Protéger les droits de propriété intellectuelle (logiciels, données).  | S'assurer que les logiciels utilisés sont sous licence valide. | ◐ | **3** | NIS2 (Art. 21)  |
| Organisationnel | A.5.34 Confidentialité et protection des données personnelles | Contrats et conformité  | Respecter les droits des personnes et garantir la confidentialité des données personnelles.  | Registre des traitements à jour, procédure de réponse aux demandes de droits.  | ◐ | **1** | RGPD (Art. 5, 12-22, 30)  |
| Technologie  | A.8.30 Développement externalisé  | Contrats et conformité  | Sécuriser le développement par des tiers.| Inclure des clauses de sécurité dans les contrats.  | ○ | **1** | RGPD (Art. 28), NIS2 (Art. 21)|
| - | - | **Audit** | -| -  | - | -  | - |
| Organisationnel | A.5.35 Examen indépendant| Audit| Faire auditer la sécurité par un tiers indépendant. | Audit de sécurité réalisé par un organisme indépendant (certification, auditeur externe), à un rythme défini.| ● | **3** | NIS2 (Art. 21), HDS (audit de certification, le cas échéant)|
| Technologie  | A.8.34 Protection des systèmes pendant les tests d'audit| Audit| Planifier et encadrer les tests d'audit pour ne pas perturber la production ni exposer des données.| Tests d'audit en accès lecture seule, hors heures de pointe, avec accord préalable du responsable.| ◐ | **2** | RGPD (Art. 32), NIS2 (Art. 21)|
| - | - | **Veille et contacts externes** | -| -  | - | -  | - |
| Organisationnel | A.5.5 Contact avec les autorités  | Veille et contacts externes| Savoir qui contacter (CNIL, ANSSI, autorité sectorielle) et comment.| Fiche des contacts autorités et délais de notification, tenue à jour.| ○ | **1** | RGPD (Art. 33-34), NIS2 (Art. 23)|
| Organisationnel | A.5.6 Contact avec les groupes d'intérêt| Veille et contacts externes| Maintenir un lien avec les communautés et groupes de veille sécurité (sectoriels, CERT nationaux, associations professionnelles).  | Adhésion à un groupe de veille e-santé ou aux alertes d'un CERT. Preuve : liste des adhésions et canaux suivis. | ○ | **2** | NIS2 (Art. 21)  |
| Organisationnel | A.5.7 Renseignements sur les menaces | Veille et contacts externes| Collecter des informations sur les menaces émergentes (cyber, physiques). | Abonnement à des alertes ANSSI ou sectorielle (p.ex. menaces sur les logiciels médicaux).| ○ | **2** | RGPD (Art. 32), NIS2 (Art. 21)|


---

**Glossaire** :
- ACL : Access Control List (liste de contrôle d'accès)
- API : Application Programming Interface (interface de programmation d'application)
- ATA Secure Erase : Commande du micrologiciel du disque (norme ATA/SATA), effaçant les données via le contrôleur du périphérique sans passer par l'OS, s'applique aux HDD et SSD compatibles ATA
- BYOD :  Bring Your Own Device (apportez votre propre équipement personnel de communication) 
- CERT : Computer Emergency Response Team, aussi appelé CSIRT ou Computer Security Incident Response Team
- CI :  Continuous Integration (Intégration continue)
- DLP : Data Loss Prevention (prévention des pertes de données)
- FTP : File Transfer Protocol (Protocole de Transfert de Fichiers)
- GPO : Group Policy Object (objet de stratégie de groupe)
- HDD : Hard Disk Drive (disque dur)
- HL7/FHIR : Fast Healthcare Interoperability Resources (norme internationale de santé du Health Level Seven International(HL7) pour faciliter l'échange électronique de données médicales)
- IAM : Identity and Access Management (gestion des identités et des accès)
- LDAP : Lightweight Directory Access Protocol (protocole léger d'accès à l'annuaire)
- Matrice RACI : Responsible (Réalisateur), Accountable (Approbateur), Consulted (Consulté), Informed (Informé)
- MFA : Multi-Factor Authentication (authentification multifacteur)
- mTLS : Mutual Transport Layer Security (TLS mutuel)
- NDA : Non-Disclosure Agreement (accord de non-divulgation)
- NTP : Network Time Protocol (protocole de temps réseau)
- NVMe : Non-Volatile Memory Express (interface de communication conçue pour accéder aux supports de stockage à mémoire flash via le bus PCI Express d'un ordinateur)
- OWASP : Open Worldwide Application Security Project (Fondation à but non lucratif, communauté internationale ouverte dédiée à l'amélioration de la sécurité des logiciels et des applications web)
- PCA : Plan de Continuité d'Activité
- PSSI : Politique de Sécurité des Systèmes d'Information
- RPO : Recovery Point Objective (Objectif de point de reprise)
- RTO : Recovery Time Objective (Objectif de délai de restauration)
- SIEM : Security Information and Event Management (gestion des informations et des événements de sécurité)
- SoA : Statement of Applicability (Déclaration d'applicabilité)
- SSD : Solid-State Drive (lecteur de stockage sans disque physique)
- TLS : Transport Layer Security (Sécurité de la couche transport)
- VLAN : Virtual Local Area Network (réseau local virtuel)


**Références** :
- ANSSI recommandations MFA : https://messervices.cyber.gouv.fr/guides/recommandations-relatives-lauthentification-multifacteur-et-aux-mots-de-passe
- CNIL recommandations mots de passe : https://www.cnil.fr/fr/mots-de-passe-recommandations-pour-maitriser-sa-securite
- Code de la Santé publique (CSP), Article L. 1111-8 : https://www.legifrance.gouv.fr/codes/section_lc/LEGIARTI000049577902
- Code de la Santé publique, Article R. 1111-8-8 : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036656709
- Code de la Santé publique, Article R. 1111-9 : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053720790
- HDS : 
   - https://esante.gouv.fr/produits-services/hds 
   - https://esante.gouv.fr/sites/default/files/media/document/R%C3%A9f%C3%A9rentiel_certification_HDS%20-%20FR%20-%20V2.1%20-%20post%20concertation.pdf
- HDS v2.1 : https://esante.gouv.fr/actualites/referentiel-hds-v21-les-evolutions-anticiper-des-maintenant
- ISO27001:2022 : https://www.iso.org/fr/standard/27001
- NIS2 : https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=uriserv%3AOJ.L_.2022.333.01.0080.01.FRA&toc=OJ%3AL%3A2022%3A333%3ATOC
- NIST SP 800-63B : https://pages.nist.gov/800-63-3/sp800-63b.html
- ReCyF (document travail ANSSI NIS2) : https://cyber.gouv.fr/reglementation/cybersecurite-systemes-dinformation/directives-nis-nis2-et-dispositif-saiv/directive-nis-2/
- RGPD : https://www.cnil.fr/fr/reglement-europeen-protection-donnees
_Dernière vérification des références réglementaires : 28/10/2026_

---

## Changelog

- Version 2.0 : 29/10/2026 (présentation par sous-catégorie et requalification des sous-catégories, priorisation divisée en effort et phase)   
_Note HDS : partage de responsabilités reformulé en questions de qualification, suivi du référentiel v2.1 à traiter en V2.1 du document_
- Version 1.1 : 13/10/2026 (Liste complétée à 93 contrôles)  
- V1.0 : 05/06/2026 (68 contrôles).

Version 2.0, date : 29/10/2026.
Les numéros et intitulés de contrôles (Annexe A, ISO 27001:2022) sont cités (abrégés ou paraphrasés) dans ce document à titre de référence uniquement, tous droits réservés ISO. Texte officiel de la norme disponible auprès de l'ISO ou de l'AFNOR.
Le reste du contenu (commentaires, exemples, priorisations, sous-catégories et structure) est mis à disposition sous licence CC BY 4.0, attribution : Solène Figueiredo, projet grc-pme-fictive.

