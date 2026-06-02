---
tags: ["elevo", "nibelis", "sftp", "architecture", "GA", "ops", "securite"]
created: 2026-05-29
---

---
projet: GA - API Nibelis
type: architecture
cible: Intégration SFTP Elevo
created: 2026-05-29
sources_elevo: ["Synchroniser les utilisateurs via SFTP – Elevo.pdf", "elevo-sftp-production.asc"]
---

# Architecture intégration SFTP Elevo

> Architecture cible et prérequis opérationnels pour la synchronisation **API Nibelis → SFTP Elevo**. Synthétise les contraintes officielles Elevo (PDF SFTP, clé GPG production fournie le 29/05/2026).

## 🔀 Périmètre — Mode SFTP (Mode B)

Cette note couvre **uniquement le Mode B (SFTP)**. Pour le Mode A (mail ponctuel à `support@elevo.io`), pas d'archi à mettre en place :
- Pas de clé SSH ni d'IP à whitelister
- Pas de SFTP, pas de scheduler
- Génération du fichier CSV ou Excel selon le mapping de [[02-Mapping-Elevo-Nibelis]] (section "Mode A") ou [[03-Mapping-Elevo-Parcours-Professionnel]]
- Envoi en pièce jointe (GPG optionnel) à `support@elevo.io`
- Traitement humain côté Elevo

→ Le Mode A est idéal pour le POC, le rebuild initial, ou des corrections ponctuelles. Le Mode B (cette note) est la cible production.

## Vue d'ensemble

```
┌─────────────┐                  ┌──────────────────┐                  ┌─────────────┐
│  API        │  REST/HTTPS      │  Connecteur GA   │  SFTP + SSH      │  Elevo SFTP │
│  Nibelis    │ ───────────────► │  (script ou      │ ───────────────► │  Gateway    │
│  (RH)       │                  │   service)       │  (GPG optionnel) │             │
└─────────────┘                  └──────────────────┘                  └─────────────┘
                                          │
                                          │ State local (snapshot précédent)
                                          ▼
                                  ┌──────────────────┐
                                  │  Storage (S3 /   │
                                  │  fichier / DB)   │
                                  └──────────────────┘
```

## Deux flux indépendants à pipelining séquentiel

| Ordre | Flux | Dossier SFTP | Mapping |
|---|---|---|---|
| **1** | Users (master) | `/uploads/users/` | [[02-Mapping-Elevo-Nibelis]] |
| **2** | Parcours pro (slave) | `/uploads/professional_background/` | [[03-Mapping-Elevo-Parcours-Professionnel]] |

⚠️ **Ordre obligatoire** : un user doit exister dans Elevo avant l'import de son parcours (sinon erreur "User does not exist", ligne ignorée).

## Authentification SFTP

### Côté Elevo (à demander à support@elevo.io)

À transmettre à Elevo lors de l'ouverture :
- ✅ Contact technique (nom + email)
- ✅ Solution source : "**API Nibelis (GA)**"
- ✅ **IP ou plage d'IPs** du runner/serveur d'exécution (whitelist réseau Elevo)
- ✅ **Clé publique SSH** (à générer côté GA — recommandation `ed25519`)

Elevo renvoie en retour :
- Identifiant SFTP
- Hostname + port du serveur SFTP
- Clé GPG publique pour chiffrement (déjà disponible : `elevo-sftp-production.asc`)
- Confirmation de readiness

### Côté GA — clé SSH

Génération recommandée :

```bash
ssh-keygen -t ed25519 -C "ga-elevo-sftp-prod@ga.fr" -f ~/.ssh/elevo_sftp_ed25519
# Garder la clé privée en secret manager (Vault, AWS Secrets, etc.)
# Transmettre uniquement la clé publique (.pub) à Elevo
```

### Algorithmes SSH autorisés par Elevo

| Catégorie | Valeurs supportées |
|---|---|
| KexAlgorithms | `diffie-hellman-group-exchange-sha256`, `curve25519-sha256@libssh.org`, `diffie-hellman-group16-sha512`, `diffie-hellman-group18-sha512` |
| Ciphers | Mêmes valeurs (typo apparente dans la doc — à confirmer auprès du support) |
| MACs | `hmac-sha2-256-etm@openssh.com`, `hmac-sha2-512-etm@openssh.com`, `umac-128-etm@openssh.com` |
| HostKeyAlgorithms | `ssh-ed25519` (+ cert), `sk-ssh-ed25519`, `rsa-sha2-256`, `rsa-sha2-512` (+ cert) |

→ **Recommandation** : utiliser `ed25519` côté client (compact, rapide, moderne, compatible).

## Chiffrement GPG (optionnel mais recommandé)

Elevo fournit `elevo-sftp-production.asc` — clé publique GPG pour chiffrer les fichiers **avant** dépôt SFTP. Double-couche de sécurité (SSH + GPG).

### Identité de la clé

- **Owner** : `Elevo SAS (Elevo Encryption Key Production)`
- **Email** : `dev+gpg-production@elevo.fr`
- **Algo** : RSA 4096
- **Création** : 2021-03-29

### Workflow

```bash
# Import unique de la clé Elevo dans le keyring GPG
gpg --import elevo-sftp-production.asc

# Chiffrement avant dépôt SFTP
gpg --encrypt --recipient "dev+gpg-production@elevo.fr" \
    --output users-2026-05-29.csv.gpg \
    users-2026-05-29.csv

# Dépôt sur SFTP
sftp -i ~/.ssh/elevo_sftp_ed25519 user@sftp.elevo.fr <<< "put users-2026-05-29.csv.gpg /uploads/users/"
```

### Décision à prendre

- ✅ **Activer GPG en prod** : recommandé (les fichiers contiennent données RH/PII)
- 🟡 Pour le POC initial : skip GPG pour simplifier, ajouter ensuite

## Format de fichier (rappel)

| Contrainte | Valeur |
|---|---|
| Format | CSV RFC 4180 |
| Encodage | UTF-8 |
| Séparateur | virgule (`,`) |
| Fin de ligne | LF ou CRLF (pas de virgule terminale) |
| Header | obligatoire en 1ère ligne |
| Ordre colonnes | libre |
| Colonnes inconnues | ignorées silencieusement |
| Nom de fichier | **sans incidence** sur le traitement (toutes les fichiers du dossier sont consommés) |

→ Bonne pratique : nommer `users-{YYYYMMDD-HHMMSS}.csv` pour le tracking côté GA, mais Elevo ne s'y fie pas.

## Comportement de la synchro Elevo (rappel)

### Pour les users

| État | Action Elevo |
|---|---|
| User dans CSV + Elevo | 🔄 Mise à jour |
| User dans CSV mais pas Elevo | ➕ Création |
| User dans Elevo mais pas CSV | ❎ **Suspension** auto |
| `skip=true` sur une ligne | 🚫 Ligne ignorée, état Elevo inchangé pour ce user |
| `uniq_identifier` dupliqué dans le CSV | ❌ **Synchro totale annulée**, rapport d'erreur |
| Ligne invalide (date, manager inexistant...) | ⚠️ Ligne sautée, autres continues. User marqué "erreur sync" |

### Pour le parcours

| État | Action Elevo |
|---|---|
| login + start_date inconnus | ➕ Nouveau poste |
| login + start_date existants | 🔄 MAJ du poste |
| Poste Elevo absent du CSV | ⚠️ **Pas de suppression auto** (historique préservé) |
| 2 lignes avec même start_date pour même login | ❌ Ligne(s) ignorée(s) |

→ **Implication architecturale** : on envoie l'**état actuel complet** des users à chaque sync. Elevo gère le delta (création / MAJ / suspension). Pas besoin de stocker un état précédent côté GA.

→ Pour le parcours, par contre, il faut **persister l'état envoyé** pour détecter les ruptures de poste (sinon on n'a aucun moyen de générer un nouvel enregistrement parcours quand un salarié change de poste — l'API Nibelis ne donne que l'état courant).

## Périodicité de synchro recommandée

| Fréquence | Effet | Coût API Nibelis |
|---|---|---|
| **Quotidienne** (recommandée) | Reflet quasi temps réel des embauches / départs / changements | (N salariés × 1 appel API 2) × 1 = ~N appels/jour |
| Hebdo | Tolérable pour un POC ou si activité RH faible | ~N/7 appels/jour |
| Temps réel | Inutile, Elevo n'a pas d'événements RH critiques | — |

→ Cadence recommandée : **1×/jour la nuit** (ex : 04:00 Europe/Paris). Confirmer SLA Elevo sur la fréquence de consommation des fichiers.

## Sécurité / RGPD

- 🔒 **Clé SSH privée** : secret manager (jamais en clair sur le runner)
- 🔒 **Fichiers locaux** : chiffrés au repos, purgés après dépôt SFTP réussi
- 🔒 **GPG** : recommandé en prod (double couche)
- 🔒 **Logs** : ne pas logger les emails, noms ou matricules en clair — masquer ou hasher
- 🔒 **IP whitelist côté Elevo** : restriction supplémentaire (IP fixe du runner nécessaire)
- 🔒 **Champs sensibles** (RQTH `travailleur_handicape`, `numero_securite_sociale`, `date_naissance`) : ne synchroniser via SFTP **qu'après validation DPO**

## Gestion des erreurs

| Source d'erreur | Comportement Elevo | Détection côté GA |
|---|---|---|
| Doublon `uniq_identifier` | Rapport mail, sync annulée totale | Validation locale avant envoi |
| Ligne invalide | Ligne ignorée, user marqué erreur | Rapport mail Elevo |
| Manager `uniq_identifier` pointant vers inexistant | Ligne ignorée | Validation locale (tri topologique ou ordre simple) |
| Email non valide | Ligne ignorée | Validation locale (regex) |
| Date format incorrect | Ligne ignorée | Formatage local en ISO 8601 |
| SFTP injoignable | Aucun traitement | Alerting interne (Slack, mail ops) |
| GPG key mismatch | Rejet silencieux | Test de déchiffrement local après chiffrement |

**Recommandation** : **validation locale exhaustive** avant dépôt, pour éviter les rapports d'erreur Elevo (peu lisibles, traités en J+1 typiquement).

## Stockage de l'état (pour parcours uniquement)

Pour détecter qu'un salarié a changé de poste (et donc créer une nouvelle ligne parcours), il faut comparer l'`emploi_libelle` actuel avec l'`emploi_libelle` envoyé la dernière fois.

Options :
- 📁 **Fichier JSON** local : simple, suffisant pour <10 K salariés
- 🗄️ **Base SQLite** : si plusieurs runners, ou besoin d'historique enrichi
- ☁️ **S3 / blob storage** : si infra cloud

Recommandation : démarrer **fichier JSON versionné** + bascule DB si volume / multi-runner.

## Checklist mise en production

- [ ] Demande SFTP envoyée à support@elevo.io avec : contact, IP, clé SSH publique
- [ ] Réception identifiant + hostname + port SFTP Elevo
- [ ] Test connexion SFTP en read-only (`/uploads/` accessible)
- [ ] Import clé GPG `elevo-sftp-production.asc` dans le keyring du runner
- [ ] Test chiffrement + déchiffrement local
- [ ] Script de génération CSV users (mapping cf [[02-Mapping-Elevo-Nibelis]])
- [ ] Validation locale des CSV (unicité, dates, regex email)
- [ ] Premier dépôt en mode "test" avec **1-2 utilisateurs** (sandbox Elevo si possible — à demander)
- [ ] Réception rapport Elevo + analyse erreurs
- [ ] Bascule sur dépôt complet
- [ ] Setup cron / scheduler quotidien
- [ ] Setup alerting (mail/Slack en cas d'échec SFTP, GPG, validation)
- [ ] Documentation runbook (rotation clé SSH, rotation GPG si Elevo change, etc.)

## Coûts et volumétrie (estimations à valider)

| Élément | Estimation |
|---|---|
| Sociétés GA dans le périmètre | À confirmer (5 ? 10 ?) |
| Salariés totaux | À confirmer (300 ? 1 000 ?) |
| Appels Nibelis / sync | ~Nb sociétés + Nb salariés |
| Taille CSV users (estim) | <1 Mo pour 1 000 salariés |
| Bande passante SFTP | Négligeable |
| Coût hébergement runner | Faible (cron sur VM existante ou serverless) |

## Questions ouvertes

- [ ] **Sandbox Elevo** : existe-t-il un environnement de test ?
- [ ] **SLA SFTP Elevo** : disponibilité, fréquence de consommation des fichiers, délai avant rapport
- [ ] **Format clé SSH** : préférence Elevo ? (ed25519 vs rsa-sha2-256)
- [ ] **Cas multi-fiches** (`multi_fiche=O` côté Nibelis) : un user multi-société = N lignes CSV ou 1 ligne ? → impact sur `uniq_identifier`

## Liens

- [[01-API-Nibelis-Reference]] — Référence API source
- [[02-Mapping-Elevo-Nibelis]] — Mapping users
- [[03-Mapping-Elevo-Parcours-Professionnel]] — Mapping parcours
