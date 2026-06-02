---
tags: [nibelis, extraction, mapping, IT]
aliases: [Nibelis IT]
fichier_modele: "Modèle extraction IT.xlsx"
destinataire: IT
statut: Mapping validé (sauf resp. hiér. = id)
---

# Nibelis Extract — IT

Voir [[Nibelis Extract - Projet]] pour les règles générales et le dictionnaire complet.

## Fichier modèle
`Documents/Claude/Nibelis/Input/Modèle extraction IT.xlsx` — 13 colonnes, 1 ligne / salarié.

## Mapping des colonnes

| # | Colonne export | Champ API | Source | Note |
|---|---|---|---|---|
| 1 | Période | *(période d'extraction)* | — | paramètre, pas un champ |
| 2 | Nom | `nom` | `@LIST` | |
| 3 | Prénom | `prenom` | `@DETAIL` | absent de la liste |
| 4 | Matricule | `matricule` | `@LIST` | |
| 5 | Société | `libelle_societe` | `@DETAIL` | |
| 6 | Établissement | `libelle_etablissement` | `@DETAIL` | |
| 7 | Localisation | champ utilisateur `Localisation` | `@CU` | id_champ_utilisateur=6 |
| 8 | Service | `service_libelle` | `@DETAIL` | |
| 9 | Emploi | `emploi_sexe` | `@DETAIL` | libellé genré |
| 10 | Catégorie | `categorie_professionnelle_libelle` | `@DETAIL` | |
| 11 | Responsable hiér. : Nom | `resp_hier_id_nibelis` | `@DETAIL` | id conservé (pas de résolution du nom) |
| 12 | Responsable hiér. seco. : Nom | `resp_hier_seco_id_nibelis` | `@DETAIL` | idem |
| 13 | Adresse mail du salarié (Module CP) | `mail_conge` | `@DETAIL` | module Congés Payés |

## Chaîne `champs`
```
nom@LIST;prenom@DETAIL;matricule@LIST;libelle_societe@DETAIL;libelle_etablissement@DETAIL;Localisation@CU;service_libelle@DETAIL;emploi_sexe@DETAIL;categorie_professionnelle_libelle@DETAIL;resp_hier_id_nibelis@DETAIL;resp_hier_seco_id_nibelis@DETAIL;mail_conge@DETAIL
```

## Requête SQL (paramétrage)
> ⚠️ Table `rh_nibelis.extraction_config` = nom à confirmer. `email_to` à remplacer par le vrai destinataire IT.
```sql
INSERT INTO rh_nibelis.extraction_config
    (libelle, description, matricules, champs, cron, email_to, active, created_by)
VALUES
    ('PROD-IT-Annuaire',
     'Extraction IT : annuaire salariés (localisation, service, responsable, mail CP)',
     '*',
     'nom@LIST;prenom@DETAIL;matricule@LIST;libelle_societe@DETAIL;libelle_etablissement@DETAIL;Localisation@CU;service_libelle@DETAIL;emploi_sexe@DETAIL;categorie_professionnelle_libelle@DETAIL;resp_hier_id_nibelis@DETAIL;resp_hier_seco_id_nibelis@DETAIL;mail_conge@DETAIL',
     '0 0 7 * * ?',
     'it@ga.fr',
     true,
     'NIBELIS_EXTRACT');
```
