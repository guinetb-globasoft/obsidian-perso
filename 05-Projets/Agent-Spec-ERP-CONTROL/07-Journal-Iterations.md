---
tags: ["journal", "iterations", "controle"]
created: 2026-04-16
---

# Journal d'itérations

Log des ajustements du prompt système et observations sur les runs réels.

## Template d'une itération

```
## [DATE] — v<X.Y> — <titre court>

**Tâche(s) testée(s)** : #XXX, #YYY
**Mode** : dry-run / réel
**Modèle** : claude-opus-4-7

### Résultat
- Tool calls : X
- Tokens in/out : X / Y
- Durée : ~X min

### Qualité perçue
- ✅ Points forts
- ❌ Points faibles
- 🤔 Observations

### Changements au prompt
- [diff concret]

### Prochaine itération
- À tester : ...
```

---

## 2026-04-16 — v1.0 — Création initiale

**Status** : installation terminée — prêt pour premier dry-run

Première version du prompt basée sur :
- Stack projet (Django + IFS + Celery)
- Exemples observés sur les 15 dernières tâches
- Principe de réutilisation maximale de l'existant

✅ Stage "Spec à enrichir" créé (ID 144)
✅ `.env` configuré (Odoo + Anthropic + REPO_PATH=ifs-env)
✅ ripgrep installé
→ Prochaine étape : `python run.py --task-id 641 --dry-run`

### Tâches candidates pour premier test
- **#640 Incident Export** : diagnostic technique, bon test de compréhension
- **#641 Modifications rôles Achat lot 4** : riche en URLs et endpoints, test grep
- **#634 Suivi factures finance** : courte, test manque d'info

---

#journal #iterations #controle
