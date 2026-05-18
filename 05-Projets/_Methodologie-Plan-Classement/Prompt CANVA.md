### Contexte

Tu vas créer une vidéo de formation interne à destination de **développeurs juniors** de notre équipe Globasoft. Le but : leur expliquer notre **méthodologie d'évaluation des plans de classement** pour qu'ils puissent l'appliquer sur nos projets IT.

Je t'ai fourni l'ensemble des fichiers Markdown qui composent la méthodologie (notes `00-Index.md`, `01-Logique-structurante.md` à `09-Livrabilite-cloture-projet.md`, `10-Normes-references.md`, `11-Glossaire.md`, `Template-Audit-Projet.md`). Tu utiliseras ces fichiers comme **source unique de vérité** pour le contenu.

### Public cible et ton

- **Audience** : développeurs juniors (1-3 ans d'expérience), techniques mais pas spécialistes en gouvernance documentaire.
- **Posture** : pédagogique, bienveillante, concrète. Pas de jargon archivistique gratuit — chaque terme métier (DUA, MECE, MoReq...) doit être défini à sa première occurrence, en s'appuyant sur le `11-Glossaire.md`.
- **Ton** : direct, professionnel mais accessible. Ni corporate creux, ni trop familier. Phrases courtes. Exemples concrets systématiques.
- **Langue** : français.
- **Posture pédagogique** : montrer **pourquoi** chaque angle compte avant de montrer **comment** l'évaluer. Toujours partir d'un problème réel que le développeur a déjà vécu (impossible de retrouver une spec, doublons dans les dossiers, livraison ratée…).

### Format technique

- **Durée cible** : 12-15 minutes (suffisant pour les 9 angles + intro/conclusion sans bâclage).
- **Format** : 16:9, 1080p.
- **Avec narration vocale** : voix off française, claire et posée. Pas d'avatar humain à l'écran — la vidéo est centrée sur les schémas et le contenu.
- **Sous-titres** : oui, intégrés en français.
- **Identité visuelle** : sobre, professionnelle, type "documentation technique". Couleurs neutres avec accents pour mettre en valeur les éléments clés (un bleu et un orange suffisent). Police sans-serif lisible.

### Structure de la vidéo (à respecter)

#### Séquence 1 — Intro (~1 min)

- Accroche par un problème réel : "Tu cherches une spec sur un projet vieux de 2 ans. Tu la trouves dans trois dossiers différents, à trois versions différentes. Laquelle est la bonne ?"
- Annonce du sujet : nous avons formalisé une méthodologie en 9 angles pour challenger un plan de classement IT.
- Pourquoi ça concerne le développeur : il produit de la doc, classe des fichiers, doit savoir livrer.
- Plan de la vidéo.

#### Séquence 2 — Le problème de fond (~1 min)

- Un plan de classement, c'est quoi ? (s'appuyer sur la définition du `11-Glossaire.md`)
- Pourquoi sur un projet IT ce n'est pas trivial : multi-phases, multi-acteurs, doc + code, livrables, archives, RGPD…
- Annoncer les 4 grandes questions auxquelles la méthodo répond : pertinence, position, durabilité, conformité (cf. `00-Index.md` §Objectif).

#### Séquence 3 — Tour des 9 angles (~8-9 min, soit ~1 min par angle)

Pour chaque angle (de 1 à 9), respecter strictement cette structure :

1. **Question clé** (telle qu'elle apparaît dans le tableau de `00-Index.md`).
2. **Le principe en une phrase** (extrait de chaque note `0X-*.md`, section "Principe").
3. **Un signal d'alerte visuel** (un des "Signaux d'alerte 🚩" listés dans chaque note, choisi pour son côté parlant pour un dev).
4. **Un exemple concret** : à chaque fois que possible, utiliser un cas réel du **DWH Aerotec** (audit dans `99-annexes/Audit-Plan-Classement-2026-05.md` du vault `dwh`) pour ancrer dans le concret. Par exemple :
    - Angle 1 : double alignement processus médaillon × domaines métier (IMP, FAC…)
    - Angle 2 : la branche `recaps-minibriefs` partie en suffixes bis/ter/quater
    - Angle 9 : le besoin de créer des sous-dossiers `_livrable/`
5. **Visuel** : un schéma minimaliste qui matérialise l'angle (arborescence, tableau, flèche…).

#### Séquence 4 — La grille de scoring (~1 min)

- Présenter la grille 0-3 par angle, total /27 (cf. `00-Index.md` §Grille de notation).
- Montrer l'interprétation : 23-27 exemplaire, 17-22 solide avec axes…, etc. (cf. `Template-Audit-Projet.md`).
- Mentionner le cas DWH Aerotec scoré à 18/27 — pour montrer qu'un projet sérieusement gouverné n'obtient pas le maximum.

#### Séquence 5 — Comment l'utiliser au quotidien (~1 min)

- Les 4 moments d'usage (revue initiale / en cours / clôture / audit interne) — cf. `00-Index.md` §Usage.
- Le template d'audit (`Template-Audit-Projet.md`) à dupliquer dans chaque projet.
- L'index livrable (sortie de l'angle 9) à maintenir vivant.

#### Séquence 6 — Conclusion (~30 sec)

- Récap : 9 angles, une grille, un template, un index.
- Message clé : un plan de classement n'est jamais "fini", il vit avec le projet.
- Appel à l'action : "Sur ton prochain projet, ouvre le template, fais le test à 10 docs, score les 9 angles. Tu verras tout de suite où ça coince."

### Règles importantes

- **Ne pas inventer** : tout le contenu doit venir des fichiers fournis. Si une information n'y est pas, ne pas extrapoler.
- **Privilégier les visuels au texte** : à chaque angle, un schéma vaut mieux qu'une liste à puces lue. Pour les arborescences, utiliser une vraie représentation graphique d'arbre (pas du texte avec des indents).
- **Cohérence visuelle entre les 9 angles** : même mise en page, mêmes codes couleur, pour faciliter la mémorisation.
- **Pas de musique envahissante** : musique de fond très discrète ou pas de musique du tout.
- **Pas d'emojis dans les visuels** sauf les drapeaux d'alerte 🚩 qui sont des marqueurs sémantiques dans la méthodo.
- **Citations exactes** : quand tu cites un nom de note, un code domaine ou un acronyme, respecter la casse et l'orthographe exacts (ex. `_livrable/`, RG-FAC-007, MEP 2).
- **Acronymes** : à chaque première occurrence, donner la signification complète (DUA = Durée d'Utilité Administrative, MECE = Mutually Exclusive Collectively Exhaustive…).

### Livrables attendus

1. La **vidéo finale** au format 16:9 1080p, prête à diffuser en interne.
2. Le **script complet** de la voix off, en document séparé, pour relecture avant production.
3. Le **storyboard** de chaque séquence (vignettes des visuels clés) pour validation.

### Boucle de validation

Avant de générer la vidéo finale :

1. Produis d'abord le **script complet**.
2. Puis le **storyboard**.
3. Attends ma validation des deux avant de lancer le rendu vidéo final.