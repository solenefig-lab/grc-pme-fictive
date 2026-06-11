# Analyse d'impact NIS2 - SantéConnect

> **Document fictif** - Projet portfolio GRC - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)
> Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité. Le niveau de granularité illustre une cible de maturité, non l'état courant du marché TPE/PME santé.

_Note de contexte réglementaire (juin 2026) : La transposition NIS2 en droit français n'est pas encore publiée. L'ANSSI met à disposition depuis le 17 mars 2026 le Référentiel Cyber France (ReCyF), document de travail correspondant au référentiel mentionné à l'article 14 du projet de loi Résilience. Les analyses et recommandations de ce livrable s'appuient sur la directive NIS2 (UE) 2022/2555 et anticipent le ReCyF comme référentiel cible, conformément à la posture recommandée par l'ANSSI pour les futurs assujettis._


---
## Objet et périmètre

### Hors périmètre NIS2 
SantéConnect est une PME française de 15 personnes fournissant des services numériques dans le domaine de la e-santé. Elle n'est ni une entité essentielle ni importante au sens de NIS2 et n'a donc pas d'obligation directe.
- Taille : SantéConnect ne franchit pas les seuils NIS2 (Art. 2(1)); NIS2 ne crée pas d'obligation directe sur les fournisseurs de taille réduite - c'est l'entité essentielle (CHU) qui porte l'obligation de sécuriser sa chaîne via Art. 21(2).
- Secteur d’activité : SantéConnect est fournisseur de services numériques en santé, non prestataire de soins au sens de l'Annexe I NIS2. Elle ne figure pas non plus dans l'Annexe II (secteurs critiques).
- Statut juridique : SantéConnect ne répond pas aux critères de taille et de secteur définis (Art. 2(1) + Art. 2(4)).
**En conséquence, SantéConnect n'a pas d'obligation de notification vers l'ANSSI, pas d'obligation d'enregistrement sur MonEspaceNIS2, et aucun contrôle ANSSI direct ne peut lui être opposé.**

### Périmètre applicable
Mais SantéConnect est impactée indirectement via le partenariat CHU et **ddes exigences contractuelles inspirées de NIS2, imposées par le CHU** pour garantir la sécurité des données partagées et des systèmes interconnectés. Ces exigences couvrent :
- Les mesures de gestion des risques et de sécurité (NIS2 Art. 21.a à 21.j), notamment :
    -   21.a : Politiques de sécurité et analyses de risques.
    -   21.c : Plans de continuité des activités (PCA/PRA).
    -   21.d : Sécurité de la chaîne d’approvisionnement (ex : conformité OVH).
    -   21.i et 21.j : Contrôle d’accès et surveillance continue.
- La notification des incidents (NIS2 Art. 23), avec des délais contractuels adaptés (ex : alerte précoce sous 4h, notification sous 24h).
_voir [Note co-responsabilité CHU NIS2](./note-coresponsabilite-CHU-maj-nis2.md)_

- **Objet** : partage et synchronisation des dossiers médicaux hospitaliers entre SantéConnect et le CHU Partenaire, dans le cadre de la continuité de la prise en charge médicale
- **Modalité technique** : synchronisation en temps réel des données médicales via API HL7/FHIR sécurisée

---

## Analyse d'écart (Gap analysis)

|Domaine NIS2| Via contrat CHU (Art. 21 et 23)| Via ISO 27001 existant | Gap | Priorité |
| ----------- | ----------- | ----------- | ----------- |  ----------- | 
| 21.a. Politiques de sécurité et analyses de risques | AIPD, mise à jour à chaque incident | A.5.1. PSSI, A.6.1. Screening RH des employés | Aucun gap: politiques en place | ✅ |
| 21.b. Plans d’intervention en cas d’incident  | AIPD + Art. 23. Gestion des incidents | A.5.24. à A.5.27. Procédure de gestion des incidents et notification, PTR + Registre des alertes, Registre de traitement | Aucun gap: politiques en place | ✅ |
| 21.c. Plans de continuité des activités | Tests annuels PCA/PRA + documentation, Activation PCA/PRA sous 4h en cas d’incident critique | A.5.29, A.5.30., A.8.13. PSSI, PRA/PCA | PRA/ PCA à finaliser | 🔴 |
| 21.d. Sécurité de la chaîne d’approvisionnement | Garantie conformité sous-traitants, yc. sécurité physique et logique, notification incidents sous 24h et audit annuel conjoint | A.5.19. à A.5.23. Contrats de sous-traitance, Preuve Certification OVH HDS, Audits annuels, Registre de traitement, AIPD | Aucun gap: OVH certifié HDS, audits en place | ✅ |
| 21.e. Sécurité dans l’acquisition, le développement et la maintenance des réseaux et des systèmes d’information | Segmentation (réseau DMZ pour les APIs) pour isoler les données partagées, audits semestriels | A.8.25 à A.8.30. PSSI, Contrats prestataires, Fiche risques e-santé | Micro-segmentation non documentée au-delà DMZ | 🟡 |
| 21.f. Evaluation de l’efficacité des mesures de gestion des risques liés à la cybersécurité | Tests de pénétration annuels sur apps critiques + documentation, correction vulnérabilités critiques sous 30 jours | A.5.36. Cadrage audit - RACI, PSSI | Aucun gap: pentests annuels documentés | ✅ |
| 21.g. Formation à la sensibilisation, à l’hygiène et aux meilleures pratiques en matière de cybersécurité | Formation NIS2 + sensibilisation annuelles bonnes pratiques + documentation | A.6.3. Plan de formation, PSSI | Preuve documentaire formation NIS2 spécifique à produire |🟡 |
| 21.h. Cryptographie et chiffrement | Données sensibles chiffrées en transit (TLS 1.3) et au repos (AES-256), audits semestriels | A.8.24. Utilisation de la cryptographie, PSSI | Aucun gap: TLS 1.3 + AES-256 en place | ✅ |
| 21.i. Procédures de contrôle d’accès, en particulier pour les employés ayant accès à des données sensibles | 2FA, audit annuel des droits d'accès (RBAC), journalisation des accès (logs conservés 1 an glissant) | A.5.9. à A.5.18., A.8.2, A.8.3., A.8.5. Fiche risques e-santé, Registre des traitements, Plan de formation, Matrice RBAC, Convention co-responsabilité, Contrat sous-traitance , Logs d'habilitation, Cartographie des risques, PSSI, Preuve d'activation MFA sur données sensibles et critiques | Automatiser les revues d’habilitation et centraliser surveillance | 🟡 |
| 21.j. Authentification multifactorielle, surveillance continue et systèmes de communication sécurisés |  2FA, audit annuel des droits d'accès (RBAC), journalisation des accès (logs conservés 1 an glissant) | A.5.17 PSSI, A.8.5 Matrice RBAC, Logs d'habilitation, Preuve d'activation MFA sur données sensibles et critiques., A.8.20. Cartographie des risques, Procédures de sécurité IT | Surveillance continue non formalisée au-delà Graylog | 🟡 |
| 23. Gestion des incidents | Alerte précoce (4h) + notification CHU sous 24h, réponse conjointe sous 72h (analyse, mitigation, sécurisation), partage des coûts au prorata responsabilité, rapport final sous 1 mois | Procédure de gestion des incidents et notification, PTR + Registre des alertes, Registre de traitement | Aucun gap: délais et procédures documentés | ✅ |


_Notes:_
_- les clauses NIS2 via le CHU sont précises, mesurables et vérifiables (preuves de formation, rapports de pentest, preuves PCA/PRA)._
_- le registre des alertes est intégré au plan de réponse aux incidents (S3)._

**Légende des Priorités** :

 | Symbole | Signification | Action Recommandée |
 |---------|---------------|--------------------|
 | 🔴 Critique | Gap bloquant pour la conformité contractuelle ou légale. | **Corriger sous 1 mois**. |
 | 🟡 Modérée | Amélioration possible, non bloquant. | **Corriger sous 6 mois**. |
 | ✅ Aucun | Conforme. | Aucune action. |

---

## Plan d’Action pour Combler les Gaps**

| **Priorité** | **Gap** | **Action** | **Responsable** | **Échéance** | 
 |--------------|---------|------------|------------------|--------------|
 | 🔴 Critique | PCA/PRA non documenté | A formaliser et faire valider, Vérifier la faisabilité du délai de 4h (services critiques) + Documenter procédures | RSSI | 30/06/2026 |
 | 🟡 Modérée | Micro-segmentation non documentée | Documenter la segmentation réseau | DevProduit (supervision RSSI) | 15/07/2026 | 
 | 🟡 Modérée | Automatiser les revues d’habilitation et centraliser surveillance | Automatiser les revues RBAC + export rapport hedomadaire avec un script Python, Centraliser la surveillance avec Wazuh + Graylog (solutions déjà en place, périmètre à élargir), Documentation à produire | DevProduit (supervision RSSI) | 15/09/2026 | 
 | 🟡 Modérée | Surveillance continue non formalisée au-delà Graylog | Configurer des alertes dans Graylog, Renforcer Wazuh pour la surveillance en temps réel, Documentation à produire | DevProduit (supervision RSSI) | 15/09/2026 | 
 | 🟡 Modérée | Preuves de formation NIS2 manquantes | Formation + PV | RH | 30/09/2026 |


---

## Signatures
Version: V1.0 - Emission : 10/06/2026

| Rôle | Nom | Date de signature | 
|---|---|---|
| CEO SantéConnect | Martin DUPONT | 10/06/2026 |
| RSSI | Claire ESPINOZA | 10/06/2026 |
| DPO SantéConnect (As a Service) | Jeanne PETIT | 10/06/2026 |
| RH | Bernard THOMAS | 10/06/2026 |


---

*Document produit dans le cadre du projet portfolio GRC - [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*
*Ce document est une synthèse pédagogique. Il ne se substitue pas à un audit réalisé par un organisme accrédité.*