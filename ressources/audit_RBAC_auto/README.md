# README - Audit RBAC simplifié

> Document réalisé dans le cadre du projet portfolio GRC - [grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive).
Ce projet est un démonstrateur pédagogique illustrant des contrôles IAM/RBAC. Il ne constitue pas un outil d'audit exhaustif et ne se substitue pas à une évaluation de sécurité réalisée dans un contexte opérationnel.

---

## **Sommaire**

1. [Objectif](#objectif)
2. [Structure des fichiers](#structure-des-fichiers)
3. [Utilisation](#utilisation)
4. [Dépendances](#dépendances)
5. [Contrôles actuellement implémentés](#contrôles-actuellement-implémentés)
6. [Modifier les règles](#modifier-les-règles)
7. [Ajouter un nouveau contrôle](#ajouter-un-nouveau-contrôle)
8. [Planification](#planification)
9. [Référentiel utilisateurs](#référentiel-utilisateurs)
10. [Rapport généré](#rapport-généré)
11. [Intégration SIEM (Wazuh / Graylog)](#intégration-siem-wazuh--graylog)

--- 

## Objectif

Ce script réalise un audit automatisé des accès à partir :

* d'une matrice RBAC (`MatriceRBAC.csv`) ;
* d'un référentiel minimal d'identités (`users.csv`) ;
* d'un journal des accès (`user_access_log.csv`).

Pour chaque accès, plusieurs contrôles indépendants sont exécutés. Les anomalies détectées sont consolidées dans un rapport CSV horodaté.

---

## Structure des fichiers

```
RBAC_audit/

│── rbac_audit.py
│── MatriceRBAC.csv
│── users.csv
│── user_access_log.csv
│── 20260626_123149_rapport_anomalies.csv
```

---

## Utilisation

Placer les trois fichiers CSV dans le même répertoire que le script :

```
MatriceRBAC.csv
users.csv
user_access_log.csv
```

Puis lancer :

```bash
python3 rbac_audit.py
```

Le script génère automatiquement un rapport :

```
YYYYMMDD_HHMMSS_rapport_anomalies.csv
```

Exemple :

```
20260626_160000_rapport_anomalies.csv
```

---

## Dépendances

Le script utilise uniquement la bibliothèque standard Python.

Aucune dépendance externe n'est nécessaire.

Modules utilisés :

```
csv
datetime
```

Compatible avec Python 3.11 ou supérieur (également testé avec Python 3.14).

---

## Contrôles actuellement implémentés

Chaque contrôle est indépendant des autres.

### Contrôle 1 — Cohérence utilisateur / rôle

```
check_user_role()
```

Vérifie :

* utilisateur connu ;
* compte actif ;
* rôle déclaré conforme au référentiel IAM (`users.csv`).

---

### Contrôle 2 — Conformité RBAC

```
check_access_compliance()
```

Vérifie :

* existence d'une règle RBAC ;
* permissions autorisées ;
* refus explicites ;
* MFA obligatoire.

---

### Contrôle 3 — Horaires d'accès

```
check_business_hours()
```

Détecte les accès réalisés en dehors des horaires définis.

Les horaires sont configurables :

```python
BUSINESS_OPEN = "08:00"
BUSINESS_CLOSE = "18:00"
```

---

## Modifier les règles

Le script a été conçu pour être facilement adaptable.

### Modifier la matrice RBAC

Éditer simplement :

```
MatriceRBAC.csv
```

---

### Modifier les horaires

Modifier :

```python
BUSINESS_OPEN
BUSINESS_CLOSE
```

---

### Modifier les niveaux de sévérité

Chaque contrôle définit sa propre sévérité :

```
critical
high
medium
```

---

## Ajouter un nouveau contrôle

L'architecture est volontairement modulaire.

Chaque contrôle :

* analyse le journal d'accès ;
* retourne une anomalie indépendante si nécessaire ;
* ne dépend pas des autres contrôles.

Ajouter un nouveau contrôle consiste simplement à :

### 1. Ajouter une configuration (si nécessaire)

Exemple :

```python
MAX_FAILED_LOGINS = 5
```

---

### 2. Créer une nouvelle fonction

Exemple :

```python
check_multiple_failed_logins()
```

---

### 3. L'appeler dans la boucle principale

```python
result = check_multiple_failed_logins(log)

if result:
    anomalies.append(result)
```

Aucune autre modification n'est nécessaire.

---

### Contrôles facilement ajoutables

L'architecture permet d'ajouter facilement de nouveaux contrôles, par exemple :

```
check_impossible_travel()

check_multiple_failed_logins()

check_privileged_account_usage()

check_country_access()

check_account_expiration()

check_password_age()

check_disabled_account_usage()

check_impossible_workstation()

check_vpn_usage()
```

Chaque fonction produit sa propre anomalie sans modifier les autres contrôles.

Cette approche est proche de celle utilisée dans les moteurs de détection (SIEM, SOAR ou outils GRC), où chaque règle est autonome, testable indépendamment et plus simple à maintenir.

---

## Planification

Le script réalise un audit lorsqu'il est exécuté.

Pour une exécution quotidienne, il est recommandé d'utiliser un ordonnanceur système, par exemple :

* `cron` sous Linux ;
* le Planificateur de tâches sous Windows ;
* un orchestrateur tel que Jenkins ou GitLab CI.

Cette séparation entre la logique d'audit et la planification facilite la maintenance et le déploiement.

---

## Référentiel utilisateurs

Le fichier :

```
users.csv
```

constitue un référentiel minimal d'identités.

Il contient uniquement les informations nécessaires aux contrôles IAM :

* identifiant ;
* utilisateur ;
* type d'utilisateur ;
* rôle ;
* statut.

Aucune donnée métier sensible (données de santé, données RH, données financières, etc.) n'y est stockée.

La séparation des données sensibles doit être assurée au niveau des applications métier. Le référentiel d'identités est limité aux informations nécessaires pour vérifier la cohérence entre l'utilisateur et le rôle déclaré.

---

## Rapport généré

Chaque anomalie comporte notamment :

* horodatage ;
* utilisateur ;
* rôle ;
* ressource ;
* action ;
* règle RBAC concernée ;
* type de contrôle ;
* classification de la ressource ;
* justification de l'anomalie ;
* niveau de sévérité.

Ce format permet une exploitation facilitée dans le cadre d'un audit, d'un contrôle interne ou d'une intégration avec un SIEM. Il peut également servir de base à des traitements automatisés ou à des tableaux de bord de conformité.

A complétion du script, le résumé suivant apparaît. Il pourrait très bien aussi être sauvegardé et envoyé sur la plateforme souhaitée.

```bash
=== [DEBUT] Audit RBAC ===
[INFO] Matrice RBAC chargée : 20 règles.
[INFO] Logs d'accès chargés : 5 entrées.
[INFO] Référentiel IAM chargé : 10 utilisateurs.
[INFO] 3 anomalies détectées.
[SUCCESS] Rapport généré : 20260626_123149_rapport_anomalies.csv
=== [FIN] Audit terminé ===
```

---

## Intégration SIEM (Wazuh / Graylog)

### Statut

Cette intégration est fournie à titre illustratif uniquement et n’est pas destinée à un environnement de production.

### Sécurité des identifiants

Les clés API et secrets :
- ne doivent jamais être codés en dur dans le script,  
- doivent être fournis via variables d’environnement :  

```bash
export SIEM_API_KEY="xxxxx"
```

ou via un gestionnaire de secrets, p.ex. :
- HashiCorp Vault  
- AWS Secrets Manager  
- Azure Key Vault  

### Bonnes pratiques non implémentées (volontairement)

Dans un contexte industriel, les éléments suivants doivent être ajoutés :
- TLS obligatoire (HTTPS)  
- retry + exponential backoff  
- validation du schéma JSON (schema enforcement)  
- signature des événements (HMAC ou JWT)  
- correlation_id pour suivi SIEM  
- circuit breaker en cas de panne SIEM  
- logs structurés (JSON logging)  
- rotation des API keys  

### Limitation du script

Ce module ne garantit pas :
- la livraison des événements au SIEM  
- la déduplication des alertes  
- la corrélation avec d'autres sources de logs  
- la conformité aux standards d'ingestion SIEM en production  

### Philosophie de conception

Cette intégration est volontairement :
- simple  
- pédagogique  
- découplée du moteur RBAC  

Elle simule un flux de type :

`Audit RBAC → Détection anomalie → Event SIEM → Analyse SOC`
