# Fiche de gestion des risques en e-santé — SantéConnect

> ⚠️ **Projet de démonstration pédagogique** — SantéConnect est une PME fictive.
> Les livrables reflètent une démarche GRC réelle adaptée à un contexte simulé.

---

## 1. Grille de cotation des risques

| Niveau | Score (Impact × Probabilité) | Délai de traitement |
|--------|------------------------------|-------------------|
| 🟢 Faible | 1 – 2 | Acceptable |
| 🟠 Modéré | 3 – 5 | Remédiation sous 3 mois |
| 🔴 Haut | 6 – 9 | Correction dans la semaine |

> **Matrice 3×3** — Impact (1=Faible / 2=Modéré / 3=Critique) × Probabilité (1=Faible / 2=Modérée / 3=Haute)
> Choix justifié : granularité adaptée à une PME de 15 personnes, permet une allocation claire des ressources sans sur-complexifier l'analyse.

---

## 2. Cartographie des actifs

| Asset | Type | Impact | Probabilité | Score | Niveau |
|-------|------|--------|-------------|-------|--------|
| App Mobile B2C | Applicatif | 3 | 2 | 6 | 🔴 Haut |
| WebApp B2C | Applicatif | 3 | 2 | 6 | 🔴 Haut |
| Plateforme B2B | Applicatif | 3 | 1 | 3 | 🟠 Modéré |
| Base de données clients | Infrastructure | 3 | 1 | 3 | 🟠 Modéré |
| Hébergement (OVH HDS) | Infrastructure | 3 | 2 | 6 | 🔴 Haut |
| APIs externes | Infrastructure | 3 | 2 | 6 | 🔴 Haut |
| Équipement routage et sécurité | Infrastructure | 3 | 2 | 6 | 🔴 Haut |
| Interconnexion médicale (CHU) | Applicatif | 2 | 2 | 4 | 🟠 Modéré |
| Poste de travail | Infrastructure | 2 | 1 | 2 | 🟢 Faible |
| Imprimante | Infrastructure | 1 | 1 | 1 | 🟢 Faible |
| Thermostat connecté | Infrastructure | 1 | 1 | 1 | 🟢 Faible |
| Caméra entrée/sortie | Infrastructure | 1 | 1 | 1 | 🟢 Faible |
| Données personnelles patient | Données | 3 | 2 | 6 | 🔴 Haut |
| Données de santé patient | Données | 3 | 2 | 6 | 🔴 Haut |
| Données de paiement patient | Données | 3 | 2 | 6 | 🔴 Haut |
| Données praticiens | Données | 1 | 1 | 1 | 🟢 Faible |
| Direction (PDG/COO) | Humain | 3 | 1 | 3 | 🟠 Modéré |
| RSSI | Humain | 3 | 1 | 3 | 🟠 Modéré |
| DPO | Humain | 2 | 1 | 2 | 🟢 Faible |
| Responsable Produit | Humain | 2 | 1 | 2 | 🟢 Faible |
| DevOps | Humain | 2 | 1 | 2 | 🟢 Faible |
| Autre employé | Humain | 1 | 1 | 1 | 🟢 Faible |
| Utilisateur B2C | Humain | 3 | 1 | 3 | 🟠 Modéré |
| Utilisateur B2B | Humain | 2 | 1 | 2 | 🟢 Faible |

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

## Prochaine étape
[Semaine 2 — Audit RGPD-HDS](../semaine-2-rgpd-hds/README.md)
