---
tags: ["comptabilité", "odoo", "globasoft", "brief"]
created: 2026-06-25
---

# Fiche Comptable — Globasoft ESN

> Instance Odoo : `globasoft` (https://globasoft.odoo.com)

> ⚠️ **NE PAS CONFONDRE avec Guinet Digital Group (GDG)** : GDG était anciennement appelée Globasoft (avant août 2025), mais c'est une personne morale distincte. GDG est dans l'instance `guinet`. Voir [[Brief-Compta-GDG]].

---

## Identité

| Élément | Valeur |
|---|---|
| Raison sociale | GLOBASOFT (SAS) |
| SIREN | **990 641 235** |
| SIRET (siège) | 990 641 235 00017 |
| N° TVA intra | **FR81 990641235** |
| Détention | **50 % Guinet Group + 50 % ZM Consulting** |
| Adresse siège | 8 Place Roger Salengro, 31000 Toulouse |
| Activité | ESN |
| Régime TVA | TVA sur encaissements |

> Source : `res.company` / `res.partner` ID 1 instance `globasoft` (relevé 25/06/2026). Forme juridique **SAS** confirmée par facture SEDOMICILIER (« Globasoft SAS »).

> ⚠️ **Identification d'entité sur facture fournisseur** — la boîte mail `globasoft-perso` (guinet.benoit@globasoft.fr) est transversale et reçoit aussi les factures de GDG. Toujours vérifier le « Bill to » avant de comptabiliser :
> - **Globasoft ESN** : TVA **FR81990641235** · adresse **8 Place Roger Salengro**
> - **GDG** (instance `guinet`, à ne pas mettre ici) : TVA **FR95985298900** · adresse **6 Place du Président Wilson**
> - Fournisseurs récurrents qui sont en réalité GDG (vus juin 2026) : **Gandi, Miro, Vercel, Screencastify**.

---

## Instance Odoo

| Paramètre | Valeur |
|---|---|
| Clé MCP | `globasoft` |
| URL | https://globasoft.odoo.com |
| Journal achats | Vendor Bills |
| Compte fournisseurs | 401100 |

---

## Règles TVA achats (tous fournisseurs)

Globasoft ESN est en **TVA sur les encaissements**. Cette règle s'applique à **tous les fournisseurs** sans exception.

| Paramètre | Valeur |
|---|---|
| Taxe à utiliser sur toutes les lignes d'achat | **20% S** (ID **27**) |
| Compte TVA déductible généré | 445640 Deductible VAT on unsettled transactions |

---

## Mapping fournisseurs → comptes de charge

> Relevé de l'existant Odoo au 25/06/2026 (factures `in_invoice` postées). À réutiliser pour toute nouvelle facture du même fournisseur.

| Fournisseur | Compte | Nature |
|---|---|---|
| VP CONSEIL | **622600** Fees | Expert-comptable (cf. section dédiée) |
| RICAUD JUSTINE | **622602** Avocate | Honoraires avocat |
| GUICHARD ANNE GERALDINE THI-THAI | **622600** Fees | Honoraires |
| SEDOMICILIER SAS | **613200** Real property rental | Domiciliation |
| REVOLUT BANK, UAB | **627000** Comptes bancaires | Abonnement / frais compte pro |
| Render | **615600** Maintenance informatique | Hébergement infra |
| Mailgun Technologies | **615600** Maintenance informatique | Service emailing |
| Google Cloud France | **6135000** Location logiciels informatiques | Workspace / Cloud |
| Odoo S.A. | **6135000** Location logiciels informatiques | Abonnement ERP |
| Canva PTY LTD | **6135000** Location logiciels informatiques | SaaS design |
| Excalidraw s.r.o. | **6135000** Location logiciels informatiques | SaaS |
| Bytedance PTE (CapCut) | **6135000** Location logiciels informatiques | SaaS |
| SnackThis (Jitter) | **6135000** Location logiciels informatiques | SaaS |
| UP COOP | **437800** Tickets restaurants (valeur faciale) + **604000** Achats prestations (commission) | Titres-restaurant — 2 lignes |
| PREVALY | **647500** Médecine du travail, pharmacie | Médecine du travail |

> **Nuance 615600 vs 6135000** : les abonnements logiciels SaaS « classiques » (Google, Odoo, Canva, Excalidraw, CapCut, Jitter) vont en **6135000 Location logiciels informatiques** ; l'hébergement applicatif (Render) et le service emailing (Mailgun) sont historiquement en **615600 Maintenance informatique**. Conserver la cohérence par fournisseur.

> **Cas UP COOP (titres-restaurant)** : la facture se ventile en 2 lignes — la valeur faciale des titres en **437800** (compte de tiers, pas une charge) et la commission UP en **604000**.

---

## Cabinet comptable — VP CONSEIL

VP CONSEIL assure la comptabilité courante de Globasoft ESN (expertise comptable, assistance sociale, bulletins de paie stagiaires).

| Paramètre | Valeur |
|---|---|
| Partenaire Odoo | VP CONSEIL (ID **361**) |
| SIRET | 93392457300019 · TVA FR26933924573 |
| Compte de charge | 622600 Fees (ID **430**) |

### Règles de saisie des factures VP CONSEIL

1. **Date comptable = date de la facture** (pas la date d'échéance, pas aujourd'hui).
2. **Libellé de la ligne TVA** = `VP CONSEIL {numéro_facture}` (ex. `VP CONSEIL F-26060481`).
3. Joindre le PDF à la facture Odoo après création.

### Prestations récurrentes et montants

| Prestation | Compte | PU | Qté | Remise | HT | TTC |
|---|---|---|---|---|---|---|
| Consultation — validation écritures mensuelles | 622600 | 100 € | 1 | 50 % | 50,00 € | 60,00 € |
| Expertise comptable (exercice en cours) | 622600 | 196,47 € | 1 | 0 % | 196,47 € | 235,76 € |
| Assistance matière sociale (exercice en cours) | 622600 | 33,00 € | 1 | 0 % | 33,00 € | 39,60 € |

> ⚠️ **Bug affichage PDF (ancien format `F-YYMM####`)** : la ligne consultation affiche HT = 125 € dans le PDF (PU 250 × 0,5 unité × remise 60 % fictive). La TVA (10 €) et le TTC (60 €) font foi. Saisir PU = 100, qty = 1, discount = 50 %.

### Deux formats de numérotation VP CONSEIL

| Format | Exemple | Caractéristiques |
|---|---|---|
| Ancien | `F-YYMM####` (ex. `F-26060481`) | Un fichier par prestation — bug d'affichage des montants HT |
| Nouveau | `F-2026-XXXXX` (ex. `F-2026-06490`) | Un fichier peut regrouper plusieurs prestations — montants fiables |

### Relevé mensuel Revolut — réflexe à ne pas oublier

Chaque mois, **3 gestes** pour le compte Revolut principal (journal **BNK3 id 10**, `FR7628233000015895091681980`) :

1. **Créer le relevé Odoo** (`account.bank.statement`) : `name = Revolut-Main-2026-MM`, `journal_id = 10`, `date` = dernier jour du mois. Soldes **réels enchaînés** : `balance_start` = `balance_end_real` du mois précédent, `balance_end_real` = solde de clôture du PDF. Puis **rattacher les lignes du mois** (`account.bank.statement.line`, `statement_id` = id du relevé). Vérifier `balance_end == balance_end_real` et `is_complete = oui` → le mois est bouclé au centime.
2. **Attacher le PDF du relevé** sur ce même `account.bank.statement` (`attach_file_to_record`, res_model `account.bank.statement`). ⚠️ Jamais sur une facture fournisseur.
3. **Copier le PDF dans le Drive** : `H:\Mon Drive\Comptabilité Groupe\Globasoft ESN\<année>\Relevés Bancaires\<seq> - Revolut-Main-AAAA-MM.pdf` (la séquence suit les fichiers existants, ex. 9 = juin → 10 = juillet).

> Fait pour juillet 2026 : relevé id 10 (691,34 → 671,21, 32 lignes), PJ id 5903, Drive `10 - Revolut-Main-2026-07.pdf`.

### Rapprochement bancaire mensuel

- Libellé du prélèvement : `COMPTA+SOCIAL MENSUEL Vp Conseil`
- Montant habituel : **−335,36 €** (consultation 60 + expertise+social 275,36)
- Outil : `reconcile_bank_line` avec les IDs des lignes `account_type = liability_payable` (401100) des deux factures concernées.

---

## Ventes — clients, produits et comptes de produit

> Relevé de l'existant Odoo au 25/06/2026 (factures `out_invoice` postées). Journal **Customer Invoices**, compte clients **411100**.

### Comptes de produit (classe 70) selon la nature de la prestation

| Compte | Libellé | Usage observé |
|---|---|---|
| **706000** | Services supplied | Modules / prestations de services génériques |
| **706100** | Ventes de prestations de services - Projet | Forfaits projet, acomptes projet, recette |
| **706200** | Ventes de prestations de services - TMA | TMA au temps passé (régie) |
| **706300** | Ventes de prestations de services - AT | Assistance technique |
| **706400** | Ventes SaaS MCP IFS | Abonnement SaaS MCP IFS |
| **707000** | Sales of goods | Développement livré, garantie |

### Clients récurrents

| Client | Prestations typiques | Comptes |
|---|---|---|
| **ONE PINK** | Modules IFS, projets, AT, développement | 706000 / 706100 / 706300 / 707000 |
| **GA SAS** | TMA développement régie (60 €/h) | 706200 |

### Produits (catalogue `product.template`)

> La plupart des produits n'ont **pas** de compte de produit forcé (`property_account_income_id` vide) : le compte est choisi **sur la ligne de facture** selon la nature (table ci-dessus). Deux exceptions ont un compte câblé sur le produit.

| Produit | Prix catalogue | Compte de produit forcé |
|---|---|---|
| **Développement** (ID 25) | 60 €/h | — (mettre 706200 TMA ou 707000 selon contexte) |
| **MCP IFS — Abonnement annuel** (ID 37) | 3 000 € | **706400** Ventes SaaS MCP IFS |
| **MCP IFS — Essai 30 jours** (ID 36) | 0 € | **706400** Ventes SaaS MCP IFS |
| **Management de projet, qualité** (ID 5) | — | **706000** Services supplied |
| **Formation** (ID 15) | 2 250 € | — |
| Autres (Recette, Garantie 3 mois, Datawarehouse, Dashboards PowerBI, Extracteurs, modules IFS…) | variable | — (compte choisi sur la ligne) |

> Produit générique le plus utilisé : **Développement** (60 €/h) pour la régie/TMA → ligne en **706200**.




---

## Mises à jour octobre 2026 (clôture septembre)

### Appariement mensuel banque ↔ facture
- **Google Workspace** : facture datée du dernier jour du mois M, prélevée le **1er de M+1** (la ligne du 01/09 solde la facture d'**août**, pas celle de septembre). Vérifier qu'une facture n'est pas déjà soldée par la ligne du mois suivant avant d'apparier.
- **Revolut** : facture « Frais Revolut Business MM/AAAA » datée fin de mois, ligne « Company Pro plan fee » du 1er.
- **Anthropic** : 3 lignes par mois (01, 04, 30), une par personne (Kwanchanok NYTUPO4U, Guillaume MALZPKPN, Mahdi RROCON21). ⚠️ Les factures NYTUPO4U sont au nom de GDG (carte 7328) : question en cours avec l'expert-comptable.
- **Up Coop** : virement « To Groupe Up » le jour de la commande ; facture 437800 (valeur faciale) + commission.

### Lignes bancaires sans facture (ventilation, pas de lettrage)
Remplacer le compte d'attente 471000 par le compte de contrepartie, sans lettrer :
| Ligne | Compte |
|---|---|
| ASP — aide unique apprenti | **741000** Subventions d'exploitation |
| Urssaf | **431000** |
| Klesia | **4370300** |
| TVA DGFiP (`TVA1-MMAAAA…`) | **445510** TVA à décaisser |

### Refacturation Guinet Group → ESN (management / assistance / mission)
Facture GG (journal Customer Invoices, compte 706999) → côté ESN **facture fournisseur** tiers GUINET GROUP, `ref` = n° de la facture GG (ex. INV/2026/00006), lignes « Management fees - selon la convention signée », « Assistance administrative », « Prestation de mission » sur **604000** avec taxe **20 % S**. Lettrage du virement sur les deux instances (ESN 401100, GG 411100). Septembre 2026 : 9 300 € HT / 11 160 € TTC.

### Tickets restaurant / notes de frais scannés
- **Avant de classer un scan en carte 7328 (GDG)**, chercher montant + date dans les lignes ESN (Revolut) : Benoit paie parfois avec la carte ESN. Les libellés bancaires ≠ nom du ticket (« Le Cactus » = Madame Baudruche).
- Facture ESN : tiers = commerçant du ticket, `ref` « NDF <commerçant> AAAA-MM-JJ », lignes « Restaurant <X> - base TVA 10 % / 20 % » en **HT** sur **625700**, taxes **10 % G** (445660) et **20 % S** (445640), PJ = scan, lettrage sur la ligne Revolut.
- Drive : `globasoft` > `2026_notes_de_frais`, nom `AAAA-MM-JJ <MARCHAND> <date achat> <montant> EUR (Repas CB0681).pdf`.
- Cas du 04/10/2026 : Madame Baudruche 19/08 (44,80) et 18/09 (36,60), Barbaque 22/09 (80,00) → ESN ; la copie du 19/08 classée par erreur GDG/CB7328 le 12/09 est à supprimer à la main dans le Drive digital.

### Conventions Drive ESN
`2026_factures_fourn` : `fournisseur_AAAA-MM-JJ_réf.pdf` (vpconseil, google, stello, sedomicilier, upcoop…) + PJ sur la facture Odoo.



## Sous-traitance ZM Consulting et facturation en régie (09/10/2026)

**Factures ZM Consulting (Mahdi)** : numéros `04NN-MMYY`, envoyées à guinet.benoit@globasoft.fr.
- « Développeur Talend – <mois> » : jours × 480 € HT, sur CRA du mois.
- « Management fee – <mois> » : 2 000 € HT/mois, sans CRA (mars → sept. 2026 reçues le 08/10 : 0404-0326 à 0410-0926).
- Même n° parfois renvoyé avec une autre échéance → garder la dernière version (ex. 0402-0826 et 0403-0926 : échéance 07/12 au lieu du 23/10).

**Contrôle** : facture « Développeur » ↔ CRA signé client du même mois ↔ facture client du même mois ; pas de jour sur deux CRA ; total ≤ jours ouvrés ; TJ client ≥ TJ ZM.

| Mois 2026 | CRA client | ZM | Facture NESS |
|---|---|---|---|
| Juillet | 8 j, signé 31/07 | 0401-0726 (8 j) | FAC/2026/00018 (8 j) |
| Août | 9 j, signé 31/08 | 0402-0826 (9 j) | FAC/2026/00025 (9 j) |
| Septembre | **manquant** | 0403-0926 (10 j) | brouillon 10 j, en attente du CRA |

**TJ** : NESS 480 = ZM 480 (refacturation au coût). Abylsen 450 (contrat art. 4) < 480 → TJ ZM à convenir ≤ 450 avant facturation des jours Abylsen.

**Facture NESS** : depuis la commande S00030 (49 j × 480), produit de la ligne de commande « Développement (jour) » (706200), ligne liée + origine S00030, libellé « Développeur Talend », date fin de mois, réf `NESS_GLOBASOFT_AAAAMM_MZO`, 45 jours, Revolut, CRA signé en PJ ; mettre à jour la quantité livrée de la commande (27 j au 09/10/2026, reste 22). Août corrigé le 09/10 (était en « Assistance technique » 706300 hors commande ; remis en brouillon, corrigé, revalidé sous le même numéro).

**Abylsen STRA** (S00035, 77 j × 450, 02/09 → 31/12/2026, client final RADIALL) : autofacturation par Abylsen sur CRA validé (client + Abylsen) → ne pas émettre de facture, enregistrer celle reçue. CRA septembre reçu le 08/10 (13 j, 14 → 30/09) mais non signé. Paiement 30 j fin de mois le 10.



## Fiche synthèse Globasoft ESN (questionnaire du 12-15/10/2026)

Réponses données pour un questionnaire (chiffres Odoo au 15/10/2026, à réactualiser).

- **Identité (Kbis 17/05/2026)** : Globasoft, SAS, capital 1 000 € (500 GG + 500 ZM), RCS Toulouse 990 641 235, début d'activité 22/08/2025, immatriculation 29/08/2025, siège 8 place Roger Salengro 31000 Toulouse (domiciliation Hellodom), NAF 62.02A, Président Guinet Group, DG ZM Consulting. Kbis dans le Drive `globasoft` > juridique.
- **Assurance** : RC Pro AXA via Stello, contrat C-ST-6A4B76790A215, 12/07/2026 → 30/06/2027, 408,87 € TTC/an, CA déclaré 300 000 € (attestation à télécharger chez Stello).
- **CA facturé depuis la création** : 175 650 € HT (2025 : 20 000 € ; 2026 jan-sept : 155 650 €). GA 113 305 €, ONE PINK 54 185 €, NESS 8 160 €.
- **Répartition** : forfaits 36 100 €, régie / temps passé 74 970 €, TMA 44 580 €, logiciel IFS 20 000 €. ⚠️ Aerotec (68 650 €) avait été ajouté à tort au CA de l'ESN dans le questionnaire : la commande 3111 - C990001 est adressée à GDG (Globasoft SARL, 6 place Wilson) et facturée par GDG (20 % le 07/06/2025, 20 % le 02/04/2026, jalon de réalisation préparé le 18/10/2026). La commande S00006 de l'ESN n'est qu'une copie.
- **TMA Talend GA** : accord-cadre 01/01 → 31/12/2026 au consommé (NP1456/AP, puis C102602/AP, C106114/AP), 60 €/h (conception 70 €/h), 743 h facturées jan-sept (≈ 0,55 ETP), 44 580 € HT ; reste 281 h (16 860 €) jusqu'en décembre.
- **Forfaits livrés** : Extraction Nibelis (GA RH, 18 305 €, PV 26/06/2026, aucun temps saisi) ; Interfaces Talend/monitoring (ONE PINK, 15 795 €, PV 25/06/2026, 630 h pour 27 j vendus, marge ≈ 60 %). Aerotec (68 650 €, contrat GDG, pas ESN) en recette, ~1 an de retard.
- **Régie** : NESS (Mahdi, 480 €/j, 49 j dont 27 réalisés fin sept.), Abylsen (Mahdi, 450 €/j, 77 j, 02/09 → 31/12/2026, autofacturation), POP PINK SAS (terminé).
- **Marge brute estimée** ≈ 106 800 € (61 %) ; trésorerie 3 069 € au 04/10, 52 908 € avec les créances échues à mi-novembre ; aucun emprunt, aide apprenti 5 000 € perçus.
- **Délais de paiement** : ≈ 39 j en moyenne (GA 40 j, ONE PINK 36 j, NESS 45 j).
- **Trous de compta à combler** : paie non saisie depuis mai 2026, 9 factures ZM du 08/10 non saisies, 1 380 € mal classés en 130000.
