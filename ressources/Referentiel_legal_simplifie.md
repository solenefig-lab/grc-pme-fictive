# Référentiel légal simplifié — Conformité RGPD-HDS

> **Ce document est une entrée, pas un audit.** Il est conçu pour donner une vision claire aux responsables de PME sans expertise juridique des réglementations applicables, des données concernées et des actions prioritaires à mener.

---

## Recommandations stratégiques

1. **Registre** — Documenter systématiquement le registre des traitements.
2. **Priorisation** — Cibler en priorité les données de santé et leur hébergement, puis les données de paiement.
3. **Preuves** — Centraliser les contrats de sous-traitance et les mentions légales (art. 28 RGPD).
4. **Formation** — Sensibiliser les équipes aux risques de sécurité et aux obligations RGPD.
5. **Audit** — Automatiser la surveillance des accès et des vulnérabilités.
6. **AIPD (PIA)** — Réaliser et documenter l'Analyse d'Impact pour les traitements de données de santé.

> **Note — Hébergement Cloud** : en cas de recours à un Cloud (AWS, Azure, OVH), vérifier que la région de stockage est en Europe (ou encadrée par des garanties adéquates) pour éviter les transferts hors UE.
>
> **Note — DPO** : pour une PME traitant des données de santé à grande échelle, la désignation d'un DPO (interne ou externe) est obligatoire.

---

## Tableau de référence

| Réglementation | Focus | Données concernées | Obligation concrète | Risque si non-conformité |
|---|---|---|---|---|
| **RGPD — Art. 6 et liés** | Juridique | Données personnelles (nom, email, identifiants…) | Vérifier la finalité légitime : consentement, exécution du contrat, obligation légale ou intérêt légitime (ex. sécurité des systèmes) | Amende RGPD jusqu'à 4% du CA mondial ou 20M€ appliquée par la CNIL + perte de confiance + responsabilité civile + possible interdiction de traitement selon la gravité |
| **RGPD — Art. 9 et liés** | Juridique + Métier (Santé) | Données de santé (dossier médical, ECG, ordonnances…) | Consentement explicite obligatoire — ou motif d'intérêt public, nécessité pour les soins, ou recherche/statistiques (pseudonymisation obligatoire dans ce dernier cas) | Amende RGPD jusqu'à 4% du CA mondial ou 20M€ + perte de confiance appliquée par la CNIL + responsabilité civile + possible interdiction de traitement selon la gravité |
| **LIL — Art. 30 + décret n° 2019-341** | Juridique | NIR — Numéro de Sécurité Sociale (identifiant à encadrement spécifique) | Usage limité aux catégories de responsables et aux finalités fixées par le décret n° 2019-341 | Amende administrative CNIL jusqu’à 20 M€ ou 4 % du CA mondial (RGPD art. 83) ; sanctions pénales possibles (Code pénal, art. 226-16 et suivants, à vérifier)|
|**CSP — Art. R. 1112-7** | Métier (Santé) | Données de santé — dossier médical | Conservation et archivage : 20 ans pour le dossier médical hospitalier ; durées unifiées pour les praticiens libéraux (conservation sous la responsabilité du médecin, aux mêmes durées que les établissements) ; archivage restreint ensuite | Amende jusqu'à 300 000 € + sanction déontologique (Conseil de l'Ordre) + perte de confiance partenaires + responsabilité civile |
|**CSP — Art. L. 1111-8 + R. 1111-8 et s.**| Technique | Données de santé hébergées | Recourir à un hébergeur certifié HDS (certification ANS) pour toutes les activités d'hébergement ; contrat d'hébergement avec clauses obligatoires ; vérification annuelle du certificat | Sanction CSP jusqu'à 300 000 € + 5 ans d'emprisonnement (exercice illégal de l'hébergement) + suspension par l'ANS + sanction RGPD en cas de violation |
| **HDS** | Technique | Données de santé hébergées | Recourir à un hébergeur certifié HDS (ex. OVH Gravelines) pour tout hébergement de données de santé | Sanction CSP jusqu'à 300 000€ + exposition à sanction RGPD en cas de violation + suspension par CNIL ou ANS + responsabilité pénale |
| **PCI-DSS** | Technique | Données de paiement (CB, RIB, tokens…) | Sécurisation des moyens de paiement — recourir à un prestataire certifié PCI-DSS (ex. Stripe Level 1) | Pénalités contractuelles jusqu'à 500 000$ + résiliation par l'acquéreur bancaire + perte de confiance clients + responsabilité civile |

---

*Ressource produite dans le cadre du projet portfolio GRC — [github.com/solenefig-lab/grc-pme-fictive](https://github.com/solenefig-lab/grc-pme-fictive)*
*Ce document est une simplification pédagogique. Il ne se substitue pas à un audit juridique ou à l'accompagnement d'un DPO.*  
_Licence : CC BY 4.0 — Attribution : Solène Figueiredo, projet grc-pme-fictive_
