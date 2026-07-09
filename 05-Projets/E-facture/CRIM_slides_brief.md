# Données pour 2 slides PowerPoint — CRIM E-Facture (GA C1113)

> 26 CRIM actifs. « nb jours » = charge en jours. Spec = spécification · Dev = réalisation.  
> **Non chiffrés = CRIM sans chiffrage dev (Charge Réal vide).**

## Consigne pour Claude PowerPoint

Crée **2 slides** à partir des données ci-dessous.

**Slide 1 — « E-Facture : vue d'ensemble des CRIM »** : bandeau KPI (26 CRIM · 17 P0 / 9 P1 · 97 j dev · **9 non chiffrés**) ; un tableau/graphe **par lot** et un **par type** avec, pour chacun, nb CRIM (P0/P1), **nb jours dev** et **nb non chiffrés**. Faire ressortir la charge (Interfaces) et le reste à chiffrer.

**Slide 2 — « E-Facture : focus P0 par lot »** : 3 colonnes = 3 lots ; une carte par CRIM P0 avec pastille de stade 🟢 PROD (date MEP) / 🔵 Dev (date = Test RSI) / 🟠 Spec (date à obtenir). Échéances GoLive : L1 → 01/09, L2 → 20/09, L3 → 10/10.

## SLIDE 1 — Vue d'ensemble (tous CRIM)

**Total : 26 CRIM** — 17 P0 / 9 P1 · 97 j dev · 8,25 j spec · **9 non chiffrés (dev)**.

### Par lot
| Lot | CRIM | P0 | P1 | Jours dev | Jours spec | **Non chiffrés** |
|---|---|---|---|---|---|---|
| L1 Fourn-invoicing | 14 | 9 | 5 | 18.5 | 2 | 5 |
| L2 Client-invoicing | 10 | 6 | 4 | 33.5 | 4.75 | 4 |
| L3 Client-reporting | 2 | 2 | 0 | 45 | 1.5 | 0 |

### Par type
| Type | CRIM | P0 | P1 | Jours dev | Jours spec | **Non chiffrés** |
|---|---|---|---|---|---|---|
| Interfaces | 13 | 12 | 1 | 87.5 | 5.5 | 1 |
| Events / BPA | 10 | 2 | 8 | 4 | 1.5 | 8 |
| Droit | 1 | 1 | 0 | 0.5 | 0.5 | 0 |
| Lobbies / BR | 1 | 1 | 0 | 1 | 0.75 | 0 |
| Edition | 1 | 1 | 0 | 4 | 0 | 0 |

## SLIDE 2 — Focus P0 par lot (situation)

### L1 Fourn-invoicing — 9 P0
| CRIM | Redmine | Stade | Date | Dev (j) | Objet |
|---|---|---|---|---|---|
| #14 | 19994 | PROD | 4/07 | 1.5 | Ajuster la mise à disposition du référentiel f |
| #30 | 20000 | PROD | 4/07 | 0.5 | Changer l'encodage du fichier .csv ref fournis |
| #31 | 20001 | PROD | 1/07 | 0.5 | Changer l'encodage du fichier .csv ref fournis |
| #16 | 19993 | Dev | 20/07 | 1.5 | Mise à disposition des factures fournisseurs " |
| #24 | 19996 | Dev | 20/07 | 6 | Gestion des lisibles factures fournisseurs dan |
| #028 | 19998 | Dev | 20/07 | 1 | Mise à disposition des factures fournisseurs " |
| #29 | 19999 | Dev | 20/07 | 3 | Gestion des lisibles factures fournisseurs dan |
| #22 | 19995 | Spec | date ? | 0.5 | Interdire le rejet technique de la facture fou |
| #026 | 19997 | Spec | date ? | 4 | Personnaliser le bon de commande (Edition Armo |

### L2 Client-invoicing — 6 P0
| CRIM | Redmine | Stade | Date | Dev (j) | Objet |
|---|---|---|---|---|---|
| #1 | 20007 | Spec | date ? | 22.5 | Mise à disposition des factures au format UBL  |
| #8 | 20008 | Spec | date ? | 1 | Fiche « Client », rendre obligatoire la saisie |
| #9 | 20009 | Spec | date ? | 3 | Intégrer l’édition de la facture pdf au titre  |
| #10 | 20010 | Spec | date ? | non chiffré | Intégrer l’édition de la facture pdf au titre  |
| #25 | 20011 | Spec | date ? | 1 | Lobby pour valider les factures préliminaires  |
| #27 | 20012 | Spec | date ? | 3 | Récupérer les PJ additionnelles (hors lisible  |

### L3 Client-reporting — 2 P0
| CRIM | Redmine | Stade | Date | Dev (j) | Objet |
|---|---|---|---|---|---|
| #2 | 20017 | Spec | date ? | 22.5 | Mise à disposition des factures éligibles à la |
| #3 | 20018 | Spec | date ? | 22.5 | Mise à disposition vers ESKER du e-reporting d |
