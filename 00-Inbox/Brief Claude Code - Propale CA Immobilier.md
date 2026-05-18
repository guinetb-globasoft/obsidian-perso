---
tags: ["commercial", "CA-Immobilier", "brief", "claude-code", "export-word"]
created: 2026-04-24
---

# Brief — Claude Code pour finalisation propale CA Immobilier

**Date :** 26/04/2026
**Objectif :** Corriger et finaliser le document Word V2 déjà produit, puis produire les livrables annexes (BPU Excel + Word).

---

## Contexte

Proposition commerciale **SoHoft x Crédit Agricole Immobilier** (migration Modern Data Stack vers Snowflake).

**Fichiers sources :**

| Fichier | Rôle |
|---|---|
| `C:/Users/Shadow/Downloads/Propale_Sohoft_CA_Immobilier_v2.docx` | **Document Word V2 — base de travail principale** |
| `C:/Users/Shadow/Documents/vault-prive/00-Inbox/Propale Sohoft - CA Immobilier - Engagement 1.md` | Source markdown de référence (vault Obsidian) |
| `C:/Users/Shadow/Downloads/SoHoft - Proposition CA Immobilier.docx` | Template design SoHoft (couleurs, polices, logo) |
| `C:/Users/Shadow/Documents/vault-prive/00-Inbox/BPU CA Immobilier - Version Markdown.md` | BPU complet en Markdown à convertir |

**Situation actuelle :** Claude Code a déjà produit la V2. Le document Word est globalement bien formaté (design SoHoft repris, texte converti). Il reste des **bugs de conversion à corriger directement dans le Word V2** avant de travailler sur les annexes.

---

## IMPORTANT — Règles de travail

- **Ne jamais modifier le fond du document** sans demander — seulement la forme et la structure
- **Jamais mentionner :** Globasoft, partenaire tiers, IA, intelligence artificielle
- **dbt Core uniquement** (jamais dbt Cloud)
- **Procéder livrable par livrable**, montrer le résultat avant de passer au suivant
- **Toujours sauvegarder** avant modification (`exports/backups/`)
- **Ne jamais corriger automatiquement** une anomalie de contenu — signaler et laisser l'utilisateur trancher

---

## Ce que j'attends de Claude Code

### Livrable 1 — Correction du Word V2 (priorité 0)

**Objectif :** corriger les bugs de conversion dans la V2, en travaillant directement sur le docx avec `python-docx`. Ne pas régénérer depuis le markdown — corriger le Word existant.

**Bugs identifiés à corriger :**

1. **Titre chapitre 5 fusionné** : dans le corps du document, le titre "5. Jalons et planning" est collé avec "6.1 Macro-planning global (3 périmètres)". Séparer en deux titres distincts : "5. Jalons et planning" (Heading 1) et "5.1 Macro-planning global (3 périmètres)" (Heading 2).

2. **Titre "34.7 Roadmap de migration globale"** : le "34" est un artefact de conversion. Corriger en "3.7 Roadmap de migration globale".

3. **"3.2 Notre approche méthodologique" manquant** : dans le sommaire on passe de 3.1.3 à 3.2.1 sans parent. Le titre "3.2 Notre approche méthodologique" existe dans le corps mais est peut-être mal stylé (pas en Heading 2). Vérifier et corriger le style.

4. **"Voir section 9 — Hypothèses structurantes.**4.2 Notre approche méthodologique**"** : en fin de section 3.1.3, le titre suivant s'est collé au paragraphe précédent. Séparer proprement.

5. **Tableaux vides** : vérifier les sections suivantes qui peuvent avoir leur tableau absent ou mal converti, et les réinsérer depuis le markdown source si besoin :
   - 4.4.2 Disponibilité des ressources pour le Périmètre 2
   - 4.4.3 Disponibilité des ressources pour le Périmètre 3
   - 5.1.1 Vue d'ensemble (tableau P1/P2/P3)
   - 5.1.2 Détail Périmètre 1 (tableau semaine par semaine)
   - 5.1.3 Détail Périmètre 2
   - 5.1.4 Détail Périmètre 3

6. **Références internes obsolètes** : rechercher dans le document les renvois vers "section 4.8", "§10.4", "§9.5" etc. qui correspondent à l'ancienne numérotation du markdown. Dans la V2, la numérotation a changé — vérifier et corriger les renvois.

7. **Table des matières** : après toutes les corrections, **régénérer la table des matières** (champ Word à mettre à jour — Field Update All).

**Méthode recommandée :**
- Utiliser `python-docx` pour inspecter et corriger les paragraphes et styles
- Pour les tableaux manquants : parser le markdown source, extraire les tableaux concernés, les insérer via `python-docx`
- Livrer la version corrigée : `Propale_Sohoft_CA_Immobilier_v3.docx`

**Reporting de fin de tâche :** indiquer le nombre de pages total du document corrigé et une ventilation approximative par chapitre.

---

### Livrable 2 — BPU Excel + Word (priorité 1)

**Objectif :** produire le BPU en Excel et en Word depuis le Markdown source.

**Fichier source :**
`C:/Users/Shadow/Documents/vault-prive/00-Inbox/BPU CA Immobilier - Version Markdown.md`

**Structure Markdown atypique — IMPORTANT :**
Chaque ligne du BPU est un **petit tableau 2 colonnes `Champ | Valeur`** précédé d'un titre `### Ligne N — Nom du poste` et suivi de blocs "Livrables" et "Commentaire" en prose. Ce n'est **pas** un grand tableau unique.

```markdown
### Ligne N — Nom du poste

| Champ | Valeur |
|---|---|
| Poste | Nom du poste |
| Feature / Lot | — |
| Points complexité | X |
| Charge | **N j** |
| Confiance | 1 à 3 |
| Prix | **N XXX €** |

**Livrables :** ...
**Commentaire :** ...
```

**Parsing requis :**
- Itérer sur les titres `### Ligne N —` pour identifier chaque poste
- Transposer chaque tableau vertical en ligne horizontale Excel
- Nettoyer les valeurs numériques (gras Markdown, "j", "€")
- Extraire Livrables et Commentaire séparément
- Utiliser une lib Markdown avec AST (`mistune` ou `markdown-it-py`), pas de regex brute
- Le sommaire synthétique en fin de BPU sert de source de vérification croisée

**Excel `BPU_Sohoft_CA_Immobilier.xlsx` — 3 feuilles :**
- **Feuille 1 — Sommaire** (en premier) : reprise du sommaire synthétique, totaux en bas
- **Feuille 2 — BPU détaillé** : 1 ligne par poste, colonnes `Poste | Feature/Lot | Complexité | Charge J/H | Confiance | TJM | Prix € HT | Commentaire`, sous-totaux par section en formules
- **Feuille 3 — Notes** : TJM, règle de chiffrage du pilotage, principe d'indissociabilité

**Contraintes Excel :**
- Formules pour les sous-totaux et total (pas de hardcoding)
- Cellules de saisie en jaune pâle, cellules calculées en gris
- Freeze panes sur l'en-tête
- Couleurs des en-têtes : reprendre la palette du template SoHoft (`SoHoft - Proposition CA Immobilier.docx`)
- Format `€ HT` avec séparateur de milliers
- Assertion de vérification en bas : total calculé = total du sommaire synthétique BPU. Alerter si écart.

**Word `BPU_Sohoft_CA_Immobilier.docx` :**
- Conversion du Markdown via Pandoc avec `--reference-doc` pointant sur le template SoHoft
- Page de garde : "Bordereau de Prix Unitaire — Proposition CA Immobilier / Annexe à la proposition technique et financière SoHoft du 22/04/2026"

**Vérifications de cohérence :**
- Sous-totaux par section = sous-totaux du BPU Markdown
- Total général BPU = forfait global de la propale §9.1 (V2)
- Si écart : alerter, ne pas livrer

**Livrer dans** `C:/Users/Shadow/Documents/vault-prive/00-Inbox/exports/` :
- `BPU_Sohoft_CA_Immobilier.xlsx`
- `BPU_Sohoft_CA_Immobilier.docx`

---

### Livrable 3 — Vérifications de cohérence sur le markdown source (priorité 1)

**Objectif :** passe de vérification sur le markdown avant toute future itération.

**Anomalies à détecter (signaler uniquement, ne pas corriger) :**
- "Engagement 1/2/3" ou "E1/E2/E3" résiduels (hors P1/P2/P3 qui sont OK)
- Prénoms "Ziyad", "Florian", "Ben Messaoud", "Chaigne"
- Mot "Globasoft"
- "partenaire d'intégration" ou "partenaire tiers"
- "IA", "intelligence artificielle", "AI"
- "atelier CISO" (basculé sur questions par mail — vérifier si l'occurrence est légitime)
- Références croisées internes (§4.8, §10.x) qui ne correspondent plus à la numérotation actuelle

**Cohérence chiffrée :**
- Parser les totaux propale §9.1, §9.2, §9.3, §9.4, §9.5 (V2) et vérifier la cohérence interne
- Croiser avec le BPU Markdown (mêmes totaux attendus)
- Vérifier que les TJM sont cohérents partout

**Livrer :** rapport texte `rapport_coherence.md` dans `exports/`

---

## Prioritisation

| # | Livrable | Priorité |
|---|---|---|
| 1 | Correction Word V2 → V3 | **P0** |
| 2 | BPU Excel + Word | **P1** |
| 3 | Vérifications de cohérence markdown | **P1** |

---

## Environnement technique

- **OS :** Windows 10/11
- **Python :** installé, `python-docx`, `openpyxl`, `mistune` ou `markdown-it-py` disponibles ou à installer
- **Pandoc :** installé
- **Accès réseau :** OK

---

## Questions à poser avant de démarrer

1. Pour les tableaux vides (Livrable 1, point 5) : tu préfères que je réinsère les tableaux depuis le markdown source, ou tu veux d'abord vérifier toi-même dans Word lesquels sont vraiment manquants ?
2. Pour la table des matières : tu veux qu'elle soit régénérée automatiquement, ou tu la gères à la main dans Word ?

Bonne session.

**Objectif :** produire un fichier `.docx` livrable au client, reprenant fidèlement le design, les couleurs, les polices et le logo de la propale SoHoft de référence.

**Fichier de référence SoHoft :**
`C:/Users/Shadow/Downloads/SoHoft - Proposition CA Immobilier.docx` (6,1 Mo — contient logo, couleurs, styles, polices, images)

C'est la propale type SoHoft pour CA Immobilier — elle contient tout le design que nous devons reprendre.

**Actions à faire :**

1. **Extraire les assets du docx SoHoft.** Un `.docx` est un fichier zip. Procéder ainsi :
   ```bash
   # Créer un dossier de travail
   mkdir -p C:/Users/Shadow/Documents/vault-prive/00-Inbox/exports/sohoft-template
   cd C:/Users/Shadow/Documents/vault-prive/00-Inbox/exports/sohoft-template

   # Copier et extraire le docx
   cp "C:/Users/Shadow/Downloads/SoHoft - Proposition CA Immobilier.docx" sohoft-source.docx
   unzip sohoft-source.docx -d extracted/
   ```

2. **Explorer les assets extraits :**
   - `extracted/word/media/` → images et logos (PNG/JPEG)
   - `extracted/word/theme/theme1.xml` → couleurs du thème (accent1, accent2, etc.)
   - `extracted/word/styles.xml` → styles des titres, paragraphes, tableaux
   - `extracted/word/document.xml` → structure et mise en page
   - `extracted/word/header*.xml` et `footer*.xml` → en-têtes / pieds de page
   - `extracted/word/settings.xml` → marges, polices par défaut

3. **Extraire les codes couleurs.** Dans `theme1.xml`, chercher les balises `<a:srgbClr val="XXXXXX"/>` pour accent1 à accent6. Logger les codes hex dans un fichier `C:/Users/Shadow/Documents/vault-prive/00-Inbox/exports/sohoft-template/palette.md` pour référence.

4. **Extraire le logo.** Identifier le fichier image dans `extracted/word/media/` qui correspond au logo SoHoft (probablement le 1er, souvent `image1.png`). Le copier vers `exports/sohoft-template/logo-sohoft.png`.

5. **Utiliser le docx SoHoft directement comme template Pandoc** — c'est l'approche la plus fiable :
   ```bash
   pandoc "C:/Users/Shadow/Documents/vault-prive/00-Inbox/Propale Sohoft - CA Immobilier - Engagement 1.md" \
     -o "C:/Users/Shadow/Documents/vault-prive/00-Inbox/exports/Propale_Sohoft_CA_Immobilier_v1.docx" \
     --toc --toc-depth=2 \
     --reference-doc="C:/Users/Shadow/Downloads/SoHoft - Proposition CA Immobilier.docx"
   ```

   **Attention :** Pandoc `--reference-doc` utilise les styles mais n'importe pas la page de garde ni les en-têtes/pieds de page. Il faudra soit :
   - Option A (simple) : accepter une version sans page de garde, que je compléterai à la main dans Word après
   - Option B (plus propre) : utiliser `python-docx` pour coller le contenu généré par Pandoc dans le docx SoHoft en conservant la page de garde, les en-têtes et pieds de page. Claude Code arbitre selon la complexité.

6. **Vérifier le rendu :**
   - Les couleurs de titres sont-elles bien celles de SoHoft ?
   - La police est-elle cohérente ?
   - Les sauts de page HTML (`<div style="page-break-after: always;">`) sont-ils bien interprétés par Pandoc ?
   - Les tableaux sont-ils lisibles ?
   - Les blocs code (annexes B et C) sont-ils en police monospace ?
   - Le schéma ASCII (annexe A) est-il préservé ?

7. **Livrer dans** `C:/Users/Shadow/Documents/vault-prive/00-Inbox/exports/` avec les fichiers :
   - `Propale_Sohoft_CA_Immobilier_v1.docx` (le livrable final)
   - `sohoft-template/palette.md` (codes couleurs extraits)
   - `sohoft-template/logo-sohoft.png` (logo extrait)

8. **Reporting de fin de tâche** : à la fin de l'export, indiquer la pagination effective du fichier produit (nombre de pages Word total, ventilation approximative par chapitre si possible). Cette info nous sert à arbitrer une éventuelle refonte éditoriale ultérieure.

**Challenges attendus :**

- **Schéma ASCII (annexe A)** : police proportionnelle en Word = rendu cassé. Forcer monospace sur ce bloc ou convertir en image PNG (livrable 5 ci-dessous).
- **Tableaux larges** (section 10.4, 5.4.1) : peuvent déborder de la page. Ajuster les largeurs de colonnes.
- **Page de garde** : Pandoc ne peut pas la recréer automatiquement. Deux approches possibles selon la qualité visée.

### Livrable 6 — BPU (Bordereau de Prix Unitaire) — priorité 1

**Objectif :** produire le BPU en Excel et en Word, en s'appuyant sur la version Markdown déjà rédigée.

**Fichier source :**
`C:/Users/Shadow/Documents/vault-prive/00-Inbox/BPU CA Immobilier - Version Markdown.md`

Cette note Markdown contient le BPU complet et validé : 4 sections, plusieurs lignes par section, ventilation cohérente avec la propale (les chiffres font foi dans le BPU et la propale, le brief ne les duplique pas pour éviter toute dérive). Pas de rédaction à faire — juste une mise en forme.

**Actions à faire :**

1. **Lire le fichier source Markdown** pour comprendre la structure (4 sections, tableaux par ligne, sous-totaux, total général, sommaire synthétique).

2. **Produire un Excel** `BPU_Sohoft_CA_Immobilier.xlsx` avec 3 feuilles :
   - **Feuille 1 — BPU détaillé** : 1 ligne par poste du BPU (compter les lignes en parsant le Markdown), avec les colonnes `Poste | Feature/Lot | Points complexité | Charge J/H | Indice confiance | TJM | Prix € HT | Commentaire`. Sous-totaux par section calculés par formules.
   - **Feuille 2 — Sommaire** : reprise du sommaire synthétique du Markdown, en format tableau propre avec totaux en bas.
   - **Feuille 3 — Notes méthodologiques** : TJM appliqués, indice de confiance, principe commercial d'indissociabilité, règle de chiffrage du pilotage projet (à reprendre depuis les notes finales du BPU Markdown).

3. **Contraintes Excel :**
   - Formules automatiques pour les sous-totaux et le total général (pas de hardcoding)
   - Cellules de saisie en jaune pâle (Charge J/H, TJM) — cellules calculées en gris
   - Cellules figées (freeze panes) sur l'en-tête
   - Police Calibri 11 cohérente avec le template SoHoft (voir Livrable 1)
   - Les couleurs des en-têtes doivent reprendre celles extraites du docx SoHoft (palette.md du Livrable 1)
   - Onglet "Sommaire" en première position, figé en haut, avec mise en forme synthétique attractive
   - Format "€ HT" avec séparateur de milliers
   - **Vérification automatique** : assertion en bas de la feuille détail comparant le total parsé depuis les lignes individuelles avec le total annoncé dans le sommaire synthétique du BPU Markdown. Si écart, alerter avant de livrer.

4. **Produire un Word** `BPU_Sohoft_CA_Immobilier.docx` (séparé de la propale principale) :
   - Utiliser le même template SoHoft (`--reference-doc`) que le Livrable 1
   - Conversion directe du Markdown source via Pandoc
   - Page de garde optionnelle avec titre "Bordereau de Prix Unitaire — Proposition CA Immobilier" et mention "Annexe à la proposition technique et financière SoHoft du 22/04/2026"

5. **Livrer dans** `C:/Users/Shadow/Documents/vault-prive/00-Inbox/exports/` :
   - `BPU_Sohoft_CA_Immobilier.xlsx`
   - `BPU_Sohoft_CA_Immobilier.docx`

**Vérifications de cohérence à faire :**

- Les sous-totaux par section parsés depuis les lignes individuelles doivent correspondre aux sous-totaux annoncés dans le BPU Markdown (sections "SOUS-TOTAL SECTION X")
- Le total général parsé doit correspondre au "FORFAIT GLOBAL" annoncé en tête du BPU Markdown ET au "Forfait global" annoncé dans la propale §10.1
- Le total parsé doit aussi correspondre au sommaire synthétique en fin de BPU Markdown
- Si une vérification échoue : alerter immédiatement, ne pas livrer un BPU avec un écart, indiquer précisément la ligne ou la section qui pose problème

**Challenge attendu — structure Markdown atypique :** la version Markdown du BPU n'utilise **PAS** un grand tableau unique avec 27 lignes. À la place, chaque ligne du BPU est un **petit tableau 2 colonnes au format `Champ | Valeur`**, précédé d'un titre `### Ligne N — Nom du poste` et suivi de blocs "Livrables" et "Commentaire" en prose.

Extrait type (les valeurs ci-dessous sont fictives, à titre illustratif uniquement — les valeurs réelles à parser sont dans le BPU Markdown source) :

```markdown
### Ligne N — Nom du poste

| Champ | Valeur |
|---|---|
| Poste | Nom du poste |
| Feature / Lot | — |
| Points complexité | X |
| Charge | **N j** |
| Confiance | 1 à 3 |
| Prix | **N XXX €** |

**Livrables :**

- ...

**Commentaire :** Propale §X.Y Lot Z...
```

**Conséquences pour le parsing :**

- Itérer sur les titres `### Ligne N —` (ou sur chaque tableau 2 colonnes) pour identifier chaque poste
- Pour chaque poste, lire le tableau vertical et reconstruire une ligne horizontale Excel (transposition)
- Extraire séparément le bloc "Livrables" (liste à puces) et "Commentaire" (prose) pour les coller dans des colonnes dédiées de l'Excel
- Les valeurs `Charge` et `Prix` ont un formatage Markdown (astérisques gras, espaces, "j", "€") qu'il faut nettoyer avant stockage numérique
- Le fichier contient aussi un **sommaire synthétique final** (grand tableau récapitulatif) qui peut servir de **source secondaire de vérification** — comparer les totaux parsés depuis les lignes individuelles avec ceux du sommaire final

**Recommandation :** commencer par une passe d'exploration pour compter les lignes, valider la structure, puis itérer. Ne pas essayer de parser directement avec une regex générique — utiliser une lib Markdown (ex: `mistune` ou `markdown-it-py`) qui expose l'AST, puis naviguer dans l'AST pour identifier les sections.

Claude Code arbitre.

### Livrable 3 — Version courte de la propale (priorité 3, optionnel)

**Objectif :** produire une version condensée adaptée à un lecteur sponsor (CDO) qui n'a pas le temps de lire la version intégrale.

**Actions à faire :**

1. Extraire du markdown source les sections suivantes uniquement :
   - Synthèse générale (ch. 1)
   - Qui est SoHoft (ch. 2) — version courte
   - Contexte et enjeux (ch. 3.1) + Vision cible résumée (ch. 3.3) + Enjeux clés (ch. 3.4)
   - Proposition technique : 4.1 périmètre + 4.3.1 Snowflake + 4.5 cas d'usage MVP + 4.8 livrables (liste sans détails)
   - Planning macro (ch. 6.1.1 uniquement, vue d'ensemble)
   - Engagements (ch. 7)
   - Hypothèses en une page (synthèse de ch. 9)
   - Proposition financière complète (ch. 10)
   - Conditions contractuelles (ch. 11)

2. Générer un second fichier Word : `Propale_Sohoft_CA_Immobilier_Synthese.docx`

3. Le document long original devient le "Dossier technique détaillé" complémentaire.

### Livrable 4 — Vérifications de cohérence (priorité 1 mais rapide)

**Objectif :** faire une passe de vérif automatique avant livraison.

**Actions à faire :**

1. **Rechercher dans le markdown les anomalies suivantes :**
   - Occurrences résiduelles des mots "Engagement 1", "Engagement 2", "Engagement 3", "E1", "E2", "E3" (hors tableaux où P1/P2/P3 est OK)
   - Occurrences des prénoms "Ziyad", "Florian", "Ben Messaoud", "Chaigne" (doivent être remplacés par fonctions)
   - Occurrence du mot "Globasoft" (ne doit JAMAIS apparaître)
   - Occurrences de "partenaire d'intégration" ou "partenaire tiers" (ne doivent plus apparaître)
   - Occurrences du mot "IA" ou "intelligence artificielle" ou "AI" (jamais dans ce doc)
   - Occurrences de "atelier CISO" (car on a basculé sur "questions par mail") — à vérifier quelle occurrence est légitime
   - Occurrences de "scénario compact"

2. **Vérifier la cohérence des chiffres entre la propale et le BPU :**
   - Parser les totaux de la propale §10.1 (tableau de synthèse) et §10.2/10.3/10.4 (détails par périmètre)
   - Parser les totaux du BPU Markdown (sous-totaux par section + forfait global + sommaire synthétique)
   - Comparer et alerter sur tout écart entre :
     - Les sous-totaux par périmètre dans la propale §10.1 et la somme des lignes dans §10.2/10.3/10.4
     - Le forfait global de la propale §10.1 et le forfait global du BPU
     - Le détail des échéances de facturation §10.5 et le forfait global
   - Vérifier que les TJM appliqués dans la propale et le BPU sont cohérents (mêmes TJM partout)

3. **Produire un rapport** listant les anomalies trouvées, avec numéro de ligne, extrait de contexte, et écart constaté le cas échéant. **Ne jamais "corriger" automatiquement** — juste signaler, je tranche.

### Livrable 5 — Génération de l'annexe A en image (priorité 2)

**Objectif :** convertir le schéma d'architecture ASCII en image propre pour intégration au Word.

**Actions à faire :**

1. Parser le bloc ASCII de l'annexe A du markdown.

2. Le recréer avec un outil graphique :
   - **Option A (Mermaid)** : traduire l'ASCII en diagramme Mermaid `flowchart TD` ou `graph`, puis exporter en PNG via `mmdc` (mermaid CLI)
   - **Option B (Python PIL/matplotlib)** : dessiner les rectangles et flèches programmatiquement
   - **Option C (Graphviz dot)** : définir le graphe en langage dot, compiler en PNG

3. Livrer le PNG dans `exports/` à 1200x800 px minimum, fond blanc, lisible.

4. Mettre à jour le markdown pour référencer l'image au lieu du bloc ASCII :
   ```markdown
   ![Schéma d'architecture cible](annexe_a_architecture.png)
   ```

---

## Contraintes de réalisation

### Environnement technique
- **OS :** Windows 10/11
- **Terminal :** PowerShell ou Git Bash disponibles
- **Python :** installé (utilisé par certains MCP), venv possible dans `C:/Users/Shadow/dev/`
- **Node.js :** à vérifier
- **Outils disponibles :** Pandoc (à installer si besoin), Git, VSCode
- **Accès réseau :** OK, packages pip/npm téléchargeables

### Règles de rédaction
- **Jamais mentionner :** Globasoft, partenaire tiers, IA, intelligence artificielle
- **Style :** type Exakis — flèches ➜, vouvoiement pro, ton concis
- **dbt Core uniquement** (jamais dbt Cloud)
- **Ne pas modifier le fond du document** sans me demander — juste la forme et les exports

### Workflow attendu
1. Claude Code commence par **me poser les questions** si certains points sont ambigus (template Word, logo SoHoft, etc.)
2. **Ne pas tout faire d'un coup** — procéder livrable par livrable, me montrer le résultat avant de passer au suivant
3. **Versionner** le markdown source avant toute modification (git commit ou copie de sauvegarde dans `exports/backups/`)

---

## Prioritsation

| # | Livrable | Priorité | Temps estimé |
|---|---|---|---|
| 1 | Export Word du document complet + vérif cohérence | **P0 — urgent** | 30-60 min |
| 6 | BPU (Excel + Word) depuis le Markdown existant | **P0 — urgent** | 30-45 min |
| 2 | Génération de l'annexe A en image PNG | P1 | 30 min |
| 4 | Vérifications de cohérence sur la propale | P1 | 15 min |
| 3 | Version courte de la propale (synthèse) | P2 — si temps | 45 min |
| 5 | Grille de chiffrage de migration (Excel) | P2 — si temps | 1-2h |

**Blocage potentiel :** si Pandoc ne rend pas correctement les tableaux complexes ou les sauts de page HTML, il faudra peut-être passer par une autre chaîne (LibreOffice headless, python-docx directement depuis le markdown parsé). Claude Code arbitre et me propose la meilleure approche.

---

## Points à me demander avant de commencer

1. **Page de garde** — tu veux que Claude Code préserve celle du docx SoHoft (approche python-docx plus complexe) ou tu accepteras de la compléter à la main dans Word à la fin (approche Pandoc simple) ?
2. **Version courte** — tu la veux vraiment ou elle peut attendre que la version longue soit validée ?
3. **Annexe A en image** — tu valides la conversion de l'ASCII en PNG ou tu préfères garder l'ASCII tel quel (au risque d'un rendu moche) ?

---

## Note finale

La propale a été itérée sur de nombreuses versions. Elle est globalement stable. L'objectif maintenant est de la **rendre livrable** (format Word propre) et de produire les **annexes techniques associées** (Excel de chiffrage, schéma d'archi en image).

Tout le contenu de fond est déjà validé — pas de réécriture sauf si tu détectes une incohérence ou une faute lors de ta passe de vérif.

Bonne session.