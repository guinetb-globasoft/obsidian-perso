---
tags: [nibelis, extraction, mapping, IT]
aliases: [Nibelis IT2, Flotte téléphones]
fichier_modele: "Modèle extraction IT 2 (flotte téléphones).xlsx"
destinataire: IT (flotte téléphones)
statut: Mapping validé
---

# Nibelis Extract — IT 2 (flotte téléphones)

Voir [[Nibelis Extract - Projet]] pour les règles générales.

## Fichier modèle
`Documents/Claude/Nibelis/Input/Modèle extraction IT 2 (flotte téléphones).xlsx` — 15 colonnes, 1 ligne / salarié. Pas de colonne Matricule.

## Mapping des colonnes

| # | Colonne export | Champ API | Source | Note |
|---|---|---|---|---|
| 1 | Période | *(période d'extraction)* | — | |
| 2 | Nom | `nom` | `@LIST` | |
| 3 | Prénom | `prenom` | `@DETAIL` | |
| 4 | Société | `libelle_societe` | `@DETAIL` | |
| 5 | Établissement | `libelle_etablissement` | `@DETAIL` | |
| 6 | Localisation | champ utilisateur `Localisation` | `@CU` | id=6 |
| 7 | Service | `service_libelle` | `@DETAIL` | |
| 8 | Équipe | `equipe` | `@DETAIL` | code (ex. CT) |
| 9 | Emploi | `emploi_sexe` | `@DETAIL` | |
| 10 | Catégorie | `categorie_professionnelle_libelle` | `@DETAIL` | |
| 11 | Sexe | `sexe` | `@DETAIL` | |
| 12 | Contrat | `type_contrat_code` | `@DETAIL` | code (ex. CDD) |
| 13 | Début de contrat | `date_debut_contrat` | `@LIST` | |
| 14 | Fin de contrat | `date_fin_contrat` | `@LIST` | |
| 15 | Adresse mail du salarié (Module CP) | `mail_conge` | `@DETAIL` | |

## Chaîne `champs`
```
nom@LIST;prenom@DETAIL;libelle_societe@DETAIL;libelle_etablissement@DETAIL;Localisation@CU;service_libelle@DETAIL;equipe@DETAIL;emploi_sexe@DETAIL;categorie_professionnelle_libelle@DETAIL;sexe@DETAIL;type_contrat_code@DETAIL;date_debut_contrat@LIST;date_fin_contrat@LIST;mail_conge@DETAIL
```

## Requête SQL (paramétrage)
> ⚠️ Nom de table et `email_to` à confirmer.
```sql
INSERT INTO rh_nibelis.extraction_config
    (libelle, description, matricules, champs, cron, email_to, active, created_by)
VALUES
    ('PROD-IT-FlotteTelephones',
     'Extraction IT : flotte téléphones (contrat, équipe, mail CP)',
     '*',
     'nom@LIST;prenom@DETAIL;libelle_societe@DETAIL;libelle_etablissement@DETAIL;Localisation@CU;service_libelle@DETAIL;equipe@DETAIL;emploi_sexe@DETAIL;categorie_professionnelle_libelle@DETAIL;sexe@DETAIL;type_contrat_code@DETAIL;date_debut_contrat@LIST;date_fin_contrat@LIST;mail_conge@DETAIL',
     '0 0 7 * * ?',
     'it@ga.fr',
     true,
     'NIBELIS_EXTRACT');
```
