---
tags: ["e-facture", "INT_281", "IFS", "brief", "questions"]
created: 2026-07-31
---

# Brief à destination d'un expert IFS — questions ouvertes sur le flux e-facture INT_281

**Date :** 31 juillet 2026
**Demandeur :** intégration Talend `INT_281`, projet `IFS_FINANCE`, société **GAE** (GA ENTREPRISE SAS)
**Tenant :** `gafr-cfg.ifs.cloud`, projection v1

## Contexte en trois phrases

IFS dépose des fichiers UBL de facture client sur un SFTP. Le job Talend `INT_281` les reprend, corrige et complète les balises pour se conformer à EN16931, y encapsule le PDF lisible et les pièces jointes, puis dépose le résultat chez Esker. Deux types de factures sont traités aujourd'hui : les **factures instantanées** (série `II`) et les **factures projet** issues des situations de contrat de vente (série `PJ`).

## Ce que le flux consomme déjà côté IFS

Utile pour situer nos questions : nous savons déjà appeler ces projections.

| Usage | Endpoint |
|---|---|
| Entité facture instantanée | `InstantInvoiceHandling.svc/InstantInvoiceSet` |
| Réimpression du lisible (instantanée) | `InstantInvoiceHandling.svc` action `ReprintInvoice` |
| Chaîne d'édition PDF | `PrintDialog.svc` — `PrintDialogInit`, `ReportDirectPrintRequest`, `GetLayoutType`, `PdfArchiveSet` / `Pdf` |
| Facture projet (AFP) | `SalesContractApplicationForPaymentHandling.svc/AfpInvoiceSet` |
| Édition du lisible projet | `AppForPaymentRep.svc/VirtualOrderReports` + action liée `IfsApp.AppForPaymentRep.VirtualOrderReport_OrderReport` |
| Fiche client | `CustomerInfoSet(CustomerId='…')` — champs `Country`, `B2bCustomer` |
| Paramétrage e-invoice client | `…/CustomerInvoiceCompanies(Company='GAE',…)` — champ `EinvoiceProcessType` |
| Pièces jointes | `DocReferenceObjectAttachmentHandling.svc` |

Champ personnalisé déjà identifié et exploité : **`Cf_Traitement_Efacture`** sur `InstantInvoice`, de type énuméré `IfsApp.InstantInvoiceHandling.CfEnum_GaTraitementEfacture`, valeurs `ARCHIVEONLY` et `OUTOFSCOPE`.

Documents de référence pour les échantillons cités : `II08400217` (instantanée, client STELLANTIS AUTO), `PJ50000088` et `PJ50000089` (projet), `PJ50000087` (avoir).

---

# Bloc A — Factures d'acompte

**Enjeu.** La spécification fonctionnelle demande de forcer `InvoiceTypeCode` à **386** (au lieu de 380) lorsque la facture projet est un acompte. Rien n'est implémenté à ce jour, faute de savoir détecter le cas de façon fiable depuis l'API.

La spécification précise que GA n'utilise **pas** le processus standard IFS de facture d'avance : ces pièces sont gérées comme des **lignes de déduction**, avec un type d'élément facturé « ACOMPTE » (et « AVANCE » pour la toute première).

**A1.** Depuis quelle projection OData, et sur quel champ, peut-on déterminer de façon fiable qu'une facture projet correspond à un **acompte** ? Nous cherchons idéalement le « type d'élément » de la ligne de situation du contrat de vente. Merci d'indiquer l'entité, le nom exact du champ et ses valeurs possibles.

**A2.** La spécification propose comme critère alternatif la présence, dans la section comptabilité de la facture, d'un **compte commençant par `419`**. Quelle projection expose les lignes comptables d'une facture projet, et ce critère est-il considéré comme fiable de votre point de vue, ou déconseillé ?

**A3.** La spécification demande de stocker, **au niveau du contrat de vente**, dans un champ personnalisé, le numéro de la première facture d'acompte — celle dont le type d'élément facturé est « AVANCE ». Le numéro se compose de l'`ID Série` et du `N° facture` pour une société donnée.
- Ce champ personnalisé a-t-il déjà été créé ? Si oui, quel est son nom exact et sur quelle entité ?
- Si non, sur quelle entité recommandez-vous de le créer, et sous quel format (chaîne concaténée, ou deux champs distincts) ?

**A4.** Pour les factures de **situation** et de **résorption d'acompte**, la spécification indique « pas de sujet, IFS gère correctement », `InvoiceTypeCode` reste à 380. Confirmez-vous ? Existe-t-il des cas où une résorption d'acompte devrait porter un autre code ?

---

# Bloc B — Avoirs (notes de crédit)

**Enjeu.** La spécification fonctionnelle **ne traite pas les avoirs**. Le mapping UBL les envisage structurellement (5 lignes sur 242 prévoient un chemin `/CreditNote/…` en alternative à `/Invoice/…`), mais aucune règle de gestion n'est écrite et `INT_281` ne sait pas les traiter.

Nous avons constaté qu'IFS dépose bien des avoirs dans le même répertoire : `PJ50000087` est un document dont la racine est `CreditNote` et non `Invoice`.

**B1.** Les avoirs empruntent-ils **le même canal de dépôt** que les factures — même répertoire, même déclencheur ? Ou existe-t-il un flux distinct ?

**B2.** Quelle projection OData porte l'**entité avoir**, pour les avoirs sur facture instantanée d'une part, et sur contrat de vente d'autre part ?

**B3.** Existe-t-il un **équivalent de `ReprintInvoice`** pour récupérer le lisible d'un avoir ? La chaîne `PrintDialog` est-elle utilisable telle quelle avec le jeton correspondant ?

**B4.** Quel `CreditNoteTypeCode` doit être émis — 381 attendu, à confirmer — et existe-t-il des balises spécifiques aux avoirs à la charge du développement, comme la référence à la facture d'origine (BT-25 / BT-26) ?

**B5.** Le champ **`Cf_Traitement_Efacture`** (`ARCHIVEONLY` / `OUTOFSCOPE`) a-t-il un équivalent sur les avoirs ?

---

# Bloc C — Champ `Cf_Traitement_Efacture` côté facture projet

**Enjeu.** Ce champ pilote la note `#BAR#` de l'UBL, qui indique à Esker le profil de traitement du document. Nous l'avons câblé pour les factures instantanées, en le lisant sur `InstantInvoiceSet`.

**C1.** Un champ personnalisé équivalent existe-t-il sur l'entité **facture projet** ? Si oui, quel est son nom exact et sur quelle projection le lire — `AfpInvoiceSet`, ou une autre ?

**C2.** Si le champ n'existe pas encore côté projet : est-il prévu de le créer, ou faut-il considérer que les factures projet retombent systématiquement sur la règle de la fiche client ?

---

# Bloc D — IBAN absent sur les factures d'un contrat de vente

**Enjeu.** La règle EN16931 **BR-50** impose un identifiant de compte bancaire dès lors que le moyen de paiement est le virement. L'UBL produit par IFS pour `PJ50000088` porte `PaymentMeansCode` = 30 (virement) **sans aucun** `cac:PayeeFinancialAccount`. Le fichier est donc rejetable par la plateforme.

Ce n'est ni générique aux factures projet, ni générique au client — comparaison faite sur les documents dont nous disposons :

| Document | Client | IBAN |
|---|---|---|
| `PJ50000088` projet | STELLANTIS AUTO | **absent** |
| `PJ50000087` avoir | STELLANTIS AUTO | **absent** |
| `PJ50000089` projet | SAFRAN ELECTRONICS & DEFENSE | présent |
| `II08400217` instantanée | STELLANTIS AUTO | présent |

**D1.** Quel paramétrage détermine l'alimentation du bloc `PayeeFinancialAccount` dans l'UBL d'une facture issue d'un contrat de vente ? Mode de règlement du contrat, adresse de paiement, compte bancaire de la société ?

**D2.** Sur le contrat de vente STELLANTIS spécifiquement, que faut-il corriger pour que l'IBAN soit émis ? Existe-t-il un contrôle amont permettant de détecter ce trou avant émission ?

---

# Bloc E — Effet de bord des `VirtualOrderReports`

**Enjeu.** Pour éditer le lisible d'une facture projet, notre flux crée un enregistrement `VirtualOrderReports` avec `Active: true` et `ScheduleOption: Daily`, puis déclenche l'action liée. Ces enregistrements s'accumulent, un par facture projet traitée, et restent actifs avec une planification quotidienne.

**E1.** Est-ce l'usage attendu de cette projection pour une édition ponctuelle, ou existe-t-il un mode non persistant / à la demande ?

**E2.** Si la création est inévitable, faut-il nettoyer ces enregistrements après édition, les désactiver, ou les réutiliser d'une facture à l'autre ? Y a-t-il un risque que la planification quotidienne déclenche des éditions non souhaitées ?

---

# Bloc F — Champs UBL manquants ou douteux

**F1 — BT-33, forme juridique et capital social.** `cac:PartyLegalEntity/cbc:CompanyLegalForm` est absent de l'UBL émis. Cette mention est obligatoire sur les factures des sociétés commerciales françaises. Où cette information est-elle portée dans IFS pour la société GAE, et pourquoi n'est-elle pas reprise dans l'UBL ?

**F2 — `cac:PartyName` vendeur et acheteur.** Le bloc n'est présent que sur `cac:Delivery`. Le nom légal est bien porté par `PartyLegalEntity/cbc:RegistrationName` des deux côtés. Est-ce le comportement standard attendu d'IFS, ou une omission ?

**F3 — `BuyerReference` littéral.** Sur `II08400217`, la balise `cbc:BuyerReference` contient la chaîne **`RÉFÉRENCE CLIENT`**, valeur présente telle quelle dans le fichier émis par IFS. Cela ressemble à un libellé de champ non substitué. S'agit-il d'une valeur par défaut de paramétrage, et où la corriger ? Sur `PJ50000088`, la balise est absente.

**F4 — `PaymentMeansCode` incohérent entre sociétés.** La facture `II08400003`, émise par **GA SERVICES SAS**, porte `PaymentMeansCode` = **1** (« instrument non défini ») là où les documents de GA ENTREPRISE portent 30 (virement). Paramétrage à corriger côté GA SERVICES ?

---

# Format de réponse souhaité

Pour chaque question, dans la mesure du possible :

1. **Le nom exact** de la projection, de l'entité et du champ — c'est ce qui nous bloque le plus, nous ne pouvons rien implémenter sur une description fonctionnelle seule.
2. Les **valeurs possibles** pour les champs énumérés.
3. Une **requête OData d'exemple** quand c'est pertinent, sur le modèle de ce que nous utilisons déjà :
   `https://gafr-cfg.ifs.cloud/main/ifsapplications/projection/v1/<Projection>.svc/<EntitySet>(<clés>)?$select=<champs>`
4. La distinction entre ce qui **existe déjà** dans le paramétrage GAE et ce qui **reste à créer**.

Les questions des blocs **A** (acomptes) et **B** (avoirs) sont les plus structurantes : elles conditionnent des développements non commencés. Le bloc **D** (IBAN) est le plus urgent en exploitation, puisqu'il produit dès aujourd'hui des fichiers rejetables.
