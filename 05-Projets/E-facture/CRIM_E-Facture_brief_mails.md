# Brief - Extraction mails : avancement des CRIM E-Facture (GA C1113)

## Contexte
Projet **E-Facture** (dematerialisation fiscale FR) du groupe GA. On suit **26 CRIM** (demandes d'evolution/parametrage) en 3 lots : L1 = Facturation **fournisseur** (e-invoicing), L2 = Facturation **client** (e-invoicing), L3 = Facturation **client** (e-reporting).
Chaque CRIM est suivi dans **Redmine projet POP** (issue #), parfois lie a un **ticket GLPI** (support.ga.fr).
Process de realisation : **Spec -> Dev -> Test RSI -> Recette -> PROD**. Environnements IFS : CFG, TRN, UAT, TST, PROD.
Acteurs : demandeur/AR **Justine Navarro** ; cote metier **Vincent Vigneaux, Elodie Bergeron, Laurence Beurrier (LAUBEU), JB Laisney, Kader, Frank** ; dev **Globasoft (TMA)** ; sous-traitant dev **BWS / BWorkshop** (jira bworkshop.atlassian.net, refs TEGSB-xxx). Editeur ERP **IFS** ; demat via **ESKER** ; ERP sources **IFS / INFOR** ; ETL **Talend**.

## Objectif
Parcourir MA boite mail et sortir, **pour chaque CRIM**, toute info d'avancement : statut reel, **dates** (spec validee, livraison dev, passage Test RSI, recette, MEP/prod), **chiffrages** (jours), **blocages / en attente de qui**, **decisions & validations**, et les echanges avec Globasoft / BWS / IFS / ESKER.

## Priorites (infos manquantes a trouver EN PREMIER)
1. **Date de livraison dev** pour **CRIM #8** (Redmine 20008 - SIRET client marche public) et **CRIM #25** (Redmine 20011 - Lobby factures preliminaires) : en dev sans date.
2. **Blocage BWS** sur **#24** (Redmine 19996) et **#29** (Redmine 19999) : quel retour BWS attendu, ETA ?
3. Les **P0 'valides' sans chiffrage et/ou date** (voir colonne 'A preciser' du tableau).
4. Confirmer **Test RSI 20/07** pour #16, #24, #28, #29 ; toute **date de MEP/prod**.

## Mots-cles de recherche
`e-facture` `e-invoicing` `e-reporting` `UBL` `dematerialisation` `25R2` `CRIM` `INT 187` `INT 188` `INT 222` `INT 185` `INT 251` `facture fournisseur` `facture preliminaire` `lisible facture` `referentiel fournisseurs` `SIRET` `marche public` `opportunite` `Globasoft` `BWorkshop` `BWS` `TEGSB` `ESKER` `INFOR` `IFS` `Talend` `gafr-uat` `gafr-trn` `Test RSI` `recette` `MEP`

## Format de restitution attendu (par CRIM)
Pour chaque CRIM cite le **n CRIM + n Redmine**, puis :
- **Avancement constate** (stade Spec/Dev/Test RSI/Recette/PROD)
- **Dates trouvees** : type -> date (+ source : date & expediteur du mail)
- **Blocage / en attente de** (qui, quoi)
- **Decisions / validations**
- **Citation courte** + reference du mail (date, objet, expediteur)
- Si rien : `aucune info`

## Tableau de reference des 26 CRIM
| CRIM | Redmine | GLPI | Lot | Stade | Objet | A preciser |
|------|---------|------|-----|-------|-------|------------|
| #14 | 19994 | 24386 | L1 fourn-invoicing | PROD | Ajuster la mise à disposition du référentiel fournisseurs | - |
| #16 | 19993 | 25884 | L1 fourn-invoicing | Dev | Mise à disposition des factures fournisseurs "e-invoicing" d | - |
| #18 | 20002 | - | L1 fourn-invoicing | Spec | Mise à disposition d’ESKER le cycle de vie de la facture fou | - |
| #20 | 20003 | - | L1 fourn-invoicing | Spec | Fiche « fournisseur » - Automatiser la définition d’une fich | - |
| #21 | 20004 | - | L1 fourn-invoicing | Spec | Fiche « fournisseur », rendre obligatoire la saisie de « id  | - |
| #22 | 19995 | - | L1 fourn-invoicing | Spec | Interdire le rejet technique de la facture fournisseur à par | date livraison |
| #23 | 20005 | - | L1 fourn-invoicing | Spec | Automatiser l’envoi des factures électroniques à l'imputatio | - |
| #24 | 19996 | - | L1 fourn-invoicing | Dev | Gestion des lisibles factures fournisseurs dans le cadre des | blocage BWS - ETA, chiffrage |
| #026 | 19997 | - | L1 fourn-invoicing | Spec | Personnaliser le bon de commande (Edition Armony) pour  enle | date livraison |
| #028 | 19998 | 25936 | L1 fourn-invoicing | Dev | Mise à disposition des factures fournisseurs "e-invoicing" d | chiffrage |
| #29 | 19999 | - | L1 fourn-invoicing | Dev | Gestion des lisibles factures fournisseurs dans le cadre des | blocage BWS - ETA, chiffrage |
| #30 | 20000 | - | L1 fourn-invoicing | PROD | Changer l'encodage du fichier .csv ref fournisseur IFS > ESK | - |
| #31 | 20001 | - | L1 fourn-invoicing | PROD | Changer l'encodage du fichier .csv ref fournisseur INFOR > E | - |
| #32 | 20006 | - | L1 fourn-invoicing | Spec | Automatiser le fait d’annuler après un refus de facture | - |
| #1 | 20007 | 25365 | L2 client-invoicing | Spec | Mise à disposition des factures au format UBL pour les clien | date livraison |
| #5 | 20013 | - | L2 client-invoicing | Spec | Fiche « client » - Automatiser la définition d’une fiche cli | - |
| #6 | 20014 | - | L2 client-invoicing | Spec | Fiche « Client », rendre obligatoire la saisie de « id adres | - |
| #7 | 20015 | - | L2 client-invoicing | Spec | Fiche « Société », rendre obligatoire la saisie de « id adre | - |
| #8 | 20008 | - | L2 client-invoicing | Dev | Fiche « Client », rendre obligatoire la saisie du « SIRET »  | date livraison, date livraison dev |
| #9 | 20009 | - | L2 client-invoicing | Spec | Intégrer l’édition de la facture pdf au titre d’une pièce at | - |
| #10 | 20010 | - | L2 client-invoicing | Spec | Intégrer l’édition de la facture pdf au titre d’une pièce at | - |
| #12 | 20016 | - | L2 client-invoicing | Spec | Personnalisation pour saisir et automatiser sur les factures | - |
| #25 | 20011 | - | L2 client-invoicing | Dev | Lobby pour valider les factures préliminaires des factures | date livraison, date livraison dev |
| #27 | 20012 | - | L2 client-invoicing | Spec | Récupérer les PJ additionnelles (hors lisible facture qui se | chiffrage, date livraison |
| #2 | 20017 | - | L3 client-reporting | Spec | Mise à disposition des factures éligibles à la dématérialisa | date livraison |
| #3 | 20018 | 25369 | L3 client-reporting | Spec | Mise à disposition vers ESKER du e-reporting de transactions | - |
