---
tags: [nibelis, extraction, mapping, trésorerie]
aliases: [Nibelis Trésorerie]
fichier_modele: "Modèle extraction Trésorerie.xlsx"
destinataire: Trésorerie
statut: Mapping validé — POPULATION BLOQUANTE (sortis)
---

# Nibelis Extract — Trésorerie

Voir [[Nibelis Extract - Projet]] pour les règles générales.

## ⚠️ Point bloquant : population = salariés SORTIS
Les 9 salariés du modèle (départs déc. 2025, dont 2 sans date de fin) sont **tous absents** de `api/salaries?id_societe=6961`, y compris avec `&periode=2025-12-01`. L'endpoint liste ne renvoie jamais les sortis → il faut d'abord trouver comment obtenir leur `id_nibelis`. La fiche `api/salaries/{id_nibelis}` fonctionne ensuite normalement.

## Fichier modèle
`Documents/Claude/Nibelis/Input/Modèle extraction Trésorerie.xlsx` — 21 colonnes, 1 ligne / salarié.

## Mapping des colonnes

| # | Colonne export | Champ API | Source | Note |
|---|---|---|---|---|
| 1 | Période | *(période d'extraction)* | — | |
| 2 | Nom | `nom` | `@LIST` | |
| 3 | Prénom | `prenom` | `@DETAIL` | |
| 4 | Matricule | `matricule` | `@LIST` | |
| 5 | Société | `libelle_societe` | `@DETAIL` | |
| 6 | Motif départ | `motif_depart` | `@DETAIL` | |
| 7 | Catégorie | `categorie_professionnelle_libelle` | `@DETAIL` | |
| 8 | Sexe | `sexe` | `@DETAIL` | |
| 9 | Contrat | `type_contrat_code` | `@DETAIL` | |
| 10 | Début de contrat | `date_debut_contrat` | `@LIST` | |
| 11 | Fin de contrat | `date_fin_contrat` | `@LIST` | |
| 12 | Date de naissance | `date_naissance` | `@DETAIL` | |
| 13 | Adresse | `adresse` | `@DETAIL` | |
| 14 | Adresse complémentaire | `adresse_complementaire` | `@DETAIL` | |
| 15 | Code postal | `code_postal` | `@DETAIL` | |
| 16 | Adresse électronique | `mail_01` | `@DETAIL` | |
| 17 | Adresse mail du salarié (Module CP) | `mail_conge` | `@DETAIL` | module Congés Payés |
| 18 | Adresse mail | `mail_coff_fort` | `@DETAIL` | coffre-fort |
| 19 | Téléphone 1 | `telephone_01` | `@DETAIL` | |
| 20 | Téléphone 2 | `telephone_02` | `@DETAIL` | |
| 21 | Téléphone 3 | `telephone_portable` | `@DETAIL` | pas de champ telephone_03 |

## Chaîne `champs`
```
nom@LIST;prenom@DETAIL;matricule@LIST;libelle_societe@DETAIL;motif_depart@DETAIL;categorie_professionnelle_libelle@DETAIL;sexe@DETAIL;type_contrat_code@DETAIL;date_debut_contrat@LIST;date_fin_contrat@LIST;date_naissance@DETAIL;adresse@DETAIL;adresse_complementaire@DETAIL;code_postal@DETAIL;mail_01@DETAIL;mail_conge@DETAIL;mail_coff_fort@DETAIL;telephone_01@DETAIL;telephone_02@DETAIL;telephone_portable@DETAIL
```

## Requête SQL (paramétrage)
> ⚠️ Nom de table et `email_to` à confirmer. La sélection des salariés sortis reste à résoudre côté moteur (cf. point bloquant).
```sql
INSERT INTO rh_nibelis.extraction_config
    (libelle, description, matricules, champs, cron, email_to, active, created_by)
VALUES
    ('PROD-Tresorerie-Departs',
     'Extraction Trésorerie : salariés sortis (coordonnées, RIB/contacts, motif départ)',
     '*',
     'nom@LIST;prenom@DETAIL;matricule@LIST;libelle_societe@DETAIL;motif_depart@DETAIL;categorie_professionnelle_libelle@DETAIL;sexe@DETAIL;type_contrat_code@DETAIL;date_debut_contrat@LIST;date_fin_contrat@LIST;date_naissance@DETAIL;adresse@DETAIL;adresse_complementaire@DETAIL;code_postal@DETAIL;mail_01@DETAIL;mail_conge@DETAIL;mail_coff_fort@DETAIL;telephone_01@DETAIL;telephone_02@DETAIL;telephone_portable@DETAIL',
     '0 0 7 * * ?',
     'tresorerie@ga.fr',
     true,
     'NIBELIS_EXTRACT');
```
