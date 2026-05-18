---
tags: ["agent-spec", "controle"]
created: 2026-04-16
---

# Agent Spec — Phase 1

## Principe

Enrichit automatiquement les specs techniques des tâches Odoo en explorant le repo Contrôle pour identifier le code réutilisable. Déclenché par le passage d'une tâche au stage "Spec à enrichir".

Voir [[02-Workflow-Odoo]] pour le workflow.

## Tools exposés à Claude

| Tool | Rôle | Implementation |
|------|------|----------------|
| `list_dir(rel_path)` | Liste le contenu d'un dossier | `os.listdir` + filtres |
| `read_file(rel_path, max_lines)` | Lit un fichier (max 200KB) | `Path.read_text` |
| `grep_code(pattern, glob)` | Cherche un motif dans tout le code | `subprocess rg` |
| `search_odoo_knowledge(query)` | Cherche tâches passées + articles | XML-RPC `search_read` |

### Sandbox

`repo_tools.py` vérifie via `_safe_path()` que le chemin demandé reste dans `REPO_PATH` — pas de path traversal possible.

## Boucle principale

```
1. CLI → Orchestrator.process_task(task_id)
2. Lit la tâche (description + spec actuelle)
3. Check idempotence (hash SHA-256 en SQLite)
4. Acquiert un lock (TTL 30 min)
5. Git pull du repo (optionnel)
6. Lance SpecAgent.run()
   └─ Boucle tool_use avec API Anthropic (max 25 tours)
      ├─ Claude demande un tool → Python l'exécute → renvoie le résultat
      └─ Claude écrit la spec HTML → stop_reason=end_turn
7. Si succès : écrit dans Odoo + déplace en "Spécification terminée"
   Si échec : remet en "En travail"
8. Libère le lock + enregistre le run dans SQLite
```

## Format de sortie imposé

HTML structuré avec 6 sections :
- 🎯 Contexte et objectif
- 🔍 Analyse de l'existant (code réutilisable identifié + patterns)
- 🏗️ Proposition technique (à modifier / à créer / appels IFS)
- 📋 Plan d'implémentation
- ⚠️ Risques et points d'attention
- ❓ Questions ouvertes pour le Responsable

Voir [[05-Prompt-System]] pour le prompt complet.

## Budgets et limites

| Paramètre | Valeur | Justification |
|-----------|--------|---------------|
| Max tours d'outils | 25 | Assez pour explorer 200k lignes, empêche les boucles |
| Max tokens sortie | 8000 | Une spec détaillée fait ~3-5k tokens |
| TTL lock | 30 min | Run typique < 5 min, marge large |
| Auto-pull repo | true | Bosser sur la dernière version |

## Idempotence

Hash = `sha256(description + "---" + spec_actuelle)[:16]`

Si ce hash existe déjà en succès dans `runs` → skip. Garantit qu'une tâche dont le contenu n'a pas bougé n'est pas retraitée.

## CLI

```bash
./run.py --task-id 641 --dry-run   # Test sans écrire
./run.py --task-id 641             # Run réel
./run.py --once                    # Un passage polling
./run.py --watch                   # Daemon polling
```

## Structure du projet Python

```
agent-spec/
├── config/
│   ├── .env.example
│   └── settings.yaml
├── orchestrator/
│   ├── main.py       # Orchestrator : polling, process_task, watch
│   └── state.py      # SQLite : runs + locks + idempotence
├── agents/
│   ├── spec_agent.py # Boucle tool_use
│   └── prompts.py    # Prompt système
├── tools/
│   ├── odoo_client.py # XML-RPC Odoo
│   ├── repo_tools.py  # list_dir, read_file, grep_code
│   └── tool_schemas.py
├── run.py
└── requirements.txt
```

## À itérer

La qualité dépend à 80% du prompt système. Prévoir 2-3 rounds d'itération sur des tâches réelles avant mise en prod. Voir [[07-Journal-Iterations]] pour le log.

---

#agent-spec #controle #phase-1
