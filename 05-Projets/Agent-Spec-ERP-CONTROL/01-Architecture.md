---
tags: ["architecture", "agents", "controle"]
created: 2026-04-16
---

# Architecture

## Vue d'ensemble

Pipeline agentique en 3 couches qui orchestre le workflow de dev de bout en bout :

1. **Source de vérité** : Odoo (projet ERP_Control_, ID 4)
2. **Orchestrateur** : worker Python local, polling Odoo toutes les 2-5 min
3. **Agents** : Spec (phase 1) + Dev (phase 2)

## Schéma fonctionnel

```
┌─────────────┐      polling       ┌────────────────┐
│    Odoo     │◄───────────────────│  Orchestrator  │
│ (tâches #4) │                    │   (Python)     │
└──────┬──────┘                    └────────┬───────┘
       │                                    │
       │ stage = "Spec à enrichir"          │
       ▼                                    ▼
┌─────────────┐                    ┌────────────────┐
│   Spec à    │                    │   SpecAgent    │
│  enrichir   │──────trigger──────▶│ (API Claude)   │
└─────────────┘                    └────────┬───────┘
                                            │
                          ┌─────────────────┼──────────────────┐
                          ▼                 ▼                  ▼
                   ┌──────────┐      ┌─────────────┐    ┌──────────────┐
                   │list_dir  │      │  grep_code  │    │search_odoo_  │
                   │read_file │      │ (ripgrep)   │    │knowledge     │
                   └──────────┘      └─────────────┘    └──────────────┘
                          │                 │                  │
                          └────────┬────────┴──────────────────┘
                                   ▼
                          ┌────────────────┐
                          │ Repo Contrôle  │
                          │ (local, RO)    │
                          └────────────────┘
```

## Choix d'architecture clés

### Exécution locale (pas de serveur)
- Machine de dev, un seul utilisateur
- Pas de Docker, pas de file distribuée
- Polling simple via APScheduler

### Accès repo en local, pas via GitHub
- ripgrep sur 207k lignes = quelques ms
- Pas de rate-limiting API GitHub
- Auto `git pull --ff-only` avant chaque run

### Client Odoo en XML-RPC direct
- Pas de dépendance à un MCP tiers
- ~50 lignes de code, autonome
- Même protocole que ce qu'on utilise déjà en MCP

### Idempotence via hash SHA-256
- Hash de `description + spec_actuelle`
- Évite de retraiter une tâche identique
- SQLite local pour l'historique

### Lock par tâche
- Empêche double exécution parallèle
- TTL de 30 min pour les locks morts

## Stack technique

| Composant | Choix |
|-----------|-------|
| Langage | Python 3.11+ |
| API LLM | Anthropic (claude-opus-4-7) |
| Odoo | xmlrpc.client (stdlib) |
| Recherche code | ripgrep (subprocess) |
| Scheduler | APScheduler ou boucle simple |
| État | SQLite |
| CLI | Click + Rich |
| Config | python-dotenv + PyYAML |

## Points de contrôle humain (important)

Pour éviter les dérives, **deux points de validation humaine obligatoires** :

1. Entre `Spec à enrichir` (agent a fini) et `Spécification terminée` → tu relis avant dev
2. Entre `Dev en cours` (agent a fini) et `En recette` → tu review la PR avant merge

Voir [[02-Workflow-Odoo]] pour le détail des stages.

---

#architecture #agents #controle
