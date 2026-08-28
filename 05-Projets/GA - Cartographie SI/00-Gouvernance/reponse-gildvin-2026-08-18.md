---
titre: Réponse à Gildvin — 18/08/2026
statut: brouillon à envoyer
tags: [communication, gildvin]
---

# Projet de réponse à Gildvin

> Objet : **RE: Document: Vision applications IT Groupe GA — les deux cartographies**

Bonjour Gildvin,

J'ai avancé sur les deux cartographies. Plutôt que deux slides, je te propose une
**page interactive** : le sujet ne tient pas sur une diapo. Une slide fige 10 applications
sur 150 et une vingtaine de flux sur 132 — c'est exactement ce qui rendait les
représentations précédentes vite obsolètes et difficiles à lire.

🔗 **https://claude.ai/code/artifact/07d37aed-c02b-4fad-a4b5-610586e0268a**
*(page privée ; je te la partage et tu la diffuses si elle te convient)*

Tout est construit **directement depuis `INVENTAIRE - Applicatifs Métier.xlsx`** : aucun
chiffre n'est ressaisi, tout est traçable jusqu'à une ligne du fichier.

---

## Ce que ça contient

**1 — La vue fonctionnelle.** IFS au centre, 10 domaines métier autour, plus deux bandeaux
transverses : le *pilotage* au-dessus (il consomme tous les domaines), le *socle numérique*
en dessous (il les porte tous). J'ai volontairement construit les domaines sur la **chaîne
de valeur** (développement → études → ingénierie → industrie → travaux → exploitation, plus
les fonctions support) et non sur l'organigramme : la colonne « service propriétaire » de
l'inventaire compte 48 valeurs et bouge à chaque réorganisation. Les 150 applications sont
classées, sans exception. Chaque domaine est cliquable et déroule la liste complète.

**2 — La vue applicative.** Comme tu le pressentais, tout le SI en un schéma n'est pas
lisible : j'ai fait le **focus Finance**. IFS au centre, six familles de flux autour
(achats/P2P, amont métier, RH-paie-NdF, trésorerie, industrie & filiales, consolidation),
avec le sens, le statut et le marquage Talend. En dessous, le tableau des **132 flux
vivants du SI complet**, filtrable — donc on garde l'exhaustivité sans sacrifier la lecture.

**3 — Deux slides PPTX** sont malgré tout générées si tu préfères garder le vMASTER comme
véhicule : `Présentation du SI vMASTER - cartos.pptx` dans mon dossier Downloads (copie,
l'original n'est pas touché), aux positions 8 et 14, à la charte du support.

---

## « Possible avec Archi ? » — oui, et mieux que ça

**Le modèle existe déjà.** En regardant `Documents\Archi`, j'ai retrouvé un modèle
ArchiMate « GA » qui n'a rien d'un brouillon : **581 éléments, dont 156 composants
applicatifs, 178 relations de flux, 26 vues**, avec tout un jeu de scripts jArchi d'import
depuis l'Excel. Ce n'est pas un outil à choisir, c'est un actif à remettre en service.

**Mais il est figé au 1ᵉʳ juillet 2024.** Le dépôt ne contient qu'**un seul commit**
(« First Commit »), et rien n'y a été versionné depuis — 25 mois d'écart avec l'inventaire.
Ce qui est frappant, c'est que l'outillage, lui, a continué jusqu'en **février 2025** :
des scripts d'import ont été écrits et deux instantanés de l'inventaire (août et
octobre 2024) sont restés à côté des scripts. Les ré-imports ont donc été **préparés mais
jamais reversés dans le modèle**. Le chaînon qui a lâché n'est pas l'outil, c'est le geste
de mise à jour — et c'est aussi ce qui explique la désynchronisation des identifiants.

*(Réserve : je n'ai pas pu interroger le dépôt GitHub `Globasoft/GA-Archi` depuis mon poste ;
si quelqu'un a poussé depuis, ma copie locale ne le voit pas. Un `git fetch` lèvera le doute.)*

Deux constats à la comparaison avec l'inventaire d'aujourd'hui :

- ❌ **le lien est rompu côté applications** : aucun des identifiants « ID Archi » de
  l'Excel ne correspond plus à un composant du modèle. Ils ont été régénérés d'un côté sans
  être reportés de l'autre ;
- ✅ **le lien est intact côté flux** : 140 des 150 identifiants pointent toujours vers la
  bonne relation.

Le modèle reflète par ailleurs un SI d'avant IFS : 47 applications actuelles y manquent
(QDV, Exfiles, Sage XRT, Project Monitor, Immolead, GLPI…), et il contient une trentaine de
composants aujourd'hui décommissionnés.

**Mon avis** : le travail utile n'est pas de redessiner, c'est de **remettre en cohérence
l'inventaire et le modèle**. J'estime ça à **≈ 3,5 jours**, et derrière on régénère les
vues par script à chaque mise à jour du fichier — au lieu de tout refaire à la main à chaque
demande. 103 des 150 applications se réapparient déjà automatiquement par leur nom, donc
l'essentiel est scriptable.

---

## Deux points sur lesquels j'ai besoin de toi

**1. Le chiffre des flux à communiquer.** La slide 6 annonce « ≈60 flux inter-applicatifs ».
C'est juste — 61 sont actifs aujourd'hui. Mais le référentiel décrit **132 flux vivants**
en comptant ceux à venir et en construction, portés en grande partie par le lot 4 IFS
(Infor Syteline → IFS, Nibelis → IFS, Expensya → IFS…). Communiquer 61 donne une image
du SI qui sous-estime ce que le projet ERP est en train de construire. À trancher :
photo ou trajectoire.

**2. La taxonomie des domaines.** Elle porte des arbitrages que je préfère te faire valider
avant diffusion (les pointages classés en RH plutôt qu'en Travaux, DocuSign en
Finance/Juridique, les outils IA au socle sauf Batisia…). C'est le genre de détail qui se
discute en 20 minutes et qui structure toute la carto.

---

## Au passage — l'état du référentiel

En instrumentant l'inventaire, quelques points bloquent l'automatisation. Rien de grave,
mais autant les traiter maintenant :

| | Constat | Effort |
|---|---|---|
| 1 | **14 extrémités de flux introuvables** dans l'inventaire applicatif (`Sage Signature`, `ViaReport`, `ICS Compta`, `Hercule`…). 7 sont des alias à normaliser, 5 des applications réellement absentes. | 30 min |
| 2 | **Talend et Power BI ne sont pas inventoriés** — alors que Talend orchestre les interfaces IFS et que Power BI est cité comme outil de pilotage Finance. | 1 h |
| 3 | **86 des 150 applications n'ont pas de statut d'utilisation.** C'est ce qui empêche de fiabiliser le « plus de 100 applications » de la slide 6. | 1/2 j métier |
| 4 | **26 applications et 52 flux sans identifiant Archi** — prérequis n°1 à un modèle synchronisable. | 2 h |
| 5 | Seuls **26 des 132 flux** portent un protocole d'échange, 19 une fréquence. Une vue applicative technique détaillée n'est pas produisible aujourd'hui. | — |

Le détail est tracé de mon côté, je peux te le passer sous forme de liste d'actions.

---

**Prochaine étape que je propose** : 30 minutes ensemble pour valider la taxonomie et
trancher le chiffre des flux. Ensuite je fige la v1 et tu peux l'envoyer à Maëlle.

Une dernière chose : je n'ai pas encore croisé les flux déclarés avec le **repo Talend** et
les documents de flux de la TMA. C'est ce qui permettrait de confronter le déclaratif au
réellement déployé — je le garde pour une v2 si ça t'intéresse.

Bonne journée,
Benoît
