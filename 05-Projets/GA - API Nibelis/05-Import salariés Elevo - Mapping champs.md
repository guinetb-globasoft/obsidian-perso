---
tags: ["elevo", "nibelis", "mapping", "GA", "import-utilisateurs", "implémenté"]
projet: GA - API Nibelis
type: mapping-implémenté
cible: Elevo — Import / mise à jour des utilisateurs (Mode A)
source: API Nibelis (fiche + champ utilisateur)
script: Documents/Claude/Nibelis/gen_elevo_import.py
sortie: Output/Elevo - Import utilisateurs (toutes societes).xlsx
created: 2026-06-22
updated: 2026-06-22
---

# Import salariés Elevo — Mapping des champs (Mode A, implémenté)

> Mapping **réellement appliqué** par le script `gen_elevo_import.py` pour générer le fichier Elevo **Mode A** (« Import ou mise à jour des utilisateurs »). Colonne par colonne : champ Nibelis source + endpoint + transformation/calcul.
> Vue d'ensemble & choix de conception : voir [[02-Mapping-Elevo-Nibelis]]. Champs source Nibelis : [[01-API-Nibelis-Reference]].

## En bref

- **Template** : `Elevo - Import ou mise à jour des utilisateurs.xlsx` — **20 colonnes officielles** + **4 colonnes custom GA** = 24 colonnes.
- **Source** : 1 fiche `api/salaries/{id_nibelis}` par salarié (cache `fiches_all.json`) + cache Localisation (champ utilisateur).
- **Sortie** : `Output/Elevo - Import utilisateurs (toutes societes).xlsx`.
- **Volume courant** : **698 salariés** (après exclusions + dédoublonnage).

## Endpoints utilisés

| Endpoint | Rôle | Paramètres | Coût |
|---|---|---|---|
| `POST portail/users/login` | token | `{email, password}` → `data.access_token` | 1 |
| `GET api/salaries?id_societe=…` | liste des `id_nibelis` par société | `id_societe` | 1 / société |
| `GET api/salaries/{id_nibelis}` | **fiche complète** (majorité des champs) | `id_nibelis` (path) | 1 / salarié |
| `GET api/salaries/champ-utilisateur` | **Localisation** (`region`) | `id_nibelis`, `periode` | 1 / salarié |

## Périmètre (sélection des lignes)

| Étape | Règle | Effet |
|---|---|---|
| Exclusion sociétés | `id_societe ∈ {2662, 5572}` retiré (OSSABOIS + OSSABOIS Fictive) + garde-fou sur libellé contenant « ossabois » | −280 |
| Dédoublonnage SIGHT | ligne **SIGHT (6969)** retirée si le matricule existe dans une autre société (on garde l'autre, ex. OMEGA) | −6 |
| Garde-fou doublons | tout matricule déjà vu → ligne ignorée (Elevo rejette les `username` dupliqués) | 0 |
| **Total** | | **698 salariés** |

## Mapping des colonnes (ordre exact du fichier)

Endpoints abrégés : **`salaries/{id}`** = `GET api/salaries/{id_nibelis}` (fiche) · **`champ-utilisateur`** = `GET api/salaries/champ-utilisateur?id_nibelis&periode` · **—** = pas d'appel (constante / calcul local).

| #   | Colonne Elevo            | Champ Nibelis                               | Endpoint Nibelis                        | Transformation / calcul                                      | Notes                                                                                                  |
| --- | ------------------------ | ------------------------------------------- | --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| 1   | `registration_number`    | `matricule`                                 | `salaries/{id}`                         | aucune                                                       |                                                                                                        |
| 2   | `first_name`             | `prenom`                                    | `salaries/{id}`                         | `name_case` (Proper Case par mot)                            | « SOUAL BOUDONIS » → « Soual Boudonis »                                                                |
| 3   | `last_name`              | `nom`                                       | `salaries/{id}`                         | `name_case`                                                  |                                                                                                        |
| 4   | `email`                  | `mail_conge` → *fallback* `mail_01`         | `salaries/{id}`                         | `lower()`                                                    | ⚠️ **`mail_conge` = mail pro `@ga.fr`** (« Module CP »). `mail_01` souvent perso/vide                  |
| 5   | `username`               | `matricule`                                 | `salaries/{id}`                         | aucune                                                       | clé Elevo si pas d'email                                                                               |
| 6   | `manager_email`          | `mail_conge`/`mail_01` **du manager**       | `salaries/{id}` (chaîné sur le manager) | résolution `resp_hier_id_nibelis` → fiche manager, `lower()` | le manager est déjà dans le cache `fiches_all.json`                                                    |
| 7   | `manager_username`       | `resp_hier_matricule`                       | `salaries/{id}`                         | aucune                                                       |                                                                                                        |
| 8   | `job_title`              | `emploi_sexe` → *fallback* `emploi_libelle` | `salaries/{id}`                         | `job_case` (casse phrase)                                    | `emploi_sexe` = libellé genré **sans** « HF » (« Comptable »), pas `emploi_libelle` (« COMPTABLE HF ») |
| 9   | `team_name`              | `service_libelle`                           | `salaries/{id}`                         | aucune                                                       |                                                                                                        |
| 10  | `work_start_date`        | `date_embauche`                             | `salaries/{id}`                         | `iso` → `YYYY-MM-DD`                                         |                                                                                                        |
| 11  | `level`                  | `categorie_professionnelle_libelle`         | `salaries/{id}`                         | aucune                                                       | ex. « Cadre au forfait »                                                                               |
| 12  | `department`             | `libelle_etablissement`                     | `salaries/{id}`                         | aucune                                                       | ⚠️ **choix GA : établissement → `department`**                                                         |
| 13  | `service`                | `service_libelle`                           | `salaries/{id}`                         | aucune                                                       |                                                                                                        |
| 14  | `gender`                 | `sexe`                                      | `salaries/{id}`                         | `H`→`male`, `F`→`female`, autre→`other`                      |                                                                                                        |
| 15  | `region`                 | champ utilisateur **Localisation** (id 6)   | **`champ-utilisateur`**                 | lookup cache par `id_nibelis`                                | seul champ **hors fiche** ; cache `localisations_*.json`                                               |
| 16  | `entity`                 | `libelle_societe`                           | `salaries/{id}`                         | aucune                                                       | ⚠️ **choix GA : société → `entity`**                                                                   |
| 17  | `locale`                 | —                                           | —                                       | **constante `"fr"`**                                         |                                                                                                        |
| 18  | `content_locale`         | —                                           | —                                       | **constante `"fr"`**                                         | spécifique Mode A                                                                                      |
| 19  | `working_time_ratio`     | `type_forfait`, `horaire_mensuel`           | `salaries/{id}`                         | **calcul** (voir ci-dessous)                                 | temps de travail en %                                                                                  |
| 20  | `use_sso`                | —                                           | —                                       | **vide**                                                     | vide = SSO actif si configuré côté Elevo                                                               |
| 21  | `custom_type_de_contrat` | `type_contrat_libelle`                      | `salaries/{id}`                         | aucune                                                       | « Contrat à durée indéterminée »                                                                       |
| 22  | `custom_code_contrat`    | `type_contrat_code`                         | `salaries/{id}`                         | aucune                                                       | « CDI » / « CDD » / « APPR » / « PROF » / « STAG » / « STAG_PROF »                                     |
| 23  | `custom_niveau`          | `niveau`                                    | `salaries/{id}`                         | aucune                                                       |                                                                                                        |
| 24  | `custom_coefficient`     | `coefficient`                               | `salaries/{id}`                         | `str()` (numérique → texte)                                  |                                                                                                        |

> `organization_admin` est calculé (vide) dans le script mais **n'existe pas** dans le template officiel → **non exporté**.
> **23 des 24 colonnes** viennent de la fiche `api/salaries/{id}` ; seule `region` nécessite un 2ᵉ endpoint (`champ-utilisateur`).

## Détail des transformations

```python
# Casse propre par mot (prénom / nom)
name_case("SOUAL BOUDONIS")            # -> "Soual Boudonis"

# Casse phrase (intitulé de poste)
job_case("CHARGÉE DE FORMATION PRO")   # -> "Chargée de formation pro"

# Date ISO
iso("2015-02-25T00:00:00")             # -> "2015-02-25"   (troncature à 10 car.)

# Genre
gender("H") -> "male" ; gender("F") -> "female" ; sinon -> "other"
```

### `working_time_ratio` (temps de travail en %)

```
si type_forfait == "J"            -> 100          # forfait jours = cadre temps plein
sinon                             -> round(horaire_mensuel / 151.67 * 100)
                                     plafonné à 100   (Elevo exige 0 ≤ ratio ≤ 100)
si valeur illisible / absente     -> 100          # défaut
```
> `151.67` = base mensuelle 35 h. Ex. `horaire_mensuel = 151.67` → **100**.

## Colonnes custom — à créer chez Elevo

Les 4 colonnes `custom_*` doivent être **créées côté support Elevo** (`support@elevo.io`) avec **ces intitulés machine exacts**, sinon elles sont ignorées à l'import.

| Colonne | Source Nibelis | Endpoint | Couverture (984 fiches) |
|---|---|---|---|
| `custom_type_de_contrat` | `type_contrat_libelle` | `salaries/{id}` | 984/984 |
| `custom_code_contrat` | `type_contrat_code` | `salaries/{id}` | 984/984 |
| `custom_niveau` | `niveau` | `salaries/{id}` | 737/984 |
| `custom_coefficient` | `coefficient` | `salaries/{id}` | 703/984 |

## Points de vigilance

- **Email pro** : toujours `mail_conge` en priorité (`mail_01` = souvent perso/vide chez GA).
- **`department` / `entity`** : correspondances volontaires (établissement → department, société → entity) — à valider si l'usage Elevo change.
- **`region` (Localisation)** : nécessite le cache champ utilisateur à jour (`fetch_localisation_all.py`, `periode` courante) ; 1 appel/salarié en plus de la fiche.
- **Alternants** : `niveau`/`coefficient` parfois vides (normal).
- **Débit API** : ~2 appels/s constatés sans throttling (la limite « 1/2 s » des anciennes notes est trop prudente).

## Liens
- [[02-Mapping-Elevo-Nibelis]] — analyse & choix de conception (Mode A vs SFTP)
- [[01-API-Nibelis-Reference]] — champs source Nibelis
- [[03-Mapping-Elevo-Parcours-Professionnel]] — import du parcours (rému + poste)
