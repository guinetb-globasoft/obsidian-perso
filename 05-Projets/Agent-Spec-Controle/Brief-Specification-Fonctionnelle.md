---
tags: ["brief", "specification", "controle", "template"]
created: 2026-04-16
---

# Brief — Spécification fonctionnelle projet Contrôle

> **Usage** : copier ce document en début de conversation avec un LLM (ou dans un prompt système) avant de lui demander une spécification fonctionnelle ou technique. Il contient tout le contexte projet nécessaire pour que la réponse soit pertinente du premier coup.

---

## 🎯 Projet : ERP CONTROL

**ERP CONTROL** est une application web à destination de clients de Globasoft ESN qui se connecte à l'ERP **IFS** pour auditer, gérer et fiabiliser les données et les droits utilisateurs.

### Ce que fait Contrôle aujourd'hui

- **Audit des droits IFS** : visualiser et modifier les permissions des utilisateurs, groupes de personnes, rôles métiers (achat, finance, travaux, prod usine, chargés d'affaires, trésorerie, etc.)
- **Imports / exports de données IFS** : extraction massive de tables IFS (ex : règles de circuit d'autorisation, 1500+ lignes), avec détection de problèmes
- **Indicateurs de qualité** : factures manuelles sans pièce jointe, suivi factures finance, comparaison d'environnements, etc.
- **Comparaison multi-environnements** : DEV / TRN / PROD, avec détection des écarts de paramétrage
- **Gestion des workflows** : droits spécifiques par processus métier (évaluation certification, validation facture STT, caution RG, capitalisation projet, trésorerie conso…)

### Périmètre utilisateurs

- Utilisateurs internes Globasoft : RSSI, DSI, équipe data, fonctionnels métier (Elodie, Lucien, Sahar, Jessica…)
- Utilisation quotidienne pour des opérations de contrôle et de remédiation
- App hébergée sur Render, accessible via `ga.erp-control.com`

---

## 🏗️ Stack technique

| Couche               | Technologies                                                                    |
| -------------------- | ------------------------------------------------------------------------------- |
| Backend              | **Python 3.11+**, **Django**                                                    |
| Frontend             | Templates **Django HTML**, **JavaScript vanilla / jQuery**, **CSS** custom      |
| Tâches asynchrones   | **Celery + Redis** (Flower pour le monitoring)                                  |
| Base de données      | PostgreSQL (Render)                                                             |
| Hébergement          | **Render** (recette + prod)                                                     |
| ERP cible            | **IFS** via API **OData / projection** (`gafr-trn.ifs.cloud`, `gafr.ifs.cloud`) |
| Authentification IFS | Selon les endpoints (token / basic auth)                                        |

### Volumétrie du code

- ~743 fichiers, ~207 000 lignes
- 289 fichiers Python, 235 templates HTML
- 62 JSON, 34 MD, 20 CSS, 19 JS

### Conventions / patterns importants

- **Modules métier** : organisés par domaine (`securite/`, `qualite/`, `utilisateurs/`, `import/`, …)
- **URLs d'app locale** souvent référencées dans les descriptions de tâches, ex : `http://localhost:8000/securite/droits-specifiques/<processus>/?env_id=<N>`
- **Appels IFS** via endpoints OData, ex :
  - `GET https://gafr-trn.ifs.cloud/main/ifsapplications/projection/v1/PersonGroupHandling.svc/DocumentGroupSet`
  - `POST https://gafr-trn.ifs.cloud/main/ifsapplications/projection/v1/PersonGroupHandling.svc/DocumentGroupSet(GroupId='XXX')/DocumentGroupMembersArray`
- **Multi-environnement** : chaque appel IFS est paramétré par `env_id` (2 = TRN, 8 = PROD, etc.)
- **Tâches longues** : systématiquement en Celery avec résultat stocké en Redis (TTL 24h), fallback base de données si expiration

### Concepts IFS récurrents

- **Groupes de personnes** (Person Groups) : collections d'utilisateurs avec des rôles
- **Groupes de permissions** : achat, finance, travaux, prod usine, sva CDC, CAF, tréso, tiers…
- **Processus métier** : évaluation_certification, validation_facture_stt, caution_rg_stt, capitalisation_projet, demande_caution_rg, tresorerie_conso…
- **Tables de référence** : coordinateur, demandeur, acheteur, approbateur, class max
- **Lobbies** : interfaces IFS regroupées en ensembles de permissions
- **Quick Reports** : rapports paramétrables IFS, dont les droits sont sensibles

---

## 📋 Principes pour la spécification

### Ce que j'attends d'une bonne spec

1. **Part de l'existant** : avant de proposer du nouveau code, identifier ce qui peut être réutilisé dans ERP CONTROL. Si je parle d'un module ou d'une URL qui existe déjà, tu as sûrement un pattern proche à exploiter.
2. **Chemins précis** : plutôt que "un module quelque part", cite `securite/views/droits_specifiques.py` ou l'équivalent le plus proche.
3. **Appels IFS explicites** : quand c'est pertinent, donne l'endpoint OData exact et la structure du payload.
4. **Penser multi-env** : toute fonctionnalité doit marcher pour plusieurs `env_id` (pas de hardcoding TRN/PROD).
5. **Découpage en étapes actionnables** : un plan d'implémentation ordonné, chaque étape doit être testable indépendamment.
6. **Questions ouvertes explicites** : si tu manques d'info, liste-la clairement plutôt que de bluffer.

### Format attendu pour une spec technique

```
## 🎯 Contexte et objectif
Reformulation concise de la demande fonctionnelle.

## 🔍 Analyse de l'existant
- Code réutilisable identifié (chemins + fonctions/classes)
- Patterns à respecter

## 🏗️ Proposition technique
- Composants à modifier (chemin → nature de la modification)
- Composants à créer (chemin → rôle)
- Appels IFS nécessaires (endpoint + payload si POST/PATCH)
- Impacts UI / templates
- Impacts Celery si tâche asynchrone

## 📋 Plan d'implémentation
1. Étape 1 (testable)
2. Étape 2
3. ...

## ⚠️ Risques et points d'attention
- Performance (ex : N+1 appels IFS)
- Rétro-compat
- Gestion erreurs IFS (timeout, lenteur PROD en journée)

## ❓ Questions ouvertes
- Points à clarifier avant dev
```

### Règles de qualité non négociables

- **Ne jamais bluffer** : si tu ne connais pas un détail, demande-le
- **Ne pas proposer de code complet** : des pointeurs, des descriptions, pas d'implémentation exhaustive (le code viendra après)
- **Rester concret** : pas de généralités du type "il faudra gérer la sécurité", mais "appliquer le même check que dans `vue_X` : appartenance au groupe Y via table Z"
- **Anticiper les problèmes de perf** quand IFS est impliqué : si la spec implique plus de 50 appels IFS, proposer du batching / parallélisme / pagination

---

## 🔄 Workflow de travail

1. Je rédige une **description fonctionnelle** dans l'onglet Description d'une tâche Odoo (projet ERP_Control_, ID 4)
2. Je donne cette description à un LLM avec ce brief en contexte
3. Le LLM produit une **spécification technique** structurée selon le format ci-dessus dans l'onget Spécifications techniques de la tâche
4. Je relis, ajuste, puis la spec sert de base au développement (humain ou Claude Code)

---

## 📚 Ressources pour aller plus loin

- [[01-Architecture]] — architecture de l'automatisation des agents (contexte projet plus large)
- [[02-Workflow-Odoo]] — stages et transitions dans le kanban
- Projet Odoo : https://globasoft1.odoo.com/odoo/project/4/tasks

---

#brief #specification #controle #template
