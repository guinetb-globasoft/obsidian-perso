---
tags: ["brief", "developpement", "controle", "template"]
created: 2026-04-16
---

---
tags: ["brief", "developpement", "controle", "template"]
created: 2026-04-16
---

# Brief — Plan de développement projet Contrôle

> **Usage** : copier ce document en début de conversation avec un LLM (ou dans un prompt système) avant de lui demander de produire un plan de développement actionnable à partir d'une spécification. Complément direct de [[Brief-Specification-Fonctionnelle]] : la spec dit **quoi faire**, ce brief dit **ce qu'il faut en plus pour coder sans revenir poser des questions**.

---

## 🎯 Rôle du plan de développement

Un plan de dev ERP CONTROL transforme une spec technique en document qu'un développeur (humain ou Claude Code) peut exécuter tête baissée. Il doit éliminer toute ambiguïté d'implémentation **avant** que le code ne soit écrit.

### Différence spec ↔ plan

| Spec technique | Plan de développement |
| --- | --- |
| Décrit la solution (quoi modifier, quels endpoints IFS) | Décrit l'exécution (dans quel ordre, avec quelle structure de code, quels tests) |
| Valide avec le métier | Valide avec le développeur |
| Stockée dans `x_studio_specifications_techniques` | Stockée en `.md` local (dossier `plans/`) ou dans une note Obsidian dédiée |
| Écrite avant le dev | Écrite juste avant le dev, après résolution des questions ouvertes |

Le plan peut (et doit) **enrichir** la spec avec des précisions d'implémentation — mais il ne la contredit jamais. S'il y a contradiction, c'est le signe qu'il faut mettre à jour la spec d'abord.

---

## 📋 Checklist de complétude d'un plan de dev

Un plan est prêt pour le dev quand toutes les cases ci-dessous sont cochées. Les items sont regroupés par criticité.

### 🔴 Bloquants — sans ça le dev va deviner ou mal faire

- [ ] **État actuel vs cible** pour chaque élément modifié
  - Pour chaque fichier config, dict, fonction : bloc de code "avant" et "après" côte à côte
  - Pas de "remplacer X par Y" sans montrer X en entier
  - Si le dict fait 500 lignes, extraire uniquement la portion concernée mais l'extraire **intégralement**

- [ ] **Signatures de fonctions définitives**
  - Pour chaque nouvelle fonction ou refactor : prototype Python complet avec annotations de type
  - Types de retour précis (`dict` ne suffit pas → `dict[str, Any]` avec les clés documentées)
  - Paramètres : ordre, obligatoires/optionnels, valeurs par défaut

- [ ] **Contrats de données**
  - Quand une structure change (ex: une clé ajoutée à `entry` consommé par un template) : montrer la structure **complète** avant/après
  - Exemple JSON ou dict Python concret, pas une description en prose
  - Préciser qui produit / qui consomme chaque clé

- [ ] **Questions ouvertes de la spec : toutes résolues**
  - Recopier chaque question ouverte de la spec en début de plan
  - Pour chaque : réponse + source (ex: "vérifié sur TRN id=2", "confirmé par Elodie le 14/04", "cf. code `utilisateurs/services/sync.py:142`")
  - Si une question reste ouverte, le plan n'est pas prêt — soit la trancher, soit la remonter

- [ ] **Règles métier limites et edge cases**
  - Tout comportement non évident doit être explicité (ex: "si le OR contient uniquement des `groupe_finance`, l'applicabilité RSI = ...")
  - Cas d'erreur : quoi retourner si un fetch IFS échoue ? `None` / `False` / exception ?
  - Cas vide : comportement si une liste est vide, si un user n'a aucun groupe, si un env n'a jamais été sync

### 🟠 Importants — le dev peut avancer mais risque des aller-retours

- [ ] **Rétro-compatibilité du config ou des modèles**
  - Le dict / modèle modifié est-il lu ailleurs que par le module principal ? (scripts d'export, commandes management, tests existants, autres apps)
  - Si oui : lister les consommateurs et vérifier qu'ils gèrent le nouveau format
  - Faut-il une migration Django ? Un script one-shot ?

- [ ] **Validation du config au démarrage**
  - Si le config gagne un nouveau type / une nouvelle clé : ajouter une validation (au démarrage ou via un test unitaire) qui échoue vite si le config est mal formé
  - Liste des règles de validation (ex: "un `ou` doit contenir ≥2 sous-couches, un `groupe_personne_ifs` doit avoir un `group_id` non vide")

- [ ] **Gestion des caches**
  - Structure du cache : clé, valeur, sémantique (notamment : `None` signifie quoi ?)
  - Invalidation : quand le cache est vidé ? (redémarrage worker, signal, TTL ?)
  - Cohérence avec les caches existants du module

- [ ] **Gestion d'erreurs IFS**
  - Timeout : quelle durée ? (défaut projet : 30s en TRN, à adapter en PROD)
  - Retry : oui/non, combien de fois ?
  - Log level : `warning` pour les échecs attendus, `error` pour les cas inattendus
  - Remontée côté UI : le user voit quoi si IFS est down ?

- [ ] **Hypothèses sur le code existant à vérifier**
  - Tout "aucun changement nécessaire côté X" doit être listé explicitement comme hypothèse à valider
  - Exemple : "le JS existant relit `dataset.groupName`" → mettre en checklist "vérifier le fichier JS avant de coder le template"

### 🟡 Utiles — confort, qualité, prod

- [ ] **Découpage en commits / PRs**
  - Si > 1 fichier touché ou > 200 lignes : proposer un découpage en 2 à 5 PRs isolées et reviewables
  - Chaque PR doit être **mergeable indépendamment** sans casser la prod (feature flag ou morceau dormant si besoin)
  - Ordre suggéré : refactor d'abord (0 changement fonctionnel), puis mécanismes transverses, puis usages

- [ ] **Plan de tests concret**
  - Un plan de test formalisé ISO 29119-3 est obligatoire pour chaque tâche — voir [[Brief-Tests]] pour le template et les règles détaillées
  - Répartition imposée : unitaires (pytest Django, logique pure) / intégration Django (pytest Django, vues sans browser) / E2E (Playwright, Gherkin systématique)
  - Tests de non-régression : lister les processus / pages **non modifiés** à vérifier après le refactor
  - Seuils de couverture : ≥ 70% line / ≥ 60% branch sur le code nouveau (cf. [[Brief-Tests]])

- [ ] **Observabilité**
  - Logs à ajouter : niveau + message + contexte (user_identity, env_pk, processus, couche)
  - Métriques éventuelles (Flower / monitoring Celery)
  - Points chauds en prod (ex: nombre d'appels IFS par requête)

- [ ] **Communication avant mise en prod**
  - Si changement de comportement utilisateur-visible : qui prévenir ? (Elodie, Lucien, Sahar, Jessica...) quand ? comment ?
  - Feature flag nécessaire ? (par défaut désactivé puis activation contrôlée)
  - Rollback : revert git suffit, ou migration inverse nécessaire ?

- [ ] **Impact sur exports / rapports existants**
  - Y a-t-il des exports Excel, rapports PDF, API qui consomment les fonctions modifiées ?
  - Le format de sortie change-t-il ? Si oui → lister les consommateurs impactés

---

## 🎭 Couverture Playwright (E2E, démos, social)

Le repo [`erp-control-playwright`](file:///C:/Users/Shadow/Documents/GitHub/erp-control-playwright) est **la seule source de E2E** du projet et le producteur des artefacts avant-vente et marketing. Toute tâche de dev doit se poser les 3 questions ci-dessous et les trancher dans le plan.

### Répartition des tests (règle forte)

| Type de test | Repo | Quand |
| --- | --- | --- |
| Unitaire (logique pure, services, helpers, calculs) | `erp-control` (pytest Django) | Systématique |
| Intégration Django (vues, DB, `Client.post()`, `TestCase`, pas de browser) | `erp-control` (pytest Django) | Dès qu'une vue / URL / formulaire est touché |
| E2E (parcours UI avec browser, intégration IFS end-to-end) | `erp-control-playwright` | Systématique pour toute feature UI-visible |
| Démo avant-vente | `erp-control-playwright` (mode `live`) | À la discrétion, cf. signaux ci-dessous |
| Capture LinkedIn / vidéo marketing | `erp-control-playwright` (mode `mock`) | À la discrétion, cf. signaux ci-dessous |

**Ligne de partage pytest Django ↔ Playwright** : si le test n'a pas besoin d'un browser, il reste dans pytest Django (plus rapide, plus stable, isolé de l'UI). Dès qu'on veut valider un parcours utilisateur réel (clic, formulaire rempli, rendu JS, interaction IFS live), c'est Playwright.

**Règle non négociable** : aucun test avec browser ne vit dans le repo `erp-control`. Si une tâche nécessite un parcours UI, il va dans `scenarios/tests/` du repo Playwright.

### Contexte repo Playwright (à connaître avant d'écrire le plan)

- **Path** : `C:\Users\Shadow\Documents\GitHub\erp-control-playwright`
- **Modes** : `IFS_MODE=mock` (déterministe, pour CI et vidéos) vs `live` (demo avant-vente sur env contrôlé)
- **Structure clé** :
  - `scenarios/tests/` — tests pytest E2E
  - `scenarios/demos/` — démos produit (avant-vente, mode `live`)
  - `scenarios/social/` — captures courtes LinkedIn (mode `mock`)
  - `scenarios/utils/` — modules partagés (browser, config, mocking IFS, recording)
  - `stories/*.yaml` — scénarios narratifs (hook, promise, steps, CTA, closing_message)
  - `config/selectors.json` — sélecteurs mutualisés (pas de sélecteur hardcodé dans le test)
  - `config/demo_profiles.json` — viewport / locale / trace / record_video par profil
  - `assets/fixtures/<profile>/ifs/` — mocks IFS (JSON/XML) par profil
  - `scripts/export_*.py` — post-prod FFmpeg (vertical LinkedIn, desktop sales)
- **User de captation** : `demo_bot` (jamais d'utilisateur réel, jamais de données client réelles)
- **Prérequis** : Django ERP Control tourne sur `http://localhost:8000` + FFmpeg installé

### Checklist Playwright à intégrer au plan

À ajouter aux 🟠 Importants de la checklist principale :

- [ ] **Décision E2E** : est-ce que la feature est UI-visible ou touche un parcours utilisateur ? Si oui → E2E obligatoire dans `scenarios/tests/test_<slug>.py`
- [ ] **Scénario E2E décrit** : fichier cible, user de test (`demo_bot` + droits nécessaires), env cible (TRN id=2 par défaut), assertions clés
- [ ] **Sélecteurs** : lister les sélecteurs à ajouter / modifier dans `config/selectors.json` (aucun sélecteur hardcodé dans le test)
- [ ] **Mocks IFS** : si un nouvel endpoint est consommé (ex: `PersonGroupHandling.svc/DocumentGroupSet`), fournir le JSON de mock dans `assets/fixtures/<profile>/ifs/`. Sinon, risque que le test échoue en CI (mock) alors qu'il passe en local (live)
- [ ] **Décision démo / social** : évaluer les signaux ci-dessous. Si non pertinent, l'écrire explicitement ("pas de démo prévue car feature interne")

À ajouter aux 🟡 Utiles :

- [ ] **Si démo produit** : fichier `stories/<slug>.yaml` avec les clés standards (`title`, `audience`, `format`, `problem`, `promise`, `hook`, `steps[]`, `closing_message`, `cta`) + script `scenarios/demos/<slug>.py`
- [ ] **Si capture LinkedIn / social** : `scenarios/social/<slug>_express.py` + post-prod via `scripts/export_linkedin_vertical.py`
- [ ] **Archivage des livrables vidéo** : préciser où les GIF / MP4 finaux atterrissent (Drive ? Notion ? Miro ?) — indispensable si c'est un livrable commercial

### Signaux pour déclencher une démo ou un social

Pas de règle automatique (à ta discrétion), mais voici les signaux qui méritent au minimum de poser la question dans le plan :

- **Gain de temps spectaculaire** (ex: "2h → 2min" comme `stories/promotion.yaml`) → candidat démo
- **Différenciation vs IFS natif** (quelque chose qui n'existe pas dans IFS standard) → candidat démo + social
- **Workflow à étapes visuelles** (comparaison avant/après, tableau de bord, visualisation) → bon pour capture
- **Feature backend invisible** (refacto, perf, sécurité silencieuse) → E2E seulement, pas de démo
- **Feature sensible / confidentielle client** → pas de social, éventuellement démo interne

### Impact sur le découpage en PRs

Les deux repos sont séparés mais couplés. Règles :

- Une feature touchant l'UI ouvre **2 PRs parallèles** : une sur `erp-control`, une sur `erp-control-playwright`
- **Ordre de merge obligatoire** : d'abord `erp-control` (sinon les E2E cassent), puis `erp-control-playwright`
- Si ajout d'un sélecteur : le commit `selectors.json` et le commit `test_<slug>.py` restent dans la **même PR Playwright** pour faciliter le rollback
- La PR Playwright référence la PR ERP Control dans son body (et inversement)

### Risques spécifiques Playwright à lister dans la section "Risques"

- **Sélecteurs fragiles** : si le HTML change dans `erp-control` sans maj de `config/selectors.json` → test casse silencieusement en CI. Mitigation : `scenarios/tests/test_selectors_validity.py` doit être relancé après tout changement de template
- **Nouveau endpoint IFS non mocké** : test passe en `live`, échoue en `mock` → toujours ajouter la fixture JSON en même temps que le test
- **Données client réelles dans capture** : interdit absolu — utiliser uniquement les fixtures `sales_demo` / `social_demo` / `minimal`
- **Cohérence `demo_bot` ↔ nouveaux droits** : si la feature ajoute des exigences de permissions (ex: appartenance à un groupe IFS), vérifier que `demo_bot` les a, sinon prévoir l'ajout dans le seed
- **Vidéo = coût temps** : une capture propre avec post-prod prend 1 à 2 h. Ne pas s'engager à en produire une par défaut, le plan doit expliciter si oui/non

---

## 🧩 Structure type d'un plan de dev

```markdown
# Plan — <Titre tâche> (Odoo task #<ID>)

## Contexte
<résumé 3-5 lignes : quoi, pourquoi, quels fichiers>

## Questions ouvertes résolues
- Q1 du spec → réponse + source
- Q2 du spec → réponse + source

## Fichiers modifiés
| Fichier | Action |
|---|---|
| path/to/file.py | résumé en 1 ligne |

## Détail d'implémentation

### 1. <Mécanisme transverse 1>
<code avant / code après>
<signature fonctions>
<contrats de données>

### 2. <Mécanisme transverse 2>
...

### 3. <Modifications applicatives>
Mod 1 — <processus> : avant / après
Mod 2 — ...

## Découpage en PRs (si pertinent)
- PR1 : refactor, 0 changement fonctionnel
- PR2 : mécanisme transverse A (+ tests, non utilisé encore)
- PR3 : mécanisme transverse B
- PR4 : UI
- PR5 : config (les modifications applicatives)

## Tests de vérification

Référence complète : [[Brief-Tests]] (template ISO 29119-3, pyramide, BDD Gherkin, seuils de couverture).

Résumé à coller dans le plan de dev :

### Unitaires (pytest Django, logique pure, règle FIRST + pattern AAA)
1. ...

### Intégration Django (pytest Django, vues / DB, pas de browser)
2. ...

### E2E (repo Playwright, browser, Gherkin obligatoire)
- Fichier : `scenarios/tests/test_<slug>.py`
- User : `demo_bot`, env TRN id=2
- Sélecteurs à ajouter dans `config/selectors.json` : ...
- Mocks IFS à ajouter dans `assets/fixtures/<profile>/ifs/` : ...
- Scénarios Gherkin :
  ```gherkin
  Feature: ...
    Scenario: ...
      Given ...
      When ...
      Then ...
  ```

### Régression
- Modules non modifiés à vérifier : ...

### Couverture cible
- ≥ 70% line / ≥ 60% branch sur code nouveau (pytest-cov)

## Couverture démo / social
- Démo produit prévue : oui / non — si oui : `stories/<slug>.yaml` + `scenarios/demos/<slug>.py`
- Capture LinkedIn prévue : oui / non — si oui : `scenarios/social/<slug>_express.py`
- Archivage livrable vidéo : <Drive ? Notion ? Miro ?>

## Observabilité
- Logs ajoutés : ...

## Risques et points d'attention
- Changements de comportement à communiquer
- Hypothèses à valider avant de coder
- Impact prod (perf, rétro-compat)

## Communication
- Qui prévenir avant merge : ...
- Qui prévenir avant prod : ...
```

---

## 🔄 Workflow de travail

1. La tâche passe en stage **Spécification terminée** avec une spec remplie dans `x_studio_specifications_techniques`
2. Avant de lancer le dev : faire un **plan local** en `.md` (ex: `C:\Users\Shadow\.claude\plans\<slug>.md`) en passant la spec + ce brief à un LLM
3. Le plan remonte les **questions ouvertes** → les trancher (IFS TRN, user, code) puis enrichir le plan
4. Valider la checklist de complétude ci-dessus
5. Le plan sert ensuite d'input à Claude Code (ou de guide humain) pour le dev
6. À la fin du dev : archiver le plan (déplacer dans `plans/archives/` ou supprimer une fois la PR mergée)

---

## ⚠️ Règles de qualité non négociables

- **Un plan n'invente rien** : il résout des questions ouvertes par vérification (code, IFS, user) ou les remonte, jamais par supposition
- **Un plan n'écrit pas le code** : il écrit assez de pseudo-code et de signatures pour lever les ambiguïtés, pas plus
- **Un plan pense à la prod** : performance IFS, rétro-compat, observabilité, communication utilisateurs doivent être abordés explicitement
- **Un plan est révisable** : si pendant le dev une hypothèse tombe, on met à jour le plan avant de coder la suite — pas l'inverse
- **Un plan est jetable** : une fois la PR mergée, il n'a plus de valeur (la vérité devient le code + la spec Odoo)
- **Playwright = seule source de tests avec browser** : aucun test nécessitant un browser ne vit dans le repo `erp-control`. Le pytest Django du repo principal couvre l'unitaire (logique pure) et l'intégration sans browser (vues, DB, `Client.post()`, `TestCase`)
- **Tranchage démo/social explicite** : chaque plan dit oui ou non pour démo et social, jamais "on verra plus tard"

---

## 📚 Ressources

- [[Brief-Specification-Fonctionnelle]] — brief amont pour produire la spec technique
- [[Brief-Tests]] — brief dédié stratégie de tests (ISO 29119-3, BDD Gherkin, seuils couverture)
- [[01-Architecture]] — architecture de l'automatisation des agents
- [[04-Agent-Dev]] — infrastructure d'exécution de l'agent dev (worktrees, Claude Code, PR GitHub)
- [[02-Workflow-Odoo]] — stages et transitions kanban
- Repo Playwright : `C:\Users\Shadow\Documents\GitHub\erp-control-playwright` — tests E2E, démos avant-vente, captures social
- Repo principal : `erp-control` (Django) — application web déployée sur Render

---

#brief #developpement #controle #template
