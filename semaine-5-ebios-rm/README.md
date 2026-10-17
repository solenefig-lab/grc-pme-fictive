## Semaine 5 - EBIOS Risk Manager - Cadrage et appréciation des risques

### Objectif

**Formaliser l'approche EBIOS Risk Manager** (ANSSI) pour SantéConnect, en capitalisant sur les analyses de risques précédentes ([PTR](../semaine-3-iso27001/plan-traitement-risques.md), [SoA](../semaine-3-iso27001/SoA.md), [Analyse impact NIS2](../semaine-4-nis2/analyse-impact-nis2.md)), et passer d’une approche conformité (S1-S4) à une **approche risque systémique** (EBIOS RM) :

- **Cadrer le périmètre d'étude** (valeurs métiers, biens supports, parties prenantes, événements redoutés).
- **Établir le socle de sécurité existant et ses écarts résiduels**, base de l'appréciation des risques.
- **Construire un scénario opérationnel** (compromission API CHU) illustrant la logique attaquant, complémentaire à l'approche conformité menée jusqu'ici.

_Note : Pourquoi avoir choisi ce scénario (compromission API CHU) ?_
_- Impact maximal : Fuite de données médicales sensibles → sanction RGPD (jusqu’à 20 M€ ou 4 % du CA mondial) + perte de confiance des patients._
_- Lien avec les gaps S4 : Micro-segmentation non documentée, surveillance continue non formalisée._ 
_- Fournisseur d'une entité essentielle : Le CHU, entité essentielle, notifie l’ANSSI sous 24h (Art. 23), SantéConnect est tenue par des délais contractuels (4h / 24h / 72h)._  


---

### Livrables
| Livrable | Description | Statut |
|---|---|---|
| [`1-ebios-rm-santeconnect-cadrage.md`](./1-ebios-rm-santeconnect-cadrage.md)| Atelier 1 - Cadrage et socle de sécurité : périmètre métier/technique, valeurs métiers, parties prenantes, événements redoutés cotés (échelle G1-G4), socle de sécurité actualisé (SoA + plan d'action NIS2). | ✅ Complet |
| [`2-sources-risque.md`](./2-sources-risque.md) | Atelier 2 - Sources de risque : cartographie sources de risque (SR) et objectifs visés (OV), couple SR/OV priorisé (3 couples P1 développés : organisation criminelle ×2, personnel interne mécontent). | ✅ Complet |
| [`3-scenarios-strategiques.md`](./3-scenarios-strategiques.md) | Atelier 3 - Parties Prenantes (PP), cartographie écosystème, principaux chemins d'attaque et mesures de sécurité écosystème. | ✅ Complet |
| [`4-compromission-chu-api.md`](./4-compromission-chu-api.md) | Atelier 4 - Scénarios opérationnels et leur vraisemblance (compromission de l’API HL7/FHIR via l’interconnexion CHU), modes opératoires techniques détaillés et vraisemblance, S2 et S3 non développés. | ✅ Complet |
| [`5-synthese-cycle.md`](./5-synthese-cycle.md) | Synthèse et plan d'action : risques résiduels priorisés, alignement avec le plan d'action NIS2 (S4). | ✅ Complet |


---

### Points méthodologiques clés

- **Réutilisation du socle existant** : conformément au guide EBIOS RM (étape "socle de sécurité"), les contrôles déjà mis en œuvre (SoA S3, plan d'action NIS2 S4, PCA/PRA S4) constituent la base éprouvée dans les ateliers d'appréciation - pas de redondance, mais actualisation continue.
- **Double échelle de gravité** : la grille 3×3 (PTR, S3) reste l'outil de cotation des risques globaux; EBIOS RM introduit une échelle à 4 niveaux (G1-G4) pour les événements redoutés, avec seuils de déclenchement explicites ancrés sur le RTO 72h, le RPO 24h et les délais NIS2 (Art. 23).
- **Posture méthodologique** : Atelier 1-3 simplifiés et ciblés (PME 15 personnes), option scénario opérationnel unique retenue pour l'atelier 4; atelier 5 (traitement du risque) remplacé par synthèse (plan d'action priorisé) ; pertinence et lisibilité du portfolio priorisées sur l'exhaustivité.
- **Contexte réglementaire anticipé** : transposition NIS2 française non publiée à ce jour ; le Référentiel Cyber France (ReCyF, ANSSI, 17/03/2026) est retenu comme référentiel cible anticipé.


---

## Prochaine étape

La Semaine 5 clôture le cycle d'analyse de risques EBIOS RM avec un plan d'action priorisé, intégré aux livrables NIS2 (S4).

```mermaid
flowchart TD
    A[Semaine 5 - EBIOS RM] --> B[Atelier 1: Cadrage]
    A --> C[Atelier 2: Sources de Risque]
    A --> D[Atelier 3: Scénarios stratégiques et PP]
    A --> E[Atelier 4: Scénario opérationnel]
    A --> F[Synthèse et Plan d'Action]
    B -->|Socle de sécurité| C
    C -->|SR/OV priorisés| D
    D -->|PP critiques et chemins d'attaque| E
    E -->|Scénario compromission API CHU| F
    F -.->|Intégration NIS2| G[Semaine 4 - Gap Analysis]
    F -.->|Intégration PCA/PRA| H[Semaine 3 - PSSI/SoA]
```

_Note : cette section "Prochaine étape" est conservée à chaque semaine du portfolio pour matérialiser la timeline et la montée en compétences progressive du projet; elle n'est pas mise à jour rétroactivement._

