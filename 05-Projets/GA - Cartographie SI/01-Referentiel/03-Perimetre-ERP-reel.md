---
titre: Périmètre ERP réel — le référentiel décrit un SI d'avant le lot 4
statut: corrections à porter
date: 2026-08-18
source: connaissance terrain (Benoît Guinet), contre les 3 sources documentaires
tags: [ifs, perimetre, lot4, referentiel, obsolescence]
---

# Le référentiel décrit un SI d'avant le lot 4

## Le problème, et pourquoi il est invisible

**Trois sources décrivent le même SI périmé, et se confortent mutuellement :**

| Source | Ce qu'elle dit | Réalité |
|---|---|---|
| `INVENTAIRE` onglet **APPS** | `Achats` et `IBAT` en « fin de vie » | **décommissionnées, n'existent plus** |
| `INVENTAIRE` onglet **Modules IFS** | `PURCH` et `RCEIPT` = LOT4 `<A venir>` | **en service** |
| `Présentation du SI vMASTER.pptx` slide 11 | « Modules LOT4 (à venir) · Achat (PURCH) • Réception (RCEIPT)… » | **en service** |

Aucune contradiction interne ne signale l'erreur. C'est ce qui la rend dangereuse : un lecteur
qui recoupe les trois sources en sort **conforté dans le faux**. Seule la connaissance terrain
permet de la détecter.

> C'est le même mécanisme que pour les flux (cf. [[01-Referentiel/02-Reconciliation-Talend-PROD]]) : le
> référentiel n'est pas incohérent, il est **en retard**. Sa fraîcheur n'est mesurée nulle part.

## La vérité au 18/08/2026

- **Lots 1 et 4 en service.** Finance (compta générale et analytique, facturation, paiements,
  immobilisations, projet, taxe) **et** Achats (commandes, réceptions, workflow facture
  fournisseur, sous-contrats).
- **Lot 5 à venir** : chantiers et usines. Le cœur « chantiers et usines à venir » des cartos
  était donc juste.
- **Ancienne chaîne facture fournisseur entièrement basculée** : `ZyScan → PROGIDOC → Compta`
  ne traite plus de factures.

## Conséquences en cascade sur le référentiel des flux

Passer 2 applications en décommissionné entraîne mécaniquement la mort de leurs flux :

| Cause | Flux à passer en « Décommissionné » |
|---|---|
| `Achats` n'existe plus | `INT-008` · `INT-009` · `INT-010` · `INT-011` · `INT-024` · `INT-035` · `INT-053` · `INT-074` · `INT-124` · `INT-141` · `INT-173` |
| `IBAT` n'existe plus | (aucun flux vivant recensé) |
| Ancienne chaîne basculée | `INT-139` · `INT-171` · `INT-172` · `INT-174` · `INT-176` (+ `INT-173` déjà compté) |

**16 flux distincts** au total, dont `INT-008-Achats-InfoLégal` qui était encore déclaré **Actif**.

### Impact sur les compteurs publiés

| Indicateur | Avant | Après |
|---|---:|---:|
| Flux vivants | 132 | **116** |
| Flux actifs | 67 | **66** |
| `Compta` au classement des applications les plus connectées | 21 flux (2ᵉ) | **15 flux (3ᵉ)** |

`Compta` perd sa deuxième place : c'est la mesure de ce que la bascule a réellement retiré du SI.

## À porter dans l'Excel

- [ ] Déplacer `Achats` et `IBAT` vers l'onglet **APPS décommissionnées** (le compteur de 150 est
      surévalué d'autant, et probablement de plus)
- [ ] Passer les **16 flux** ci-dessus en « Décommissionné »
- [ ] Corriger l'onglet **Modules IFS** : `PURCH`, `RCEIPT`, `SINWOF`, `SUBCON`, `SHPMNT` ne sont
      plus `<A venir>`
- [ ] Corriger la **slide 11** du vMASTER : « Modules LOT4 (à venir) » → en service
- [ ] Vérifier le reste de la liste « fin de vie » : `DevisNomenclatures`, `ProjetCommercial`,
      `Factory PF`, `PAQ`, `MyGapéo`, `Annuaire Accueil` sont-ils réellement encore là ?

## La recommandation de fond

Ajouter à l'inventaire une colonne **`Dernière vérification`** (date + qui), au moins sur le
statut. Une donnée sans date de fraîcheur est indistinguable d'une donnée fausse — et c'est
exactement ce qui s'est produit ici. Sans elle, chaque carto reproduira l'état du SI au jour où
quelqu'un a rempli la case, sans que personne ne sache quel jour c'était.

## Corrections portées dans les artefacts

Les trois pages appliquent désormais un **calque de corrections** au-dessus du référentiel, dans
`payload.py` : `CORRECTIONS` (statuts et Talend), `APPS_MORTES` et `LEGACY_P2P`. Le calque est
signalé au lecteur — bandeau sur la page P2P, encadré « statuts corrigés au réel » sur la page
DSI. Il disparaîtra quand l'Excel sera à jour.
