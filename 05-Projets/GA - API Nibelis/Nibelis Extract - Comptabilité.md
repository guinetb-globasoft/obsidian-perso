---
tags: [nibelis, extraction, mapping, comptabilité]
aliases: [Nibelis Comptabilité]
fichier_modele: "Modèle extraction comptabilité.xlsx"
destinataire: Comptabilité
statut: Mapping validé (13 colonnes, en-tête ligne 13)
updated: 2026-06-22
---

# Nibelis Extract — Comptabilité

Voir [[Nibelis Extract - Projet]] pour les règles générales.

> ✅ **Correction 2026-06-22** : le modèle n'était PAS vide. Comme le CDG, c'est un export « Gestion avancée » dont **l'en-tête est en ligne 13** (les lignes 1-12 = paramètres du filtre). **13 colonnes**, 1 ligne / salarié. Mapping vérifié sur ADODO (matricule 10037).

## Fichier modèle
`Documents/Claude/Nibelis/Input/Modèle extraction comptabilité.xlsx` — titre « Effectifs pour Compta », **13 colonnes** (en-tête L13), données à partir de L14. Population = **effectifs actifs** (période mensuelle).

## Mapping des colonnes

Endpoint : `@LIST` = `GET api/salaries?id_societe` · `@DETAIL` = `GET api/salaries/{id_nibelis}` (fiche).

| # | Colonne export | Champ Nibelis | Endpoint | Transformation | Notes |
|---|---|---|---|---|---|
| 1 | Période | *(période d'extraction)* | — | paramètre | mois de l'extraction |
| 2 | Nom | `nom` | `@LIST` | aucune | |
| 3 | Prénom | `prenom` | `@DETAIL` | aucune | absent de la liste → fiche |
| 4 | Matricule | `matricule` | `@LIST` | aucune | |
| 5 | Société | `libelle_societe` | `@DETAIL` | aucune | ex. « GA SAS » |
| 6 | Établissement | `libelle_etablissement` | `@DETAIL` | aucune | |
| 7 | Catégorie | `categorie_professionnelle_libelle` | `@DETAIL` | aucune | ex. « ETAM Bureaux » |
| 8 | Sexe | `sexe` | `@DETAIL` | aucune | `H` / `F` |
| 9 | Contrat | `type_contrat_code` | `@DETAIL` | aucune | ⚠️ **code** (`CDD`), pas le libellé `type_contrat` |
| 10 | Début de contrat | `date_debut_contrat` | `@LIST` | ⚠️ **texte ISO → date Excel** (`datetime`, format `dd/MM/yyyy`) | entrée `"2025-09-08"` (str) → sortie cellule date `08/09/2025` |
| 11 | Fin de contrat | `date_fin_contrat` | `@LIST` | ⚠️ **texte ISO → date Excel** (`datetime`, format `dd/MM/yyyy`) | vide si CDI en cours |
| 12 | Équipe | `equipe` | `@DETAIL` | aucune | ex. « CT » |
| 13 | Adresse mail du salarié (Module CP) | `mail_conge` | `@DETAIL` | aucune | ⚠️ **mail pro `@ga.fr`** (Module Congés Payés), **pas** `mail_01` (souvent perso) |

**Exemple vérifié (ADODO, 10037)** : GA SAS · GA SAS · ETAM Bureaux · F · CDD · 2025-09-08 → 2026-06-06 · CT · adodo@ga.fr.

## Chaîne `champs`
```
nom@LIST;prenom@DETAIL;matricule@LIST;libelle_societe@DETAIL;libelle_etablissement@DETAIL;categorie_professionnelle_libelle@DETAIL;sexe@DETAIL;type_contrat_code@DETAIL;date_debut_contrat@LIST;date_fin_contrat@LIST;equipe@DETAIL;mail_conge@DETAIL
```

## Requête SQL (paramétrage)
> ⚠️ Nom de table et `email_to` à confirmer.
```sql
INSERT INTO rh_nibelis.extraction_config
    (libelle, description, matricules, champs, cron, email_to, active, created_by)
VALUES
    ('PROD-Comptabilite-Effectifs',
     'Extraction Comptabilité : effectifs (identité, société/établissement, catégorie, contrat, équipe, mail pro)',
     '*',
     'nom@LIST;prenom@DETAIL;matricule@LIST;libelle_societe@DETAIL;libelle_etablissement@DETAIL;categorie_professionnelle_libelle@DETAIL;sexe@DETAIL;type_contrat_code@DETAIL;date_debut_contrat@LIST;date_fin_contrat@LIST;equipe@DETAIL;mail_conge@DETAIL',
     '0 0 7 * * ?',
     'comptabilite@ga.fr',
     true,
     'NIBELIS_EXTRACT');
```

## Points ouverts
- [ ] Confirmer le **périmètre sociétés** (toutes ? une seule ?) et l'e-mail réel du destinataire.
- [ ] Confirmer le nom réel de la table de paramétrage.
