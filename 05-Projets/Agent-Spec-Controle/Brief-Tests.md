---
tags: ["brief", "tests", "controle", "template", "iso-29119"]
created: 2026-04-16
---

---
tags: ["brief", "tests", "controle", "template", "iso-29119"]
created: 2026-04-16
---

# Brief — Stratégie de tests projet Contrôle

> **Usage** : copier ce document en début de conversation avec un LLM (ou dans un prompt système) quand il s'agit de concevoir ou d'auditer les tests d'une tâche. Complément de [[Brief-Specification-Fonctionnelle]] et [[Brief-Plan-Developpement]] : la spec dit **quoi faire**, le plan dit **comment coder**, ce brief dit **comment vérifier**.

---

## 🎯 Rôle du brief test

Un plan de test ERP CONTROL transforme une spec et un plan de dev en stratégie de vérification exhaustive et traçable. Il garantit qu'on ne livre pas une feature sans l'avoir testée à tous les niveaux pertinents de la pyramide, avec des critères d'acceptation explicites et une couverture mesurée.

Ce brief impose un **plan de test formalisé ISO 29119-3 pour chaque tâche**, le **format BDD/Gherkin pour tous les scénarios E2E Playwright**, et des **seuils de couverture ISO par défaut**.

---

## 🏛️ Normes de référence appliquées

| Norme | Sujet | Application ERP CONTROL |
| --- | --- | --- |
| **ISO/IEC 25010** | Modèle de qualité logicielle | Définit les caractéristiques à tester (fiabilité, sécurité IFS, maintenabilité) |
| **ISO/IEC 29119-2** | Processus de test | Structure les phases (planification, conception, exécution, clôture) |
| **ISO/IEC 29119-3** | Documentation | **Format obligatoire du plan de test par tâche** (cf. section dédiée) |
| **ISO/IEC 29119-4** | Techniques de test | Classes d'équivalence, valeurs limites, tables de décision, transitions d'états |
| **ISTQB** | Référentiel de bonnes pratiques | Règle FIRST (unitaires), pattern AAA, BDD/Gherkin |

Ces normes ne sont pas des gadgets académiques : elles donnent un vocabulaire commun et une garantie qu'on n'oublie pas de dimension. Elles s'appliquent **proportionnellement à l'enjeu** de la tâche — une petite correction de template n'aura pas le même volume de documentation qu'un refactor de `check_droits.py`.

---

## 🧱 Pyramide des tests adaptée ERP CONTROL

```
                    ╔══════════════╗
                    ║   E2E UI     ║  Playwright, browser Chromium
                    ║  + Stories   ║  → parcours utilisateur, rendu JS, démos
                    ║   Gherkin    ║  Peu nombreux, lents, fragiles
                  ╔══════════════════╗
                  ║  Intégration     ║  pytest Django
                  ║  Django          ║  → vues, URLs, DB, Client.post()
                  ║  (sans browser)  ║  Moyennement nombreux
              ╔══════════════════════════╗
              ║      Unitaires           ║  pytest Django
              ║  services / helpers /    ║  → logique pure, isolée, rapide
              ║  calculs / config        ║  Très nombreux, millisecondes
              ╚══════════════════════════╝
```

**Règle d'or** : plus on monte, plus c'est cher à maintenir. L'essentiel de la couverture passe par l'unitaire et l'intégration Django. Playwright intervient pour les parcours critiques, pas pour valider des calculs.

### Répartition cible (indicative)

| Niveau | Proportion cible | Temps d'exécution max |
| --- | --- | --- |
| Unitaires | ~70% | < 10 ms par test |
| Intégration Django | ~20% | < 500 ms par test |
| E2E Playwright | ~10% | < 30 s par test |

Une tâche qui n'a que des E2E doit alerter : la pyramide est à l'envers, on va payer cher en maintenance.

---

## ✅ Tests fonctionnels (intégration Django + E2E Playwright)

### Structure d'un cas de test (ISO 29119-3)

Chaque cas de test, quelle que soit sa forme finale (pytest ou Playwright), est conçu avec ces champs :

```
ID           : TC-<MODULE>-<NNN>         (ex: TC-SECURITE-001)
Titre        : <Action ciblée en 1 ligne>
Précondition : <État du système, user connecté, env, données>
Données      : <Inputs précis>
Étapes       : 1. ... / 2. ... / 3. ...
Résultat attendu : <Observable et mesurable>
Résultat obtenu  : <À remplir à l'exécution>
Statut       : PASS / FAIL / BLOCKED
Priorité     : critique / majeure / mineure
```

Le champ **Résultat attendu** doit être **observable** (apparition d'un badge, statut HTTP, contenu DOM) pas conceptuel ("le système réagit correctement" ne suffit pas).

### Techniques de conception (ISO 29119-4)

À appliquer lors de la rédaction des cas de test, pas au moment du code :

- **Classes d'équivalence** — regrouper les entrées qui se comportent pareil, tester un représentant par classe. Exemple couches `ou` : (a) user dans aucune sous-couche / (b) user dans une seule / (c) user dans plusieurs → 3 classes, 3 tests suffisent
- **Valeurs limites** — tester les bornes. Pour un champ `max_length=500` : 499, 500, 501. Pour un OR à N sous-couches : N=2 (minimum), N=4 (cas réel), N=10 (stress)
- **Tables de décision** — combinaisons de conditions. Pour 3 états de couverture × 4 environnements × 2 types de processus : table explicite, on ne liste pas au feeling
- **Transitions d'états** — pour les statuts métier. Tester toutes les transitions valides ET invalides (peut-on passer de ❌ à ✅ sans événement déclencheur ?)
- **Tests basés sur l'expérience** — pour les bugs récurrents du projet (ex: timeouts IFS en journée PROD, caches non invalidés, N+1 sur les `DocumentGroupSet`)

### Critères d'acceptation : format BDD/Gherkin obligatoire pour les E2E Playwright

**Règle non négociable** : tout scénario E2E Playwright est rédigé en Given/When/Then avant d'être codé, même pour une petite tâche. Le Gherkin vit dans le plan de test et dans `stories/*.yaml` le cas échéant.

```gherkin
Feature: Vérification des couches OR dans droits-specifiques

  Scenario: Utilisateur dans une seule branche du OR
    Given je suis connecté en tant que "demo_bot" sur TRN (env_id=2)
    And "demo_bot" appartient au groupe IFS "GAIFS_SVA_ACHAT"
    And "demo_bot" n'appartient à aucun autre groupe parmi CDC, USINE, TRAVAUX
    When j'accède à "/securite/droits-specifiques/achat/?processus=creation_commande&user_identity=DEMOBOT"
    Then je vois la couche "Profil Achat" expansée avec 4 sous-statuts
    And la sous-couche "GAIFS_SVA_ACHAT" est marquée ✓
    And les sous-couches "CDC", "USINE", "TRAVAUX" sont marquées ✗ avec un bouton "Demander"
    And le statut global de la couche parente est ✓

  Scenario: Utilisateur dans aucune branche du OR
    Given je suis connecté en tant que "demo_bot" sur TRN
    And "demo_bot" n'appartient à aucun groupe parmi ACHAT, CDC, USINE, TRAVAUX
    When j'accède à la même URL
    Then les 4 sous-couches sont ✗
    And 4 boutons "Demander" sont affichés, un par sous-couche
    And le statut global de la couche parente est ✗
```

Un Gherkin bien écrit se relit avec un fonctionnel (Elodie, Lucien…) sans aucune connaissance du code.

### Règles de rédaction Gherkin

- **Un scénario = un comportement** — pas de Given/When/Then à tiroirs
- **Given** = état initial vérifiable, pas d'action utilisateur
- **When** = une seule action principale (enchaîner 2-3 `And` si la sémantique reste unitaire)
- **Then** = observation, jamais "et après ça on fait…"
- **Données concrètes** — "demo_bot", "env_id=2", noms de groupes IFS réels, pas "un utilisateur", "un groupe"
- **Factualité** — pas de "le système réagit normalement", écrire ce qu'on voit à l'écran

---

## 🔧 Tests techniques (unitaires + intégration Django)

### Règle FIRST (ISTQB)

Tout test unitaire du projet respecte :

- **F**ast — s'exécute en millisecondes, pas secondes
- **I**solated — aucune dépendance externe (DB réelle, IFS, Redis, filesystem) → mocks obligatoires
- **R**epeatable — même résultat à chaque exécution, quelle que soit la machine, l'heure, l'ordre
- **S**elf-validating — assertion claire, PASS/FAIL, pas d'inspection manuelle de logs
- **T**imely — écrit en même temps que le code, jamais "on ajoutera les tests plus tard"

Un test qui échoue à une seule de ces règles n'est pas un test unitaire : c'est soit un test d'intégration (fast/isolated tombe), soit un test fragile à refactorer.

### Pattern AAA (Arrange / Act / Assert)

Structure imposée de tout test unitaire et d'intégration :

```python
def test_ou_user_dans_une_seule_branche():
    # ARRANGE — préparer les données et mocks
    config = {
        "key": "profil",
        "type": "ou",
        "couches": [
            {"key": "achat", "type": "groupe_ifs", "group_name": "GAIFS_SVA_ACHAT"},
            {"key": "cdc",   "type": "groupe_ifs", "group_name": "GAIFS_SVA_CDC"},
        ],
    }
    mock_group_members = {"GAIFS_SVA_ACHAT": {"DEMOBOT"}, "GAIFS_SVA_CDC": set()}

    # ACT — appeler le code à tester
    result = _evaluer_couche(config, user_identity="DEMOBOT", env=mock_env,
                             caches={"groups": mock_group_members})

    # ASSERT — vérifier le résultat
    assert result["ok"] is True
    assert len(result["sub_results"]) == 2
    assert result["sub_results"][0]["ok"] is True
    assert result["sub_results"][1]["ok"] is False
```

Pas de logique avant `# ARRANGE`, pas de setup mélangé avec des assertions, pas d'assertion intermédiaire entre `# ACT` et `# ASSERT`.

### Ce qui mérite un test unitaire

Toute fonction avec **au moins une branche conditionnelle** ou **au moins un calcul non trivial** doit être testée unitairement. Exemples typiques ERP CONTROL :

- Fonctions de `securite/services/check_droits.py` (`check_couches_for_user`, `_evaluer_couche`, `get_rsi_matrix`, `_fetch_person_group_members`)
- Calculs de couverture, de RSI, de différences d'environnements
- Validation du dict `DOMAINES` au démarrage
- Helpers de parsing des réponses IFS
- Transitions de statuts (si/quand un modèle Django avec workflow existe)

### Ce qui mérite un test d'intégration Django (sans browser)

Tout endpoint, vue, formulaire ou commande management :

- Endpoints AJAX (`POST /securite/api/demande-groupe/`, JSON attendu en retour)
- Vues liste avec filtres query string (`?env_id=2&processus=…`)
- Authentification / permissions (user anonyme → 403, user sans groupe → accès limité)
- Migrations Django (données initiales, rétro-compat des données existantes)
- Tâches Celery (exécution synchrone avec `CELERY_TASK_ALWAYS_EAGER=True` en test)

### Tests de régression

Pour chaque tâche, lister **explicitement** les comportements existants qui ne doivent pas changer :

- Les vues / processus **non modifiés** doivent produire exactement le même rendu qu'avant
- Les exports existants (Excel, rapports) doivent sortir le même format
- Les MigrationRun / snapshots historiques ne doivent pas apparaître cassés
- Les endpoints AJAX existants (non touchés) doivent retourner le même JSON

Un test de régression absent = un bug futur garanti à la prochaine release.

---

## 📊 Couverture de code

### Seuils imposés (défaut ISO 29119-4)

| Métrique | Seuil minimal | Mesure |
| --- | --- | --- |
| **Line coverage** | **≥ 70%** | Lignes de code exécutées |
| **Branch coverage** | **≥ 60%** | Toutes les branches if/else testées |
| **Function coverage** | ≥ 80% (indicatif) | Fonctions appelées au moins une fois |

Ces seuils s'appliquent au **code nouveau ou modifié** dans la tâche. Le code legacy non touché n'est pas un sujet (tant qu'il n'est pas modifié, il n'est pas aggravé).

### Mesure

- Outil : `pytest-cov` sur le repo `erp-control`
- Commande : `pytest --cov=securite --cov-report=term-missing --cov-report=html`
- Rapport HTML archivé dans `htmlcov/` (non commité), résumé collé dans la PR

### Piège "100% ≠ qualité"

Une couverture à 100% ne garantit rien : un test peut exécuter une ligne sans en vérifier le résultat. La couverture mesure l'**exécution**, pas la **pertinence des assertions**. Un test sans `assert` donne 100% de couverture et ne détecte aucun bug.

**Contrôle qualité complémentaire** : pour toute fonction critique (sécurité, calculs de droits), au moins un test par branche logique avec assertion sur le **résultat métier**, pas juste "ne lève pas d'exception".

---

## 🚦 Plan de test par tâche — structure ISO 29119-3

Chaque tâche doit produire un plan de test formalisé. Le plan vit :

- En section dédiée du plan de dev local (`plans/<slug>.md` → section "Plan de test")
- Ou en note Obsidian dédiée `05-Projets/Tests-Tache-<ID>.md` pour les tâches majeures

### Template imposé

```markdown
# Plan de test — <Titre tâche> (Odoo task #<ID>)

## 1. Objectifs et périmètre
### Ce qui est testé
- Fonction / module / parcours X
- Interaction Y
### Ce qui est exclu
- IFS lui-même (hors périmètre)
- Modules Z non modifiés (sauf régression ciblée)

## 2. Stratégie
Répartition dans la pyramide pour cette tâche :
- Unitaires : N tests (pytest Django)
- Intégration Django : M tests (pytest Django, Client.post/get)
- E2E Playwright : P scénarios Gherkin

## 3. Environnements de test
- DB de test isolée (pytest-django crée/détruit)
- Mocks IFS depuis `assets/fixtures/<profile>/ifs/` (repo Playwright)
- Env cible E2E : TRN (env_id=2) en mode `mock` pour CI, `live` pour validation pre-merge
- Snapshot de test fixe (pas J-1 réel)

## 4. Données de test
- Factories / fixtures : <liste des factories Django nécessaires>
- User Django : `demo_bot` avec groupes <…>
- Fixtures IFS JSON : `<chemins précis>`

## 5. Critères d'entrée
- Migrations Django appliquées
- `demo_bot` existe avec les droits requis
- `config/selectors.json` à jour (repo Playwright)
- Mocks IFS présents pour tous les endpoints consommés

## 6. Critères de sortie
- 0 test FAIL dans les 3 niveaux
- Couverture ≥ 70% line / ≥ 60% branch sur le code nouveau
- Gherkin relu et validé par un fonctionnel (si applicable)
- Pipeline CI vert

## 7. Cas de test
### 7.1 Unitaires (pytest Django)
- TC-<MODULE>-001 : <titre> (AAA, FIRST)
- TC-<MODULE>-002 : ...
### 7.2 Intégration Django (pytest Django, pas de browser)
- TC-<MODULE>-010 : POST /endpoint → 200 + side-effect DB vérifié
- ...
### 7.3 E2E Playwright (Gherkin + code)
- TC-<MODULE>-020 : Feature + Scenario Gherkin ci-dessous
  ```gherkin
  Feature: ...
    Scenario: ...
      Given ...
      When ...
      Then ...
  ```
### 7.4 Tests de régression
- TC-REG-001 : vue / processus non modifié X → rendu identique
- ...

## 8. Techniques appliquées
- Classes d'équivalence sur <entrée X> : 3 classes identifiées
- Valeurs limites sur <champ Y>
- Table de décision pour <combinatoire Z>
- Transitions d'états sur <workflow W> (si applicable)

## 9. Gestion des anomalies
Sévérités :
- **Bloquant** : empêche l'usage de la feature → stoppe la release
- **Majeur** : dégrade l'expérience, contournement possible
- **Mineur** : cosmétique, à corriger en v+1
Chaque bug détecté → ticket Odoo lié à la tâche d'origine.
```

---

## 🔄 Definition of Done (à coller dans chaque plan de dev)

Pour que la tâche passe de `Dev en cours` à `En recette` :

```
☐ Plan de test ISO 29119-3 rédigé et archivé
☐ Tests unitaires écrits (pytest Django, AAA, FIRST)
☐ Tests d'intégration Django écrits (endpoints, vues, DB)
☐ Scénarios E2E Playwright rédigés en Gherkin ET codés
☐ Sélecteurs ajoutés dans config/selectors.json (repo Playwright)
☐ Mocks IFS ajoutés dans assets/fixtures/ (repo Playwright)
☐ Tests de régression listés et exécutés
☐ Couverture ≥ 70% line / ≥ 60% branch sur code nouveau (pytest-cov)
☐ Gherkin relu et validé par le fonctionnel (si applicable)
☐ Pipeline CI vert sur les 2 repos (erp-control + erp-control-playwright)
☐ PR applicative et PR Playwright ouvertes et liées
```

Une case non cochée = la tâche ne passe pas en recette.

---

## ⚠️ Règles de qualité non négociables

- **Plan de test ISO 29119-3 obligatoire** par tâche, proportionné à l'enjeu mais jamais absent
- **BDD/Gherkin systématique** pour tout scénario E2E Playwright, même les petits
- **Règle FIRST** appliquée aux unitaires sans exception — si un test ne peut pas être Fast+Isolated, ce n'est plus un unitaire
- **Pattern AAA** imposé pour la structure de tout test pytest
- **Pas de test sans assertion** — un `@pytest.mark.parametrize` avec un `pass` ne compte pas
- **Seuils de couverture** mesurés et respectés : 70% line / 60% branch sur le code nouveau
- **Tests de régression listés explicitement** pour les modules adjacents non modifiés
- **Rédaction des tests avant ou avec le code**, jamais après ("je coderai les tests après" = tests jamais écrits)

---

## 🧩 Intégration aux autres briefs

- [[Brief-Specification-Fonctionnelle]] définit **ce qu'on teste** (fonctionnalité cible, endpoints IFS, comportements attendus)
- [[Brief-Plan-Developpement]] définit **comment le code est organisé** (fichiers, signatures, découpage PRs) — le plan de test s'insère en section dédiée du plan de dev
- Ce brief définit **comment on vérifie** (pyramide, formats, seuils, templates)

La cohérence des 3 documents est le gage qu'une tâche passe sans frictions de la spec au merge.

---

## 📚 Ressources

- [[Brief-Specification-Fonctionnelle]] — brief amont (quoi faire)
- [[Brief-Plan-Developpement]] — brief milieu (comment coder)
- [[01-Architecture]] — architecture d'automatisation des agents
- [[04-Agent-Dev]] — infrastructure d'exécution (worktree, Claude Code, PR)
- Repo Playwright : `C:\Users\Shadow\Documents\GitHub\erp-control-playwright`
- Repo principal : `erp-control` (Django)
- ISO/IEC 29119 : https://www.iso.org/standard/81291.html
- ISTQB Foundation Level Syllabus : https://www.istqb.org/certifications/certified-tester-foundation-level

---

#brief #tests #controle #template #iso-29119
