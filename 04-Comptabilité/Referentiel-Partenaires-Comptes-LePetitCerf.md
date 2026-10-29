---
tags: ["comptabilité", "le-petit-cerf", "référentiel", "partenaires"]
created: 2026-09-10
---

# Référentiel Marchand → Compte — Le Petit Cerf (company_id=7)

> **Source** : dérivé de l'historique réel des écritures `posted` LPC (2025→2026), pas d'invention.
> **Usage** : compte par défaut pour ventiler un paiement bancaire / une facture d'un marchand connu.
> Instance `guinet`, société co7. Journaux : Bank (BQ1, id 37) + CB « Stripe » (BNK2, id 51, compte 580002 CB BP Différé).

## Mapping confirmé par l'historique

| Compte | id | Marchands / tiers |
|---|---|---|
| **601100** Achats matières & fournitures | — | Amazon (Amazon Payments/Business, Changting/Guangzhou via Amazon), Sticker Mule, **Ecardify** (ECARDIFY.IO), **Etsy — achats** (Etsy.com*…), Midica, Monoprix, Copy Top, Commande Vincennes |
| **607100** Achats de marchandises (revente) | — | **Glamsten AB** (skincare coréen : Biodance, Medicube, Torriden, Dr Althea, d'Alba, SKIN1004, Celimax, Numbuzin, Haruharu, Medi-Peel…), **Alipay / AliExpress**, **Eleven Labs** (classé 607 dans l'histo — atypique pour un SaaS) |
| **613200** Location immobilière | — | Digidom (domiciliation, libellé « KOAH ») |
| **62260000** Honoraires | — | VP Conseil (expertise, honoraires, frais rejet, missions juridiques), PGPS (paie / bulletins) |
| **62700000** Frais bancaires | 3129 | **Tous frais BPO** : COMMISSION FACTURETTE CB, FRAIS COM INTERVENTION, ARRÊTÉ DE COMPTE, **COTIS RYTHMEO PRO** (abon CyberPlus + Securipro + Visa Business + forfait), COTIS E-CB PRO, FRAIS BILAN NON REMIS. → justifiés par les « **Facture pro** » mensuelles BPO. (Compte existait mais jamais utilisé jusqu'au 10/09/2026.) |

## Points de mécanique
- **Carte à débit différé** : l'agrégat mensuel « CARTE FACTURETTES CB » (compte banque) a sa contrepartie sur **580002 CB BP Différé (id 3147)** ; il se solde contre le **détail carte** (journal CB). ≠ frais bancaires.
- Frais BPO = **non soumis à TVA** (prestations bancaires).

## À confirmer (aucun historique — ne pas deviner)
- **CapCut** (SaaS montage vidéo) → compte ?
- **QUDO STORE / QUDOBEAUTY** (fournisseur beauté RO) → probable **607100** par analogie Glamsten, à valider.
- **Etsy*Monthly Bi** (abonnement vendeur Etsy, ≠ achats Etsy) → compte ? (601100 comme les achats Etsy, ou un compte commissions/services ?)

## Liens
- [[Brief-Compta-LePetitCerf]] · référentiel jumeau GDG : [[Referentiel-Partenaires-Comptes-GDG]]




## MàJ 2026-09-10 — 3 comptes tranchés
- **Etsy*Monthly Bi** (abonnement vendeur) → **601100** (comme les achats Etsy).
- **CapCut** (SaaS) → **651100** Redevances licences/logiciels (id 2187) — « comme les logiciels ».
- **QUDO STORE / QUDOBEAUTY** → **607100** (revente beauté, analogie Glamsten).
Référentiel désormais complet pour la ventilation LPC 2026.