---
tags: ["design", "sohoft", "palette"]
source: SoHoft - Proposition CA Immobilier.docx
extracted: 2026-04-24
---

# Palette SoHoft — extraite du template

## Thème Office (theme1.xml)

Le document utilise le thème Office par défaut (pas de thème custom) :

| Rôle | Code hex |
|---|---|
| dk1 | `windowText` (auto noir) |
| lt1 | `window` (auto blanc) |
| dk2 | #44546A |
| lt2 | #E7E6E6 |
| accent1 | #4472C4 |
| accent2 | #ED7D31 |
| accent3 | #A5A5A5 |
| accent4 | #FFC000 |
| accent5 | #5B9BD5 |
| accent6 | #70AD47 |
| hlink | #0563C1 |
| folHlink | #954F72 |

## Couleurs réellement utilisées dans les styles (styles.xml)

| Code | Usage |
|---|---|
| **#F0A057** | Orange SoHoft — accent principal des titres/highlights (6 occurrences) |
| **#2F5496** | Bleu marine — titres secondaires (4 occurrences) |
| **#BF8F00** | Or sombre (3) |
| **#1F3763** | Bleu nuit (2) |
| **#504765** | Violet sombre (2) |
| **#C00000** | Rouge — alertes (2) |
| #FFFFFF | Blanc (sur fond coloré) |
| #000000 | Noir (corps de texte) |

## Couleurs dans le corps du document (document.xml)

| Code | Occurrences | Rôle probable |
|---|---|---|
| **#F0A057** | 38 | Orange de marque SoHoft |
| #FFC000 | 6 | Jaune mise en avant |
| #002060 | 4 | Bleu marine fort |
| #00B050 | 4 | Vert validation |
| #FFF2CC | 8 (fill) | Fond jaune pâle (encadrés) |
| #171717 | 4 (fill) | Fond gris très foncé |

## Polices

| Police | Usage | Occurrences |
|---|---|---|
| **Karla** | Corps de texte | 10 |
| **Montserrat Black** | Titres principaux | 8 |
| **ATC Arquette** | Titre de couverture ? | 3 |
| Montserrat Light | Sous-titres | 2 |
| Montserrat | Variantes titres | 2 |

## Identité visuelle (images)

Le logo n'est pas un fichier compact — le branding "SoHoft" est composé de plusieurs images :
- `image1.png`, `image2.png`, `image4.png`, `image5.png` : taches violettes (brush strokes), violet de marque ~#6B3FE8
- `image7.png` : mot "Tech" en violet
- `image9.png` : mot "Good" en jaune (#FFC000)
- `image10.png` : mot "OffTheWall" en vert teal (~#00B894)
- `image6.png` : planche logos clients
- Les autres : variantes ou éléments décoratifs

**Couleur de marque violette principale** (non présente dans les styles mais visible dans les images) : ≈ `#6B3FE8`

## Résumé pour intégration

Pour un document aligné au style SoHoft :
- **Corps** : Karla 11 pt, noir (#000000)
- **H1** : Montserrat Black, gros (74pt sur Title1), orange (#F0A057) ou bleu (#2F5496)
- **H2** : Montserrat Black ou équivalent, orange (#F0A057)
- **H3** : orange (#F0A057) ou bleu (#2F5496)
- **Mise en avant** : fond jaune pâle (#FFF2CC) ou encadré gris foncé (#171717) avec texte blanc
- **Liens** : bleu (#0563C1)
