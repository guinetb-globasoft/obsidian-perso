---
tags: ["installation", "controle"]
created: 2026-04-16
---

# Installation pas à pas

## Prérequis

- Python 3.11+
- Git
- ripgrep (`rg`) — obligatoire pour `grep_code`
- Clé API Odoo (Paramètres → Mon profil → Clés API dans globasoft)
- Clé API Anthropic (console.anthropic.com)
- Repo Contrôle cloné localement

## Étape 1 — Créer le stage Odoo

1. Aller sur https://globasoft1.odoo.com/odoo/project/4/tasks
2. Vue kanban → cliquer sur le bouton "+" à côté de "En travail"
3. Nommer la colonne **"Spec à enrichir"**
4. Drag-and-drop pour la positionner entre "En travail" et "En attente de reprio"
5. Noter l'ID du stage (via développeur mode ou en inspectant l'URL du stage)

## Étape 2 — Extraire le zip

```bash
cd ~/dev
unzip agent-spec.zip
cd agent-spec
```

## Étape 3 — Environnement Python

```bash
python -m venv .venv
source .venv/bin/activate          # Linux/macOS
# .venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

## Étape 4 — Installer ripgrep

```bash
# macOS
brew install ripgrep

# Ubuntu/Debian
sudo apt install ripgrep

# Windows
choco install ripgrep
# ou via scoop : scoop install ripgrep
```

Vérif : `rg --version`

## Étape 5 — Configuration

### Copier les templates
```bash
cp config/.env.example config/.env
```

### Éditer `config/.env`
```ini
# Odoo
ODOO_URL=https://globasoft1.odoo.com
ODOO_DB=globasoft1
ODOO_USERNAME=ton.email@globasoft.com
ODOO_API_KEY=xxxxxxxxxxxxxxxxxxxx
ODOO_PROJECT_ID=4

# Anthropic
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxx
ANTHROPIC_MODEL=claude-opus-4-7

# Repo Contrôle
REPO_PATH=/Users/benoit/dev/controle    # chemin absolu vers le repo
REPO_AUTO_PULL=true

# Runtime
POLL_INTERVAL_SECONDS=120
MAX_TOOL_TURNS=25
LOG_LEVEL=INFO
```

### Éditer `config/settings.yaml`
Renseigner l'ID du stage créé à l'étape 1 :
```yaml
stages:
  spec_a_enrichir: <ID>   # À renseigner
transitions:
  trigger_stage_id: <même ID>
```

## Étape 6 — Premier test

Test sans impact sur Odoo :
```bash
./run.py --task-id 641 --dry-run
```

Tu devrais voir :
- Les appels Claude qui arrivent
- Les tools appelés (list_dir, grep, read_file, ...)
- La spec HTML générée en console à la fin

Si OK, tester sans dry-run sur une tâche que tu mets expressément en "Spec à enrichir" :
```bash
./run.py --task-id <X>
```

## Étape 7 — Mise en polling

Une fois que les specs produites te conviennent :
```bash
./run.py --watch
```

Tourne en continu, poll toutes les 2 min (configurable). `Ctrl+C` pour stopper.

Pour le lancer en tâche de fond en permanence :
- **macOS** : créer un fichier `.plist` launchd
- **Linux** : unit systemd
- **Windows** : Task Scheduler avec `pythonw run.py --watch`

## Troubleshooting

| Erreur | Cause probable | Solution |
|--------|----------------|----------|
| `Authentification Odoo échouée` | Clé API ou user incorrect dans `.env` | Régénérer clé API dans Odoo |
| `ripgrep (rg) n'est pas installé` | `rg` absent du PATH | Réinstaller + relancer le shell |
| `trigger_stage_id non configuré` | Oubli étape 5 sur `settings.yaml` | Renseigner l'ID du stage |
| Chemin hors du repo | `REPO_PATH` mal défini | Mettre chemin absolu |
| `Max turns atteint` | Agent perdu dans l'exploration | Affiner le prompt (voir [[05-Prompt-System]]) |

---

#installation #controle
