---
tags: [nibelis, extraction, spec, talend, IT, comptabilité, trésorerie]
projet: GA - API Nibelis
type: spec-fonctionnelle
objet: Comparaison au développement Talend en place
exports: [IT, IT2 Flotte téléphones, Comptabilité, Trésorerie]
created: 2026-07-24
updated: 2026-07-24
---

# Spec fonctionnelle — Exports Nibelis (IT, IT2, Comptabilité, Trésorerie)

> **Objet** : décrire précisément les 4 exports (population, source, colonnes, transformations, format, livraison) afin de les **comparer au développement Talend en place** et repérer les écarts (« trous »).
> Référence d'implémentation : `Documents/Claude/Nibelis/gen_extractions.py`. Champs source : [[01-API-Nibelis-Reference]].

## 1. Généralités (communes aux 4 exports)

| Élément | Règle |
|---|---|
| **Source** | API REST Nibelis — `https://api.nibelis.com/` |
| **Auth** | `POST portail/users/login` `{email, password}` → `data.access_token` (Bearer) |
| **Endpoints** | `GET api/salaries?id_societe` (liste) · `GET api/salaries/{id_nibelis}` (fiche) · `GET api/salaries/champ-utilisateur?id_nibelis&periode` (champ utilisateur, ex. Localisation) |
| **Débit** | ~2 appels/s constatés, aucun throttling jusqu'à 6-8 appels parallèles (la limite « 1/2 s » des vieilles notes est trop prudente) |
| **Périmètre sociétés (défaut)** | **toutes les sociétés SAUF OSSABOIS Fictive (5572)** → 888 salariés actifs. ⚠️ **OSSABOIS (2662) est INCLUS** (contrairement à l'import Elevo). *À confirmer par export.* |
| **Format sortie** | 1 fichier Excel `.xlsx`, 1 onglet, en-tête stylée figée (ligne 1), 1 ligne / salarié |
| **Période** | paramètre d'extraction (`PERIODE`, ex. `2026-05-01`), reporté en 1ʳᵉ colonne |
| **Livraison / cadence** | ⏳ *à confirmer* (dépôt ? mail au destinataire ? mensuel ?) |

### Notation source des champs
- **`@LIST`** = renvoyé par `api/salaries?id_societe` (1 appel/société) : `matricule`, `nom`, `date_embauche`, `date_anciennete`, `date_depart`, `date_debut_contrat`, `date_fin_contrat`, `numero_contrat`.
- **`@DETAIL`** = renvoyé par la fiche `api/salaries/{id}` (1 appel/salarié) : tout le reste (dont `prenom`, société, établissement, mails, téléphones, adresse…).

## 2. Règles de transformation communes ⚠️ (points critiques pour le benchmark Talend)

Ce sont les endroits où un développement peut diverger sans que ce soit visible :

| Règle | Détail | Piège |
|---|---|---|
| **Mail pro** | `mail_conge` (Module Congés Payés) | ⚠️ **PAS `mail_01`** : `mail_01` est perso chez GA, pro chez OSSABOIS → non fiable. `mail_conge` = pro fiable (667/984) |
| **Mails perso** | `mail_02` et `mail_coff_fort` = adresses persos (gmail, laposte…) | 3 mails distincts en Trésorerie (voir §6) |
| **Emploi** | `emploi_sexe` (libellé genré, ex. « Comptable ») | ⚠️ PAS `emploi_libelle` (« COMPTABLE HF ») |
| **Contrat** | `type_contrat_code` (`CDI`, `CDD`, `APPR`, `PROF`, `STAG`, `STAG_PROF`) | ⚠️ PAS le libellé `type_contrat` (« Contrat à durée déterminée ») |
| **Dates** | source Nibelis = **texte ISO** `"YYYY-MM-DD"` → export = **date Excel** (`dd/MM/yyyy`) | changement de **type** (texte → date), pas juste de format |
| **Responsable hiér.** | `resp_hier_matricule` / `resp_hier_seco_matricule` | ⚠️ le **matricule**, PAS le Nom/Prénom (pas de 2ᵉ lookup) |
| **Localisation** | champ utilisateur id 6 via `champ-utilisateur` (`id_nibelis`+`periode`) | actuellement **laissée vide** dans le code (colonne présente mais non alimentée) |
| **Téléphone 3** | `telephone_portable` | ⚠️ il n'existe **pas** de champ `telephone_03` |

---

## 3. Export IT

- **Destinataire** : service IT · **Population** : actifs, toutes sociétés (hors Fictive) · **13 colonnes**

| # | Colonne | Champ Nibelis | Source | Transfo |
|---|---|---|---|---|
| 1 | Période | *(paramètre)* | — | — |
| 2 | Nom | `nom` | @LIST | — |
| 3 | Prénom | `prenom` | @DETAIL | — |
| 4 | Matricule | `matricule` | @LIST | — |
| 5 | Société | `libelle_societe` | @DETAIL | — |
| 6 | Établissement | `libelle_etablissement` | @DETAIL | — |
| 7 | Localisation | champ utilisateur (id 6) | @CU | ⚠️ **vide** aujourd'hui |
| 8 | Service | `service_libelle` | @DETAIL | — |
| 9 | Emploi | `emploi_sexe` | @DETAIL | genré |
| 10 | Catégorie | `categorie_professionnelle_libelle` | @DETAIL | — |
| 11 | Responsable hiér. : Nom | `resp_hier_matricule` | @DETAIL | ⚠️ matricule |
| 12 | Responsable hiér. seco. : Nom | `resp_hier_seco_matricule` | @DETAIL | ⚠️ matricule |
| 13 | Adresse mail du salarié (Module CP) | `mail_conge` | @DETAIL | mail pro |

---

## 4. Export IT2 — Flotte téléphones

- **Destinataire** : IT (téléphonie) · **Population** : actifs, toutes sociétés (hors Fictive) · **15 colonnes**

| # | Colonne | Champ Nibelis | Source | Transfo |
|---|---|---|---|---|
| 1 | Période | *(paramètre)* | — | — |
| 2 | Nom | `nom` | @LIST | — |
| 3 | Prénom | `prenom` | @DETAIL | — |
| 4 | Société | `libelle_societe` | @DETAIL | — |
| 5 | Établissement | `libelle_etablissement` | @DETAIL | — |
| 6 | Localisation | champ utilisateur (id 6) | @CU | ⚠️ **vide** aujourd'hui |
| 7 | Service | `service_libelle` | @DETAIL | — |
| 8 | Équipe | `equipe` | @DETAIL | — |
| 9 | Emploi | `emploi_sexe` | @DETAIL | genré |
| 10 | Catégorie | `categorie_professionnelle_libelle` | @DETAIL | — |
| 11 | Sexe | `sexe` | @DETAIL | `H`/`F` |
| 12 | Contrat | `type_contrat_code` | @DETAIL | code |
| 13 | Début de contrat | `date_debut_contrat` | @LIST | date Excel |
| 14 | Fin de contrat | `date_fin_contrat` | @LIST | date Excel |
| 15 | Adresse mail du salarié (Module CP) | `mail_conge` | @DETAIL | mail pro |

---

## 5. Export Comptabilité

- **Destinataire** : Comptabilité · **Population** : effectifs actifs, toutes sociétés (hors Fictive) · **13 colonnes** (en-tête ligne 13 du modèle « Gestion avancée »)

| # | Colonne | Champ Nibelis | Source | Transfo |
|---|---|---|---|---|
| 1 | Période | *(paramètre)* | — | — |
| 2 | Nom | `nom` | @LIST | — |
| 3 | Prénom | `prenom` | @DETAIL | — |
| 4 | Matricule | `matricule` | @LIST | — |
| 5 | Société | `libelle_societe` | @DETAIL | — |
| 6 | Établissement | `libelle_etablissement` | @DETAIL | — |
| 7 | Catégorie | `categorie_professionnelle_libelle` | @DETAIL | — |
| 8 | Sexe | `sexe` | @DETAIL | `H`/`F` |
| 9 | Contrat | `type_contrat_code` | @DETAIL | code |
| 10 | Début de contrat | `date_debut_contrat` | @LIST | date Excel |
| 11 | Fin de contrat | `date_fin_contrat` | @LIST | date Excel |
| 12 | Équipe | `equipe` | @DETAIL | — |
| 13 | Adresse mail du salarié (Module CP) | `mail_conge` | @DETAIL | mail pro |

---

## 6. Export Trésorerie ⚠️ population particulière

- **Destinataire** : Trésorerie · **Population = salariés SORTIS** (départs) · **21 colonnes**

### 🔑 Règle de population (le point clé vs Talend)
`api/salaries?id_societe` **standard ne renvoie QUE les actifs** → les sortis sont invisibles. Il faut :
```
GET api/salaries?id_societe={X}&optionFiltrage=2   → actifs + SORTIS
    puis filtrer les lignes ayant une date_depart renseignée
```
(`optionFiltrage=2` = 268 lignes sur 6961 dont **145 sortis** ; `optionFiltrage=0/1` = 123 actifs.) La fiche `api/salaries/{id}` fonctionne ensuite normalement pour un sorti.
> ⚠️ **À vérifier dans le Talend** : utilise-t-il bien `optionFiltrage=2` (ou équivalent) pour capter les sortis ? Sinon l'export est **vide/faux**.

### Colonnes

| # | Colonne | Champ Nibelis | Source | Transfo |
|---|---|---|---|---|
| 1 | Période | *(paramètre)* | — | — |
| 2 | Nom | `nom` | @LIST | — |
| 3 | Prénom | `prenom` | @DETAIL | — |
| 4 | Matricule | `matricule` | @LIST | — |
| 5 | Société | `libelle_societe` | @DETAIL | — |
| 6 | Motif départ | `motif_depart` | @DETAIL | — |
| 7 | Catégorie | `categorie_professionnelle_libelle` | @DETAIL | — |
| 8 | Sexe | `sexe` | @DETAIL | `H`/`F` |
| 9 | Contrat | `type_contrat_code` | @DETAIL | code |
| 10 | Début de contrat | `date_debut_contrat` | @LIST | date Excel |
| 11 | Fin de contrat | `date_fin_contrat` | @LIST | date Excel |
| 12 | Date de naissance | `date_naissance` | @DETAIL | date Excel *(libellé modèle tronqué « Date de naissance (J »)* |
| 13 | Adresse | `adresse` | @DETAIL | — |
| 14 | Adresse complémentaire | `adresse_complementaire` | @DETAIL | — |
| 15 | Code postal | `code_postal` | @DETAIL | — |
| 16 | Adresse électronique | `mail_02` *(perso)* | @DETAIL | ⚠️ **à confirmer** : `mail_01` (note) vs `mail_02` (code). Pour un sorti, le **perso** (`mail_02`) est plus pertinent (mail pro désactivé) |
| 17 | Adresse mail du salarié (Module CP) | `mail_conge` *(pro)* | @DETAIL | — |
| 18 | Adresse mail | `mail_coff_fort` *(perso coffre-fort)* | @DETAIL | — |
| 19 | Téléphone 1 | `telephone_01` | @DETAIL | — |
| 20 | Téléphone 2 | `telephone_02` | @DETAIL | — |
| 21 | Téléphone 3 | `telephone_portable` | @DETAIL | ⚠️ pas de `telephone_03` |

---

## 7. Grille de comparaison au Talend (checklist des « trous » probables)

Points où le Talend en place risque de diverger — à cocher un par un :

- [ ] **Population Trésorerie** : capte-t-il les **sortis** (`optionFiltrage=2` ou équivalent) ? *(risque n°1)*
- [ ] **Mail pro** : utilise-t-il `mail_conge` ou (à tort) `mail_01` ?
- [ ] **« Adresse électronique » Trésorerie** : `mail_01` ou `mail_02` ?
- [ ] **Emploi** : `emploi_sexe` (genré) ou `emploi_libelle` (avec « HF ») ?
- [ ] **Contrat** : `type_contrat_code` ou le libellé ?
- [ ] **Dates** : sorties en **date Excel** (`dd/MM/yyyy`) ou en texte ?
- [ ] **Responsable hiér.** : matricule ou Nom/Prénom résolu ?
- [ ] **Localisation** : colonne alimentée (via `champ-utilisateur`) ou vide ?
- [ ] **Périmètre sociétés** : OSSABOIS (2662) inclus ou exclu ? Fictive (5572) bien exclue ?
- [ ] **Ordre & libellés exacts** des colonnes conformes aux modèles (ex. « Date de naissance (J » tronqué) ?
- [ ] **Cadence & destinataires** identiques ?

## 8. Points ouverts (métier / infra)
- [ ] Périmètre sociétés définitif par export.
- [ ] `email_to` réels des destinataires (IT, Trésorerie, Comptabilité…).
- [ ] Cadence (mensuel probable) et canal de livraison.
- [ ] « Adresse électronique » Trésorerie : trancher `mail_01` vs `mail_02`.
- [ ] Localisation : à alimenter ou laisser vide selon besoin.

## Liens
- [[Nibelis Extract - Projet]] · [[Nibelis Extract - IT]] · [[Nibelis Extract - IT2 Flotte téléphones]] · [[Nibelis Extract - Comptabilité]] · [[Nibelis Extract - Trésorerie]]
