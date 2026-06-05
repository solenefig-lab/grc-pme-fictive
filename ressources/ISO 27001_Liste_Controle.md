# ISO 27001:2022 – Contrôles regroupés par sous-catégorie pour les PME e-santé

> Alignement HDS/RGPD/NIS2 et priorisation pratique.  
> Ce document est une entrée, pas un audit. Il est conçu pour donner une vision claire aux responsables de PME sans expertise juridique des contrôles ISO 27001:2022, des informations concernées et des actions prioritaires à mener.

## **Objectif**
Ce tableau a pour but de **simplifier l’application de l’ISO 27001:2022** pour les PME du secteur e-santé, en :
- **Regroupant les contrôles par sous-catégorie** (ex: Gouvernance, Sensibilisation, Sauvegardes) pour une approche thématique.
- **Priorisant les actions** selon leur **coût, complexité et impact** (🟢 Basique / 🟡 Intermédiaire / 🔴 Avancé).
- **Alignant chaque contrôle** avec les exigences **HDS (Hébergement de Données de Santé), RGPD, et NIS2** pour éviter les redondances et maximiser l’efficacité.

---

## **Méthodologie**
1. **Classement par sous-catégorie** :
   Inspiré de la structure de [SantéConnect](https://github.com/solenefig-lab/grc-pme-fictive/tree/main/semaine-3-iso27001), avec des sous-catégories **métiers** (ex: "Contrats et conformité", "Sauvegardes et continuité").

2. **Priorisation** :
   - **🟢 Basique** : Contrôles **peu coûteux, rapides à implémenter**, et à fort impact (ex: A.5.10 Utilisation acceptable, A.7.7 Bureau dégagé).
   - **🟡 Intermédiaire** : Contrôles nécessitant des **ressources modérées** (ex: A.8.8 Gestion des vulnérabilités, A.12.4 Enregistrement des logs).
   - **🔴 Avancé** : Contrôles **complexes ou coûteux** (ex: A.8.12 Prévention des fuites de données, A.8.25 Cycle de vie du développement sécurisé), souvent réservés aux PME matures ou en phase 2.

3. **Alignement réglementaire** :
   - **HDS** : Contrôles liés à la **sécurité des données de santé** (ex: A.8.13 Sauvegarde, A.9.1 Contrôle d’accès).
   - **RGPD** : Contrôles liés à la **protection des données personnelles** (ex: A.5.13 Étiquetage des informations, A.8.10 Suppression d’informations).
   - **NIS2** : Contrôles liés à la **résilience et la cybersécurité critique** (ex: A.5.29 Sécurité en cas de perturbation, A.8.16 Surveillance).

4. **Exemples concrets** :
   Chaque contrôle est illustré par un **cas d’usage e-santé/PME** pour faciliter l’appropriation.

---
## **Utilisation recommandée**
- **Phase 1** : Commencer par les contrôles **🟢** pour couvrir 80% des risques avec 20% d’effort.
- **Phase 2** : Ajouter les contrôles **🟡** en fonction des ressources disponibles.
- **Phase 3** : Implémenter les contrôles **🔴** pour une conformité complète (ex: pour une certification HDS).

Ce tableau est également disponible en format CSV pour permettre filtrage et tri (p.ex. par sous-catégorie): [Liste Contrôles ISO 27001:2022](./ISO27001_Liste-Controle.csv)

___


| Thème | Contrôle | Sous-catégorie | Courte explication | Court exemple | Priorité PME | Liens HDS/RGPD/NIS2 |
| --- | --- | --- | --- | --- | --- | --- |
| Organisationnel | A.5.3 Séparation des tâches | Gouvernance et rôles | Éviter les conflits d’intérêts ou les erreurs en séparant les responsabilités critiques. | Dans un cabinet médical, la personne qui valide les prescriptions ne gère pas les paiements. | 🟢 | RGPD (Art. 32), HDS (exigence organisationnelle) |
| Organisationnel | A.5.6 Contact avec les groupes d’intérêt | Communication | Maintenir un dialogue avec les parties prenantes (clients, régulateurs, etc.). | Organiser des réunions trimestrielles avec les patients pour recueillir leurs retours sur la sécurité des données. | 🟡 | RGPD (Art. 12-14), HDS (transparence) |
| Organisationnel | A.5.7 Renseignements sur les menaces | Veille stratégique | Collecter des informations sur les menaces émergentes (cyber, physiques). | Abonnement à des alertes ANSSI ou sectorielle (ex: menaces sur les logiciels médicaux). | 🟡 | NIS2 (Art. 21), RGPD (Art. 32) |
| Organisationnel | A.5.8 Sécurité dans la gestion de projet | Gestion de projet | Intégrer la sécurité dès la phase de conception des projets. | Inclure une analyse de risques cyber dans le cahier des charges d’un nouveau logiciel de dossier patient. | 🟡 | HDS (exigence de sécurité par défaut) |
| Organisationnel | A.5.9 Inventaire des informations | Gestion des actifs | Identifier et classer les informations sensibles. | Lister tous les fichiers contenant des données de santé (DMP, comptes-rendus) et leur niveau de sensibilité. | 🟢 | RGPD (Art. 30), HDS (inventaire des données) |
| Organisationnel | A.5.10 Utilisation acceptable | Politiques | Définir des règles claires sur l’usage des ressources (IT, données). | Charte informatique interdisant l’usage de clés USB personnelles pour transférer des données patients. | 🟢 | RGPD (Art. 28-29), HDS (bonnes pratiques) |
| Organisationnel | A.5.11 Retour des actifs | Gestion des actifs | S’assurer que les actifs (clés, badges, équipements) sont retournés en fin de contrat. | Récupérer les badges d’accès et les ordinateurs portables des employés partants. | 🟢 | RGPD (Art. 32), HDS (gestion des accès) |
| Organisationnel | A.5.13 Étiquetage des informations | Classification | Classer et étiqueter les informations selon leur sensibilité. | Marquer les dossiers patients avec des étiquettes "Confidentiel – RGPD". | 🟢 | RGPD (Art. 32), HDS (classification des données) |
| Organisationnel | A.5.14 Transfert d’informations | Sécurité des échanges | Sécuriser les transferts de données (chiffrement, protocoles). | Utiliser un VPN ou un outil chiffré (ex: Signal) pour envoyer des données médicales à un partenaire. | 🟡 | RGPD (Art. 32, 44), HDS (chiffrement) |
| Organisationnel | A.5.15 Contrôle d’accès | Gestion des accès | Limiter l’accès aux informations aux personnes autorisées. | Restreindre l’accès aux dossiers patients aux seuls médecins et infirmiers concernés. | 🟢 | RGPD (Art. 29, 32), HDS (contrôle d’accès strict) |
| Organisationnel | A.5.16 Gestion des identités | IAM | Créer, modifier et supprimer les identités numériques de manière sécurisée. | Utiliser un annuaire LDAP pour gérer les comptes utilisateurs et leurs droits. | 🟡 | RGPD (Art. 32), HDS (IAM) |
| Organisationnel | A.5.17 Informations d’authentification | IAM | Protéger les informations d’authentification (mots de passe, clés, certificats) contre les accès non autorisés, avec une rotation uniquement en cas de compromission avérée (recommandation NIST/ANSSI). | Utiliser des mots de passe robustes (12+ caractères, gestionnaire de mots de passe) et désactiver la rotation périodique automatique sauf en cas de fuite. Privilégier le MFA pour les accès sensibles (ex: DMP, PMS). | 🟢 |ANSSI (Reco MFA et mots de passe), CNIL (Reco mots de passe 2022), RGPD (Art. 32) |
| Organisationnel | A.5.18 Droits d’accès | IAM | Accorder des droits minimaux nécessaires (principe du moindre privilège). | Donner un accès en lecture seule aux secrétaires pour les dossiers patients. | 🟢 | RGPD (Art. 29), HDS (moindre privilège) |
| Organisationnel | A.5.21 Chaîne d’approvisionnement TIC | Contrats et conformité | Évaluer et surveiller la sécurité des fournisseurs IT. | Pour PME avec hébergeur HDS certifié : Vérifier annuellement la certification et auditer les sous-traitants (ex: sauvegarde). Pour une PME non certifiée (priorité haute) : Choisir un hébergeur HDS et auditer la chaîne complète. | 🟡 | HDS (exigence), NIS2 (Art. 21) |
| Organisationnel | A.5.22 Surveillance des services fournisseurs | Contrats et conformité | Surveiller les performances et la sécurité des services externalisés. | Auditer annuellement le fournisseur de sauvegarde pour vérifier la conformité RGPD. | 🟡 | RGPD (Art. 28), NIS2 (Art. 21) |
| Organisationnel | A.5.25 Évaluation des événements de sécurité | Gestion des incidents | Analyser les incidents pour en tirer des enseignements. | Après une tentative de phishing, organiser une rétrospective pour identifier les failles. | 🟡 | NIS2 (Art. 20), RGPD (Art. 33-34) |
| Organisationnel | A.5.27 Leçons tirées des incidents | Gestion des incidents | Documenter et partager les enseignements tirés des incidents. | Créer un rapport interne avec les causes racines et les actions correctives. | 🟡 | NIS2 (Art. 20), RGPD (Art. 33) |
| Organisationnel | A.5.29 Sécurité en cas de perturbation | Résilience | Préparer des plans pour maintenir la sécurité en cas de crise. | Avoir un plan de continuité d’activité (PCA) pour les pannes électriques ou cyberattaques. | 🔴 | NIS2 (Art. 21), HDS (résilience) |
| Organisationnel | A.5.30 Préparation TIC à la continuité | Sauvegardes et continuité | S’assurer que les systèmes IT critiques peuvent être rétablis rapidement. | Sauvegarder quotidiennement les bases de données patients sur un site distant. | 🔴 | HDS (exigence), NIS2 (Art. 21) |
| Organisationnel | A.5.31 Exigences légales et contractuelles | Contrats et conformité | Respecter les obligations légales (RGPD, HDS, etc.). | Vérifier que les contrats avec les sous-traitants incluent des clauses de confidentialité. | 🟢 | RGPD (Art. 28), HDS (exigence légale) |
| Organisationnel | A.5.32 Droits de propriété intellectuelle | Conformité | Protéger les droits de propriété intellectuelle (logiciels, données). | S’assurer que les logiciels utilisés sont sous licence valide. | 🟡 | RGPD (Art. 30), NIS2 (Art. 21) |
| Organisationnel | A.5.33 Protection des documents | Gestion des actifs | Protéger les documents physiques et numériques contre les accès non autorisés. | Verrouiller les armoires contenant des dossiers papier et chiffrer les fichiers sensibles. | 🟢 | RGPD (Art. 32), HDS (protection physique) |
| Organisationnel | A.5.35 Examen indépendant | Audit | Faire auditer la sécurité par un tiers indépendant. | Faire réaliser un audit ISO 27001 par un organisme certifié tous les 3 ans. | 🔴 | HDS (audit obligatoire), NIS2 (Art. 21) |
| Organisationnel | A.5.36 Conformité aux politiques | Gouvernance | Vérifier que les politiques de sécurité sont respectées. | Organiser des audits internes pour vérifier l’application de la charte informatique. | 🟡 | RGPD (Art. 24), HDS (conformité) |
| Organisationnel | A.5.37 Procédures opérationnelles documentées | Gouvernance | Documenter les procédures critiques pour assurer la traçabilité. | Rédiger une procédure pour la gestion des mots de passe ou des sauvegardes. | 🟢 | RGPD (Art. 30), HDS (documentation) |
| Personnes | A.6.3 Sensibilisation et formation | Sensibilisation et formation | Former les employés aux bonnes pratiques de sécurité. | Organiser une formation annuelle sur la cybersécurité avec des cas pratiques (ex: phishing). | 🟢 | RGPD (Art. 39), HDS (formation obligatoire) |
| Personnes | A.6.7 Télétravail | Sécurité physique et logique | Sécuriser les accès à distance. | Imposer l’usage d’un VPN et d’un ordinateur dédié (pas de BYOD) pour le télétravail. | 🟡 | RGPD (Art. 32), NIS2 (Art. 21) |
| Physiques | A.7.3 Sécurisation des locaux | Sécurité physique | Protéger les bureaux et installations contre les intrusions. | Installer des serrures électroniques et des caméras dans les salles serveurs. | 🟢 | HDS (exigence physique), RGPD (Art. 32) |
| Physiques | A.7.4 Surveillance physique | Sécurité physique | Surveiller les accès aux zones sensibles. | Journaliser les entrées/sorties des salles contenant des équipements critiques. | 🟡 | HDS (surveillance), NIS2 (Art. 21) |
| Physiques | A.7.5 Protection contre les menaces physiques | Sécurité physique | Protéger contre les risques (incendie, inondation, etc.). | Installer des détecteurs de fumée et des extincteurs près des serveurs. | 🟢 | HDS (exigence), RGPD (Art. 32) |
| Physiques | A.7.6 Travail en zones sécurisées | Sécurité physique | Limiter l’accès aux zones sensibles aux personnes autorisées. | Réserver l’accès à la salle serveurs aux administrateurs IT. | 🟢 | HDS (accès restreint), RGPD (Art. 32) |
| Physiques | A.7.7 Bureau dégagé et écran propre | Sécurité physique | Éviter les fuites d’informations via des documents visibles. | Imposer de verrouiller les écrans en cas d’absence et de ranger les documents sensibles. | 🟢 | RGPD (Art. 32), HDS (bonnes pratiques) |
| Physiques | A.7.8 Implantation des équipements | Sécurité physique | Placer les équipements de manière sécurisée. | Installer les serveurs dans une salle climatisée et sécurisée. | 🟢 | HDS (exigence physique) |
| Physiques | A.7.9 Sécurité des actifs hors site | Sécurité physique | Protéger les équipements en déplacement. | Chiffrer les disques durs des ordinateurs portables et activer le verrouillage automatique. | 🟡 | RGPD (Art. 32), HDS (chiffrement) |
| Physiques | A.7.10 Supports de stockage | Gestion des actifs | Sécuriser et gérer les supports de stockage. | Interdire l’usage de clés USB non chiffrées pour stocker des données patients. | 🟢 | RGPD (Art. 32), HDS (stockage sécurisé) |
| Physiques | A.7.12 Sécurité du câblage | Sécurité physique | Protéger les câbles réseau contre les interceptations ou dommages. | Faire passer les câbles dans des gaines sécurisées. | 🟡 | HDS (exigence physique), NIS2 (Art. 21) |
| Physiques | A.7.13 Maintenance des équipements | Gestion des actifs | Maintenir les équipements en bon état de fonctionnement. | Planifier une maintenance préventive des onduleurs et climatiseurs. | 🟡 | HDS (maintenance), RGPD (Art. 32) |
| Physiques | A.7.14 Élimination sécurisée des équipements | Gestion des actifs | Effacer les données avant de se débarrasser des équipements. | Utiliser un logiciel d’effacement sécurisé (ex: DBAN) avant de recycler un ordinateur. | 🟢 | RGPD (Art. 32), HDS (destruction sécurisée) |
| Technologie | A.8.1 Dispositifs terminaux | Sécurité des postes | Sécuriser les ordinateurs, tablettes et smartphones. | Installer un antivirus et un pare-feu sur tous les postes de travail. | 🟢 | RGPD (Art. 32), HDS (sécurité des postes) |
| Technologie | A.8.3 Restriction d’accès | Gestion des accès | Limiter l’accès aux informations sensibles. | Configurer des ACL sur les dossiers partagés. | 🟢 | RGPD (Art. 29), HDS (contrôle d’accès) |
| Technologie | A.8.4 Accès au code source | Développement sécurisé | Contrôler l’accès au code source. | Utiliser Git avec des droits d’accès différenciés. | 🟡 | RGPD (Art. 32), NIS2 (Art. 21) |
| Technologie | A.8.6 Gestion des capacités | Performance et sécurité | S’assurer que les systèmes ont les ressources nécessaires. | Surveiller l’utilisation CPU/mémoire des serveurs. | 🟡 | NIS2 (Art. 21) |
| Technologie | A.8.7 Protection contre les malwares | Sécurité des postes | Protéger contre les virus, ransomwares, etc. | Déployer une solution antivirus centralisée. | 🟢 | RGPD (Art. 32), HDS (antivirus obligatoire) |
| Technologie | A.8.8 Gestion des vulnérabilités | Maintenance et correctifs | Identifier et corriger les vulnérabilités logicielles. | Appliquer les correctifs de sécurité sous 30 jours. | 🟢 | RGPD (Art. 32), NIS2 (Art. 21) |
| Technologie | A.8.9 Gestion de la configuration | Sécurité des systèmes | Maintenir une configuration sécurisée. | Désactiver les services inutiles (ex: Telnet, FTP). | 🟡 | RGPD (Art. 32), HDS (durcissement) |
| Technologie | A.8.10 Suppression d’informations | Gestion des données | Effacer les données de manière sécurisée. | Utiliser shred (Linux) pour supprimer définitivement des fichiers. | 🟢 | RGPD (Art. 17), HDS (destruction) |
| Technologie | A.8.11 Masquage des données | Protection des données | Masquer les données sensibles dans les environnements non production. | Remplacer les noms de patients par des pseudonymes dans les bases de test. | 🟡 | RGPD (Art. 25), HDS (anonymisation) |
| Technologie | A.8.12 Prévention des fuites | Protection des données | Empêcher les fuites accidentelles ou malveillantes. | Configurer des DLP pour bloquer l’envoi de données patients par email. | 🔴 | RGPD (Art. 32), HDS (exigence) |
| Technologie | A.8.13 Sauvegarde des informations | Sauvegardes et continuité | Sauvegarder régulièrement les données critiques. | Sauvegarder les bases de données patients quotidiennement. | 🟢 | HDS (exigence), RGPD (Art. 32) |
| Technologie | A.8.14 Redondance des installations | Sauvegardes et continuité | Assurer la disponibilité des systèmes critiques. | Avoir un serveur de secours prêt à prendre le relais. | 🔴 | HDS (exigence), NIS2 (Art. 21) |
| Technologie | A.8.15 Enregistrement (logs) | Surveillance | Conserver des traces des activités pour analyse ou audit. | Centraliser les logs des accès aux dossiers patients dans un SIEM. | 🟡 | RGPD (Art. 30), NIS2 (Art. 21) |
| Technologie | A.8.16 Activités de surveillance | Surveillance | Surveiller les systèmes pour détecter les anomalies. | Configurer des alertes pour : accès hors plage horaire aux données médicales, requêtes HL7/FHIR anormales, ou échecs répétés d’authentification sur les systèmes critiques (ex: PMS, LIS). | 🟡 | NIS2 (Art. 21), RGPD (Art. 32) |
| Technologie | A.8.17 Synchronisation de l’horloge | Sécurité des systèmes | Synchroniser les horloges pour une traçabilité fiable. | Utiliser NTP pour synchroniser tous les équipements. | 🟢 | RGPD (Art. 30), NIS2 (Art. 21) |
| Technologie | A.8.18 Utilisation de programmes privilégiés | IAM | Contrôler l’usage des outils administratifs. | Limiter l’usage de sudo aux administrateurs et journaliser les commandes. | 🟡 | RGPD (Art. 32), HDS (traçabilité) |
| Technologie | A.8.19 Installation de logiciels | Sécurité des postes | Contrôler les installations logicielles. | Bloquer l’installation de logiciels non approuvés via une GPO. | 🟢 | RGPD (Art. 32), HDS (contrôle des logiciels) |
| Technologie | A.8.20 Sécurité des réseaux | Sécurité réseau | Protéger les réseaux contre les intrusions. | Configurer un pare-feu (ex: pfSense) pour filtrer le trafic. | 🟢 | RGPD (Art. 32), NIS2 (Art. 21) |
| Technologie | A.8.21 Sécurité des services réseau | Sécurité réseau | Sécuriser les services exposés. | Désactiver les services réseau inutiles. | 🟡 | NIS2 (Art. 21) |
| Technologie | A.8.22 Séparation des réseaux | Sécurité réseau | Isoler les réseaux sensibles. | Créer des VLANs séparés pour les équipements médicaux et administratifs. | 🟡 | HDS (exigence), NIS2 (Art. 21) |
| Technologie | A.8.23 Filtrage web | Sécurité réseau | Bloquer l’accès à des sites malveillants. | Utiliser un proxy avec filtrage URL (ex: Squid). | 🟡 | RGPD (Art. 32), NIS2 (Art. 21) |
| Technologie | A.8.25 Cycle de vie du développement sécurisé | Développement sécurisé | Intégrer la sécurité à toutes les étapes. | Inclure des revues de code et des tests OWASP ZAP. | 🔴 | RGPD (Art. 25), NIS2 (Art. 21) |
| Technologie | A.8.26 Exigences de sécurité des applications | Développement sécurisé | Définir des exigences de sécurité pour les applications. | Exiger un chiffrement TLS pour toute application manipulant des données patients. | 🟡 | RGPD (Art. 32), HDS (chiffrement) |
| Technologie | A.8.27 Principes d’architecture sécurisée | Développement sécurisé | Concevoir des systèmes avec la sécurité en tête. | Appliquer le principe de défense en profondeur. | 🔴 | RGPD (Art. 25), NIS2 (Art. 21) |
| Technologie | A.8.28 Codage sécurisé | Développement sécurisé | Éviter les vulnérabilités courantes. | Former les développeurs aux bonnes pratiques OWASP. | 🔴 | RGPD (Art. 25), NIS2 (Art. 21) |
| Technologie | A.8.29 Tests de sécurité | Développement sécurisé | Tester la sécurité des applications. | Réaliser des pentests avant la mise en production. | 🔴 | RGPD (Art. 32), NIS2 (Art. 21) |
| Technologie | A.8.30 Développement externalisé | Développement sécurisé | Sécuriser le développement par des tiers. | Inclure des clauses de sécurité dans les contrats. | 🔴 | RGPD (Art. 28), NIS2 (Art. 21) |
| Technologie | A.8.31 Séparation des environnements | Développement sécurisé | Isoler les environnements (dev, test, prod). | Utiliser des serveurs dédiés pour chaque environnement. | 🟡 | RGPD (Art. 25), HDS (exigence) |
| Technologie | A.8.32 Gestion du changement | Maintenance et correctifs | Contrôler les modifications des systèmes. | Documenter et valider les changements via GitLab ou Jira. | 🟡 | RGPD (Art. 30), NIS2 (Art. 21) |
| Technologie | A.8.33 Informations de test | Développement sécurisé | Protéger les données de test. | Utiliser des données fictives ou anonymisées. | 🟢 | RGPD (Art. 25), HDS (anonymisation) |