---
tags: [nibelis, extraction, mapping, CDG, EVP]
aliases: [Nibelis CDG, Contrôle de gestion]
fichier_modele: "Modèle Extraction CDG.xlsx"
destinataire: Contrôle de gestion
statut: Mapping ossature validé — EVP dynamiques
---

# Nibelis Extract — CDG (Contrôle de gestion)

Voir [[Nibelis Extract - Projet]] pour les règles générales.

## Fichier modèle
`Documents/Claude/Nibelis/Input/Modèle Extraction CDG.xlsx` — 72 colonnes : **16 colonnes fixes (fiche) + ~56 colonnes EVP** (éléments variables de paie). C'est l'extraction la plus complète.

## Ossature fixe (16 premières colonnes)

| # | Colonne export | Champ API | Source |
|---|---|---|---|
| 1 | Période | *(période d'extraction)* | — |
| 2 | Nom | `nom` | `@LIST` |
| 3 | Prénom | `prenom` | `@DETAIL` |
| 4 | Matricule | `matricule` | `@LIST` |
| 5 | Matricule groupe | `matricule_groupe` | `@DETAIL` |
| 6 | Société | `libelle_societe` | `@DETAIL` |
| 7 | Établissement | `libelle_etablissement` | `@DETAIL` |
| 8 | Sexe | `sexe` | `@DETAIL` |
| 9 | Emploi | `emploi_sexe` | `@DETAIL` |
| 10 | Contrat | `type_contrat_code` | `@DETAIL` |
| 11 | Catégorie | `categorie_professionnelle_libelle` | `@DETAIL` |
| 12 | Équipe | `equipe` | `@DETAIL` |
| 13 | Service | `service_libelle` | `@DETAIL` |
| 14 | Date Ancienneté | `date_anciennete` | `@LIST` |
| 15 | Date de départ | `date_depart` | `@LIST` |
| 16 | Date de naissance | `date_naissance` | `@DETAIL` |

## Colonnes EVP (dynamiques)
Les ~56 colonnes suivantes (salaire base, primes, avantages en nature, forfaits, participation…) sont des **EVP** : pas de code stable côté `champs`. Récupération via `api/element-variable-paie/evp-accessible?id_societe` (liste + libellés) puis `api/element-variable-paie?id_nibelis&code_variable&periode` (valeur par salarié/période). Cf. script `nibelis_extraction.py` (génère exactement cette ossature + EVP).

## Chaîne `champs`
Vu le nombre d'EVP, utiliser le joker :
```
*
```
*(= fiche complète + tous les EVP accessibles).* Si on veut figer l'ossature sans EVP, voir le bloc explicite dans [[Nibelis Extract - Projet]].

## Requête SQL (paramétrage)
> ⚠️ Nom de table et `email_to` à confirmer.
```sql
INSERT INTO rh_nibelis.extraction_config
    (libelle, description, matricules, champs, cron, email_to, active, created_by)
VALUES
    ('PROD-CDG-Complet',
     'Extraction Contrôle de gestion : fiche complète + tous les EVP (salaire, primes, AN...)',
     '*',
     '*',
     '0 0 7 * * ?',
     'cdg@ga.fr',
     true,
     'NIBELIS_EXTRACT');
```
