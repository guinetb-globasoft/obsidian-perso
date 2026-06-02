---
tags: [projet, nibelis, api, extraction, talend]
aliases: [Nibelis Extract, API Nibelis]
source: API Nibelis (paie)
cible: Fichiers Excel par destinataire
statut: En cadrage
maj: 2026-06-02
---

# Nibelis Extract — Projet

## Objectif

Remplacer l'envoi manuel d'extractions Excel par les RH : appeler l'**API REST Nibelis** pour générer automatiquement, par destinataire, un fichier Excel mensuel. Pilotage par une **table de paramétrage** (1 ligne = 1 abonnement/destinataire).

## API Nibelis

- Base PROD : `https://api.nibelis.com/`
- Compte API : `api_nibelis_talend@ga.fr` (identifiants dans `Documents/Claude/Nibelis/nibelis_extraction.py`)
- **Limite de débit : 1 appel maximum toutes les 2 secondes.**
- Auth : `POST portail/users/login` `{email, password}` → `data.access_token` (Bearer).
- Collection Postman : `Documents/Claude/Nibelis/Input/API REST Nibelis PROD.postman_collection.json`

### Endpoints utiles à l'extraction

| Usage | Endpoint | Paramètres |
|---|---|---|
| Token | `POST portail/users/login` | `email`, `password` |
| Liste salariés | `GET api/salaries` | `id_societe` |
| Fiche salarié | `GET api/salaries/{id_nibelis}` | (path) |
| Champ utilisateur | `GET api/salaries/champ-utilisateur` | `id_nibelis`, `periode` |
| EVP accessibles | `GET api/element-variable-paie/evp-accessible` | `id_societe` |
| Lire un EVP | `GET api/element-variable-paie` | `id_nibelis`, `code_variable`, `periode` |

## Règle des annotations `champs`

La colonne `champs` liste les champs à extraire sous forme `code@SOURCE`, séparés par `;`. `champs = *` = tous les champs (fiche complète + EVP). L'annotation indique **dans quel endpoint** le champ est lu :

| Annotation | Source | Coût |
|---|---|---|
| `@LIST` | `api/salaries?id_societe` | 1 appel / société |
| `@DETAIL` | `api/salaries/{id_nibelis}` | 1 appel / salarié |
| `@CU` *(proposé, à ajouter au validateur)* | `api/salaries/champ-utilisateur?id_nibelis&periode` | 1 appel / salarié / période |

⚠️ **Les lignes `TEST-*` (`INIT_QUAL_V2`) ont des annotations FAUSSES** (ex. `prenom@LIST` alors que `prenom` n'existe pas dans la liste). Ne pas s'en servir de référence.

### Champs réellement renvoyés par la **liste** (donc seuls éligibles à `@LIST`)
`matricule`, `nom`, `date_embauche`, `date_anciennete`, `date_depart`, `date_debut_contrat`, `date_fin_contrat`, `numero_contrat` (+ `id_*`, `present_periode`, `bulletin_periode`, `multi_fiche`, `ordr`). **`prenom` n'y est pas → `@DETAIL`.**

## Dictionnaire de mapping (libellé export → champ API)

Vérifié sur le terrain (matricule 10037 ADODO, société 6961).

| Libellé colonne export | Champ API | Source |
|---|---|---|
| Période | *(période d'extraction — paramètre)* | — |
| Nom | `nom` | `@LIST` |
| Prénom | `prenom` | `@DETAIL` |
| Matricule | `matricule` | `@LIST` |
| Matricule groupe | `matricule_groupe` | `@DETAIL` |
| Société | `libelle_societe` | `@DETAIL` |
| Établissement | `libelle_etablissement` | `@DETAIL` |
| Service | `service_libelle` | `@DETAIL` |
| Équipe | `equipe` | `@DETAIL` |
| Emploi | `emploi_sexe` | `@DETAIL` |
| Catégorie | `categorie_professionnelle_libelle` | `@DETAIL` |
| Sexe | `sexe` | `@DETAIL` |
| Contrat | `type_contrat_code` | `@DETAIL` |
| Début de contrat | `date_debut_contrat` | `@LIST` |
| Fin de contrat | `date_fin_contrat` | `@LIST` |
| Date Ancienneté | `date_anciennete` | `@LIST` |
| Date de départ | `date_depart` | `@LIST` |
| Motif départ | `motif_depart` | `@DETAIL` |
| Date de naissance | `date_naissance` | `@DETAIL` |
| Adresse | `adresse` | `@DETAIL` |
| Adresse complémentaire | `adresse_complementaire` | `@DETAIL` |
| Code postal | `code_postal` | `@DETAIL` |
| Adresse électronique | `mail_01` | `@DETAIL` |
| Adresse mail du salarié (Module CP) | `mail_conge` | `@DETAIL` |
| Adresse mail | `mail_coff_fort` | `@DETAIL` |
| Téléphone 1 | `telephone_01` | `@DETAIL` |
| Téléphone 2 | `telephone_02` | `@DETAIL` |
| Téléphone 3 | `telephone_portable` | `@DETAIL` |
| Responsable hiér. : Nom | `resp_hier_id_nibelis` | `@DETAIL` *(on garde l'id, pas de résolution du nom)* |
| Responsable hiér. seco. : Nom | `resp_hier_seco_id_nibelis` | `@DETAIL` *(idem)* |
| Localisation | champ utilisateur `Localisation` (id 6) | `@CU` |

### Pièges de mapping (corrections vérifiées)
- « Module CP » = **module Congés Payés** → `mail_conge` (≠ `mail_01`, qui peut être un mail perso).
- « Contrat » = `type_contrat_code` (`CDD`), pas le libellé `type_contrat` (« Contrat à durée déterminée »).
- « Emploi » = `emploi_sexe` (libellé genré « COMPTABLE »), pas `emploi_libelle` (« COMPTABLE HF »).
- « Téléphone 3 » = `telephone_portable` (pas de champ `telephone_03`).

## Champs utilisateurs disponibles (`api/salaries/champ-utilisateur`)
`Manager`, `Personnel chantier`, `Niveau Hay`, `CODIR`, **`Localisation`**, `SITE`, `Catégorie PaieGRH`, `Temps de travail`, `Support ou Opérationnel`.

## Points ouverts / à cadrer

- [ ] **Population « Trésorerie » = salariés SORTIS** : les 9 matricules du modèle sont tous absents de `api/salaries` (même avec `&periode=2025-12-01`). L'endpoint liste ne renvoie jamais les sortis → trouver comment obtenir leur `id_nibelis` (param non documenté ? autre endpoint ?).
- [ ] **Comptabilité** : modèle Excel vide (« Gestion avancée ») → obtenir la spec des colonnes.
- [ ] Ajouter l'annotation `@CU` au validateur de `champs`.
- [ ] Nom réel de la table de paramétrage (schéma/table) à confirmer pour les `INSERT`.
- [ ] E-mails réels des destinataires.

## Notes de mapping par fichier
- [[Nibelis Extract - IT]]
- [[Nibelis Extract - IT2 Flotte téléphones]]
- [[Nibelis Extract - Trésorerie]]
- [[Nibelis Extract - CDG]]
- [[Nibelis Extract - Comptabilité]]

## Liens
- [[Dashboard]]
- [[INT-209 - Nibelis→IFS ODPAIE]]
