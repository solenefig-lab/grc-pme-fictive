# Fiche de gestion des risques en e-santé — SantéConnect

> ⚠️ **Projet de démonstration pédagogique** — SantéConnect est une PME fictive.
> Les livrables reflètent une démarche GRC réelle adaptée à un contexte simulé.
> La démarche s'appuie sur une logique inspirée d'EBIOS Risk Manager
> (formalisation complète en semaine 5).

---

## 1. Grille de cotation des risques

### Niveaux de risque
| Niveau | Score (Impact × Probabilité) | Délai de traitement |
|--------|------------------------------|-------------------|
| 🟢 Faible | 1 – 2 | Acceptable |
| 🟠 Modéré | 3 – 5 | Remédiation sous 3 mois |
| 🔴 Haut | 6 – 9 | Correction dans la semaine |

> **Matrice 3×3** — Impact (1=Faible / 2=Modéré / 3=Critique) × Probabilité (1=Faible / 2=Modérée / 3=Haute)
> Choix justifié : granularité adaptée à une PME de 15 personnes, permet une allocation claire des ressources sans sur-complexifier l'analyse.

### Critères d'évaluation de l'impact
 
| Score | Niveau | Définition |
|-------|--------|------------|
| 1 | Faible | Conséquence limitée, sans effet sur le fonctionnement |
| 2 | Modéré | Perturbation partielle, impact métier limité |
| 3 | Critique | Conséquence importante, effet négatif sur le bon fonctionnement |
 
### Critères d'évaluation de la probabilité
 
| Score | Niveau | Critères objectifs |
|-------|--------|--------------------|
| 1 | Faible | Accès interne uniquement + contrôles forts en place |
| 2 | Modérée | Exposé Internet OU contrôles partiels / supposés |
| 3 | Élevée | Exposé Internet + contrôles faibles ou absents |

---

## 2. Cartographie des actifs

### Applicatifs

| Asset | Type | Impact | Probabilité | Score | Niveau | Justification |
|-------|------|--------|-------------|-------|--------|---------------|
| App Mobile B2C | Applicatif | 3 | 2 | 6 | 🔴 Haut | Exposée Internet, téléchargeable publiquement, surface d'attaque large |
| WebApp B2C | Applicatif | 3 | 2 | 6 | 🔴 Haut | Exposée Internet, accessible depuis tout navigateur |
| Plateforme B2B | Applicatif | 3 | 1 | 3 | 🟠 Modéré | Accès professionnel sur poste dédié, périmètre restreint |
| Interconnexion médicale (CHU) | Applicatif | 2 | 2 | 4 | 🟠 Modéré | Exposition externe, pivot vers CHU, systèmes tiers non maîtrisés |

### Infrastructure
 
| Asset | Type | Impact | Probabilité | Score | Niveau | Justification |
|-------|------|--------|-------------|-------|--------|---------------|
| Hébergement (OVH HDS) | Infrastructure | 3 | 2 | 6 | 🔴 Haut | Exposition via apps hébergées, dépendance critique toute l'infrastructure |
| APIs externes | Infrastructure | 3 | 2 | 6 | 🔴 Haut | Exposition Internet, intégrations multiples, contrôles supposés faibles |
| Équipement routage et sécurité | Infrastructure | 3 | 2 | 6 | 🔴 Haut | Accès réseau complet, PME sans SOC ni monitoring 24/7 |
| Base de données clients | Infrastructure | 3 | 1 | 3 | 🟠 Modéré | PII sensible, accès interne, hébergeur certifié HDS |
| Poste de travail | Infrastructure | 2 | 1 | 2 | 🟢 Faible | Accès interne, réseau entreprise, contrôles supposés en place |
| Imprimante | Infrastructure | 1 | 1 | 1 | 🟢 Faible | Réseau entreprise, accès physique requis |
| Thermostat connecté | Infrastructure | 1 | 1 | 1 | 🟢 Faible | Réseau entreprise, impact limité |
| Caméra entrée/sortie | Infrastructure | 1 | 1 | 1 | 🟢 Faible | Réseau entreprise, impact limité |
 
### Données
 
| Asset | Type | Impact | Probabilité | Score | Niveau | Justification |
|-------|------|--------|-------------|-------|--------|---------------|
| Données personnelles patient | Données | 3 | 2 | 6 | 🔴 Haut | Exposition directe via App, surface d'attaque large (80 patients) |
| Données de santé patient | Données | 3 | 2 | 6 | 🔴 Haut | Exposition via apps publiques, attractivité forte attaquants spécialisés santé |
| Données de paiement patient | Données | 3 | 2 | 6 | 🔴 Haut | Transactions en ligne, vecteur Stripe, cible fraude financière |
| Données praticiens | Données | 1 | 1 | 1 | 🟢 Faible | PII souvent publiques (annuaires, web), impact limité |
 
### Humains
 
| Asset | Type | Impact | Probabilité | Score | Niveau | Justification |
|-------|------|--------|-------------|-------|--------|---------------|
| Direction (PDG/COO) | Humain | 3 | 1 | 3 | 🟠 Modéré | Décideur, conscient des risques et responsabilités |
| RSSI | Humain | 3 | 1 | 3 | 🟠 Modéré | Formé aux risques, accès privilégiés maîtrisés |
| Utilisateur B2C | Humain | 3 | 1 | 3 | 🟠 Modéré | Porte d'entrée potentielle, public senior peu à l'aise avec la technologie |
| DPO | Humain | 2 | 1 | 2 | 🟢 Faible | Formé aux risques, accès direct aux assets critiques limité |
| Responsable Produit | Humain | 2 | 1 | 2 | 🟢 Faible | Accès possible aux infrastructures critiques, formation non obligatoire |
| DevOps | Humain | 2 | 1 | 2 | 🟢 Faible | Formé aux risques, accès techniques encadrés |
| Utilisateur B2B | Humain | 2 | 1 | 2 | 🟢 Faible | Public professionnel sensibilisé aux risques secteur |
| Autre employé | Humain | 1 | 1 | 1 | 🟢 Faible | Sans accès direct aux assets critiques |

---

## 3. Identification des menaces

### Infrastructure

| Asset | Menace | Vecteur d'attaque | Tactique MITRE ATT&CK | Réglementation impactée |
|-------|--------|-------------------|-----------------------|------------------------|
| **Hébergement** | Compromission fournisseur | Supply chain | [T1195](https://attack.mitre.org/techniques/T1195/) — Supply Chain Compromise | RGPD Art. 28 + Art. 32 · NIS2 Obj. 8 + Obj. 20 |
| **Hébergement** | Indisponibilité | DDoS | [T1498](https://attack.mitre.org/techniques/T1498/) — Network Denial of Service | RGPD Art. 28 + Art. 32 · NIS2 Obj. 8 + Obj. 13 + Obj. 20 |
| **APIs** | Fuite de données | API mal configurée | [T1190](https://attack.mitre.org/techniques/T1190/) — Exploit Public-Facing Application | RGPD Art. 5 + Art. 9 + Art. 32 + Art. 33 + Art. 34 + Art. 90 · NIS2 Obj. 8 + Obj. 10 + Obj. 12 + Obj. 20 |
| **APIs** | Intrusion | Vol de clé API (token) | [T1552.001](https://attack.mitre.org/techniques/T1552/001/) — Credentials in Files | RGPD Art. 5 + Art. 9 + Art. 32 + Art. 33 + Art. 34 · NIS2 Obj. 8 + Obj. 9 + Obj. 10 + Obj. 12 + Obj. 20 |
| **Équipement routage** | Intrusion | Port 23 (Telnet) ouvert | [T1133](https://attack.mitre.org/techniques/T1133/) — External Remote Services | NIS2 Obj. 3 + Obj. 8 + Obj. 9 + Obj. 10 + Obj. 12 + Obj. 20 |
| **Équipement routage** | Mouvement latéral | Équipement non autorisé (USB/MitM) | [T1557](https://attack.mitre.org/techniques/T1557/) — Adversary-in-the-Middle | NIS2 Obj. 3 + Obj. 8 + Obj. 9 + Obj. 10 + Obj. 12 + Obj. 20 |

### Données

| Asset | Menace | Vecteur d'attaque | Tactique MITRE ATT&CK | Réglementation impactée |
|-------|--------|-------------------|-----------------------|------------------------|
| **Données personnelles** | Intrusion | Force brute — compte compromis | [T1110](https://attack.mitre.org/techniques/T1110/) — Brute Force | RGPD Art. 5 + Art. 32 + Art. 33 + Art. 34 · NIS2 Obj. 3 + Obj. 9 + Obj. 10 + Obj. 12 + Obj. 20 |
| **Données personnelles** | Fuite de données | Exploit Public-Facing Application | [T1190](https://attack.mitre.org/techniques/T1190/) — Exploit Public-Facing Application | RGPD Art. 5 + Art. 32 + Art. 33 + Art. 34 · NIS2 Obj. 3 + Obj. 8 + Obj. 9 + Obj. 10 + Obj. 12 + Obj. 20 |
| **Données de santé** | Fuite de données | Injection SQL / XSS | [T1059](https://attack.mitre.org/techniques/T1059/) — Command and Scripting Interpreter | RGPD Art. 5 + Art. 9 + Art. 32 + Art. 33 + Art. 34 + Art. 90 · NIS2 Obj. 8 + Obj. 10 + Obj. 12 + Obj. 20 |
| **Données de santé** | Extorsion | Ransomware — chiffrement données santé | [T1486](https://attack.mitre.org/techniques/T1486/) — Data Encrypted for Impact | RGPD Art. 5 + Art. 9 + Art. 32 + Art. 33 + Art. 34 + Art. 90 · NIS2 Obj. 8 + Obj. 10 + Obj. 12 + Obj. 20 |
| **Données de paiement** | Usurpation d'identité | Phishing / ingénierie sociale | [T1566](https://attack.mitre.org/techniques/T1566/) — Phishing | RGPD Art. 5 + Art. 32 + Art. 33 + Art. 34 · NIS2 Obj. 3 + Obj. 8 + Obj. 9 + Obj. 10 + Obj. 12 + Obj. 20 · PCI-DSS Req. 12 |
| **Données de paiement** | Fuite de données | Écoute clandestine — absence TLS/SSL sur réseau public | [T1040](https://attack.mitre.org/techniques/T1040/) — Network Sniffing | RGPD Art. 5 + Art. 32 + Art. 33 + Art. 34 · NIS2 Obj. 3 + Obj. 8 + Obj. 9 + Obj. 10 + Obj. 12 + Obj. 20 · PCI-DSS Req. 4 + Req. 7 |

---

## 4. Top 5 des risques prioritaires

> Classement par **impact** (réglementaire + business + réputationnel).
> Les risques 2 à 5 sont des **angles morts** fréquemment oubliés dans la sécurisation d'un réseau, pourtant vecteurs d'attaques de plus en plus courants.

| Priorité | Risque | Asset | Score | Recommandation |
|----------|--------|-------|-------|----------------|
| 1 | Fuite de données via élévation de privilèges | Données personnelles + santé + paiement | 6 | Mettre en place l'authentification 2FA sur tous les accès critiques et appliquer le principe du moindre privilège (least privilege) sur tous les comptes. |
| 2 | Mouvement latéral via Man in the Middle | Équipement routage | 6 | Mettre en place une politique d'autorisation stricte pour tout ajout d'équipement (refus par défaut) et interdire les périphériques USB non autorisés. |
| 3 | Intrusion via port ouvert | Équipement routage | 6 | Désactiver Telnet sur tous les équipements réseau et remplacer par SSH avec authentification par clé. Cartographier tous les ports ouverts et fermer ceux non nécessaires. |
| 4 | Fuite de données via mauvaise configuration API | APIs | 6 | Mettre en place une authentification robuste (OAuth2) et une validation stricte des entrées/sorties sur toutes les APIs exposées. |
| 5 | Intrusion via vol de clé de configuration API | APIs | 6 | Scanner les secrets existants (tokens, credentials) dans les dépôts de code et mettre en place un `.gitignore` + rotation régulière des clés. |

---
 
## 5. Exemple d'arbitrage — Risque accepté
 
| Asset | Score | Décision | Justification |
|-------|-------|----------|---------------|
| Interconnexion médicale (CHU) | 4 🟠 | ✅ Risque accepté | Interconnexion avec systèmes historiques indépendants de l'infrastructure PME — compensé par chiffrement BDD, authentification renforcée et contrôle des flux. |
 
> **Note :** Ce risque est accepté car le coût et la complexité d'une remédiation
> complète sont disproportionnés par rapport à la capacité d'action de SantéConnect
> sur des systèmes tiers. Les mesures compensatoires réduisent l'exposition résiduelle.
 
---
 
## 6. Note sur NIS2
 
> SantéConnect (15 employés) n'entre a priori pas directement dans le périmètre
> NIS2 au regard de sa taille. Toutefois, en tant que prestataire d'un
> établissement de santé (CHU), elle peut être concernée **indirectement** via
> des exigences de sécurité imposées par ses partenaires (logique de supply chain
> et chaîne de sous-traitance).
 
