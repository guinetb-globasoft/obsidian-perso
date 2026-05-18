---
tags: ["methodologie", "plan-classement", "metadonnees", "iso-23081"]
created: 2026-05-17
---

# 6. Métadonnées

> Que sait-on de chaque document, au-delà de son emplacement dans le plan ?

## Principe

Le plan de classement définit **où** se trouve un document. Les métadonnées définissent **ce qu'il est** : auteur, date, statut, version, projet, mots-clés, etc.

**ISO 23081** est la norme de référence : elle décrit ce qu'on doit savoir d'un document pour qu'il reste **authentique, fiable, intègre et exploitable** dans le temps.

Un plan sans métadonnées = un système qui ne tient pas dans la durée.

## Pourquoi c'est critique sur un projet IT ?

- Permet la **recherche multi-axes** (pas juste navigation hiérarchique)
- Permet la **traçabilité** (qui a modifié quoi, quand, pourquoi)
- Permet l'**audit** et la valeur probante
- Permet la **migration** entre systèmes
- Survit aux changements d'outil (les métadonnées peuvent être exportées)

## Catégories de métadonnées (ISO 23081)

### 1. Identification
- Identifiant unique (UUID, référence)
- Titre
- Auteur(s) / créateur(s)
- Date de création
- Format / type MIME

### 2. Contexte
- Projet / activité de rattachement
- Processus métier
- Émetteur / destinataire (si échange)
- Référentiel(s) lié(s)

### 3. Contenu
- Mots-clés / tags
- Résumé / abstract
- Langue
- Confidentialité / classification

### 4. Structure
- Version / révision
- Document parent / enfants
- Pièces jointes / annexes
- Liens vers autres documents

### 5. Cycle de vie
- Statut (brouillon, validé, obsolète, archivé)
- Date de validation
- Date d'expiration / sort final
- Historique des modifications

### 6. Droits et accès
- Propriétaire
- Niveau de confidentialité
- Restrictions d'accès
- Mentions légales (RGPD, secret pro...)

## Questions à poser

- [ ] Existe-t-il un **schéma de métadonnées** documenté pour le projet ?
- [ ] Quelles métadonnées sont **obligatoires** vs facultatives ?
- [ ] Comment sont-elles **saisies** (manuelles, automatiques, héritées) ?
- [ ] Comment sont-elles **stockées** (dans le fichier, base externe, GED) ?
- [ ] Sont-elles **interrogeables** (recherche par auteur, par date, etc.) ?
- [ ] Survivent-elles à un **export / migration** ?
- [ ] Y a-t-il un **vocabulaire contrôlé** (liste de tags autorisés) ?

## Signaux d'alerte 🚩

- Aucune métadonnée formalisée (juste le nom de fichier)
- Métadonnées noyées dans le nom de fichier (`Spec_V3_DUPONT_2024-03-15_VALIDÉ.docx`)
- Tags / mots-clés en saisie libre (anarchie)
- Auteur identifié uniquement par le compte Windows utilisé à l'enregistrement
- Pas de versioning explicite (qui sait quelle est la dernière version ?)
- Métadonnées présentes mais non exploitées en recherche

## Niveaux de maturité

### Niveau 0 — Aucune métadonnée
Juste le système de fichiers. Tout est dans le nom du fichier ou rien.

### Niveau 1 — Convention de nommage
Une convention écrite : `[Projet]_[Type]_[Date]_[Auteur]_[Version].ext`
✅ Mieux que rien, mais fragile (cassures, erreurs de saisie)

### Niveau 2 — Métadonnées dans le fichier
Propriétés Office, EXIF, en-têtes de fichiers
✅ Survit à un renommage
❌ Perdu si export en autre format

### Niveau 3 — GED / SharePoint avec colonnes
Métadonnées stockées en base, indexées, requêtables
✅ Recherche multi-critères performante
✅ Vocabulaire contrôlé possible

### Niveau 4 — Schéma normalisé ISO 23081
Schéma documenté, vocabulaires contrôlés, intégration aux processus métier
✅ Niveau attendu pour des dispositifs à valeur probante

## Vocabulaires contrôlés à mettre en place

Au minimum :
- **Statut** : Brouillon | En revue | Validé | Publié | Obsolète | Archivé
- **Type** : Spécification | CR réunion | Contrat | Livrable | Code source | ...
- **Confidentialité** : Public | Interne | Confidentiel | Secret
- **Projet** : liste fermée des projets en cours

## Cas concrets à challenger

**Document trouvé : `CR-Reunion-15-03.docx`**
- Quelle réunion ? Quels participants ? Quel projet ? Validé par qui ?
- Sans métadonnées, c'est un document mort.

**Migration de SharePoint vers une autre GED**
- Les colonnes / métadonnées sont-elles exportables ?
- Le schéma est-il documenté pour reconstitution ?

## Lien avec les autres angles

- Les métadonnées peuvent compenser certaines ambiguïtés du [[03-Exhaustivite-exclusivite|MECE]]
- Elles soutiennent la [[05-Stabilite-evolutivite|durabilité]] (résistance aux migrations)
- Elles permettent de mesurer l'[[07-Adequation-usages|usage]] (dernier accès, fréquence)
- Elles sont indispensables au [[04-Calendrier-conservation-DUA|calcul des DUA]]

## Référence

- ISO 23081-1:2017 (Principes)
- ISO 23081-2:2021 (Aspects conceptuels et de mise en œuvre)
- ISO 23081-3:2011 (Méthode d'auto-évaluation)
- Dublin Core (jeu minimal de métadonnées)
- SEDA (Standard d'Échange de Données pour l'Archivage, secteur public FR)
