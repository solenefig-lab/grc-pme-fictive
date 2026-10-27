# README - Audit RBAC simplifié

> Document réalisé dans le cadre du projet portfolio GRC - [grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive).
> Ce projet est un démonstrateur pédagogique illustrant des contrôles IAM/RBAC. Il ne constitue pas un outil d'audit exhaustif et ne se substitue pas à une évaluation de sécurité réalisée dans un contexte opérationnel.

_Notes : les données des jeux (noms, rôles, ressources, identifiants RBAC-xx)_
_sont fictives et propres à cette ressource. Elles s'inspirent du projet_
_pédagogique SantéConnect, dont elles divergent volontairement : classifications_
_et paramètres MFA propres au démonstrateur, identifiants indépendants des_
_autres livrables du dépôt._

---

## **Sommaire**

1. [Objectif](#objectif)
2. [Périmètre](#périmètre)
3. [Structure des fichiers](#structure-des-fichiers)
4. [Utilisation](#utilisation)
5. [Jeux de données](#jeux-de-données)
6. [Dépendances](#dépendances)
7. [Contrôles implémentés](#contrôles-implémentés)
8. [Hiérarchie et sévérité des contrôles](#hiérarchie-et-sévérité-des-contrôles)
9. [Modifier les règles](#modifier-les-règles)
10. [Ajouter un nouveau contrôle](#ajouter-un-nouveau-contrôle)
11. [Planification](#planification)
12. [Référentiel utilisateurs](#référentiel-utilisateurs)
13. [Rapport généré](#rapport-généré)
14. [Exemples de sorties](#exemples-de-sorties)
15. [Protocole de test](#protocole-de-test)
16. [Intégration SIEM (perspective)](#intégration-siem-perspective)
17. [Changelog](#changelog)

--- 

## Objectif

Ce script réalise un audit automatisé des accès à partir :

* d'une matrice RBAC (`MatriceRBAC.csv`),
* d'un référentiel minimal d'identités (`users.csv`),
* d'un journal des accès (`user_access_log.csv`).

Pour chaque accès, des contrôles indépendants sont exécutés. Les anomalies détectées sont consolidées dans un rapport CSV horodaté généré à chaque
exécution, y compris sans anomalie (preuve d'exécution).

---

## Périmètre

Ce script est un **contrôle détectif** : il analyse *a posteriori* des
journaux d'accès déjà collectés.

Il ne remplace pas :
* la **revue d'habilitations** : vérifier que les droits *attribués* sont
  toujours nécessaires (moindre privilège), les données d'entrée ne sont
  pas les mêmes (matrice des droits accordés vs journal des accès
  réalisés),
* un outil d'analyse comportementale temps réel.

Cadence possible pour une PME : **hebdomadaire**. Un journal d'accès
hebdomadaire reste lisible et exploitable par un RSSI à temps partagé,
une exécution plus fréquente ne raccourcit pas la réaction si personne
n'ouvre le rapport.

---

## Structure des fichiers

```
audit_RBAC_auto/
├── README.md                         # ce document
├── rbac_audit.py                     # script d'audit
├── MatriceRBAC.csv                   # source de vérité des rôles (20 règles)
├── users.csv                         # référentiel minimal d'identités
├── user_access_log.csv               # jeu de démonstration (accès conformes + écarts volontaires)
├── user_access_log_nominal.csv       # jeu conforme (sortie 0 anomalie attendue)
├── user_access_log_negatif.csv       # suite de tests (1 entrée par type de contrôle, sortie 13 lignes, 14 anomalies attendues)
├── .gitignore                        # sorties d'exécution non versionnées
├── .gitattributes                    # fins de ligne normalisées (LF)
└── exemples/                         # sorties curatées, reproductibles
  ├── rapport_exemple_jeu_demo.csv
  ├── rapport_exemple_jeu_nominal.csv
  └── rapport_exemple_jeu_negatif.csv
```

Les rapports d'anomalies générés à l'exécution
(`YYYYMMDD_HHMMSS_rapport_anomalies.csv`) restent à la racine, non
versionnés : `.gitignore` les exclut, de même que `__pycache__/`.
Seuls des exemples curatés, sans timestamp, sont versionnés dans
`exemples/`.

`.gitignore` et `.gitattributes` sont des fichiers du dépôt : ils sont
**clonés avec la ressource et actifs dès le clone**, aucune commande
n'est nécessaire pour les activer. 
Le premier exclut les sorties d'exécution des commits, le second normalise les fins de ligne en LF :
git gère la conversion automatiquement, un contributeur sous Windows
n'a rien à faire. Fichiers cachés (préfixe `.`) : pour les voir après
clonage : `ls -a`.

---

## Utilisation

Placer `MatriceRBAC.csv`, `users.csv` et `user_access_log.csv` dans le même
répertoire que le script, puis :

```bash
python3 rbac_audit.py
```

**Comportement en cas d'erreur de chargement (politique uniforme) :**

- **structure du fichier** → arrêt immédiat, code de sortie `1`, **aucun
  rapport** (*fail-closed* : un rapport issu de données incomplètes ou
  ambiguës serait trompeur). 
    - Sont concernés : 
      - fichier absent ou illisible, en-tête invalide (journal, référentiel ou **matrice**), 
      - nombre de colonnes incorrectes, 
      - jeton de permission hors vocabulaire, 
      - valeur MFA de la matrice hors vocabulaire (O/N), 
      - **règle dupliquée** dans la matrice (même Rôle/Ressources), 
      - **utilisateur dupliqué** dans le référentiel, 
      - statut hors vocabulaire, 
      - rôle d'un compte actif absent de la matrice, 
      - **journal vide** (aucune entrée, un rapport « tout vert » sans matière analysée ne prouve rien),
      - **matrice RBAC vide** (aucune règle exploitable),
      - **référentiel IAM vide** (aucune identité de référence, chaque accès serait signalé `UnknownUser`, masquant les violations réelles). 
- **valeur d'un champ du journal** (MFA, horodatage, action hors vocabulaire) : anomalie dédiée et poursuite de l'audit.   
  - le journal est la matière auditée, pas une configuration à rejeter.

En exécution planifiée (cron, CI), le code de sortie non nul permet d'alerter sur l'échec du job.

---

## Jeux de données

Trois jeux sont fournis, trois rôles distincts :  
- le **jeu nominal** prouve l'absence de faux positifs (0 anomalie sur des accès conformes),  
- le **jeu négatif** prouve la couverture des détections (un cas par type de contrôle, plus les cas d'anomalies multiples + test de non-régression : si une évolution du script casse une détection, ce jeu la révèle),  
- le **jeu de démonstration** montre un journal réaliste (majorité d'accès conformes, quelques écarts).
  
| Fichier | `wc -l` (en-tête compris) | Anomalies attendues | `grep -c -E "OVH\|write"` |
|---|---|---|---|
| `user_access_log.csv` | 6 | 3 | 3 |
| `user_access_log_nominal.csv` | 6 | 0 | 0 |
| `user_access_log_negatif.csv` | 14 | 14 | 3 |

Le compte de lignes et le comptage discriminent ensemble les trois
jeux. Le script lit toujours user_access_log.csv : pour auditer un autre
jeu, copier son contenu dans ce fichier (copie de travail locale),
exécuter, puis restaurer le jeu de démonstration.

Le jeu négatif couvre les 9 types de contrôle, dont un compte inactif
volontaire (`USR011`, dé-provisionnement normal), un **accès un jour non ouvré** (la branche jours ouvrés est couverte en non-régression) et une
ligne produisant **deux** anomalies (accès explicitement interdit **et**
valeur MFA invalide : le niveau critical ne peut pas être masqué par un
défaut de qualité de log). 
Les lignes d'action et d'horodatage hors
vocabulaire produisent une anomalie `MalformedValue` chacune, l'audit
continue. Le cas « valeur MFA invalide sur accès sans règle » (deux
anomalies) n'est **pas** dans le jeu : il figure dans la table des cas
du [Protocole de test](#protocole-de-test).

Avant tout test, vérifier la baseline du jeu chargé :

```bash
wc -l user_access_log.csv && grep -c -E "OVH|write" user_access_log.csv
```
_`grep -c` sort en code `1` sur comptage nul, comportement POSIX, valable dans tous les shells. Ne pas l'enchaîner avec `&&`. (Autre piège, propre à zsh cette fois : un joker sans correspondance fait échouer la commande, cf. [Protocole de test](#protocole-de-test).)_

---

## Dépendances

Le script n'utilise que la bibliothèque standard Python :  

```
csv
datetime
unicodedata
```

Annotations `dict | None` : Python 3.10 minimum. Testé avec Python 3.11 et 3.14.

---

## Contrôles implémentés

Chaque contrôle produit ses propres anomalies. 
En cas d'anomalie d'identité (contrôle 1), les contrôles suivants ne sont pas exécutés pour cette entrée (cf. Hiérarchie et sévérité).

### Contrôle 1 - Cohérence utilisateur / rôle : check_user_role()

Vérifie, dans cet ordre (le premier échec court-circuite les contrôles suivants pour cette entrée) :

* utilisateur connu (UnknownUser),  
* compte actif (InactiveAccount),  
* rôle déclaré strictement conforme au référentiel (RoleMismatch).

### Contrôle 2 - Conformité RBAC : check_access_compliance()

Retourne la liste des anomalies d'une entrée (0 à 3 : au plus
une anomalie d'action, une de valeur MFA, un résultat RBAC) :

* action hors vocabulaire → `MalformedValue` (permissions non évaluables),
* valeur `mfa_enabled` invalide → `MalformedValue`, validée **avant la
  recherche de règle** (contrôle de qualité de la donnée : il ne dépend
  pas de l'existence d'une règle),
* règle RBAC inexistante → `NoMatchingRule` (retour immédiat : la
  conformité MFA exige une règle),
* refus explicite → `ExplicitDeny`,
* permissions → `PermissionViolation`,
* MFA requis non activé → `MFA` (évalué seulement si la valeur est valide
  et la règle existe).


### Contrôle 3 - Horaires d'accès : check_business_hours()

Détecte les accès hors **jours ouvrés** et hors **horaires**, le message
d'anomalie distingue le jour non ouvré du hors-horaires.  
Les rôles exemptés (usage légitime à toute heure : patients, praticiens, partenaires, comptes de service 24/7 - cf. `HOUR_EXEMPT_ROLES`) ne sont pas contrôlés,
un rôle exempté absent de la matrice génère un avertissement au démarrage (une exemption qui ne s'applique jamais ne doit pas être silencieuse).  
Un horodatage invalide produit une anomalie MalformedValue.  

Fuseau horaire : l'horodatage est supposé en heure locale du site.  
Un journal d'hébergeur en UTC doit être converti en amont (gouvernance des journaux), le script ne devine pas les fuseaux.  

Les horaires sont configurables :

```python
BUSINESS_OPEN = "08:00"
BUSINESS_CLOSE = "18:00"
```

---

## Hiérarchie et sévérité des contrôles

**Ordre d'évaluation et court-circuit :**

1. Contrôle utilisateur : une anomalie (`UnknownUser`, `InactiveAccount`, `RoleMismatch`) interrompt l'évaluation de l'entrée, l'identité faisant défaut, la conformité RBAC n'aurait pas de sens.  
2. Conformité RBAC : 0, 1, 2 ou 3 anomalies par entrée (la conformité RBAC et la qualité des valeurs du journal sont indépendants).  
3. Fenêtre d'accès : s'exécute après, indépendamment du résultat RBAC.


**Tableau sévérité × type de contrôle**, validé par le jeu négatif (14 anomalies, une attribution par type) :

| Type | Sévérité | Lecture |
| --- | --- | --- |
| `ExplicitDeny` | critical | accès interdit explicitement par la politique |
| `NoMatchingRule` | critical | défaut de couverture de la matrice (refus implicite) |
| `RoleMismatch` | critical | rôle déclaré ≠ référentiel (usurpation possible) |
| `PermissionViolation` | high | action hors permissions de la règle |
| `UnknownUser` | high | utilisateur absent du référentiel IAM |
| `InactiveAccount` | high | compte dé-provisionné utilisé |
| `MalformedValue` | high | valeur de journal invalide - source à corriger |
| `MFA` | medium | MFA requis non activé lors de l'accès |
| `BusinessHours` | medium | signal faible - à corroborer avant escalade |

Lecture des niveaux :

* **critical** - la politique ou la matrice est contournée : escalade.  
* **high** - violation réelle, mais corroboration du contexte utile (source de la donnée, gestion du compte).  
* **medium** - signal faible : une occurrence ne suffit pas, la répétition (fréquence, autres signaux) transforme le signal en alerte.

---

## Modifier les règles

**Matrice :** éditer `MatriceRBAC.csv`.  
Le chargement détecte automatiquement le séparateur (`,` ou `;`), les fichiers de journal et le référentiel utilisateurs attendent strictement `;`.

**Colonnes lues** par le script : `ID`, `Rôle`, `Classification`,
`Ressources`, `Permission` (ou `Permissions`) et `MFA`. Les autres
colonnes (ex. `Justification`) sont **ignorées**. Une colonne obligatoire
absente ou renommée arrête l'audit avec un message listant l'attendu.

**Vocabulaire des permissions :** 
chaque cellule `Permission` ne contient que des jetons parmi `L` (lecture), `E` (écriture), `S` (suppression), `X` (exécution), `A` (administration) ou `-` seul (refus explicite). 
Les commentaires sont interdits dans les cellules de permission : toute nuance temporelle relève de la colonne Justification ou d'une règle distincte.
Le script valide ce vocabulaire au chargement (`fail-closed`) : un jeton non reconnu pourrait être interprété comme une autorisation.
Une cellule `Permission` vide vaut refus explicite (`-`).

**Vocabulaire du MFA** : `O` ou `N`, rien d'autre. Une valeur imprévue
(« Oui ») désactiverait le contrôle MFA sans signal, le chargement arrête.

**Doublons** : deux règles portant le même couple Rôle/Ressources, ou un
utilisateur figurant deux fois dans le référentiel, **arrêtent l'audit**.
Le premier trouvé ne « gagne » pas : une donnée ambiguë de la source de
vérité est à corriger, pas à départager, un refus ne doit pas pouvoir
être contourné par une ligne insérée avant lui.

**Horaires :** `BUSINESS_OPEN`, `BUSINESS_CLOSE` (format `HH:MM`).
**Jours ouvrés :** `WORKING_DAYS` (norme ISO : lundi = 0 ... dimanche = 6).
**Exemptions :** HOUR_EXEMPT_ROLES.

**Sévérité :** chaque contrôle définit la sienne (critical / high / medium) dans son code.

---

## Ajouter un nouveau contrôle

Architecture modulaire : chaque contrôle analyse une entrée du journal et retourne ses anomalies sous l'une des **deux formes documentées** :

* **contrôle simple** : `check_xxx(log_entry: dict) -> dict | None`.
  - `None` si conforme, un dictionnaire d'anomalie sinon,
  -  la boucle principale l'ajoute avec `anomalies.append(...)`.
* **contrôle multi-anomalies** : retourne une **liste** de dictionnaires
  (zéro, une ou plusieurs anomalies par entrée - cf.
  `check_access_compliance`), la boucle utilise `anomalies.extend(...)`.

Pour en ajouter un :

1. Si nécessaire, une constante de configuration (ex. `MAX_FAILED_LOGINS = 5`).  
2. Une fonction `check_xxx(log_entry: dict) -> dict | None`.  
3. L'appeler dans la boucle principale de `rbac_audit.py`, après le contrôle utilisateur (continue sur anomalie d'identité) et après `check_access_compliance()`.
4. Le dictionnaire retourné doit contenir **toutes** les clés lues par `generate_report()` : les six champs du journal (`timestamp`, `user`, `role`, `resource`, `action`, `mfa_enabled`) **et** `rbac_rule`, `control_type`, `classification`, `severity`, `reason`. Une clé manquante interrompt le rapport en fin de run (`KeyError`).

**Exemples de contrôles ajoutables :** 
`check_impossible_travel()`, `check_multiple_failed_logins()`, `check_privileged_account_usage()`, `check_account_expiration()`…   
Chaque fonction produit son anomalie sans modifier les autres contrôles, _la même approche que les moteurs de détection (SIEM, SOAR), où chaque règle est autonome et testable indépendamment_.

---

## Planification

Pour une exécution hebdomadaire, un ordonnanceur système convient :  
`cron` sous Linux, Planificateur de tâches sous Windows, ou un orchestrateur (Jenkins, GitLab CI). 

La séparation entre logique d'audit et planification facilite maintenance et déploiement, le code de sortie non nul alerte en cas d'échec du job.

---

## Référentiel utilisateurs

Le fichier `users.csv` contient uniquement les informations nécessaires aux contrôles IAM : identifiant, utilisateur, type d'utilisateur, rôle, statut. 
Aucune donnée métier sensible n'y est stockée : la séparation relève des applications métier.

**Référentiel des rôles (gouvernance) :**

- **La matrice RBAC est la source de vérité des rôles** : toute évolution est d'abord actée dans la matrice, puis répercutée dans le référentiel IAM.  
- La comparaison est **stricte** (casse et accents compris) : une graphie approximative est une donnée à corriger, pas à tolérer. La normalisation Unicode (NFKC) ne sert qu'à détecter la **quasi-correspondance**, citée dans le message d'arrêt.   
- Le vocabulaire des statuts est contrôlé : `Active` / `Inactive`, toute autre valeur bloque l'audit (`fail-closed`).

**Contrôle automatique au démarrage (`check_roles_consistency()`) :**

* statut hors vocabulaire → arrêt immédiat (exit 1),  
* rôle d'un compte actif absent de la matrice → arrêt immédiat, avec citation de la quasi-correspondance si elle existe : chaque accès
de ce compte produirait un `NoMatchingRule` et saturerait le rapport, masquant les violations réelles,  
* rôle de la matrice sans utilisateur référencé → avertissement seul (cas légitime : rôle en préparation, compte de service non provisionné),  
* les comptes inactifs sont exclus du contrôle bloquant (dé-provisionnement normal, couvert par `InactiveAccount`),  
* un rôle exempté du contrôle horaire mais absent de la matrice → avertissement (exemption silencieuse impossible).

---

## Rapport généré

Chaque anomalie comporte : horodatage, utilisateur, rôle, ressource, action, valeur MFA, règle RBAC concernée, type de contrôle, classification de la ressource, justification, sévérité. Format exploitable en audit, contrôle interne, ou ingestion SIEM.

**Format** : CSV séparateur virgule, encodage UTF-8 sans BOM, fins de ligne LF (cf. `.gitattributes`). Les fichiers d'entrée, eux, sont au
point-virgule.

**Un rapport n'est généré que si l'audit a tourné sur une matière analysable.** 
Un journal vide arrête l'audit (aucun rapport) : un rapport « tout vert » sans entrée analysée serait un faux rassurant, le symptôme d'un export en échec, pas d'une semaine sans écart. 
À l'inverse, un run sur des entrées réelles sans anomalie produit un rapport horodaté réduit à l'en-tête : preuve que le contrôle a été exécuté et n'a rien détecté. 
Un rapport d'audit se lit toujours avec son compte d'entrées (console). 
En exécution planifiée, l'absence de rapport récent signale un job qui n'a pas tourné : deux défaillances distinctes, deux alertes
distinctes.

**Prudence à l'ouverture** : le rapport contient des valeurs issues des journaux d'accès (champs non maîtrisés par l'outil). 
À l'ouverture dans Excel, une cellule commençant par `=`, `+`, `-` ou `@` peut être interprétée comme une formule. 
Le script ne modifie jamais la donnée (intégrité de la preuve) : ouvrir le rapport dans un éditeur de texte ou un tableur configuré pour ne pas évaluer les formules.

**Sortie console attendue (jeu de démonstration) :**

```bash
=== [DEBUT] Audit RBAC ===
[INFO] Matrice RBAC chargée : 20 règles.
[INFO] Logs d'accès chargés : 5 entrées.
[INFO] Référentiel IAM chargé : 11 utilisateurs.
[AVERTISSEMENT] Rôles de la matrice sans utilisateur référencé : ['DPO', 'Laboratoires']
[INFO] 3 anomalie(s) détectée(s).
[SUCCESS] Rapport généré : YYYYMMDD_HHMMSS_rapport_anomalies.csv (3 anomalie(s)).
=== [FIN] Audit terminé ===
```

---

## Exemples de sorties

Le dossier `exemples/` contient des sorties **réelles**, capturées lors des tests sur les jeux fournis, et volontairement figées :

* `rapport_exemple_jeu_demo.csv` : rapport complet du jeu de démonstration (3 anomalies),
* `rapport_exemple_jeu_negatif.csv` : rapport complet du jeu négatif (14 anomalies, un exemplaire par type de contrôle),
* `rapport_exemple_jeu_nominal.csv` : rapport 0 anomalie du jeu nominal (preuve d'exécution).

Conventions :
* pas de timestamp dans un exemple committé (le timestamp est la signature
  d'une exécution réelle),
* les exemples sont régénérés à chaque évolution de l'outil,
* les sorties du run courant ne sont jamais committées (`.gitignore`).

**Test de non-régression par comparaison** : une commande par jeu, avec
chargement du jeu et nettoyage préalable (le script lit toujours
`user_access_log.csv`), le rapport ne contient d'horodatage interne
nulle part, la comparaison avec l'exemple est exacte. Le verdict se lit à l'écho « conforme à l'exemple », la restauration, elle, est inconditionnelle.

```bash
# une sauvegarde unique, en tête de bloc
cp user_access_log.csv /tmp/sauvegarde_log.csv
# jeu de démonstration (déjà chargé)
find . -maxdepth 1 -name "*_rapport_anomalies.csv" -delete; python3 rbac_audit.py && diff *_rapport_anomalies.csv exemples/rapport_exemple_jeu_demo.csv && echo "conforme à l'exemple"
# jeu nominal - la restauration suit un « ; » : elle s'exécute même si le diff échoue
cp user_access_log_nominal.csv user_access_log.csv; find . -maxdepth 1 -name "*_rapport_anomalies.csv" -delete; python3 rbac_audit.py && diff *_rapport_anomalies.csv exemples/rapport_exemple_jeu_nominal.csv && echo "conforme à l'exemple"; cp /tmp/sauvegarde_log.csv user_access_log.csv
# jeu négatif - même structure
cp user_access_log_negatif.csv user_access_log.csv; find . -maxdepth 1 -name "*_rapport_anomalies.csv" -delete; python3 rbac_audit.py && diff *_rapport_anomalies.csv exemples/rapport_exemple_jeu_negatif.csv && echo "conforme à l'exemple"; cp /tmp/sauvegarde_log.csv user_access_log.csv
# fin de bloc : démonstration en place, sauvegarde supprimée
rm /tmp/sauvegarde_log.csv
```

---

## Protocole de test

**Objectif** : vérifier le comportement du script avant de l'implémenter, dans un dossier de test distinct du dossier de la ressource (ne jamais tester dans le dossier d'exécution réel).


Pour chaque test, la même séquence :

1. **Restaurer** la baseline : copier le fichier cible depuis le dossier de la ressource, avant toute injection.  
2. **Vérifier** la baseline : comptage de lignes ou empreinte, comparé à sa valeur attendue, pas de GO sans chiffre.  
3. **Nettoyer** les rapports résiduels : `find . -maxdepth 1 -name "*_rapport_anomalies.csv" -delete` (forme portable, sans échec sur dossier déjà propre: un `rm -f` à joker échoue sous zsh si aucun fichier ne matche).  
4. **Injecter** la modification testée, puis **prouver** l'injection : une commande de modification silencieuse (`sed`, `echo`) n'a rien démontré tant que son marqueur n'a pas été vérifié (`grep, wc -l`). Et ne jamais réexécuter une commande ayant produit un effet de bord avant sa vérification : chaque `echo >>` répété duplique la ligne.
5. **Exécuter** : `python3 rbac_audit.py`, `echo "code retour : $?"`. Le code dans la ligne du run.   
6. **Vérifier les attendus** : comptages sur le rapport, chaque chiffre comparé à sa valeur prévue. La valeur prévue est calculée depuis la table de conception, jamais depuis la mémoire.   
7. **Restaurer** la baseline et **nettoyer** : le terrain est rendu identique.  


**Tests conseillés :**  
- Exécuter les trois jeux et vérifier leurs sorties attendues (0 / 3 / 14 anomalies), puis la comparaison `diff` avec les exemples,  
- Injecter un accès conforme à une règle de votre matrice (la lire d'abord : `grep "<rôle>" MatriceRBAC.csv`) et vérifier l'absence d'anomalie,  
- Vérifier les cas `fail-closed` et la politique valeur/structure :

| Cas | Attendu | Code |
|---|---|---|
| fichier d'entrée absent | `[ERREUR]` nom du fichier, aucun rapport | 1 |
| en-tête invalide (journal, référentiel, matrice) | `[ERREUR]` en-tête attendu/lu | 1 |
| colonne obligatoire absente de la matrice | `[ERREUR]` colonnes attendues | 1 |
| jeton de permission inconnu | `[ERREUR]` ligne et jeton cités | 1 |
| valeur MFA de la matrice hors O/N (ex. « Oui ») | `[ERREUR]` ligne et valeur citées | 1 |
| règle dupliquée (même Rôle/Ressources) | `[ERREUR]` lignes citées | 1 |
| utilisateur dupliqué | `[ERREUR]` lignes citées | 1 |
| journal vide (en-tête seul) | `[ERREUR]` journal vide, aucun rapport | 1 |
| matrice RBAC vide (en-tête seul) | `[ERREUR] Matrice RBAC vide ou sans règle exploitable`, aucun rapport | 1 |
| référentiel IAM vide (en-tête seul) | `[ERREUR] Référentiel IAM vide`, aucun rapport | 1 |
| statut hors Active/Inactive | `[ERREUR]` vocabulaire | 1 |
| rôle d'un compte actif absent de la matrice | `[ERREUR]` + quasi-correspondance | 1 |
| valeur MFA du journal invalide | anomalie `MalformedValue`, audit poursuivi | 0 |
| valeur MFA du journal invalide **et** accès sans règle | 2 anomalies : `MalformedValue` + `NoMatchingRule`, audit poursuivi | 0 |
| horodatage invalide | anomalie `MalformedValue`, audit poursuivi | 0 |
| action hors vocabulaire | anomalie `MalformedValue`, audit poursuivi | 0 |
| accès jour non ouvré / hors horaires | anomalie `BusinessHours` (jour/horaires distingués) | 0 |

---

## Intégration SIEM (perspective)

L'audit ne comporte **aucune intégration SIEM**.
Le script n'a pas de dépendance externe et produit deux artefacts : un rapport CSV aux champs structurés et un code de sortie. 
Ces deux artefacts sont la matière première d'une intégration ultérieure (Wazuh, Graylog ou autre) : ingestion du rapport, alerte sur code non nul, corrélation avec d'autres sources.

Si vous implémentez cette perspective : secrets via variables d'environnement ou gestionnaire de secrets (jamais en dur), HTTPS obligatoire, retry avec backoff, validation de schéma, signature des événements, rotation des clés. 
Ces exigences relèvent de votre environnement : elles ne sont ni testées ni fournies ici.

---

## Changelog

**Version 2.0 (26/10/2026)** durcissement du script : 
- fail-closed des chargeurs (fichiers, en-têtes, colonnes),  
- comparaison stricte des rôles avec citation de la quasi-correspondance,  
- vocabulaire des statuts,  
- évaluation RBAC indépendante de la validité MFA (plus de masquage de critical),  
- vocabulaire des actions, jours ouvrés et avertissement d'exemption,  
- jeux nominal et négatif (13 lignes, 14 anomalies, attribution une par type),  
- dossier exemples/ reproductible,  
- protocole de test en 7 temps,  
- .gitignore, .gitattributes.

**Version 1.0 (26/06/2026)** publication initiale.

*Document produit dans le cadre du projet portfolio GRC - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*
*Ce document est une synthèse pédagogique. Il ne se substitue ni à une analyse adaptée au contexte de l'organisation, ni à un audit ou à un accompagnement juridique lorsque ceux-ci sont nécessaires.* 


Licences : code sous licence MIT (SPDX: MIT), documentation sous licence CC BY 4.0 (SPDX: CC-BY-4.0). 
Attribution : Solène Figueiredo, projet grc-pme-fictive.