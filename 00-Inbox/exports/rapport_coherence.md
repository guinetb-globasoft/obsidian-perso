---
tags: ["verif", "propale", "CA-Immobilier"]
date: 2026-04-24
source: Propale Sohoft - CA Immobilier - Engagement 1.md
---

# Rapport de vérification de cohérence

## Mots interdits / sensibles

| Terme recherché | Nb occurrences | Statut |
|---|---|---|
| `Globasoft` | 0 | ✅ OK |
| `Engagement 1/2/3`, `E1/E2/E3` | 0 | ✅ OK |
| `partenaire d'intégration`, `partenaire tiers` | 0 | ✅ OK |
| `IA`, `intelligence artificielle`, `AI` | 0 | ✅ OK |
| `scénario compact` | 0 | ✅ OK |
| **Noms propres (Ziyad, Florian, Ben Messaoud, Chaigne)** | 3 | ⚠️ À trancher |
| **`atelier CISO`** | 2 | ⚠️ À trancher |

## Détail des anomalies à arbitrer

### Noms propres (brief : "doivent être remplacés par fonctions")

**Ligne 582** (section 4.8.3 Cartographie AS-IS — Destinataires)
> **Destinataires :** Direction Data, **Florian Chaigne**, futurs prestataires de migration.

Proposition de remplacement : `Direction Data, responsable du patrimoine data, futurs prestataires de migration.` (ou autre fonction à préciser)

---

**Ligne 642** (section 4.8.5 Packs de communication — Destinataires)
> **Destinataires :** **Ziyad Ben Messaoud** (sponsor), CISO, DSI, Direction Générale.

Proposition de remplacement : `Sponsor (CDO), CISO, DSI, Direction Générale.`

---

**Ligne 1006** (section 7.3 Engagement de qualité)
> ➜ **Cartographie** : format exploitable (Excel structuré), revue avec **Florian Chaigne**.

Proposition de remplacement : `revue avec le responsable du patrimoine data.` (ou équivalent)

### Occurrences "atelier CISO"

Le brief note : *"car on a basculé sur 'questions par mail' — à vérifier quelle occurrence est légitime"*

**Ligne 1064** (section 8.2 Plan de mitigation — tableau risque R2)
> R2 — CISO | **Atelier CISO** calé dès la semaine 2, dates de revue sécurisées en début de projet

**Ligne 1115** (section 9.3 Hypothèses sur le référentiel CISO)
> ➜ **Validation CISO en une itération principale** : l'**atelier CISO** en semaine 2 permet d'identifier les points durs en amont ; la validation formelle en semaine 5 se fait sur un DAT aligné avec ces points, sans refonte majeure.

**À arbitrer :** ces deux occurrences sont cohérentes l'une avec l'autre (atelier CISO S2 + validation S5). Si on bascule sur "questions par mail", il faut reformuler les deux de manière cohérente.

> Note : une recherche rapide montre que **ligne 1065** (risque R3) mentionne aussi *"Présentation intermédiaire au CISO en semaine 2"* — pas le terme "atelier" mais même cadence à revoir.

## Vérification des chiffres financiers

Tous les montants et totaux ont été additionnés à partir du tableau de chiffrage (section 10) :

| Contrôle | Attendu | Calculé | OK |
|---|---|---|---|
| Périmètre 1 | 56 j / 39 200 € | 56 j / 39 200 € | ✅ |
| Périmètre 2 | 5 j / 3 500 € | 5 j / 3 500 € | ✅ |
| Périmètre 3 | 36 j / 21 300 € | 36 j / 21 300 € | ✅ |
| Forfait global | 97 j / 64 000 € | 97 j / 64 000 € | ✅ |
| Jalonnement de facturation (19 200 + 12 800 + 12 800 + 3 500 + 9 600 + 6 100) | 64 000 € | 64 000 € | ✅ |
| TJM 700 € (conception) / 550 € (dev) | Utilisé cohérent | Confirmé | ✅ |

## Conclusion

- **Chiffres** : 100% cohérents, aucune correction nécessaire.
- **Mots interdits** : aucun résidu bloquant (Globasoft, IA, Engagement 1/2/3…).
- **À arbitrer avant export** : 3 noms propres + 2 mentions "atelier CISO".

**Question :** tu veux que j'applique les 5 remplacements proposés ci-dessus (noms → fonctions ; "atelier CISO" → "questions par mail" ou reformulation), ou je laisse en l'état pour le premier export Word ?
