---
tags: ["normes", "design", "ux", "ui", "accessibilité", "sécurité", "web", "ISO", "méthode", "qualité"]
created: 2026-08-15
---

---
tags:
  - normes
  - design
  - ux
  - ui
  - accessibilité
  - sécurité
  - web
  - ISO
  - méthode
  - qualité
created: 2026-08-15
source: conversation Claude
liens: "[[Normes à suivre - Rédaction documents professionnels]]"
---

# Normes & Bonnes pratiques — Design UI/UX & Développement Web

> [!tip] Objectif de cette note
> Référentiel personnel des normes et bonnes pratiques à appliquer sur tout développement d'interface web (ERP CONTROL, applications Django, interfaces métier).

---

## 🎨 UX / Ergonomie

### ISO 9241-110 — Les 7 principes de dialogue

| Principe | Résumé | Exemple concret |
|---|---|---|
| **Adéquation à la tâche** | Afficher uniquement ce qui est pertinent au moment T | Pré-remplir les champs connus, ne pas demander ce que le système peut déduire |
| **Auto-description** | L'interface s'explique sans doc externe | Labels précis ("Enregistrer et continuer"), messages d'erreur avec solution |
| **Contrôlabilité** | L'utilisateur pilote, pas le système | Toujours proposer Annuler / Retour / Défaire, confirmation avant actions irréversibles |
| **Conformité aux attentes** | Se comporter comme l'utilisateur l'anticipe | Conventions plateforme respectées, cohérence interne, logo → accueil |
| **Tolérance aux erreurs** | Limiter les erreurs et permettre de s'en sortir | Validation temps réel, confirmation avant suppression, messages d'erreur clairs |
| **Adaptabilité** | S'adapter aux préférences et au niveau d'expertise | Raccourcis clavier, mode expert vs guidé, responsive |
| **Adéquation à l'apprentissage** | Faciliter la montée en compétence progressive | Onboarding progressif, tooltips contextuels, états vides explicatifs |

> [!warning] Pièges fréquents
> - Bouton rouge pour une action positive → viole la conformité aux attentes
> - Suppression par simple clic sur un badge → viole la contrôlabilité et la tolérance aux erreurs
> - État d'un processus persisté uniquement en `sessionStorage` → non tolérant aux pannes
> - Modale sans focus trap → viole la contrôlabilité

### ISO 9241-210 — Conception centrée utilisateur (UCD)

Processus **itératif** en 4 activités à répéter jusqu'aux objectifs atteints :

```
1. Comprendre le contexte d'utilisation
   → Méthodes : interviews, observations terrain, shadowing
   → Livrables : personas, carte d'empathie

2. Définir les besoins utilisateurs
   → Format : "L'utilisateur doit pouvoir… afin de…"
   → Livrables : user stories, job-to-be-done, critères d'acceptation

3. Produire des solutions de conception
   → Méthodes : sketching, wireframing, prototypage lo-fi → hi-fi
   → Livrables : wireframes annotés, prototypes interactifs, specs

4. Évaluer par rapport aux besoins
   → Méthodes : tests utilisateurs, évaluation heuristique, A/B test
   → Livrables : rapport de tests, liste de problèmes priorisés
```

**Impératifs fondamentaux :**
- Pas de conception sans contact avec de vrais utilisateurs
- Une seule passe ne suffit pas — tester et corriger
- Équipe pluridisciplinaire (UX, dev, métier, QA)
- Concevoir pour des tâches réelles, pas des cas idéaux

---

## ♿ Accessibilité

### Hiérarchie des normes

```
WCAG 2.2 (W3C)          → Standard mondial, niveaux A / AA / AAA
    ↓ reprise par
EN 301 549              → Norme européenne (obligatoire secteur public EU)
    ↓ déclinaison française
RGAA 4.2                → Avec critères de tests détaillés
```

> [!important] Obligation légale en France
> Le RGAA est **obligatoire** pour les services publics et les entreprises avec un CA > 250M€. Niveau cible minimum : **WCAG 2.2 AA**.

### Les 4 principes WCAG (POUR)

| Principe | Critères clés |
|---|---|
| **P**erceptible | Alternatives textuelles (1.1.1), Pas de couleur seule (1.4.1), Contraste 4.5:1 minimum (1.4.3) |
| **U**tilisable | Navigation clavier (2.1.1), Pas de piège clavier (2.1.2), Focus visible (2.4.7) |
| **C**ompréhensible | Labels clairs (1.3.1), Langue déclarée (3.1.1), Messages d'erreur descriptifs (3.3.1) |
| **R**obuste | HTML valide (4.1.1), Rôles ARIA corrects (4.1.2), Annonces live (4.1.3) |

### ARIA 1.2 — Points critiques

```html
<!-- Modale : obligatoire -->
<div role="dialog" aria-modal="true" aria-labelledby="titre-modal">

<!-- Bouton icône seul : obligatoire -->
<button aria-label="Ajouter un tag CRIM">+</button>

<!-- Mise à jour AJAX : obligatoire -->
<div aria-live="polite" class="sr-only" id="status-region"></div>

<!-- Barre de progression : ne pas utiliser la couleur seule -->
<div role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  75% — 9 publiés, 2 non publiés, 1 absent
</div>
```

> [!warning] Règle d'or accessibilité
> **Ne jamais utiliser la couleur comme seul vecteur d'information** (critère 1.4.1 niveau A). Toujours combiner couleur + texte + icône.

---

## 🔒 Sécurité

### OWASP Top 10 — Les plus fréquents en contexte Django/Web

| Rang | Vulnérabilité | Application concrète |
|---|---|---|
| **A01** | Contrôle d'accès défaillant | Matrice de permissions claire, gardes sur chaque vue |
| **A02** | Échecs cryptographiques | HTTPS/TLS obligatoire, pas de données sensibles en URL |
| **A03** | Injection | Valider `type_objet` contre une whitelist, ne pas faire confiance au client JS |
| **A05** | Mauvaise configuration | CSP headers, CSRF protégé sur tous les POST/DELETE |
| **A07** | Auth & sessions | Tokens CSRF transmis via header `X-CSRFToken`, pas en URL |

### Checklist sécurité Django

- [ ] CSRF token transmis sur tous les appels AJAX (`X-CSRFToken` header)
- [ ] `type_objet` validé contre une liste blanche (`choices=` ou validation vue)
- [ ] Convertisseur `<path:>` dans les URLs : valider strictement le contenu
- [ ] Permissions vérifiées côté serveur (jamais uniquement côté client)
- [ ] `on_delete` CASCADE documenté avec avertissement utilisateur

---

## ⚡ Performance Web

### Core Web Vitals (Google)

| Métrique | Cible | Description |
|---|---|---|
| **LCP** (Largest Contentful Paint) | < 2.5s | Chargement du contenu principal |
| **INP** (Interaction to Next Paint) | < 200ms | Réactivité aux interactions |
| **CLS** (Cumulative Layout Shift) | < 0.1 | Stabilité visuelle du layout |

> [!tip] Impact SEO
> Les Core Web Vitals sont un critère de classement Google depuis 2021. Une interface lente = moins de visibilité.

### Bonnes pratiques performance

- 1 requête DB par vue pour les données calculées (ne pas faire N+1)
- Cache avec stratégie d'invalidation explicite (pas de cache sans expiry ou trigger)
- Pagination sur les longues listes
- Afficher la fraîcheur des données calculées ("Données au JJ/MM à HH:MM")
- Éviter les appels réseau bloquants côté client avant le premier rendu

---

## 🌐 Standards techniques Web

### HTML & sémantique

- Utiliser les éléments sémantiques : `<main>`, `<nav>`, `<article>`, `<section>`, `<aside>`
- Un seul `<h1>` par page, hiérarchie de titres respectée (pas de saut H1 → H3)
- Formulaires : `<label for="">` associé à chaque `<input>` sans exception
- Valider le HTML produit (W3C Markup Validator)

### CSS & design tokens

- Variables CSS pour couleurs, typographie, espacements — séparées de la logique métier
- Approche mobile-first pour le responsive
- Ne jamais encoder des valeurs en dur dans les composants (utiliser des tokens)

### HTTP & APIs

- HTTPS obligatoire, TLS 1.3 recommandé
- OpenAPI 3.x pour documenter les APIs consommées / exposées
- HTTP/2 minimum pour les assets statiques

---

## 🧪 Tests — Normes et structure

### ISO 29119 — Les 5 parties

| Partie | Sujet |
|---|---|
| **29119-1** | Concepts et vocabulaire |
| **29119-2** | Processus de test |
| **29119-3** | Documentation (plans, cas, rapports) |
| **29119-4** | Techniques de test |
| **29119-5** | Keyword-Driven Testing |

### La pyramide des tests

```
           ╔════════════╗
           ║   E2E/UI   ║  Peu, lents → parcours critiques
         ╔══════════════════╗
         ║   Intégration    ║  Moyens → interactions composants
       ╔══════════════════════════╗
       ║       Unitaires          ║  Beaucoup, rapides → logique isolée
       ╚══════════════════════════╝
```

### Structure d'un cas de test (ISO 29119-3)

```
ID          : TC-XXX-001
Titre       : [Description courte]
Précondition: [État initial requis]
Données     : [Jeux de données utilisés]
Étapes      : [Numérotées, une action par étape]
Résultat attendu : [Observable, mesurable]
Résultat obtenu  : [À remplir à l'exécution]
Statut      : PASS / FAIL / BLOCKED
```

### Pattern AAA (tests unitaires)

```python
def test_nom_explicite():
    # ARRANGE — préparer les données
    ...
    # ACT — appeler le code testé
    result = fonction_testee(...)
    # ASSERT — vérifier le résultat
    assert result == valeur_attendue
```

### Règle FIRST (ISTQB)

| Lettre | Règle |
|---|---|
| **F**ast | Millisecondes par test |
| **I**solated | Pas de dépendance externe (mock DB, réseau) |
| **R**epeatable | Même résultat à chaque exécution |
| **S**elf-validating | PASS ou FAIL, pas d'inspection manuelle |
| **T**imely | Écrit au moment du code, pas après |

### Format Gherkin (BDD)

```gherkin
Scenario: [Description du cas nominal]
  Given [état initial]
  And [contexte complémentaire]
  When [action de l'utilisateur]
  Then [résultat attendu]
  And [résultat complémentaire]
```

### Métriques de couverture

| Métrique | Seuil recommandé | Seuil critique |
|---|---|---|
| Line coverage | > 70% | > 90% sur code critique |
| Branch coverage | > 60% | > 80% sur logique métier |
| Function coverage | > 80% | 100% sur services publics |

> [!warning] Couverture ≠ qualité
> 100% de couverture avec des tests sans assertions ne détecte rien. La couverture mesure l'exécution, pas la pertinence des vérifications.

---

## 🔬 Postman — Bonnes pratiques API

### Structure de collection recommandée

```
Nom du projet
├── 📁 APIs Externes (IFS, tiers)
│   ├── Authentification (token auto-refresh)
│   └── [Un dossier par domaine fonctionnel]
└── 📁 APIs Internes (Django CONTROL)
    ├── CRUD [Entité]
    ├── Endpoints AJAX
    └── Webhooks / Callbacks
```

### Environments — variables essentielles

```
base_url          → URL de l'app Django selon l'env
api_base_url      → URL de l'API externe (IFS, etc.)
api_token         → Token auto-rempli par pre-request script
api_token_expiry  → Timestamp d'expiry pour éviter les re-auth inutiles
csrf_token        → Token CSRF Django (auto-rempli)
env_src / env_tgt → Environnements source/cible pour migrations
```

### Pre-request script — token auto-refresh

```javascript
const token = pm.environment.get('api_token');
const expiry = pm.environment.get('api_token_expiry');
if (!token || Date.now() > parseInt(expiry)) {
    pm.sendRequest({ /* appel auth */ }, (err, res) => {
        const body = res.json();
        pm.environment.set('api_token', body.access_token);
        pm.environment.set('api_token_expiry', Date.now() + body.expires_in * 1000);
    });
}
```

### Tests Postman à systématiser

```javascript
pm.test("Statut attendu", () => pm.response.to.have.status(200));
pm.test("Temps de réponse < 2s", () => pm.expect(pm.response.responseTime).to.be.below(2000));
pm.test("Structure de réponse valide", () => {
    const body = pm.response.json();
    pm.expect(body).to.have.property('id');
});
// Chaînage : stocker un ID pour la requête suivante
pm.environment.set('created_id', pm.response.json().id);
```

### Newman (CLI) — intégration CI/CD

```bash
newman run collection.json \
  --environment ENV_TRN.json \
  --reporters cli,junit \
  --reporter-junit-export results.xml
```

---

## 🛡️ Protection des données (RGPD)

- **Privacy by Design** : intégrer la protection dès la conception, pas en correctif
- Champ `created_by` avec `on_delete=SET_NULL` → préférer anonymisation ("Utilisateur supprimé") à NULL brut pour conserver la traçabilité
- Données personnelles non encodées en dur dans les logs ou les URLs
- Recommandations CNIL pour les cookies et le consentement
- Durée de conservation documentée (DUA) sur les données collectées

---

## 📋 Checklist "Definition of Done" — Interface web

### Par fonctionnalité

- [ ] Cas nominaux testés (unitaire + intégration)
- [ ] Cas limites et états vides documentés et testés
- [ ] États de l'interface spécifiés : vide, chargement, erreur, succès, désactivé
- [ ] Confirmations avant toute action irréversible
- [ ] Labels ARIA sur tous les éléments interactifs sans texte visible
- [ ] Focus management documenté pour les modales et overlays
- [ ] Pas de couleur seule pour véhiculer une information
- [ ] Données fraîches : indicateur de date si données calculées en batch
- [ ] Permissions vérifiées côté serveur pour chaque endpoint
- [ ] CSRF protégé sur tous les POST/DELETE

### Par mise en production

- [ ] HTTPS activé
- [ ] CSP headers configurés
- [ ] Couverture de tests > 80% sur le code nouveau
- [ ] Tests de régression sur les fonctionnalités existantes
- [ ] Core Web Vitals dans les seuils (LCP < 2.5s, INP < 200ms, CLS < 0.1)
- [ ] HTML validé (W3C Validator)
- [ ] RGAA / WCAG 2.2 AA : aucune erreur de niveau A

---

## 📚 Références

| Ressource | URL |
|---|---|
| WCAG 2.2 | https://www.w3.org/TR/WCAG22/ |
| RGAA 4.2 | https://accessibilite.numerique.gouv.fr |
| OWASP Top 10 | https://owasp.org/Top10/ |
| OWASP ASVS | https://owasp.org/www-project-application-security-verification-standard/ |
| Core Web Vitals | https://web.dev/vitals/ |
| ISO 9241-110 | Norme ISO (accès payant) |
| ISO 29119 | Norme ISO (accès payant) |
| ISTQB Glossary | https://glossary.istqb.org |
