---
tags: ["commercial", "CA-Immobilier", "suivi", "corrections", "word"]
created: 2026-04-26
statut: en-cours
---

# Suivi corrections — Propale CA Immobilier V2 → V3

**Fichier à corriger :** `C:/Users/Shadow/Downloads/Propale_Sohoft_CA_Immobilier_v2.docx`
**Cible :** `Propale_Sohoft_CA_Immobilier_v3.docx`
**Markdown source :** `vault-prive/00-Inbox/Propale Sohoft - CA Immobilier - Engagement 1.md`
**Analyse source :** Claude dans Word (26/04/2026)

---

## 🔴 Corrections critiques

### C1 — Section 5 : titre fusionné + H1 manquant
**Diagnostic :** Le paragraphe idx 676 contient deux titres collés via un saut de ligne vertical (`\u000b`) : "5. Jalons et planning" + "5.1 Macro planning global (3 périmètres)". Stylé en H2 alors que "5. Jalons et planning" devrait être H1. La section 5 n'a donc pas de H1 propre.
**Correction :** Scinder en deux paragraphes distincts. "5. Jalons et planning" → Heading 1. "5.1 Macro-planning global (3 périmètres)" → Heading 2.
**Statut :** [x] ✅ fait

### C2 — Deux H1 vides (paragraphes fantômes)
**Diagnostic :** Paragraphes idx 131 et 132 stylés "Titre 1" mais sans texte. Polluent le sommaire.
**Correction :** Supprimer ces deux paragraphes, ou les passer en style "Normal".
**Statut :** [x] ✅ fait

---

## 🟡 Corrections moyennes

### C3 — 4 titres H2 en police Karla au lieu de Calibri
**Diagnostic :** La majorité des H2 est en Calibri. 4 H2 dévient en Karla :
- "3.2 Notre approche méthodologique"
- "3.7 Roadmap de migration globale"
- "5.4 Points de vigilance planning"
- Le titre fusionné §5 (corrigé avec C1)
**Correction :** Police Calibri appliquée sur les 3 titres. Saut de page parasite (`\f`) dans "3.7 Roadmap" nettoyé.
**Statut :** [x] ✅ fait

### C4 — Tableaux 17 et 19 (chiffrage) — cellules vides
**Diagnostic :** Tableau 17 (§9.2 Périmètre 1) a 34% de cellules vides. Tableau 19 (§9.4 Périmètre 3) a 32% de cellules vides. Les colonnes "Phase", "Charge" et "Prix" ont des lignes sans données.
**Analyse :** C'est **intentionnel** — les lignes de "Bloc fonctionnel" (ex: "Lot 1 — Cadrage et ateliers") sont des en-têtes de regroupement qui n'ont pas de charge/prix propre. Les valeurs sont sur les sous-lignes. **Pas de correction nécessaire**, mais vérifier visuellement que le rendu est clair (fusion de cellules ou grisage des lignes de regroupement).
**Statut :** [ ] à vérifier visuellement

### C5 — Zone §2.5 : tableau simulé en paragraphes Normal
**Diagnostic :** Le tableau "Composant / Intitulé / Positionnement SoHoft" sous 2.5 est formaté avec des paragraphes Normal individuels (idx 240-257), pas un vrai tableau Word (`<w:tbl>`). Les deux autres occurrences de ce tableau (3.1.1 et 9.1) sont de vrais tableaux Word.
**Correction :** Recréer le tableau 2.5 comme un vrai tableau Word, cohérent avec les sections 3.1.1 et 9.1. OU accepter le rendu actuel si visuellement correct.
**Statut :** [ ] à vérifier visuellement

### C6 — 3 tableaux "Composant" potentiellement redondants
**Diagnostic :** Les tableaux 0, 1 et 2 partagent le même en-tête "Composant / Intitulé / Positionnement SoHoft" avec 6 lignes chacun. Ils apparaissent en sections 2.5, 3.1.1 et 9.1.
**Analyse :** C'est **intentionnel** — le tableau apparaît dans 3 contextes différents :
- §2.5 : "voici comment votre démarche se découpe" (compréhension du besoin)
- §3.1.1 : "voici comment on couvre vos 5 composants" (périmètre)
- §9.1 : synthèse financière avec les montants
Cependant, §2.5 et §3.1.1 sont **très proches** et le lecteur verra la répétition. **À arbitrer** : supprimer l'un des deux (de préférence 2.5 qui est le moins contextuel) ou garder.
**Statut :** [ ] arbitrage nécessaire

---

## 🟢 Corrections mineures

### C7 — 5 titres H3 sans numérotation
**Diagnostic :** Sous §9.4 et Annexe C, des H3 n'ont pas de préfixe numérique :
- "Détail par cas d'usage"
- "Conditions d'activation"
- "Livrables du Périmètre 3"
- "Principe" (Annexe C)
- "Impact sur le chiffrage" (Annexe C)
**Correction :** Numérotation ajoutée sur les 3 premiers (9.4.1, 9.4.2, 9.4.3). Annexe C laissée sans numérotation globale (choix éditorial).
**Statut :** [x] ✅ fait

### C8 — Annexe C : numérotation locale conflictuelle
**Diagnostic :** Les H3 "1.", "2.", "3." dans l'Annexe C utilisent une numérotation locale qui entre en conflit visuel avec la numérotation globale du document.
**Correction :** Acceptable tel quel — c'est dans une annexe, pas dans le corps. Mais on pourrait renommer en "C.1 Le fichier de configuration YAML", "C.2 La macro Jinja", "C.3 Les modèles dbt".
**Statut :** [ ] optionnel

---

## 📋 Corrections reportées de la phase précédente

### C9 — Références internes obsolètes
**Diagnostic :** 21 références trouvées, 6 cassées, 15 valides. Le décalage vient de la renumérotation V2 (10 chapitres au lieu de 11 dans le markdown).

**6 corrections à appliquer :**

| # | Texte actuel | Section | Correction | Justification |
|---|---|---|---|---|
| 1 | "Voir section 9.3.1" | §3.1.3 | → "Voir section 9.3" | 9.3.1 n'existe pas, c'est 9.3 directement |
| 2 | "voir section 10.6" | §4.4.5 | → "voir section 9.6" | §10 ne va que jusqu'à 10.5, les conditions de révision sont en 9.6 |
| 3 | "listés en section 4.8" | §6.1 | → "listés en section 3.8" | Les livrables sont en 3.8 dans la V2 |
| 4 | "décrit en section 4.5" | §7.3 | → "décrit en section 3.5" | Le focus MVP est en 3.5 dans la V2 |
| 5 | "décrit en section 4.5" | §9.4.2 | → "décrit en section 3.5" | Idem |
| 6 | "section 7.4" | §9.6 | → "section 6.4" | L'engagement de transparence est en 6.4 |

**Statut :** [x] ✅ fait (6/6 corrigées en redlines)

### C10 — Table des matières à régénérer
**Diagnostic :** Après toutes les corrections de titres, styles et chiffrage, la TDM était obsolète.
**Correction :** Champ TOC rafraîchi — numéros de page et titres à jour.
**Statut :** [x] ✅ fait

---

## Ordre de traitement recommandé

1. **C1** (titre fusionné §5) — critique, impacte la TDM
2. **C2** (H1 vides) — critique, impacte la TDM
3. **C3** (police Karla) — rapide, 3 clics
4. **C7** (H3 sans numéro) — rapide
5. **C5 + C6** (tableau §2.5 + redondance) — vérification visuelle + arbitrage
6. **C4** (tableaux chiffrage) — vérification visuelle
7. **C9** (références internes) — demander à Claude dans Word
8. **C10** (TDM) — en tout dernier

---

## Historique

| Date | Action | Par |
|---|---|---|
| 2026-04-26 | Diagnostic initial V2, correction bugs 1/3/4/bonus | Claude Code |
| 2026-04-26 | Analyse complète format par Claude dans Word (115 titres, 21 tableaux) | Claude dans Word |
| 2026-04-26 | Corrections C1, C2, C3, C7, C9 appliquées | Claude dans Word |
| 2026-04-26 | Audit normes ISO 24495 / conventions marché — 23 critères évalués | Claude dans Word |
| 2026-04-26 | N3 synthèse insérée + reformatée, N4 sauts de page, N6 Times New Roman (16 paras) | Claude dans Word |
| 2026-04-26 | N1/N2 en-tête+pied de page, N9 tableaux (en-têtes gras+alignement), N11 annulé, chiffrage §9 | Claude dans Word + utilisateur |
| 2026-04-26 | N7 interligne (1063 paras → 1,15), N8 justification (1058 paras) + harmonisation styles (350 "Corps de texte" → "Normal" Calibri) | Claude dans Word |
| 2026-04-26 | C10 TDM régénérée | Claude dans Word |
| 2026-04-26 | V1 schéma architecture cible produit en Excalidraw, inséré en §3.3 | Claude.ai |
| 2026-04-26 | N12 hiérarchie titres corrigée : H2 11→14pt, H3 9→12pt | Claude dans Word |
| 2026-04-26 | Changement chiffrage P3 : Natio 19→10j, NPM Altaix 11→5j, tests/recette/doc offerts. Propagé sur propale markdown (§10.1, §10.4, §10.5) + BPU complet. Nouveau forfait : 73,5 j / 49 800 € | Claude.ai |
| 2026-04-26 | Chiffrage P3 propagé dans le Word V2 : §9.1, §9.4 (2 lignes supprimées + 4 valeurs modifiées), §9.5 (échéancier complet), Synthèse. 73,5 j / 49 800 € partout | Claude dans Word |
| 2026-04-26 | Chiffrage P1 agressif : DAT 12→10j (fusion CISO), CISO 9→0j (fusionné), présentations 6→2j. P1 49,5→34,5j. Nouveau forfait : 58,5 j / 39 300 €. Propagé propale markdown + BPU | Claude.ai |
| 2026-04-26 | Chiffrage P1 propagé dans le Word V2 : §9.1, §9.2 (1 ligne supprimée + 3 valeurs modifiées), §9.5 (échéancier complet), Synthèse. 58,5 j / 39 300 € partout | Claude dans Word |
| 2026-04-26 | P2 élargi : 5j→15j, intégrations Groupe incluses (Private Link, SSO, BIOK/Key Vault, Usercube, Graylog). TJM 575€. Nouveau forfait : 68,5 j / 44 425 €. Propagé propale markdown (§10.1, §10.3, §10.5, §4.1.3, §9.4) + BPU complet (lignes renumérotées 10-29) | Claude.ai |
| 2026-04-26 | P2 élargi propagé dans le Word V2 : §9.1, §9.3 (5 nouvelles lignes, TJM→575€, bloc hors périmètre supprimé), §9.5 (échéancier 5 jalons), Synthèse. 68,5 j / 44 425 € partout | Claude dans Word |
| 2026-04-26 | V2 diagramme 3 périmètres (sans charges, prix uniquement) + V3 Gantt 18 semaines (sans prix) produits en Excalidraw, insérés en §3.1 et §5.1 | Claude.ai + utilisateur |
| 2026-04-26 | Suppression des notions de charge (j) et TJM dans le Word : colonnes supprimées dans §9.1/9.2/9.3/9.4, notes pilotage supprimées, Synthèse sans jours | Claude dans Word ✅ fait |
| 2026-04-26 | Ajout bullet "Time-to-market accéléré" dans §3.3 (Pourquoi Snowflake change la donne) — propale markdown + Word | Claude.ai + utilisateur |
| 2026-04-26 | Visuels : approche méthodologique (4 principes, §3.2) + 6 livrables P1 (grille 2×3, §3.8) produits en Excalidraw, insérés | Claude.ai + utilisateur |
| 2026-04-26 | Correction cohérence P2 élargi : §2.5 texte + tableau + §3.1.3 titre et contenu mis à jour (hors périmètre → pris en charge par SoHoft) | Claude.ai + utilisateur |
| 2026-04-26 | Expert Snowflake : suppression certif SnowPro + notion d'audit → "déploiement complet de la plateforme et des intégrations Groupe". §5.1 + §5.2.2 + "certifiée"→"pointue" | Claude.ai + utilisateur |
| 2026-04-26 | Fusion rôles : "Expert Data Engineering" + "Développeur Data Engineer" → un seul "Expert Data Engineering" sur P1+P3. §5.1 + §5.2.2 | Claude.ai + utilisateur |
| 2026-04-26 | Suppression paragraphe explicatif écarts COPIL (§5.3) — le tableau se suffit | Utilisateur |
| 2026-04-26 | Visuel disponibilité ressources client (planning × charge par personne, 18 semaines) produit en Excalidraw — remplace §5.4.1 + §5.4.2 + §5.4.3 | Claude.ai |
| 2026-04-26 | Reformulation §6.1.4 période estivale : posture constructive (anticipation + risque) au lieu de binaire (arrêt si pas verrouillé). Jalon J8 reste structurant | Claude.ai + utilisateur |
| 2026-04-26 | §6.4.2 : compte Snowflake "contrat en place, activation + accès à effectuer" (plus de mention contractualisation) + intégrations Groupe "portées par SoHoft" (plus "hors périmètre") | Claude.ai + utilisateur |

---

## 📊 Ventilation par nature d'activité (68,5 j)

| Nature | Postes | Charge | % |
|---|---|---:|---:|
| **Production documentaire** | DAT+CISO (10j) + FinOps (3j) + Roadmap (2j) + Présentations (2j) | **17 j** | **25%** |
| **Conception / Ateliers** | Animation ateliers (8j) + Cartographie AS-IS (5j) + Spécifications MVP (3j) | **16 j** | **23%** |
| **Réalisation MVP** | Natio (10j) + NPM Altaix (5j) | **15 j** | **22%** |
| **Déploiement Snowflake** | Setup base (5j) + Intégrations Groupe (10j) | **15 j** | **22%** |
| **Pilotage** | Pilotage P1 (1,5j) + Pilotage P3 (1j) | **2,5 j** | **4%** |
| **Transverse P3** | Airflow (2j) + Coordination Snowflake (1j) | **3 j** | **4%** |
| **Recette / Tests / Doc** | Offert | **0 j** | **0%** |

**Points clés :**
- Pilotage à 4% (vs 15-20% chez une ESN classique) — offre agressive
- Équilibre cadrage (48%) / réalisation (48%) / pilotage (4%) — le client paie pour du livrable, pas du management
- Snowflake à 22% — l'inclusion des intégrations Groupe donne un interlocuteur unique au client pour tout le déploiement
- MVP à 22% — 15 j pour 2 cas d'usage complets, tests/recette/doc offerts
- Recette à 0% — geste commercial visible dans le BPU

---

## 🎨 Visuels à produire et intégrer

### V1 — Schéma d'architecture cible ✅
**Section :** §3.3 Architecture cible recommandée (+ remplacement Annexe A)
**Contenu :** Flux complet Sources → Zone sécurisée → DLT → Snowflake (4 zones) → dbt → Power BI, avec services Groupe (SSO, Private Link, BIOK+Key Vault, Usercube, Graylog) en externe connectés à Snowflake
	**Statut :** [x] ✅ produit en Excalidraw, inséré en §3.3

### V2 — Diagramme des 3 périmètres (P1→P2→P3)
**Section :** §3.1 Périmètre de notre intervention
**Contenu :** 3 blocs P1 (34,5 j / 24 150 €) → P2 (15 j / 8 625 €) → P3 (19 j / 11 650 €) avec flèches d'enchaînement, composants couverts, livrables, jalons J6/J7/J10. Tests/recette/doc offerts mis en avant.
**Statut :** [x] ✅ produit en Excalidraw (avec chiffres à jour 68,5 j / 44 425 €)

### V3 — Frise chronologique / Gantt simplifié (18 semaines)
**Section :** §5.1 Macro-planning global
**Contenu :** Bandes colorées horizontales P1 (S1-S8) / P2 (S7-S9, en recouvrement) / P3 (S10-S18), jalons J1-J10 positionnés, coupure estivale S12-S15 marquée, 4 COPIL positionnés. Sans prix.
**Statut :** [x] ✅ produit en Excalidraw, inséré en §5.1

### V4 — Encadré chiffres clés (Synthèse)
**Section :** Page Synthèse en tête de document
**Contenu :** Encadré visuel avec les 4 chiffres clés (68,5 j / 44 425 € / 18 semaines / 3 périmètres) — plus impactant qu'un tableau
**Statut :** [ ]

### V5 — Schéma zones × domaines Snowflake
**Section :** §3.3.1 Snowflake, plateforme data centrale
**Contenu :** Matrice 2 axes montrant l'organisation logique Snowflake — axe vertical (zones : raw/staging/core/marts) × axe horizontal (domaines : patrimoine, vente de neuf, locatif, promotion, gestion, finance, transverse). MVP P3 (Patrimoine + Vente Neuf) surlignés en bleu.
**Statut :** [x] ✅ produit en Excalidraw, à insérer en §3.3.1

### V6 — Camembert répartition charges P1/P2/P3
**Section :** §9.1 Modèle d'engagement
**Contenu :** Répartition visuelle des 68,5 j entre P1 (34,5 j = 50%), P2 (15 j = 22%), P3 (19 j = 28%)
**Statut :** [ ]

---

## 🔴 Correction critique identifiée tardivement

### N12 — Hiérarchie visuelle des titres inversée
**Critère :** Typographie §9 + ISO 24495 (repérabilité)
**Diagnostic :** H2 = 11pt (même taille que le corps), H3 = 9pt (plus petit que le corps). Le lecteur ne peut pas naviguer visuellement.
**Correction :** H2 passé de 11pt à 14pt, H3 passé de 9pt à 12pt. Appliqué via la définition de style sur les 49 H2 et 52+ H3 du document.
**Statut :** [x] ✅ fait

### Priorité de production des visuels

| # | Visuel | Impact | Effort |
|---|---|---|---|
| V1 | Architecture cible | Fort | ✅ fait |
| V3 | Gantt 18 semaines | Fort — le planning tableau est illisible | Moyen |
| V2 | 3 périmètres | Moyen — clarifie l'articulation | Faible |
| V5 | Zones × domaines Snowflake | Fort — structurant pour le CISO | Moyen |
| V4 | Encadré chiffres clés | Moyen — synthèse déjà insérée en tableau | Faible |
| V6 | Camembert charges | Moyen — les chiffres sont déjà en tableau | Faible |

---

## 🔴 Nouveaux points identifiés — Audit normes (26/04/2026)

### N1 — En-tête vide (placeholder `<<<<`)
**Critère :** Structure §4
**Diagnostic :** L'en-tête contient uniquement `<<<<` — placeholder vide. Pas de logo SoHoft, pas de nom du document.
**Correction :** Non nécessaire — le rendu réel dans Word affiche déjà le design SoHoft en place.
**Statut :** [x] ✅ déjà OK

### N2 — Pied de page incomplet
**Critère :** Structure §5
**Diagnostic :** Numérotation "Page X sur Y" présente ✅, mais pas de mention "Confidentiel", pas de date, pas de version.
**Correction :** Ajouté "Confidentiel — V3 — Avril 2026" dans le pied de page.
**Statut :** [x] ✅ fait

### N3 — Résumé opérationnel / synthèse absent
**Critère :** Structure §6 + ISO 24495
**Diagnostic :** Le document commence directement par §1 "SoHoft". Aucune page de synthèse.
**Correction :** Page "Synthèse" insérée avant le chapitre 1, reformatée (tableau Word, bullets ➜, Calibri 11pt).
**Statut :** [x] ✅ fait

### N4 — 7 chapitres H1 sans saut de page avant
**Critère :** Structure §3
**Diagnostic :** Seuls 4 H1 sur 10 précédés d'un saut de page.
**Correction :** Style Heading 1 configuré avec "Saut de page avant" — appliqué à tous les H1.
**Statut :** [x] ✅ fait

### N5 — Marges trop serrées (1,3 cm au lieu de 2,5 cm)
**Critère :** Typographie §12
**Diagnostic :** Les 4 marges sont à 1,3 cm. Norme = 2,5 cm minimum.
**Correction :** Passer les marges à 2,5 cm. **Attention :** impact fort sur la pagination et les tableaux larges.
**Statut :** [ ] ⚠️ P2 — à arbitrer

### N6 — Times New Roman parasite
**Critère :** Typographie §7
**Diagnostic :** Initialement 4 paragraphes identifiés, 16 corrigés au total (tous vides, zones de garde + transitions).
**Correction :** Passés en Calibri 11pt.
**Statut :** [x] ✅ fait

### N7 — Interligne non homogène
**Critère :** Typographie §10
**Diagnostic :** 3 valeurs d'interligne coexistent (12pt / 12,95pt / 14pt). La valeur 12pt est en dessous du seuil 1,15 recommandé.
**Correction :** 1063 paragraphes uniformisés à 13,8pt (= 1,15 × 12pt, mode Multiple). Titres et cellules de tableau non touchés.
**Statut :** [x] ✅ fait

### N8 — Texte narratif pas systématiquement justifié
**Critère :** Typographie §11
**Diagnostic :** Certains paragraphes "Corps de texte" narratifs ne sont pas justifiés.
**Correction :** 1058 paragraphes justifiés. Style "Corps de texte" (ATC Arquette, 350 paras) basculé en "Normal" (Calibri 11pt) — le document n'utilise plus qu'un seul style de corps. Listes, cellules de tableau et titres inchangés.
**Statut :** [x] ✅ fait

### N9 — 14 tableaux sur 21 sans en-tête en gras
**Critère :** Tableaux §13
**Diagnostic :** Seuls 4 tableaux sur 21 avec en-tête en gras.
**Correction :** Première ligne de chaque tableau passée en gras + fond bleu SoHoft (#1F3864) + texte blanc. Alignement des autres tableaux harmonisé.
**Statut :** [x] ✅ fait

### N10 — 23 blocs de texte > 10 lignes sans rupture visuelle
**Critère :** Lisibilité §18 — ISO 24495
**Diagnostic :** 23 blocs détectés, les plus critiques en §2.4, §2.5, §3.5.2, §3.5.3, §1.
**Correction :** Travail éditorial (découpage avec sous-titres, bullets, encadrés).
**Statut :** [ ] P2 — travail éditorial

### N11 — 15 termes techniques sans explication
**Critère :** Lisibilité §21 — ISO 24495
**Diagnostic :** 15 acronymes/outils sans définition à leur première occurrence.
**Correction :** Non nécessaire — les interlocuteurs (CDO, référent technique, CISO) sont des profils techniques qui connaissent ces termes.
**Statut :** [x] ❌ annulé

---

## Priorisation des nouveaux points

| # | Point | Impact | Effort | Priorité |
|---|---|---|---|---|
| N3 | Résumé opérationnel absent | 🔴 Fort — le CDO ne lira pas 41 pages | Moyen (rédaction 1 page) | **P0** ✅ fait (inséré, reformatage à prévoir) |
| N4 | Sauts de page avant H1 | 🔴 Fort — lisibilité structurelle | Faible (7 insertions) | **P0** ✅ fait |
| N1 | En-tête vide | 🟡 Moyen — visuel | Faible | **P1** ✅ déjà OK (design SoHoft en place) |
| N2 | Pied de page incomplet | 🟡 Moyen — pro | Faible | **P1** ✅ fait |
| N9 | Tableaux sans en-tête gras | 🟡 Moyen — lisibilité | Moyen (14 tableaux) | **P1** ✅ fait + alignement des autres tableaux |
| N6 | Times New Roman parasite | 🟢 Mineur | Faible (4 paras) | **P1** ✅ fait (16 paras corrigés — tous vides, zones de garde + transitions) |
| N11 | Termes techniques non définis | 🟡 Moyen — compréhension | Moyen (15 termes) | **P1** ❌ annulé — interlocuteurs techniques, pas besoin de définitions |
| N10 | Blocs > 10 lignes | 🟡 Moyen — lisibilité | Fort (23 blocs, éditorial) | **P2** |
| N5 | Marges trop serrées | 🟡 Moyen mais impact pagination | Fort | **P2** |
| N7 | Interligne non homogène | 🟢 Mineur | Moyen | **P2** ✅ fait (1063 paras → 13,8pt / 1,15) |
| N8 | Justification incomplète | 🟢 Mineur | Moyen | **P2** ✅ fait (1058 paras justifiés + 350 "Corps de texte" → "Normal" Calibri) |
