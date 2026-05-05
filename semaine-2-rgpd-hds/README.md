## Semaine 2 — Conformité RGPD-HDS

### Objectif
Poser les bases de la conformité RGPD-HDS pour SantéConnect : structurer les traitements de données, évaluer les risques associés aux données de santé et produire les documents opérationnels de conformité.

### Livrables

| Livrable | Description | Statut |
|---|---|---|
| [`/registre-traitements`](./registre-traitements/) | Notice + registre complet D-001→D-010, basé sur modèle simplifié CNIL augmenté secteur e-santé | ✅ Complet |
| [`aipd-synthetique.md`](./aipd-synthetique.md/) | AIPD données de santé — évaluation des risques et priorisation des mesures (D-002 + D-005) |✅ Complet |
| [`note-co-responsabilite-chu.md`](./note-co-responsabilite-chu.md/) | Note convention co-responsabilité CHU (RGPD art. 26) | ✅ Complet |
| [`procedure-incident-notification.md`](./procedure-incident-notification.md/) | Procédure de gestion des incidents + template notification CNIL (art. 33-34) | ✅ Complet |
| [`checklist-audit-rgpd-hds.md`](./checklist-audit-rgpd-hds.md) | Checklist audit RGPD-HDS adaptée PME e-santé | ✅ Complet |
| [`synthese-clauses-sous-traitants.md`](./synthese-clauses-sous-traitants.md/) | Synthèse des clauses critiques art. 28 — OVH, Stripe, CHU | ✅ Complet  |

## Points méthodologiques clés

- NIR repositionné en donnée à protection renforcée (LIL art. 25).
- Co-responsabilité CHU limitée à D-002 et D-005 (fiche Données de Santé et Interconnexion avec CHU),
- Agrégation retenue sur D-009 (fiche Données Statistiques/R&D) avec documentation du risque de ré-identification.
- Matomo : choix structurant entre auto-hébergé (pas de sous-traitant art. 28) et Cloud (sous-traitant art. 28); arbitrage à documenter en situation réelle.".
- Choix des sous-traitants sans transfert hors EEE.

## 🛠️ Ressource associée

Ce template est issu de ce projet et réutilisable pour toute PME :

- [Référentiel légal simplifié](../ressources/Referentiel_legal_simplifie.md) 
*bases d'entrée conformité RGPD-HDS dont réglementation, obligation concrète, sanction et recommandations priorisation*

---

## ➡️ Prochaine étape

La semaine 3 traduit l'analyse de risques et les exigences RGPD-HDS en contrôles ISO 27001 opérationnels (PSSI, SoA et matrice RBAC) calibrés pour une PME e-santé à ressources limitées.

[Semaine 3 - Sécurité de l'information - ISO 27001](../semaine-3-iso27001/README.md)
