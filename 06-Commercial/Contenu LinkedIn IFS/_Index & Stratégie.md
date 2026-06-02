---
tags: ["linkedin", "contenu", "ifs", "tipdujour"]
created: 2026-06-01
---

# Contenu LinkedIn — #tipdujour IFS (source : community.ifs.com)

> Série de posts LinkedIn **EN**, format **#tipdujour** : 1 tip concret = 1 solution
> tirée du **best answer** d'un fil du forum IFS. **La source n'apparaît PAS dans le
> post** (elle est en bas de chaque note, pour ta réf interne).

## Format validé
- **Post (EN)** : hook (le problème) → la solution concrète → hashtags. Court, actionnable.
- **Source** (dans la note, pas dans le post) : auteur du best answer + URL du fil.
- 1 note = 1 tip = `tips/Tip - ….md`

## Stock de tips prêts → dossier `tips/`
18 tips disponibles (créés 2026-05-30) :
1. Table view vs List view (column limit)
2. Force a clean value with Page Designer (non-editable + default)
3. Auto-enable Send Email on PO (BPA workflow)
4. ACH / electronic payment setup
5. Export user profiles in bulk (CLIENT_PROFILE_NODE_FULL)
6. %_REP tables empty after 25R2 (EBR)
7. Prevent default radio selection
8. No global decimal setting
9. ISO-20022 structured vs address lines
10. CAMT.053 bank statement setup
11. Copy/paste posting lines back in 26R1
12. Oracle SE2 deprecated in 25R2
13. Custom field enum not defaulting
14. Lock a pick location to one customer
15. Export the Navigator tree to Excel
16. DMM combination values import order
17. Schedule a migration job from a file
18. Skip Lot inspection quantity is automatic

## Cadence suggérée
- 1 tip / jour ouvré (ou 2-3/semaine). Publier le bloc **Post (EN)** uniquement (sans la source).

## Pour produire plus de tips
- Relancer `community-ifs-analyzer/get_tips.py` (ouvre des fils, extrait best answers, ≥5 s/appel) → `tips_raw.json`, puis créer de nouvelles notes.
- Prioriser les fils **résolus** (best answer) ; éviter les fils "error/issue" non résolus.
- Outils : `scrape_topics.py` (listes de sujets) → `get_tips.py` (réponses). 250 sujets déjà dans `topics.json`.

**Pipeline source** : community.ifs.com (session Playwright, rythme lent ≥5 s).
