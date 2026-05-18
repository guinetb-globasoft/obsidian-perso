---
tags: ["agent-dev", "controle", "phase-2"]
created: 2026-04-16
---

# Agent Dev — Phase 2 (à construire après)

> ⚠️ Cette phase n'est pas encore implémentée. À attaquer une fois l'Agent Spec stabilisé. Voir [[03-Agent-Spec]] pour la phase 1.

## Principe

Prend une tâche en stage `Spécification terminée`, crée une branche Git, lance Claude Code en mode headless pour coder, ouvre une PR, puis déplace la tâche en `En recette`.

## Pipeline cible

```
1. Polling détecte tâche en "Spécification terminée"
2. git worktree add ../controle-TASK-<ID> -b feature/TASK-<ID>-<slug>
3. cd <worktree>
4. claude -p "$(build_dev_prompt.sh)" --dangerously-skip-permissions
5. claude-code développe, teste, commit
6. git push -u origin feature/TASK-<ID>-<slug>
7. API GitHub : create_pull_request(title, body, head, base=main)
8. Odoo : déplace tâche en "En recette (sur Render)" + ajoute URL de la PR
9. git worktree remove <worktree>
```

## Choix techniques

### Worktrees Git plutôt que clones
- Partagent le `.git` du repo principal → rapide
- Isolent chaque run → pas de conflit si deux tâches en parallèle
- Nettoyage trivial après run

### Claude Code en subprocess
```python
subprocess.run(
    ["claude", "-p", prompt, "--dangerously-skip-permissions"],
    cwd=worktree_path,
    timeout=3600  # 1h max par run
)
```

Le flag `--dangerously-skip-permissions` est raisonnable dans un worktree isolé sur machine locale. Alternative plus sûre : configurer `~/.claude/settings.json` avec allowlist d'actions.

### PR via API GitHub
- Library : PyGitHub ou requests direct
- Token avec scope `repo` stocké dans `.env`
- Template de PR : titre = nom de la tâche, body = spec + lien Odoo

## Prompt de l'Agent Dev (esquisse)

```
Tu es un développeur senior sur le projet Contrôle (Django + IFS).

Voici la spécification technique à implémenter :
<spec_html_from_odoo>

Conventions du projet :
- <conventions à lister depuis le repo>
- Tests : <framework utilisé>
- Commits : <style Conventional Commits ?>

Ta mission :
1. Implémente la spec en respectant les conventions
2. Ajoute des tests pour ta nouvelle code
3. Lance les tests et assure-toi qu'ils passent
4. Commit avec un message clair
5. Termine en affichant un résumé de ce qui a été fait

Tu n'as PAS à ouvrir de PR, je le ferai après.
```

## Points d'attention

### Stratégie d'échec
Si Claude Code :
- Ne termine pas en 1h → kill + remettre tâche en "Dev en cours" manuel
- Fait des tests qui échouent → quand même push avec un commentaire "WIP - tests à fixer" ?
- Modifie trop de fichiers → seuil de sécurité, demande de validation

### Review humaine obligatoire
La PR reste ouverte. **Toi seul merge**. L'agent ne touche jamais `main`.

### Traçabilité
Chaque commit mentionne `TASK-<ID>` + "Generated with Claude Code".

## Intégration avec phase 1

Si on reprend l'architecture Orchestrator :
- Un seul point d'entrée, deux types d'agents
- Table SQLite étendue : `runs.agent_type = 'spec' | 'dev'`
- Config étendue : `settings.yaml` avec section `agent_dev`

## À décider plus tard

- [ ] GitHub ou GitLab ou autre ?
- [ ] Style de commits (Conventional ?)
- [ ] Suite de tests à lancer systématiquement
- [ ] Auto-link PR ↔ tâche Odoo (commentaire Odoo avec URL PR)
- [ ] Gestion des merge conflicts si plusieurs branches ouvertes

---

#agent-dev #controle #phase-2 #backlog
