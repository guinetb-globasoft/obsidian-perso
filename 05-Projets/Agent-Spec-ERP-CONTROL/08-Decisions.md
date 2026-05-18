---
tags: ["decisions", "adr", "controle"]
created: 2026-04-16
---

# Décisions — Journal (ADR)

Registre des décisions prises sur le projet, avec leur contexte et leurs conséquences. Format inspiré des **Architecture Decision Records (ADR)** : léger, daté, avec le "pourquoi" plutôt que juste le "quoi".

## Template à copier pour chaque nouvelle décision

```
## ADR-XXX — [TITRE COURT DE LA DÉCISION]

**Date** : YYYY-MM-DD
**Statut** : 🟢 Actée / 🟡 En cours de réflexion / 🔴 Abandonnée / 🔄 Remplacée par ADR-YYY
**Tags** : #archi / #process / #outil / #coût / ...

### Contexte
Quel problème ou choix on essaie de résoudre ? Quelles contraintes ?

### Options envisagées
- **Option A** : ...
- **Option B** : ...
- **Option C** : ...

### Décision
Option retenue : ...

### Rationale
Pourquoi cette option ? Qu'est-ce qui a fait pencher la balance ?

### Conséquences
- ✅ Bénéfices attendus
- ⚠️ Trade-offs acceptés
- 🔁 Choses à revisiter si ...

### Liens
- [[autre-note-liée]]
- Commits/PR : ...
```

---

# Décisions actées

## ADR-001 — Exécution locale, pas de serveur

**Date** : 2026-04-16
**Statut** : 🟢 Actée
**Tags** : #archi #infra

### Contexte
Il faut héberger l'orchestrateur et l'agent quelque part. Machine locale, VPS, serveur dédié, cloud ?

### Options envisagées
- **Local** : sur la machine du Responsable de dev
- **VPS** (OVH, Scaleway) : ~10€/mois
- **Cloud géré** (Render, Fly.io) : 0-20€/mois

### Décision
**Local** sur la machine du Responsable.

### Rationale
- Un seul utilisateur (Benoît), pas de besoin de partage
- Polling Odoo est léger (un appel toutes les 2 min)
- Le repo Contrôle est déjà local → accès filesystem instantané
- Zéro coût d'infra
- Simple à démarrer/arrêter/debugger

### Conséquences
- ✅ Setup minimal (venv + .env)
- ✅ Pas de latence réseau pour lire le repo
- ⚠️ Ne tourne que quand la machine est allumée (OK : tâches non urgentes)
- 🔁 À revisiter si : équipe élargie, besoin 24/7, CI/CD intégré

### Liens
- [[01-Architecture]]

---

## ADR-002 — Repo accédé en local plutôt que via GitHub API

**Date** : 2026-04-16
**Statut** : 🟢 Actée
**Tags** : #archi #perf

### Contexte
L'Agent Spec doit lire beaucoup de fichiers (grep sur 207k lignes, read sur des dizaines de fichiers par run). Où accéder au code source ?

### Options envisagées
- **Local** : filesystem direct + ripgrep
- **GitHub API** : `/repos/{owner}/{repo}/contents/...`
- **GitHub + cache local** : clone initial + refresh périodique

### Décision
**Local** avec `git pull --ff-only` automatique avant chaque run (désactivable via `REPO_AUTO_PULL=false`).

### Rationale
- ripgrep sur 200k lignes = **quelques ms** (vs secondes via API)
- Pas de rate-limit GitHub (5000 req/h peut être saturé sur un gros run)
- Code simple (pas de pagination, pas de gestion auth HTTP)
- `git pull` suffit à garantir la fraîcheur

### Conséquences
- ✅ Performances excellentes
- ✅ Gratuit (pas d'API calls payantes)
- ⚠️ Nécessite que la machine soit à jour sur `main`
- ⚠️ Limité à un seul repo à la fois (OK : un seul projet Contrôle)

### Liens
- [[01-Architecture]]
- `tools/repo_tools.py`

---

## ADR-003 — Client Odoo XML-RPC direct, pas de MCP

**Date** : 2026-04-16
**Statut** : 🟢 Actée
**Tags** : #archi #dépendances

### Contexte
L'agent doit lire/écrire des tâches Odoo. On a déjà un MCP Odoo configuré côté Claude Desktop, mais l'agent tourne en Python autonome côté machine.

### Options envisagées
- **MCP Odoo** : invoquer via le protocole MCP
- **XML-RPC direct** : `xmlrpc.client` (stdlib Python)
- **odoorpc** (library tierce) : wrapper pythonique

### Décision
**XML-RPC direct** avec ~50 lignes de wrapper (`tools/odoo_client.py`).

### Rationale
- Protocole déjà utilisé par le MCP Odoo → même backend, même fiabilité
- Stdlib Python → zéro dépendance supplémentaire
- Contrôle total sur les champs retournés, domaines, etc.
- Permet les écritures (write) tout aussi facilement
- Indépendant du MCP (qui pourrait tomber / changer)

### Conséquences
- ✅ Autonome, pas de dépendance au MCP
- ✅ Léger et performant
- ⚠️ À maintenir nous-mêmes si Odoo change son API (rare sur XML-RPC)
- 🔁 À revisiter si : besoin de features MCP spécifiques (pas prévu)

### Liens
- `tools/odoo_client.py`

---

## ADR-004 — Stage dédié "Spec à enrichir" dans le kanban (pas de champ booléen)

**Date** : 2026-04-16
**Statut** : 🟢 Actée
**Tags** : #workflow #UX

### Contexte
Il faut un déclencheur pour l'Agent Spec. Comment l'exprimer dans Odoo ?

### Options envisagées
- **Nouveau stage kanban** "Spec à enrichir" entre "En travail" et "En attente de reprio"
- **Champ booléen custom** `x_declencher_agent` à cocher
- **Tag** "spec-to-enrich" à poser manuellement
- **Les deux** (stage + booléen)

### Décision
**Nouveau stage kanban** "Spec à enrichir".

### Rationale
- Visible dans le kanban en un coup d'œil
- Pipeline explicite : toi tu pousses la carte → l'agent la prend → elle revient validée
- Pas de champ invisible qui pourrait être oublié ou mal coché
- Cohérent avec la logique "une tâche = un stage" du kanban
- Permet aussi d'ajouter un stage "Spec à relire" plus tard si besoin d'un point de validation

### Conséquences
- ✅ UX claire, pas de risque d'ambiguïté
- ✅ Filtrage trivial : `domain=[("stage_id", "=", <ID>)]`
- ⚠️ Pollue légèrement le kanban avec un stage de plus
- 🔁 Si besoin d'un flag "agent working" (pour verrouiller pendant un run), on ajoutera un champ séparé

### Liens
- [[02-Workflow-Odoo]]

---

## ADR-005 — Modèle Claude Opus 4.7 pour l'Agent Spec

**Date** : 2026-04-16
**Statut** : 🟢 Actée
**Tags** : #outil #coût #qualité

### Contexte
Quel modèle utiliser pour générer les specs techniques ?

### Options envisagées
- **Claude Haiku 4.5** : rapide, pas cher, mais moins bon en raisonnement
- **Claude Sonnet 4.6** : équilibre coût/qualité
- **Claude Opus 4.7** : le plus intelligent, plus cher, plus lent

### Décision
**Claude Opus 4.7** pour la phase 1.

### Rationale
- La qualité de la spec est **le** point critique (toute la suite en dépend)
- Opus gère mieux les raisonnements complexes sur du code volumineux
- La fréquence des runs est faible (quelques tâches par jour max) → coût acceptable
- On pourra tester Sonnet plus tard si la qualité est suffisante sur Opus

### Conséquences
- ✅ Meilleure qualité de spec attendue
- ⚠️ Coût plus élevé par run (~0.50-1€ par tâche estimé)
- ⚠️ Latence plus élevée (~2-5 min par run)
- 🔁 À revisiter : basculer en Sonnet après 10 runs si la qualité tient

### Liens
- [[05-Prompt-System]]
- [[07-Journal-Iterations]]

---

# Décisions en attente (à acter)

## ADR-006 — Agent Dev : plateforme Git

**Statut** : 🟡 En cours de réflexion
**Contexte** : L'Agent Dev devra pusher une branche et ouvrir une PR. Sur quelle plateforme ? GitHub ? GitLab ? Bitbucket ? Autre ?

**À décider après** : phase 1 stabilisée.
**Question ouverte** : où est hébergé le repo Contrôle aujourd'hui ?

---

## ADR-007 — Agent Dev : flag `--dangerously-skip-permissions`

**Statut** : 🟡 En cours de réflexion
**Contexte** : Claude Code peut tourner sans confirmation de permissions. Est-ce acceptable dans un worktree isolé sur machine locale ?

**Options** :
- Oui, sans restriction (risque : commande destructive si Claude part en vrille)
- Non, utiliser l'allowlist fine dans `~/.claude/settings.json`
- Mi-figue mi-raisin : autoriser tout sauf `rm`, `git push origin main`, etc.

**À décider** : avant de coder la phase 2.

---

## ADR-008 — Stage intermédiaire "Spec à relire" ?

**Statut** : 🟡 En cours de réflexion
**Contexte** : Actuellement, l'agent passe la tâche directement en "Spécification terminée". Faut-il un stage intermédiaire "Spec à relire" pour matérialiser le point de validation humaine ?

**Options** :
- **Non** : tu relis quand tu veux avant de passer en "Dev en cours", c'est toi qui déclenches manuellement
- **Oui** : stage intermédiaire qui force l'œil humain

**À décider** : après 3-5 runs réels, selon ton ressenti.

---

## ADR-009 — Mode de déclenchement : polling ou event-driven ?

**Statut** : 🟡 En cours de réflexion (actuellement polling)
**Contexte** : L'orchestrateur fait du polling toutes les 2 min. Odoo propose aussi des webhooks / automated actions qui pourraient déclencher un endpoint.

**Options** :
- **Polling** (actuel) : simple, pas de config Odoo, délai max 2 min
- **Webhook Odoo → endpoint local** : nécessite ngrok ou tunnel, plus complexe mais instantané

**À décider** : seulement si le polling devient frustrant à l'usage. Probablement jamais.

---

## ADR-010 — Où publier les runs et leurs métriques ?

**Statut** : 🟡 En cours de réflexion
**Contexte** : On log dans SQLite local. Faut-il une interface pour visualiser ? Export vers un endroit central ?

**Options** :
- **SQLite + CLI `runs`** : suffisant pour 1 utilisateur
- **Dashboard web minimal** (Streamlit, FastAPI) : joli mais overkill
- **Note Obsidian quotidienne** auto-générée avec le résumé des runs : intéressant !

**À décider** : après 20-30 runs, quand on aura des données à regarder.

---

#decisions #adr #controle
