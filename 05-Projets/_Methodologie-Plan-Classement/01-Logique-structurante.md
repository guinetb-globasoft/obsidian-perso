---
tags: ["methodologie", "plan-classement", "logique-structurante", "iso-15489"]
created: 2026-05-17
---

# 1. Logique structurante

> Sur quoi repose la structure du plan de classement ?

## Principe

Selon **ISO 15489-1:2016**, un bon plan de classement reflète les **activités et fonctions** de l'organisation, pas son organigramme ni les types de documents.

## Les 3 logiques possibles

### ✅ Par fonctions / activités (recommandé)
Structure le plan autour de ce que fait l'organisation : "Gestion commerciale", "Production", "RH"... puis activités : "Prospection", "Contractualisation", "Facturation".

**Avantages**
- Stable dans le temps (les fonctions changent peu)
- Survit aux réorganisations
- Reflète la vraie vie métier
- Conforme ISO 15489

### ⚠️ Par organigramme (fragile)
Structure le plan selon les services/directions : "Direction Commerciale", "Direction Technique"...

**Inconvénients**
- Se périme à chaque réorganisation
- Crée des silos artificiels
- Ne reflète pas les processus transverses

### ❌ Par types de documents (anti-pattern)
Classe selon "Contrats", "Factures", "Comptes-rendus"...

**Inconvénients**
- Perd tout le contexte métier
- Multiplie les doublons potentiels
- Rend la recherche difficile (un contrat client n'est pas un contrat fournisseur)

## Questions à poser

- [ ] Sur quelle logique repose le premier niveau du plan ?
- [ ] Si on réorganise demain, le plan tient-il ?
- [ ] Un nouvel arrivant comprend-il la structure sans formation lourde ?
- [ ] Les libellés sont-ils des **noms d'activité** (verbes substantivés) ou des étiquettes administratives ?
- [ ] Y a-t-il une cartographie des processus métier en amont du plan ?

## Signaux d'alerte 🚩

- Le plan commence par "Direction XXX"
- Les niveaux 1 ou 2 reprennent les noms des services
- Une catégorie "Divers" ou "Autres" existe à un niveau élevé
- Le plan a été conçu par la DSI seule, sans les métiers
- Aucune cartographie fonctionnelle préalable

## Cas concrets à challenger

**Exemple d'un projet ERP**
- ❌ Mauvais : `01-DAF/01-Comptabilité/01-Factures`
- ✅ Bon : `01-Gestion-financiere/01-Facturation-client/01-Factures-emises`

**Exemple d'un projet DWH**
- ❌ Mauvais : `Documents-Equipe-Data/Spécifications`
- ✅ Bon : `01-Conception/01-Specifications-fonctionnelles`

## Lien avec les autres angles

- Une logique fonctionnelle facilite la [[05-Stabilite-evolutivite|stabilité]]
- Elle améliore l'[[07-Adequation-usages|adéquation aux usages]]
- Elle s'articule naturellement avec [[06-Metadonnees|les métadonnées]]

## 🔄 Cohérence doc ↔ code (enrichissement issu de l'audit DWH)

> Sur un projet IT, la documentation ne vit pas en isolation : elle est couplée au code (modèles dbt, scripts Python, schémas SQL, fichiers de migration). La cohérence **codes domaine ↔ noms de tables ↔ noms de fichiers ↔ noms de fiches doc** est un marqueur fort de qualité.

### Le principe

Un projet IT mature aligne **plusieurs nomenclatures** sur les mêmes codes domaine :

| Artefact | Exemple aligné |
|---|---|
| Codes domaine (référentiel projet) | `IMP` (Imputations), `FAC` (Factures) |
| Codes KPI | `KPI-IMP-001`, `KPI-FAC-002` |
| Codes règles de gestion | `RG-IMP-003`, `RG-FAC-007` |
| Noms de tables (bronze/silver) | `silver_mep1.pointages_unifies` (domaine IMP) |
| Noms de fichiers SQL/dbt | `30_factures_fournisseurs.sql` (domaine FAC) |
| Noms de fiches doc | `rg-fac-007-integration-sage-achats.md` |
| Tags des fiches | `#domaine-fac #domaine-imp` |

### Pourquoi c'est important

- **Traçabilité bout-en-bout** : depuis un KPI sur un dashboard jusqu'à la requête SQL qui l'alimente, on suit le même fil rouge.
- **Recherche transverse** : un grep `RG-FAC-007` retrouve simultanément la fiche doc, le commit Git, le code SQL et le commentaire dans le pipeline.
- **Onboarding** : un nouveau contributeur comprend instantanément que `RG-FAC-` est lié au domaine `Factures`.
- **Refactor** : changer un code domaine devient un refactor traçable, pas une chasse au trésor.

### Questions à poser

- [ ] Les codes domaine documentés sont-ils utilisés dans le code (commentaires, noms de fonctions, schémas) ?
- [ ] Les noms de tables / schémas / fichiers SQL portent-ils la marque du domaine ?
- [ ] Existe-t-il un **référentiel unique** des codes domaine (idéalement une ADR ou note dédiée) ?
- [ ] Une fiche doc peut-elle être retrouvée par grep depuis le code, et inversement ?

### Signaux d'alerte 🚩

- Codes domaine documentés mais absents du code.
- Plusieurs nomenclatures concurrentes pour la même chose (ex : `factures` vs `invoices` vs `fact-fou`).
- Pas de référentiel unique des codes domaine.
- Doc et code maintenus par des personnes différentes sans pont entre les deux.

## Référence


- ISO 15489-1:2016, §9.4 (Classification)
- R2GA, partie I (principes du classement fonctionnel)
