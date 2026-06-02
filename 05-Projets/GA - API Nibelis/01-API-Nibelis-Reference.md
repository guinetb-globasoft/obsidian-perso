---
tags: ["nibelis", "api", "GA", "reference", "RH"]
created: 2026-05-29
---

---
projet: GA - API Nibelis
type: référence technique
created: 2026-05-29
---

# API Nibelis — Référence technique

> Note de référence sur les deux endpoints API Nibelis disponibles pour le projet GA, leurs champs, limites et points d'attention.

## Endpoints disponibles

### API 1 — Liste des salariés

```
GET {{url_api_prod}}api/salaries?id_societe={id}
```

Retourne un tableau allégé des salariés d'une société. Sert principalement à récupérer les `id_nibelis` pour itérer ensuite sur l'API 2.

**Champs retournés :**

| Champ | Type | Description |
|---|---|---|
| `id_nibelis` | int | Identifiant unique Nibelis du salarié |
| `matricule` | string | Matricule interne |
| `nom` | string | Nom complet (nom + prénom concaténés dans cet endpoint) |
| `date_embauche` | date | Date d'embauche YYYY-MM-DD |
| `date_anciennete` | date | Date d'ancienneté reprise |
| `date_depart` | date | Date de départ (vide si présent) |
| `date_debut_contrat` | date | Début du contrat en cours |
| `date_fin_contrat` | date | Fin du contrat (vide si CDI) |
| `numero_contrat` | string | Numéro de contrat |
| `present_periode` | O/N | Présent sur la période |
| `bulletin_periode` | O/N | Bulletin sur la période |
| `multi_fiche` | O/N | Multi-fiche |
| `id_societe`, `id_etablissement` | int | Rattachement |
| `ordr` | int | Ordre de tri |

### API 2 — Détail d'un salarié

```
GET {{url_api}}api/salaries/{id_nibelis}
```

Retourne la fiche complète d'un salarié. Inclut tous les champs API 1 + l'ensemble des données RH structurelles.

**Champs additionnels par catégorie :**

#### Identité
- `prenom`, `nom_naissance`, `nom_usuel`, `sexe` (H/F)
- `date_naissance`, `commune_naissance`, `departement_naissance`, `pays_naissance`
- `nationalite`, `situation_familiale`
- `numero_securite_sociale`
- `titr` (Mr/Mme)

#### Contrat
- `type_contrat`, `type_contrat_code` (CDI/CDD/etc.), `type_contrat_libelle`
- `date_debut_contrat`, `date_fin_contrat`, `date_fin_periode_essai`
- `motif_recours_cdd`, `motif_depart`, `date_depart`
- `type_forfait` (J pour jours), `nombre_forfait` (218 jours typique cadre)
- `horaire_mensuel` (151,67h = temps plein), `horaire_hebdo`
- `mode_paiement` (VIRE)

#### Poste & qualification
- `emploi_libelle`, `emploi_code`, `code_inse`
- `categorie_professionnelle_code/libelle` (ex: Cadre au forfait)
- `qualification` (Cadre / ETAM / etc.)
- `convention_collective`
- `coefficient`, `niveau`, `echelon`, `indice`, `position`

#### Organisation
- `id_societe`, `code_societe`, `libelle_societe`, `societe_siren`
- `id_etablissement`, `libelle_etablissement`, `etablissement_siret`
- `departement_libelle`, `service_libelle`
- `equipe`, `division`, `unite`, `regroupement`, `organisation`, `groupe_saisie`

#### Coordonnées
- `adresse`, `adresse_complementaire`, `code_postal`, `commune`, `bureau_distributeur`, `pays`
- `mail_01` (mail principal), `mail_02`, `mail_conge` (Module CP), `mail_coff_fort`
- `telephone_01`, `telephone_02`, `telephone_portable`

#### Hiérarchie
- `resp_hier_id_nibelis`, `resp_hier_matricule`, `resp_hier_societe`
- `resp_hier_seco_id_nibelis`, `resp_hier_seco_matricule`, `resp_hier_seco_societe`
- `resp_form_*`, `resp_cong_*`

#### Avantages
- `avantage_voiture`, `avantage_logement`, `avantage_nourriture`, `avantage_autre`

#### Médecine du travail
- `date_derniere_visite_medicale`, `date_prochaine_visite_medicale`
- `motif_visite_medicale_code/libelle`

#### Handicap (RQTH)
- `travailleur_handicape` (O/N), `statut_boeth`, `taux_invalidite`
- `date_debu_handicape`, `date_fin_handicape`

#### Statut
- `statut_utilisateur` (O/N), `cipd`

## Points d'attention

### Champs disponibles mais nécessitant un traitement

- **Noms des responsables hiérarchiques** : l'API ne retourne que `resp_hier_id_nibelis` et `resp_hier_matricule`. Pour obtenir nom + prénom, il faut un **2ème appel API 2** sur cet ID.
  - Optimisation : dédupliquer les IDs managers avant les appels (N salariés → souvent 5-10 managers uniques).
  - 📌 **Pour l'intégration Elevo**, cet appel chaîné n'est **pas nécessaire** : Elevo se contente de `manager_uniq_identifier` = `resp_hier_id_nibelis` (déjà dispo dans API 2 du salarié). Voir [[02-Mapping-Elevo-Nibelis]].

- **Ratio temps de travail** : pas exposé directement. Calculer depuis `horaire_mensuel` (151,67 = 100%). Attention aux forfaits jours (`type_forfait = J`) où le calcul est différent.

### Champs non identifiés dans l'API

- **Localisation** (valeurs type "LABEGE 1", "NIWA", "PARIS") : présent dans les exports Nibelis mais aucun champ API ne correspond clairement. Ce n'est ni `commune` (adresse perso) ni `bureau_distributeur`. Hypothèses :
  - Champ `unite` ? À vérifier
  - Axe analytique custom (`division`, `regroupement`, `organisation`) ?
  - Champ non exposé par défaut nécessitant une configuration Nibelis
  - ⏳ En attente retour support Nibelis

- **telephone_03** : référencé dans le CDC mais l'API n'expose que `telephone_01`, `telephone_02`, `telephone_portable`. Probablement = `telephone_portable`, à confirmer.

### Hors scope des 2 endpoints

Ces données ne sont **pas accessibles** via `/api/salaries` :
- Éléments de paie (rubriques, brut, net, charges)
- Bulletins
- Heures travaillées (réelles, pas contractuelles)
- Notes de frais (API dédiée existante mais non fonctionnelle selon doc Nibelis — ticket ouvert)
- Données de chèques vacances

→ Endpoints dédiés nécessaires (`/api/bulletins`, `/api/notes-de-frais`, etc.). Demande accès en cours auprès de Nibelis.

## Stratégie d'appels typique

Pour reconstituer un export complet sur N salariés :

1. **API 1** : `/api/salaries?id_societe=X` → liste des `id_nibelis` (1 appel par société)
2. **API 2** : `/api/salaries/{id}` pour chaque salarié → données complètes (N appels)
3. **API 2 bis** (optionnelle) : `/api/salaries/{resp_hier_id_nibelis}` pour chaque manager unique → résolution noms managers (≤ N/5 appels après dédup)

**Coût total estimé** :
- Pour Elevo SFTP : **~Nb_sociétés + N appels** (manager résolu via `manager_uniq_identifier` directement, pas besoin d'appel chaîné)
- Pour un export avec noms managers : **~1,2 × N appels**

## État des accès Nibelis

| Élément | Statut |
|---|---|
| API 1 + API 2 (RH) | ✅ Opérationnel |
| API Notes de frais | ❌ Non fonctionnelle (doc Nibelis incohérente, ticket ouvert) |
| Endpoints paie / rubriques | ⏳ En attente — demande reformulée suite à info de Marie (accès à toutes les rubriques nécessaire) |
| Champ Localisation | ⏳ En attente identification côté Nibelis |

## Liens

- [[02-Mapping-Elevo-Nibelis]] — Mapping vers l'import utilisateurs Elevo (SFTP)
- [[03-Mapping-Elevo-Parcours-Professionnel]] — Mapping vers l'import parcours professionnel Elevo (SFTP)
- [[04-Architecture-SFTP-Elevo]] — Architecture intégration SFTP Elevo
