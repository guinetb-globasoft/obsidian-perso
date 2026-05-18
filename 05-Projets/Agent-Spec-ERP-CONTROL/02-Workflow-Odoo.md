---
tags: ["workflow", "odoo", "controle"]
created: 2026-04-16
---

# Workflow Odoo — Stages du kanban

## Projet cible

- **Nom** : ERP_Control_
- **Instance** : globasoft (globasoft1.odoo.com)
- **ID** : 4
- **URL** : https://globasoft1.odoo.com/odoo/project/4/tasks

## Stages actuels (project.task.type)

| Seq | Stage | ID | Rôle |
|-----|-------|----|------|
| 0 | Brouillon | 22 | Idée brute, pas traitée |
| 1 | En travail | 59 | **Tu rédiges la description** |
| 2 | En attente de reprio | 115 | Backlog |
| 3 | Spécification terminée | 42 | **Prêt pour dev** |
| 4 | Dev en cours | 23 | Développement en cours |
| 6 | En recette (sur Render) | 26 | Test en environnement de recette |
| 7 | Validé | 57 | Terminé |

## Stage à ajouter

**"Spec à enrichir"** — à positionner en séquence 2, après "En travail" et avant "En attente de reprio".

- Action à faire : créer manuellement via le kanban Odoo (drag-and-drop pour l'ordre)
- Une fois créé → récupérer l'ID et le reporter dans `config/settings.yaml` :
  - `stages.spec_a_enrichir: <ID>`
  - `transitions.trigger_stage_id: <même ID>`

## Workflow cible

```
Brouillon → En travail → [Spec à enrichir] → Spécification terminée → Dev en cours → Recette → Validé
    0          1              2 (NEW)              3 → 4                  4 → 5        6        7
   (toi)     (toi)        (trigger agent)     (agent a fini)           (dev)
                                               (tu relis avant)
```

## Transitions déclenchées par l'agent

| Événement | Transition |
|-----------|------------|
| Tâche en `Spec à enrichir` détectée | Agent Spec démarre |
| Agent Spec réussit | Écriture spec HTML + déplacement en `Spécification terminée` |
| Agent Spec échoue | Retour en `En travail` (pour que tu saches qu'il y a un souci) |

## Champ cible pour la spec

- **Nom technique** : `x_studio_specifications_techniques`
- **Type** : HTML (Studio custom field)
- **Libellé onglet** : "Spécifications techniques"

L'agent écrit du HTML propre (pas de Markdown) directement dans ce champ.

## Observations sur les tâches existantes

Sur les 15 tâches récentes observées :
- Les descriptions sont **riches et structurées** (URLs, tableaux, diagnostics, priorisation)
- Aucune n'a actuellement de contenu dans `x_studio_specifications_techniques`
- L'agent partira de zéro à chaque fois, clean

Exemples de tâches intéressantes pour les premiers tests :
- **#640 Incident Export** : description type "diagnostic + proposition", bon pour tester la compréhension technique
- **#641 Modifications sur les rôles Achat lot 4** : description très riche avec URLs d'endpoints, parfait pour tester le grep et la réutilisation de code
- **#634 Suivi factures finance** : description courte avec images, voir comment l'agent gère le manque d'info

---

#workflow #odoo #kanban #controle
