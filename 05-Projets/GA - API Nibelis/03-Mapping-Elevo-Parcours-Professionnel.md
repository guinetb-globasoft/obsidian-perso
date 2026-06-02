---
tags: ["elevo", "nibelis", "mapping", "GA", "parcours-professionnel", "remuneration", "sftp"]
created: 2026-05-29
updated: 2026-05-29
---

---
projet: GA - API Nibelis
type: mapping
cible: Elevo — Import parcours professionnel (SFTP)
source: API Nibelis
created: 2026-05-29
updated: 2026-05-29
sources_elevo: ["Importer les données relatives au parcours professionnel des collaborateurs – Elevo.pdf", "Elevo - Import du parcours professionnel.xlsx"]
---

# Mapping Elevo Parcours Professionnel (SFTP) ↔ API Nibelis

> Mapping des champs Elevo pour l'**import du parcours professionnel** vers l'API Nibelis. MAJ 2026-05-29 suite à la doc officielle (PDF + template Excel). Voir [[01-API-Nibelis-Reference]] pour les champs source, [[02-Mapping-Elevo-Nibelis]] pour l'import users et [[04-Architecture-SFTP-Elevo]] pour l'archi.

**Périmètre :** historique des postes occupés par chaque collaborateur, avec leur date de début/fin et la rémunération associée. Ce mapping est **distinct** de l'import des utilisateurs ([[02-Mapping-Elevo-Nibelis]]).

## 🔀 Deux modes de dépose, même template

Contrairement à l'import users qui propose 2 templates différents ([[02-Mapping-Elevo-Nibelis]]), l'import parcours utilise **un seul template** (`Elevo - Import du parcours professionnel.xlsx`) mais peut être déposé selon **2 modes** :

| Aspect | **Mode A — Mail ponctuel** | **Mode B — SFTP** |
|---|---|---|
| Cas d'usage | Setup initial, import historique, ajustements | Synchronisation quotidienne |
| Dépose | Mail à `support@elevo.io` | Dépôt SFTP `/uploads/professional_background/` |
| Template | `Elevo - Import du parcours professionnel.xlsx` (identique aux 2 modes) | Idem |
| Traitement | Manuel par Elevo (H+1 à J+1) | Automatique |
| Colonnes | 8 colonnes identiques | 8 colonnes identiques |

→ **Bonne nouvelle** : le template est le même. Le choix se fait uniquement sur le **canal de dépose**.

### Recommandation pour GA

| Phase | Mode | Pourquoi |
|---|---|---|
| **POC initial** | Mode A (Mail) | Validation rapide, pas besoin du SFTP setup |
| **Production** | Mode B (SFTP) | Automatisable, cohérent avec sync users |

→ **Cible projet GA = Mode B (SFTP)** pour la prod.

## ⚠️ Précisions 2026-05-29 — corrections vs version initiale

| Note initiale | Correction (doc officielle + template) |
|---|---|
| Format date `AAAA-MM-YY` | **ISO 8601 = `YYYY-MM-DD`** (ex `2015-02-25`) — confirmé par le template Excel |
| `Job_title` (J majuscule) | **`job_title`** minuscule (confirmé template Excel) |
| `fixed_amount` peut être 0 | **Ne peut pas être 0** — laisser **VIDE** si non applicable |
| Devise par défaut implicite | **41+ devises supportées** (AUD, EUR, USD, GBP, BRL, CAD, CHF, CNY/RMB, COP, DKK...) |
| Mapping vers mail manuel | **SFTP officiel** disponible → dossier `/uploads/professional_background/` |

## Synthèse

Le template parcours attend **8 colonnes**. Sur ces 8 :

- ✅ **3 directement** récupérables (`login`, `job_title`, `start_date`)
- ⚠️ **1 partiel** (`end_date` — disponible uniquement pour le poste actuel si parti)
- ❌ **4 non disponibles via API actuelle** (`fixed_amount`, `variable_amount`, `custom`, `currency`) — **données paie** non exposées par les endpoints `/api/salaries`

**Conclusion** : couverture insuffisante en l'état pour l'usage cible (parcours + rémunération). Les 3 champs obligatoires sont accessibles, mais l'import n'aura de valeur métier qu'avec les endpoints paie.

⚠️ **Limitation structurelle persistante** : l'API actuelle ne retourne que la **situation courante**, pas l'**historique des postes**. Pour reconstituer un vrai parcours multi-postes, il faudrait un endpoint d'historique côté Nibelis (à confirmer).

## Mapping détaillé (8 colonnes CSV Elevo)

### ✅ Récupérables directement (3)

| Colonne CSV | Obligatoire | Champ Nibelis | Transformation |
|---|---|---|---|
| `login` | ✅ | `mail_01` ou `matricule` (selon choix users) | Doit correspondre à l'`email` ou `username` de [[02-Mapping-Elevo-Nibelis]] (cohérence cross-fichier obligatoire) |
| `job_title` | ✅ | `emploi_libelle` | aucune. **Casse confirmée : minuscule** |
| `start_date` | ✅ | `date_debut_contrat` | ISO 8601 (YYYY-MM-DD) |

### ⚠️ Récupérable partiellement (1)

| Colonne CSV | Solution | Limite |
|---|---|---|
| `end_date` | Si parti : `date_depart` ou `date_fin_contrat`. Si encore en poste : **laisser vide** | Vide = "poste actuel" côté Elevo |

### ❌ Non disponibles via /api/salaries (4)

| Colonne CSV       | Statut Nibelis                                                         | Solution                                                                  |
| ----------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `fixed_amount`    | ⏳ Endpoint paie en attente                                             | **Laisser vide** si pas dispo. ⚠️ **Ne pas mettre 0** (Elevo rejette `0`) |
| `variable_amount` | ⏳ idem                                                                 | Idem (vide si non applicable)                                             |
| `custom`          | ⏳ idem. Pourrait inclure les avantages (`avantage_voiture` × 12, etc.) | Vide ou JSON/string selon format Elevo                                    |
| `currency`        | Hypothèse raisonnable EUR pour 100 % des sociétés FR                   | **Constante `EUR`** dès qu'un montant est rempli, sinon vide              |

## Comportement de synchronisation (officielle)

| Cas | Comportement Elevo |
|---|---|
| Login + start_date inconnus | ✅ **Nouveau poste créé** |
| Login + start_date existants | 🔄 **Mise à jour** des données du poste |
| Poste présent Elevo mais absent CSV | ❎ **AUCUNE suppression** (parcours = historique, par ajout/MAJ uniquement) |
| 2 lignes avec même start_date pour même login | ❌ Ligne(s) ignorée(s) — rapport d'erreur |
| `currency` vide alors que `fixed_amount` rempli | ❌ Ligne ignorée |
| end_date < start_date | ❌ Ligne ignorée |
| `login` absent d'Elevo (user pas encore créé) | ❌ Ligne ignorée |

→ **Prérequis impératif** : l'import users ([[02-Mapping-Elevo-Nibelis]]) doit avoir tourné avant. Le matching se fait par `login` = `email` ou `username` exact.

→ **Suppression manuelle uniquement** : un poste à retirer du parcours doit l'être directement dans l'UI Elevo.

## Devises supportées (extrait du template)

41+ devises ISO 4217. Liste partielle : `EUR`, `USD`, `GBP`, `CHF`, `CAD`, `AUD`, `CNY` (ou `RMB`), `BRL`, `COP`, `DKK`, `JPY`, `KRW`, `SGD`, `THB`, `INR`...

→ Pour GA toutes sociétés FR : **`EUR`** systématique.

## Stratégie d'import phasée

### Phase 1 — Sans accès paie (faisable maintenant)

Import minimal avec uniquement les 3 champs obligatoires + login :

| Colonne CSV | Source |
|---|---|
| `login` | `mail_01` (ou `matricule` si pas d'email) |
| `job_title` | `emploi_libelle` |
| `start_date` | `date_debut_contrat` (format ISO 8601) |

→ 1 ligne par salarié actif (poste actuel). Permet de poser la base du parcours dans Elevo + sert de socle pour la phase 2.

⚠️ Pour les **anciens postes**, sans endpoint historique Nibelis, on ne peut pas les reconstituer automatiquement.

### Phase 2 — Avec accès paie Nibelis

Enrichissement avec rémunérations :
- `fixed_amount` ← rubrique salaire de base annualisée (rubrique à identifier après accès endpoint paie)
- `variable_amount` ← rubriques variables annualisées (primes contractuelles)
- `custom` ← potentiellement les avantages en nature (`avantage_voiture` + `avantage_logement` + `avantage_nourriture` + `avantage_autre`) × 12, formaté selon convention Elevo
- `currency` ← `EUR`

⚠️ Attention : `fixed_amount` ne peut pas être `0`. Pour les bénévoles / stages / contrats sans rémunération → laisser **vide** (et `currency` aussi vide).

### Phase 3 — Avec historique des postes (si endpoint disponible côté Nibelis)

Plusieurs lignes par salarié reflétant les changements successifs de poste avec leurs rémunérations historiques. Aujourd'hui **non faisable** — endpoint nécessaire à confirmer auprès du support Nibelis.

**Question pour Nibelis** : existe-t-il un endpoint type `/api/historique-postes/{id}`, `/api/contrats/{id}/historique`, ou un export Excel batch contenant la chronologie ?

## Format de fichier (rappel)

- CSV RFC 4180, UTF-8
- 1ère ligne = en-têtes
- Ordre des colonnes libre
- Pas de virgule en fin de ligne
- Dépôt SFTP : `/uploads/professional_background/`

## Décisions / clarifications à obtenir

- [ ] **Existe-t-il un endpoint d'historique des postes côté Nibelis ?** → demande support Nibelis
- [ ] **Format `custom`** côté Elevo : string, JSON, liste libellé:montant ? → demande support Elevo
- [ ] **Annualisation des avantages en nature** (`avantage_voiture` mensuel × 12) : confirmer la convention Elevo
- [ ] **Démarrer Phase 1 maintenant** ou attendre la paie pour un import unique ? Recommandation : Phase 1 maintenant pour valider le pipeline + cohérence login

## Liens

- [[01-API-Nibelis-Reference]] — Détail des champs Nibelis source
- [[02-Mapping-Elevo-Nibelis]] — Import users (prérequis OBLIGATOIRE avant ce parcours)
- [[04-Architecture-SFTP-Elevo]] — Archi SFTP, GPG, sécurité, ops
