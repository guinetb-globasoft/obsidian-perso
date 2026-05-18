---
tags: ["projet", "agents", "automation", "controle"]
created: 2026-04-16
---

# Agent Spec — Contrôle

Projet d'agents IA pour automatiser l'enrichissement des spécifications techniques et le développement dans le projet **ERP_Control_** (Globasoft ESN, Odoo projet ID 4).

## Objectif

1. **Agent Spec** (phase 1) : enrichit automatiquement les specs techniques des tâches Odoo en explorant le code existant pour maximiser la réutilisation.
2. **Agent Dev** (phase 2) : code la fonctionnalité via Claude Code à partir de la spec enrichie, crée une branche Git et une PR.

## Statut

- [x] Architecture définie
- [x] Squelette Python généré (15 fichiers, ~700 lignes)
- [x] Stage "Spec à enrichir" créé dans Odoo
- [x] Installation locale (venv + ripgrep + .env)
- [ ] Premier test en `--dry-run` sur tâche existante
- [ ] Prompt système itéré (2-3 rounds)
- [ ] Mise en production de l'Agent Spec
- [ ] Agent Dev (phase 2)

## Navigation

- [[01-Architecture]] — Vue d'ensemble et diagramme
- [[02-Workflow-Odoo]] — Stages du kanban et transitions
- [[03-Agent-Spec]] — Phase 1 : détails techniques
- [[04-Agent-Dev]] — Phase 2 : détails techniques (à venir)
- [[05-Prompt-System]] — Le prompt calibré (à itérer)
- [[06-Installation]] — Étapes d'installation pas à pas
- [[07-Journal-Iterations]] — Log des ajustements et observations

## Livrables

- Squelette Python : `agent-spec.zip` (généré le 16/04/2026)
- Repo cible : Contrôle (~743 fichiers, ~207k lignes, Python/Django + HTML/JS)
- Connexions : Odoo (globasoft) + IFS (gafr-trn.ifs.cloud) + Claude API

## Tags

#projet #agents #automation #claude-code #odoo #controle




---

## Mise à jour 2026-04-16 (suite)

Ajout de la note [[08-Decisions]] — registre ADR (Architecture Decision Records) qui trace les choix d'architecture et de workflow avec leur contexte et leurs conséquences. 5 décisions déjà actées, 5 en attente de ton retour d'usage.
