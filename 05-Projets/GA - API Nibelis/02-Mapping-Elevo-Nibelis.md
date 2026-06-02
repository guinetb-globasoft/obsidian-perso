---
tags: ["elevo", "nibelis", "mapping", "GA", "import-utilisateurs", "sftp"]
created: 2026-05-29
updated: 2026-06-02
---

---
projet: GA - API Nibelis
type: mapping
cible: Elevo — Synchronisation des utilisateurs (SFTP)
source: API Nibelis
created: 2026-05-29
updated: 2026-06-02
sources_elevo: ["Synchroniser les utilisateurs via SFTP – Elevo.pdf", "Elevo - Fichier type synchronisation SFTP (FR).xlsx", "Fichier d'import Elevo x Simbel.xlsx"]
doc_elevo_url: "https://docs.elevo.fr/hc/fr/articles/4403024287249-Ajouter-importer-ou-mettre-%C3%A0-jour-des-utilisateurs"
---


# Mapping Elevo (SFTP) ↔ API Nibelis

> Mapping pour la **synchronisation SFTP** des utilisateurs Elevo depuis Nibelis. Mise à jour majeure suite à la doc Elevo officielle (SFTP, fichier type FR, exemple Simbel). Voir [[01-API-Nibelis-Reference]] pour les champs source et [[04-Architecture-SFTP-Elevo]] pour l'archi.

## 📑 Sommaire

- [[#🔀 Deux modes d'import Elevo — quel template choisir]]
	- [[#Comparaison des deux modes]]
	- [[#Colonnes différentes par mode]]
	- [[#Recommandation pour GA]]
- [[#⚠️ Refonte 2026-05-29 — corrections vs version initiale]]
- [[#Synthèse (Mode B — Sync SFTP, cible projet)]]
- [[#Mapping détaillé (21 colonnes CSV Elevo)]]
	- [[#✅ Récupérables directement (14)]]
	- [[#⚠️ Récupérables avec traitement (3)]]
	- [[#❌ Non disponibles dans Nibelis (4)]]
- [[#Champs custom — option à exploiter]]
- [[#Mapping override (nommage des colonnes)]]
- [[#Comportement de synchronisation (officielle)]]
- [[#Décisions à prendre côté GA]]
- [[#Prérequis bloquants]]
- [[#Flux d'import recommandé (SFTP)]]
- [[#Optimisation : appel chaîné manager]]
- [[#Mapping détaillé (Mode A — Import ponctuel)]]
	- [[#✅ Récupérables directement (13)]]
	- [[#⚠️ Avec traitement (3)]]
	- [[#Spécifiques au Mode A — ❌ Non disponibles (5)]]
	- [[#Différences clés Mapping A vs B]]
- [[#Liens]]

## 🔀 Deux modes d'import Elevo — quel template choisir

Elevo propose **deux flux distincts** pour importer / synchroniser les utilisateurs. Les **templates Excel diffèrent**.

### Comparaison des deux modes

| Aspect                                     | **Mode A — Import ponctuel**                                | **Mode B — Sync SFTP**                                                           |
| ------------------------------------------ | ----------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Fichier modèle Elevo                       | `Elevo - Import ou mise à jour des utilisateurs.xlsx`       | `Elevo - Fichier type synchronisation SFTP (FR).xlsx`                            |
| Cas d'usage                                | Setup initial, ajustements ponctuels, populations hors SIRH | Synchronisation récurrente automatisée                                           |
| Dépose                                     | Mail à `support@elevo.io`                                   | Dépôt SFTP `/uploads/users/`                                                     |
| Traitement                                 | Manuel par équipe Elevo (H+1 à J+1)                         | Automatique (~H+1)                                                               |
| **Clé d'unicité**                          | `email` ou `username`                                       | **`uniq_identifier`** (colonne dédiée obligatoire) + email/username              |
| **Manager**                                | `manager_email` **OU** `manager_username` (matricule)       | **`manager_uniq_identifier`** (pointe vers un `uniq_identifier` du même fichier) |
| `content_locale` (langue contenus)         | ✅ Présent                                                   | ❌ Absent                                                                         |
| `skip` (exclure une ligne sans la retirer) | ❌ Absent                                                    | ✅ Présent                                                                        |
| Suspension auto des sortants               | ❌ Non (action manuelle Elevo)                               | ✅ Oui (absent du CSV = suspendu)                                                 |
| Modifs manuelles Elevo possibles           | ✅ Oui après import                                          | ❌ Désactivées pour users synchronisés                                            |
| GPG                                        | optionnel (pièce jointe mail)                               | optionnel (chiffrer avant dépôt)                                                 |

### Colonnes différentes par mode

**Présent en Import mais absent en SFTP** :
- `manager_email` (résolution manager par email)
- `content_locale` (langue des contenus consultés, distincte de `locale` = langue de l'app)

**Présent en SFTP mais absent en Import** :
- `uniq_identifier` (clé maître, doit être constant et unique)
- `manager_uniq_identifier` (résolution manager par ID interne)
- `skip` (booléen pour exclure une ligne sans la retirer du fichier)

### Recommandation pour GA

| Phase | Mode | Pourquoi |
|---|---|---|
| **POC initial** | Mode A (Import) | Plus simple, pas besoin d'ouvrir SFTP, validation rapide avec quelques users |
| **Production** | Mode B (Sync SFTP) | Automatisable, gestion auto sortants, traçabilité, moins de friction support Elevo |
| Cas hybride | Mix possible | Population synchro = SFTP, population spéciale (freelances, externes) = Mode A en surcharge |

→ **Cible projet GA = Mode B (SFTP)**. Le Mode A reste utile pour le POC ou pour des correctifs ponctuels.

## ⚠️ Refonte 2026-05-29 — corrections vs version initiale

| Hypothèse initiale | Réalité (doc officielle) |
|---|---|
| Mapping vers une API publique Elevo | Pas d'API → **SFTP** (ou mail manuel) |
| `manager_username` = matricule | C'est **`manager_uniq_identifier`** = uniq_identifier du manager |
| `manager_email` via appel chaîné Nibelis | Optionnel, **debug uniquement**, **pas utilisé pour la sync** |
| Clé d'unicité = email ou username | Clé = **`uniq_identifier`** dédiée, en plus de email/username |
| Champs custom = "à demander au support" | Confirmé : préfixe **`custom_xxx`** (cf cas Simbel) |
| 13 champs directs récupérables | Toujours vrai, mais avec mapping ajusté |

## Synthèse (Mode B — Sync SFTP, cible projet)

Le fichier CSV Elevo SFTP attend **21 colonnes** (5 obligatoires + 16 optionnelles incluant `skip`). Sur ces 21 :

- ✅ **14 récupérables directement** de l'API Nibelis
- ⚠️ **3 avec traitement** (calcul, valeur dérivée, champ Nibelis incertain)
- ❌ **4 non disponibles** dans Nibelis (paramètres Elevo ou hors RH)

**Conclusion** : faisable maintenant. Bloquant unique = identification du champ "Localisation" Nibelis si on veut renseigner `region`.

## Mapping détaillé (21 colonnes CSV Elevo)

### ✅ Récupérables directement (14)

| Colonne CSV Elevo | Obligatoire | Champ Nibelis | Transformation | Notes |
|---|---|---|---|---|
| `uniq_identifier` | ✅ | `id_nibelis` | `str(id_nibelis)` | **Clé maître**. Doit être constant et unique. Conversion int→str obligatoire (note Elevo : "1" ≠ "001") |
| `email` | ✅ (si username vide) | `mail_conge` | `lower()` | ⚠️ **`mail_conge` = email pro `@ga.fr`** (vérifié 10/10 RH + ADODO). `mail_01` est souvent perso/vide chez GA → fallback seulement |
| `username` | ✅ (si email vide) | `matricule` | aucune | Alphanum + `.`, `-`, `_`. Fallback si pas d'email pro |
| `first_name` | ✅ | `prenom` | aucune (Elevo Proper Case auto) | |
| `last_name` | ✅ | `nom` | aucune (Elevo Proper Case auto) | |
| `manager_uniq_identifier` | recommandé | `resp_hier_id_nibelis` | `str(...)` | Doit correspondre à un autre `uniq_identifier` du fichier |
| `registration_number` | optionnel | `matricule` | aucune | Différent de `username` même si on y met la même valeur |
| `job_title` | optionnel | `emploi_libelle` | aucune | |
| `team_name` | optionnel | `equipe` | aucune | |
| `work_start_date` | optionnel | `date_embauche` | ISO 8601 (YYYY-MM-DD) | Confirmé : `2015-02-25` |
| `department` | optionnel | `departement_libelle` | aucune | |
| `service` | optionnel | `service_libelle` | aucune | |
| `gender` | optionnel | `sexe` | `H→m`, `F→f`, autre→`other` (Elevo accepte aussi `M`/`F`/`male`/`Male`/`Other`) | |
| `entity` | optionnel | `libelle_etablissement` | aucune | **À utiliser uniquement si "gestion droits admin restreints" Elevo activée**. Sinon ignorer |

### ⚠️ Récupérables avec traitement (3)

| Colonne CSV Elevo | Obligatoire | Solution | Effort |
|---|---|---|---|
| `region` | optionnel | Si "site/bureau" attendu → champ **Localisation** Nibelis (⏳ en attente identification). Si "ville" → `commune`. Si "établissement" → `libelle_etablissement`. **À arbitrer côté GA selon usage Elevo** | Faible une fois tranché |
| `working_time_ratio` | optionnel | `round(horaire_mensuel / 151.67 * 100)` pour 35h.<br>Cas forfait jours (`type_forfait = J`) : par défaut **100** (cadre temps plein). Cas autres temps de travail à valider | Moyen |
| `level` | optionnel | Choisir parmi `qualification` (ex: "Cadre"), `categorie_professionnelle_libelle` (ex: "Cadre au forfait"), ou `coefficient`. **À arbitrer côté GA** | Faible une fois tranché |

### ❌ Non disponibles dans Nibelis (4)

| Colonne CSV Elevo | Obligatoire | Solution de contournement |
|---|---|---|
| `locale` | optionnel | Constante "fr" pour 100 % des salariés (ou champ custom Nibelis si multi-pays) |
| `use_sso` | optionnel | Vide (= SSO actif si configuré côté Elevo). Mettre `false` pour exclure du SSO |
| `skip` | optionnel | Vide par défaut. Mettre `true`/`yes`/`Oui` pour exclure une ligne de la sync sans la retirer du fichier (utile pour pause temporaire) |
| ~~`organization_admin`~~ | n/a (hors template SFTP) | **Pas dans le template SFTP officiel** (vs ancienne doc). Si besoin de droits admin → géré côté Elevo manuellement |

## Champs custom — option à exploiter

Le cas Simbel (`Fichier d'import Elevo x Simbel.xlsx`) montre des colonnes custom synchronisées via SFTP :

- `custom_contract_end_date` (date de sortie)
- `custom_site`, `custom_country`
- `custom_contract_type`, `custom_socio_professional_category`
- `custom_birth_date`, `custom_phone_number`
- `custom_simbel_billing_entity` (entité de facturation)

**Création** : demander au support Elevo (intitulé exact transmis par eux).

**Pertinent pour Nibelis** (à valider avec RH/Elevo) :
- `custom_contract_type` ← `type_contrat_libelle` (CDI/CDD/...)
- `custom_socio_professional_category` ← `categorie_professionnelle_libelle`
- `custom_birth_date` ← `date_naissance`
- `custom_nationality` ← `nationalite`
- `custom_convention` ← `convention_collective`
- `custom_contract_end_date` ← `date_fin_contrat`
- `custom_disability` ← `travailleur_handicape` (sensible RGPD — à valider DPO)

## Mapping override (nommage des colonnes)

Le tab "Mapping" du fichier Simbel montre qu'on peut **livrer un CSV avec d'autres noms de colonnes** + fournir un mapping override à Elevo. Exemple Simbel (format Ruby/JSON) :

```json
{
  "uniq_identifier": "employee_number",
  "registration_number": "employee_number",
  "username": "employee_number",
  "manager_uniq_identifier": "manager_employee_number",
  "first_name": "firstname",
  "last_name": "lastname",
  "custom_gender": "gender",
  "job_title": "job"
}
```

→ Si on préfère exporter `nibelis_id` au lieu de `uniq_identifier` côté pipeline, c'est techniquement possible. **Recommandation : garder les noms par défaut Elevo pour éviter une couche de mapping côté Elevo.**

## Comportement de synchronisation (officielle)

| Cas | Comportement Elevo |
|---|---|
| User dans CSV mais absent Elevo | ✅ **Créé** automatiquement |
| User dans Elevo mais absent CSV | ⚠️ **Désactivé** (= "suspendu") automatiquement |
| `skip=true` | Ligne ignorée totalement, état Elevo inchangé |
| `uniq_identifier` en doublon dans le CSV | ❌ **Synchro annulée totalement** + rapport d'erreur mail |
| Ligne invalide (date format, currency manquant...) | Ligne ignorée, user marqué "erreur sync", autres lignes continuent |
| User synchronisé | Modifications manuelles dans Elevo **désactivées** pour ce user |
| Manager via `manager_email` | **Ignoré pour la sync** — seul `manager_uniq_identifier` est utilisé |

→ **Implication majeure** : envoyer l'**état complet courant** (snapshot de tous les salariés actifs) à chaque sync. Pas besoin de gérer les delta côté pipeline — Elevo gère.

→ Salariés sortis = absents du CSV = désactivés Elevo automatiquement. **Pas besoin d'un champ "status" custom**.

## Décisions à prendre côté GA

- [ ] **Sémantique `region`** Elevo : ville, site, zone géo ? (à clarifier avec Elevo support OU avec RH)
- [ ] **Source `level`** : `qualification` / `categorie_professionnelle_libelle` / `coefficient` ?
- [ ] **Salariés sans email pro Nibelis** : utiliser `username` = `matricule` ou les exclure via `skip` ?
- [ ] **Champs custom à créer** chez Elevo : liste finale + intitulés (demande à support@elevo.io)
- [ ] **Activer "gestion droits admin restreints" Elevo** pour utiliser `entity` ? Sinon laisser vide

## Prérequis bloquants

- 🟡 **Champ `region`** : identification "Localisation" Nibelis si on veut un site/bureau (⏳ en attente Nibelis)
- ✅ Tous les autres bloquants peuvent être contournés

## Flux d'import recommandé (SFTP)

```
[API 1 Nibelis] GET /api/salaries?id_societe={X}
   ↓ liste des id_nibelis par société (pour chaque société du périmètre)
[API 2 Nibelis] (×N salariés) GET /api/salaries/{id_nibelis}
   ↓ extraction de 14 champs directs + 3 avec traitement
[Transformation]
   ↓ sexe H/F → m/f/other
   ↓ horaire_mensuel → working_time_ratio (151.67 → 100)
   ↓ id_nibelis (int) → uniq_identifier (str)
   ↓ resp_hier_id_nibelis (int) → manager_uniq_identifier (str)
   ↓ valeurs par défaut (locale="fr", use_sso="")
[Validation locale]
   ↓ unicité uniq_identifier
   ↓ pas de manager_uniq_identifier pointant vers un id absent
   ↓ format dates ISO 8601
   ↓ Proper Case (info, Elevo le fait aussi)
[CSV UTF-8 RFC 4180]
   ↓ 21 colonnes + custom_xxx éventuels
[GPG (optionnel)]
   ↓ chiffrement avec clé publique Elevo (elevo-sftp-production.asc)
[SFTP Elevo]
   ↓ dépôt dans /uploads/users/
[Rapport Elevo par mail]
```

## Optimisation : appel chaîné manager

| Mode | Appel chaîné manager nécessaire ? | Coût |
|---|---|---|
| **Mode A — Import ponctuel** | ✅ **Oui** pour résoudre `manager_email` (= `mail_01` du manager) | ~1,2 × N appels (N salariés + N/5 managers uniques après dédup) |
| **Mode B — Sync SFTP** | ❌ **Non** — `manager_uniq_identifier` = `resp_hier_id_nibelis` directement | ~Nb_sociétés + N appels |

→ Mode B optimisé : pas d'appel chaîné. Mode A : appel chaîné indispensable car le fichier exige email OU matricule du manager (le matricule de l'API 2 existe déjà, mais l'email du manager nécessite un fetch supplémentaire).

## Mapping détaillé (Mode A — Import ponctuel)

Si on utilise le fichier `Elevo - Import ou mise à jour des utilisateurs.xlsx` (template Import), voici le mapping Nibelis.

> ✅ **Template officiel vérifié** (2026-06-02, fichier `Elevo - Import ou mise à jour des utilisateurs.xlsx`, onglet *Liste des utilisateurs*) : **20 colonnes de données** (la colonne A est un simple marqueur « ligne à supprimer/conserver », pas un champ). **`organization_admin` n'existe pas** dans ce template. Ordre et noms machine exacts (ligne à conserver) :
> ```
> registration_number; first_name; last_name; email; username; manager_email; manager_username; job_title; team_name; work_start_date; level; department; service; gender; region; entity; locale; content_locale; working_time_ratio; use_sso
> ```

### ✅ Récupérables directement (13)

| Colonne CSV Elevo | Obligatoire | Champ Nibelis | Transformation |
|---|---|---|---|
| `registration_number` | optionnel | `matricule` | aucune |
| `first_name` | recommandé | `prenom` | aucune |
| `last_name` | recommandé | `nom` | aucune |
| `email` | ✅ (si username vide) | `mail_conge` | ⚠️ email pro `@ga.fr` (fallback `mail_01`) |
| `username` | ✅ (si email vide) | `matricule` | aucune (alphanum + `.`, `-`, `_`) |
| `manager_username` | recommandé | `resp_hier_matricule` | aucune |
| `job_title` | optionnel | `emploi_libelle` | aucune |
| `team_name` | optionnel | `equipe` | aucune |
| `work_start_date` | optionnel | `date_embauche` | ISO 8601 (YYYY-MM-DD) |
| `department` | optionnel | `departement_libelle` | aucune |
| `service` | optionnel | `service_libelle` | aucune |
| `gender` | optionnel | `sexe` | `H→m`, `F→f`, autre→`other` |
| `entity` | optionnel | `libelle_etablissement` | aucune |

### ⚠️ Avec traitement (3)

| Colonne CSV Elevo | Solution |
|---|---|
| `manager_email` | **Appel chaîné API 2** sur `resp_hier_id_nibelis` → `mail_01` du manager. Dédup les IDs avant les appels |
| `region` | À arbitrer : commune / établissement / champ Localisation Nibelis ⏳ |
| `working_time_ratio` | `round(horaire_mensuel / 151.67 * 100)`, défaut 100 pour forfait jours |

### Spécifiques au Mode A — ❌ Non disponibles (4)

| Colonne CSV Elevo | Solution |
|---|---|
| `level` | À arbitrer parmi `qualification` / `categorie_professionnelle_libelle` / `coefficient` |
| `locale` | Constante "fr" |
| **`content_locale`** (langue des contenus) | Constante "fr" (spécifique Mode A — absent du SFTP) |
| `use_sso` | Vide ou "false" |

> ~~`organization_admin`~~ : **n'existe pas** dans le template Import officiel (vérifié). Droits admin gérés manuellement côté Elevo.

### Différences clés Mapping A vs B

| Champ Nibelis | Mode A (Import) | Mode B (SFTP) |
|---|---|---|
| `id_nibelis` | ❌ pas utilisé | ✅ → `uniq_identifier` (clé obligatoire) |
| `mail_01` du manager (chaîné) | ✅ → `manager_email` | ❌ inutile pour la sync |
| `resp_hier_matricule` | ✅ → `manager_username` | ❌ inutile (Elevo veut `uniq_identifier`) |
| `resp_hier_id_nibelis` | ❌ pas utilisé | ✅ → `manager_uniq_identifier` |
| Pas de mapping (constante "fr") | ✅ `content_locale` à remplir | ❌ champ absent |
| Pas de mapping (booléen) | ❌ champ absent | ✅ `skip` (exclusion ligne) |

→ **En Mode A** : 13 directs + 3 avec traitement + 4 indisponibles = **20 colonnes** (template officiel vérifié)
→ **En Mode B (SFTP)** : 14 directs + 3 avec traitement + 4 indisponibles = 21 colonnes

## Liens

- 📖 [Doc officielle Elevo — Ajouter, importer ou mettre à jour des utilisateurs (Mode A)](https://docs.elevo.fr/hc/fr/articles/4403024287249-Ajouter-importer-ou-mettre-%C3%A0-jour-des-utilisateurs)
- [[01-API-Nibelis-Reference]] — Détail des champs Nibelis source
- [[03-Mapping-Elevo-Parcours-Professionnel]] — Import parcours pro (prérequis : ce mapping users doit tourner avant)
- [[04-Architecture-SFTP-Elevo]] — Archi SFTP, GPG, sécurité, ops
