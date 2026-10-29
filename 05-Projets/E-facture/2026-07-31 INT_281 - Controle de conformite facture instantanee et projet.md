---
tags: ["e-facture", "INT_281", "IFS", "Esker", "UBL", "conformite"]
created: 2026-07-31
---

# INT_281 — Contrôle de conformité, facture instantanée et facture projet

**Date :** 31 juillet 2026
**Référentiels :** `C1113 - GA - Flux AR E-invoice - Facture UBL client _VF (1).docx` et `EFACT - GA - Mapping UBL.xlsx` (onglet *E-Invoicing - GA*)
**Périmètre :** job `INT_281_main`, projet `IFS_FINANCE`

## Conditions du test

Les deux factures ont été rejouées sur **le même build**, après rechargement du Studio, sur le banc local (SFTP paramiko sur `127.0.0.1:2222`, base de monitoring PostgreSQL locale). C'est un point important : un premier passage avait été fait sur un code généré obsolète, ses résultats ont été écartés.

| | Facture instantanée | Facture projet |
|---|---|---|
| Source | `O2C_IFS_eInvoicing_II08400217_20260723_095408_UTC.xml` | `O2C_IFS_eInvoicing_PJ50000088_20260630_174523_UTC.xml` |
| Numéro | `II08400217` | `PJ50000088` |
| Sortie | 457 889 o | 384 320 o |
| Heure | 17:25 | 17:26 |
| Chaîne du lisible | `ReprintInvoice` → `PrintDialog` | `AfpInvoiceSet` → `VirtualOrderReports` → `PrintDialog` |
| Nom du lisible | `FACTURE_62599.pdf` | `SITUATION_PJ50000088.pdf` |

Le code généré exécuté (`INT_281_main.java`, 17:24:28) a été vérifié : il contient bien la bifurcation et la correction du nom de pièce jointe.

## Synthèse

**La partie commune du flux est conforme sur les deux branches.** Les 8 règles de gestion GA sont appliquées à l'identique, et 43 des 45 champs obligatoires EN16931 testables sont servis dans les deux fichiers.

**Un défaut fonctionnel réel a été trouvé : la note `#BAR#` est inversée.** Il touche les deux branches indifféremment.

Les autres écarts se répartissent en trois familles : ce qui vient d'IFS et que le flux recopie fidèlement, ce qui reste à arbitrer avec la MOA, et ce que le jeu de test n'a pas pu couvrir.

## 1. Les 8 règles de gestion GA

| # | Règle | Instantanée | Projet |
|---|---|---|---|
| 1 | Namespaces IFS remplacés par OASIS | ✅ aucun `urn:ifs` résiduel | ✅ |
| 2 | `CustomizationID` = `urn:cen.eu:en16931:2017` | ✅ | ✅ |
| 3 | Note `#AAB#` en dur | ✅ 1 occurrence | ✅ |
| 4 | `ClassifiedTaxCategory/cbc:ID` (BT-151) repris de `TaxSubtotal` | ✅ `E` = `E` | ✅ `S` = `S` |
| 5 | `schemeID="0225"` sur les deux `EndpointID` | ✅ vendeur et acheteur | ✅ |
| 6 | Unités PCS→C62, m→MTR, kg→KGM | ✅ `C62` | ✅ `C62` |
| 7 | `mimeCode` `pdf` → `application/pdf` | ✅ sur les 2 pièces jointes | ✅ |
| 8 | Note `#BAR#` avec le profil client | ⚠️ présente mais **valeur fausse** | ⚠️ idem |

Les quatre notes sortent dans l'ordre attendu sur les deux fichiers : `#PMD#`, `#PMT#`, `#BAR#`, `#AAB#`.

## 2. Champs obligatoires EN16931

Le mapping compte 242 lignes BT, dont 57 marquées obligatoires. 45 d'entre elles portent un XPath `/Invoice` exploitable automatiquement — les autres sont en `N/A`, ou portent une règle de gestion textuelle plutôt qu'un chemin.

**43 sur 45 sont servies dans les deux fichiers.** Les deux restantes sont en cardinalité `0..1`, donc conditionnelles :

- **BT-33** — `PartyLegalEntity/cbc:CompanyLegalForm`, forme juridique et capital social. Absent des deux. À confirmer avec la MOA : la mention est obligatoire sur les factures des sociétés commerciales françaises.
- **BT-149** — `Price/cbc:BaseQuantity`, quantité de base du prix. Absent des deux. Sans objet ici, le prix étant unitaire.

En-têtes contrôlés et conformes sur les deux : `UBLVersionID` 2.1, `ProfileID` S1, `InvoiceTypeCode` 380, `DocumentCurrencyCode` EUR, `IssueDate`/`DueDate` cohérentes, `PaymentMeansCode` 30.

Cohérence arithmétique vérifiée :

- Instantanée — 200 HT, TVA exonérée (`E`, 0 %), 200 à payer.
- Projet — 1 000 HT, TVA 20 % (`S`), 200 de TVA, 1 200 à payer.

## 3. La bifurcation du lisible (tâche 874)

L'architecture demandée est en place et vérifiée sur les deux passages : tronc commun pour les modifications de balises et les pièces jointes, bifurcation uniquement sur la récupération du lisible.

- La facture instantanée passe par `ReprintInvoice`, la trace le confirme, et le lisible sort sous `FACTURE_62599.pdf`. **Aucune régression** : c'est le comportement d'avant la modification.
- La facture projet ne passe pas par `ReprintInvoice`. Elle récupère son jeton via `AfpInvoiceSet` puis `VirtualOrderReports`, et le lisible sort sous `SITUATION_PJ50000088.pdf`, avec le bon PDF de situation.

Le point de convergence (`tJavaRow_8`) protège le jeton AFP : si la branche projet a produit un jeton, `ReprintInvoice` ne peut plus l'écraser. C'est ce qui garantit qu'une facture projet ne repart pas avec le lisible d'une facture instantanée.

## 4. Écarts constatés

### 4.1 Défaut de développement — note `#BAR#` inversée

**C'est le point bloquant de ce contrôle.**

La spécification (p. 276-305) définit :

| Coche B2B | Code pays | Résultat attendu |
|---|---|---|
| Coché | FR | B2B FR |
| Coché | ≠ FR | B2B INT |
| Non coché | FR ou ≠ FR | B2C |

L'expression du `tXMLMap` fait l'inverse :

```java
"true".equalsIgnoreCase(row17.B2bCustomer) ? "#BAR#B2C"
: "UBL-FR".equals(row18.EinvoiceProcessType) ? "#BAR#B2B"
: !"FR".equals(row17.Country) ? "#BAR#B2BINT"
: null
```

Un client coché B2B produit `#BAR#B2C`. C'est ce qui s'est passé sur les deux factures : le destinataire est **STELLANTIS AUTO**, une société, et les deux fichiers sortent `#BAR#B2C`.

Trois défauts distincts dans cette seule expression :

1. **La condition est inversée.** `B2bCustomer = true` doit donner B2B, pas B2C.
2. **Le test pays est mal placé et ne peut pas fonctionner.** La spécification l'applique à l'intérieur du cas « coché » pour distinguer B2B FR de B2B INT ; ici il est dans la branche « non coché ». Et surtout, `row17.Country` vaut `FRFRANCE` — la concaténation du code et du libellé — donc `"FR".equals(Country)` est toujours faux.
3. **La branche `null`.** Si aucune condition ne tombe, aucune note `#BAR#` n'est émise, alors que la spécification la rend obligatoire.

Sont par ailleurs non implémentés : la lecture préalable du champ de la facture pouvant valoir `ARCHIVEONLY` ou `OUTOFSCOPE`, qui doit primer sur la fiche client.

**Point de forme à trancher :** la spécification écrit `<cbc:Note>#BAR#B2B#BAR#</cbc:Note>`, avec un marqueur de fermeture. Le flux produit `#BAR#B2C`, sans. Les trois autres notes (`#PMD#`, `#PMT#`, `#AAB#`) n'ont qu'un marqueur d'ouverture. À confirmer auprès d'Esker avant de corriger.

### 4.2 Écarts provenant d'IFS, recopiés fidèlement

Ceux-ci ne sont pas des défauts du flux. Comparaison faite entre le fichier source et le fichier de sortie, à l'identique dans les deux cas.

- **Facture projet, IBAN absent.** `PaymentMeansCode` vaut 30 (virement) mais il n'y a aucun `PayeeFinancialAccount`. La règle EN16931 **BR-50** impose un identifiant de compte dès lors que le virement est utilisé. La source IFS ne le fournit pas. La facture instantanée, elle, porte bien `FR8830002040240000062322F09` et le BIC `CRLYFRPP`. **Le fichier projet est donc rejetable en l'état par la plateforme.** À remonter côté IFS.
- **Facture projet, `BuyerReference` absent.** Absent de la source également.
- **Facture instantanée, `BuyerReference` = `RÉFÉRENCE CLIENT`.** La valeur littérale est présente telle quelle dans le fichier IFS. Cela ressemble à un libellé de champ non substitué plutôt qu'à une référence réelle. À faire confirmer.

### 4.3 Points à arbitrer

- **`cac:PartyName` absent du vendeur et de l'acheteur.** Il n'est présent que sur `cac:Delivery` (`STELLANTIS AUTO`). Le nom légal est bien porté par `PartyLegalEntity/cbc:RegistrationName` sur les deux parties, ce qui satisfait BT-27 et BT-44. À confirmer selon ce qu'Esker attend réellement.
- **Fiche 883 — le bloc `schemeID="0009"` est toujours présent.** Vérification faite : côté fournisseur, `PartyIdentification/ID = 42826603500123` avec `schemeID="0009"` est bien dans les deux fichiers. La modification ERR-027 ne l'a donc pas supprimé, contrairement à ce que je craignais. Le point est levé.
- **Structure ERR-027 conforme.** Côté acheteur, les deux `PartyIdentification` attendus sont là : le code client `102471` sans `schemeID`, et le SIREN `542065479` en `schemeID="0002"`. `SupplierAssignedAccountID` n'est plus alimenté.
- **Facture projet sans pièce jointe `ACD`.** Le fichier projet ne porte que le lisible (`ATS`), l'instantanée en porte deux (`ATS` + `ACD`). C'est conforme aux sources : la facture projet n'a pas de pièce jointe IFS. Comportement normal, mais non testé sur une facture projet qui en aurait une.

## 5. Ce que ce test ne couvre pas

À dire explicitement, pour ne pas surinterpréter le résultat.

- **Un seul client sur les deux factures** (STELLANTIS AUTO, français). Les chemins B2B, B2BINT, OUTOFSCOPE et ARCHIVEONLY de la règle `#BAR#` n'ont pas pu être exercés — et vu le défaut identifié, ils sont de toute façon à retester après correction.
- **Une seule ligne de facture par document.** Le comportement multi-lignes, notamment sur les unités et les catégories de TVA, n'est pas validé.
- **Deux catégories de TVA sur cinq** : `E` (exonéré) et `S` (taux normal).
- **Une seule unité** : `C62`. Les conversions `m`→`MTR` et `kg`→`KGM` sont dans le code mais non exercées.
- **Aucun avoir.** `INT_281` ne traite pas les `CreditNote` — c'est un sujet ouvert, distinct.
- **Le multi-fichier n'est pas testé** (fiche 881), un seul fichier était déposé à chaque passage.
- **Le contrôle est structurel, pas normatif.** Il vérifie la présence et la valeur des champs, pas la validation par un schematron EN16931. Une validation officielle reste à faire.

## Suite à donner

1. **Corriger la règle `#BAR#`** — inversion, place du test pays, normalisation de `Country` qui vaut `FRFRANCE`, branche `null`, et prise en compte de `ARCHIVEONLY`/`OUTOFSCOPE`. Faire trancher au préalable le marqueur de fermeture.
2. **Remonter à IFS l'absence d'IBAN sur les factures projet** — rejet probable par la plateforme.
3. Faire confirmer BT-33, `cac:PartyName` et le `BuyerReference` littéral.
4. Rejouer le contrôle avec un client B2B et une facture multi-lignes.

---

**Rappel technique :** le dépôt est en état bascule locale (10 valeurs modifiées dans `sftp_ga_ifs_0.1.item`, `DB_MNTR_0.1.item` et `INT_281_main_0.1.item`). Lancer `bascule.ps1 -Restaure` **avant tout commit**.



---

# Annexe — Essai multi-fichiers (fiche 881)

**Date :** 31 juillet 2026, même build que le contrôle ci-dessus.

## Protocole

Quatre factures déposées d'un coup dans `AR-Einvoicing`, deux de chaque type, l'avoir `PJ50000087` volontairement écarté pour ne pas brouiller la lecture :

| Fichier | Type | Taille source |
|---|---|---|
| `O2C_IFS_eInvoicing_II08400003_...` | instantanée | 104 325 o |
| `O2C_IFS_eInvoicing_II08400217_...` | instantanée | 81 413 o |
| `O2C_IFS_eInvoicing_PJ50000088_...` | projet | 78 512 o |
| `O2C_IFS_eInvoicing_PJ50000089_...` | projet | 81 224 o |

L'ordre alphabétique fait passer les instantanées avant les projet.

## Résultat : le traitement multi-fichiers ne fonctionne pas

**Un seul fichier sur quatre a été livré**, et c'est le dernier de la liste. Les trois autres sont restés dans le répertoire d'arrivée, intacts, sans message d'erreur.

État du SFTP après exécution :

```
AR-Einvoicing/II08400003...xml        ← non traité, toujours là
AR-Einvoicing/II08400217...xml        ← non traité, toujours là
AR-Einvoicing/PJ50000088...xml        ← non traité, toujours là
AR-Einvoicing/Archive_Original/PJ50000089...xml
AR-Einvoicing/Archive_Transfo/PJ50000089..._.xml
In_Invoices/PJ50000089..._.xml
```

**Et le fichier livré porte le lisible d'une autre facture.** `PJ50000089` est parti avec `FACTURE_62599.pdf` — le PDF de la facture instantanée `II08400217`, identifié par comparaison :

| Fichier | Nom du lisible | Taille base64 |
|---|---|---|
| `PJ50000089` livré dans le lot de 4 | `FACTURE_62599.pdf` | 378 080 |
| `II08400217` en passage unitaire | `FACTURE_62599.pdf` | 378 080 |
| `PJ50000088` en passage unitaire | `SITUATION_PJ50000088.pdf` | 376 756 |

Une facture de situation est donc partie chez Esker avec le PDF d'une facture instantanée, **sans la moindre erreur pour le signaler**. C'est exactement le scénario que la bifurcation de la tâche 874 visait à empêcher — sauf qu'ici la fuite passe par une variable qui n'avait pas été identifiée.

## Trois causes distinctes

### 1. `context.PDF_IFS_InvoiceId` n'est pas remis à zéro entre deux fichiers

`tJava_3`, exécuté à chaque itération, remet bien à zéro `PDF_IFS_AFP_ResultKey`, `PDF_IFS_ResultKey`, `PDF_LISIBLE_*`, `FACTURE_FINALE_DOM`, `PROCHAIN_ID_PJ` et `ATTACHMENT_ID`. **Mais pas `PDF_IFS_InvoiceId`.**

Cette variable est posée par `tJavaRow_5`, sur la branche instantanée uniquement, et relue par `tJavaRow_6` pour construire le nom du lisible :

```java
(context.PDF_IFS_InvoiceId != null && !context.PDF_IFS_InvoiceId.trim().isEmpty()
    ? "FACTURE_" + context.PDF_IFS_InvoiceId
    : "SITUATION_" + context.InvoiceId) + ".pdf"
```

Une facture projet traitée après une instantanée hérite donc de l'identifiant de cette dernière, choisit la branche `FACTURE_`, et `tJavaRow_6` relit sur disque le PDF laissé par l'itération précédente sous ce nom. Le lisible est remplacé silencieusement.

**Correction :** ajouter `context.PDF_IFS_InvoiceId = "";` dans `tJava_3`, aux côtés des autres remises à zéro. Une ligne.

Il faut noter que le ternaire, introduit pour corriger le `FACTURE_.pdf`, est ce qui rend la fuite silencieuse : sans lui le nom serait resté vide et l'anomalie aurait sauté aux yeux. La correction est bonne, c'est la remise à zéro qui manquait.

### 2. La livraison et l'archivage sont hors de la boucle

Structure constatée dans le job :

```
tFileList_1 --ITERATE--> tJava_3 --OnComponentOk--> tFileInputXML_1 --OnSubjobOk--> tRunJob_15 --> …
tRunJob_5 --OnSubjobOk--> tJava_4 --OnSubjobOk--> tRunJob_2 --> tRunJob_3 --> tRunJob_14 --> tRunJob_4
```

La seconde chaîne — envoi Esker, archivage de l'original, archivage du transformé — ne descend pas de `tFileList_1`. Elle constitue un sous-job racine indépendant, qui s'exécute **une seule fois**, après la boucle, avec l'état laissé par la dernière itération.

C'est cohérent avec l'observation : un seul fichier livré, un seul archivé, et c'est le dernier de la liste.

**Correction :** c'est la restructuration de la fiche 881. La livraison et l'archivage doivent être rattachés à l'itération, pas au job.

### 3. Aucune erreur remontée sur les fichiers non traités

Trois fichiers sont restés en place sans traitement, sans rejet, sans trace. En production le répertoire se remplirait sans que personne ne le sache, et les factures concernées ne partiraient jamais.

À traiter avec la fiche 881 : un contrôle de fin de traitement comparant le nombre de fichiers entrants au nombre de fichiers livrés.

## Ce que cet essai n'a pas pu couvrir

- **La fuite dans l'autre sens, projet → instantanée**, n'est pas testée : l'ordre alphabétique fait passer les `II…` avant les `PJ…`. À refaire une fois les points 1 et 2 corrigés.
- **L'avoir `PJ50000087`** n'a pas été mis dans le lot. Le comportement du flux face à un `CreditNote` au milieu d'un lot reste inconnu — sujet distinct, `INT_281` ne traite pas les avoirs.
- **Les collisions d'archives** liées à `context.DateCourante` vide n'ont pas pu être observées, puisqu'un seul fichier a été archivé.

## Portée

Ce défaut ne se voit pas en passage unitaire, qui est le mode de test employé jusqu'ici. Il n'apparaît que dès qu'au moins deux factures arrivent ensemble — ce qui sera le cas nominal en production.

**Conséquence à retenir : dans l'état actuel, un lot de N factures livre une seule facture, et pas forcément avec son propre lisible.** À corriger avant toute mise en production.



---

# Précision sur l'IBAN absent (§ 4.2)

La formulation initiale — « facture projet, IBAN absent » — était trop large. Comparaison faite sur les cinq sources disponibles :

| Document | Société émettrice | Client | IBAN / BIC | Code règlement |
|---|---|---|---|---|
| `PJ50000088` projet | GA ENTREPRISE SAS | STELLANTIS AUTO | **absent** | 30 |
| `PJ50000087` avoir | GA ENTREPRISE SAS | STELLANTIS AUTO | **absent** | 30 |
| `PJ50000089` projet | GA ENTREPRISE SAS | SAFRAN ELECTRONICS & DEFENSE | `FR7618359000430002123574585` / `CPMEFRPPXXX` | 30 |
| `II08400217` instantanée | GA ENTREPRISE SAS | STELLANTIS AUTO | `FR8830002040240000062322F09` / `CRLYFRPP` | 30 |
| `II08400003` instantanée | GA SERVICES SAS | GES LIMITED | `FR7630004024970001046085677` / `BNPAFRPPCTO` | 1 |

**Ce n'est donc ni un défaut du flux projet, ni un défaut lié au client.** Une autre facture projet (`PJ50000089`, SAFRAN) porte son IBAN, et STELLANTIS en facture instantanée aussi.

L'absence est spécifique à la combinaison **STELLANTIS AUTO + contrat de vente** : les deux documents projet de ce client en sont dépourvus, l'avoir inclus. Cela oriente vers un paramétrage du mode de règlement sur le contrat de vente dans IFS, sans compte bancaire rattaché.

**À vérifier côté IFS** sur le contrat de vente STELLANTIS, et non comme une anomalie générique du flux.

À noter au passage, sans lien avec le sujet : `II08400003` (GA SERVICES SAS) sort avec un `PaymentMeansCode` à **1** — « instrument non défini » — là où les autres sont à 30, virement. Cohérence à vérifier, une deuxième société est concernée.
