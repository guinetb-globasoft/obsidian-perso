---
tags: ["compta", "odoo", "guinet-group", "GDG", "virement", "CCA", "mode-operatoire"]
created: 2026-05-12
parent: "[[Workflow-Bancaire-Guinet-Group]]"
---

# Mode opératoire — Virement GDG → Guinet Group 1 000 € (avance CCA)

> **Objet** : exécuter un virement SEPA Credit Transfer de 1 000 € depuis GDG (instance Odoo `guinet`, company_id=4) vers Guinet Group (id=1) au titre d'une **avance en compte courant d'associé**, en passant par le workflow complet Odoo 19 → portail Banque Populaire.
>
> **Premier test du workflow** mis en place dans le cadre de [[Workflow-Bancaire-Guinet-Group]].
>
> **Cadre juridique** : ce virement s'inscrit dans la **convention de trésorerie de groupe** déjà signée entre **Guinet Group, Guinet Digital Group et Le Petit Cerf** (voir §0).

---

## 0. Cadre juridique — Convention de trésorerie de groupe existante

L'avance s'effectue dans le cadre de la **convention de trésorerie multilatérale** déjà signée entre les 3 sociétés du groupe :
- **Guinet Group SAS** (associée de GDG)
- **Guinet Digital Group SAS** (GDG)
- **Le Petit Cerf**

### Pourquoi c'est important

En France, le **monopole bancaire** (article L511-5 du Code monétaire et financier) interdit aux entreprises non bancaires de réaliser des opérations de crédit à titre habituel. **Exception** : article **L511-7 1° du Code monétaire et financier** autorise les **opérations de trésorerie entre sociétés ayant des liens capitalistiques directs ou indirects**, à condition qu'une **convention de trésorerie** encadre ces flux.

→ La convention de trésorerie existante remplit cette obligation. **Pas besoin de rédiger une convention par virement** : chaque virement entre dans le cadre déjà approuvé.

### Articulation avec L227-10 (convention réglementée SAS)

Comme Guinet Group est **associée de GDG**, la convention de trésorerie est aussi une **convention réglementée** au sens de l'article L227-10 du Code de commerce. **Mais elle a déjà été approuvée** lors de sa signature :
- Si pas de CAC : approuvée par décision du dirigeant ou des associés
- Mention dans le rapport de gestion annuel
- L'AG annuelle se prononce sur les conventions réglementées (article L227-10)

→ **Le virement de 1 000 € est une simple EXÉCUTION** de la convention déjà approuvée. Aucune nouvelle approbation nécessaire à chaque virement.

### À faire pour ce virement spécifique

1. **Vérifier** que les conditions du virement respectent la convention :
   - Sociétés parties ✅ (GDG et Guinet Group sont signataires)
   - Plafond de la convention non dépassé (à vérifier dans la convention signée)
   - Modalités de rémunération (intérêts ou pas) conformes à la convention
   - Si la convention prévoit un taux d'intérêt : les intérêts seront calculés à la clôture annuelle
2. **Référencer la convention** dans le libellé du virement (cf. étape 2.2) — utile pour la traçabilité
3. **Conserver le justificatif** du virement dans les dossiers GDG et GG (statement bancaire + écriture Odoo)

> **Action** : récupérer le PDF signé de la convention de trésorerie et l'archiver dans `vault-prive/04-Comptabilite/Conventions/` si pas déjà fait. Identifier la date de signature et les éventuels avenants pour faire la référence dans le libellé.

---

## 1. État actuel audité (Odoo `guinet`, company_id=4 GDG)

### Côté GDG (émetteur)

| Élément | État | ID Odoo |
|---|---|---|
| Société | ✅ GDG | company_id=4 |
| Journal banque BNK1 "Bank" | ✅ Configuré | journal id=27 |
| IBAN émetteur BNK1 | ✅ `FR76 1780 7000 1755 6210 0463 426` (BP) | — |
| Compte par défaut BNK1 | ✅ 512001 Bank | — |
| Méthode SEPA Credit Transfer sur BNK1 | ✅ Active | payment.method.line id=105 |
| Compte CCA Groupe | ✅ **451000 "Group"** (asset, plan comptable GDG) | — |
| Historique flux GDG→GG | ✅ Toujours via 451000 (9 mouvements 2025) | — |

### Côté partner Guinet Group (destinataire, dans la base GDG)

| Élément | État | À modifier ? |
|---|---|---|
| res.partner Guinet Group | ✅ Existe | id=1 |
| IBAN destinataire | ✅ `FR76 1780 7000 1795 5219 7114 463` (BP Occitane) | Non |
| property_account_payable_id | ⚠️ 401100 Suppliers (défaut Odoo) | **À changer pour 451000 Group** |
| property_account_receivable_id | 411100 Customers (défaut Odoo) | Non (pas concerné par ce virement) |

---

## 2. Étape par étape

### Étape 2.1 — Créer un sous-compte 451100 dédié à Guinet Group (en type Payable)

**Pourquoi** : Odoo filtre le champ "Compte fournisseur" du partner sur les seuls comptes de type `liability_payable`. Le compte **451000 "Group"** actuel chez GDG est typé `asset_current` (créance) — invisible dans le sélecteur. Plutôt que de re-typer 451000 (risqué car il a un historique), on crée un **sous-compte 451100 dédié** en type Payable.

**Doctrine PCG respectée** : la classe 45 doit normalement être **ventilée par contrepartie** (451100 pour Guinet Group, 451200 pour Le Petit Cerf, etc.). Cette opération en profite pour mettre en place cette ventilation.

> Le typage Odoo `liability_payable` est juste un classement par défaut pour le filtrage UI — il **ne contraint pas le sens débit/crédit** des écritures. Le 451100 peut très bien avoir un solde débiteur (créance) malgré son type "payable". C'est d'ailleurs le typage par défaut de la plupart des plans comptables Odoo pour les comptes 45.

**Action manuelle dans Odoo** :

1. Vérifier la société active : **GUINET DIGITAL GROUP**
2. Aller dans **Comptabilité** → **Configuration** → **Plan comptable** *(EN : Accounting → Configuration → Chart of Accounts)*
3. Cliquer **Nouveau** *(EN : New)*
4. Remplir :

   | Libellé Odoo FR | Libellé Odoo EN | Valeur |
   |---|---|---|
   | Code | Code | **451100** |
   | Nom du compte | Account Name | **Compte courant Groupe - Guinet Group** |
   | Type | Type | **Comptes fournisseurs** *(Payable)* |
   | Devise | Currency | EUR (défaut) |
   | Permettre la réconciliation | Allow Reconciliation | **Coché** ✅ *(important pour le lettrage)* |

5. Cliquer **Sauvegarder** *(EN : Save)*

### Étape 2.2 — Aligner le compte fournisseur du partner Guinet Group sur 451100

**Action manuelle dans Odoo** :

1. Vérifier la société active : **GUINET DIGITAL GROUP**
2. Aller dans **Contacts** → ouvrir **Guinet Group** (id=1)
3. Cliquer sur l'onglet **Comptabilité** *(EN : Accounting)*
4. Modifier les 2 champs :

   | Libellé Odoo FR | Libellé Odoo EN | Action |
   |---|---|---|
   | Compte client | Account Receivable | Laisser sur `411100 Customers - Sales of goods or services` (non concerné par ce virement) |
   | Compte fournisseur | Account Payable | Remplacer `401100 Suppliers - Purchase of goods and services` par **`451100 Compte courant Groupe - Guinet Group`** *(maintenant visible dans le sélecteur car type liability_payable)* |

5. Cliquer **Sauvegarder** *(EN : Save)*

> Cette modification est **permanente** mais **cohérente** avec la pratique groupe (toutes les opérations GDG → Guinet Group passent par le compte courant). Si un jour Guinet Group facture une vraie prestation commerciale à GDG (rare), on surchargerait la ligne sur 401100 manuellement à la création de la facture.

### Étape 2.3 — Créer directement le paiement SEPA Credit Transfer

**Pas de facture intermédiaire** : on crée un paiement standalone qui imputera automatiquement sur 451100 (grâce au compte fournisseur configuré sur le partner).

**Action manuelle dans Odoo** :

1. Vérifier la société active : **GUINET DIGITAL GROUP**
2. Aller dans **Comptabilité** → **Fournisseurs** → **Paiements** *(EN : Accounting → Vendors → Payments)*
3. Cliquer **Nouveau** *(EN : New)*
4. Remplir le formulaire :

   | Libellé Odoo FR | Libellé Odoo EN | Valeur |
   |---|---|---|
   | Type de paiement | Payment Type | **Envoyer de l'argent** *(outbound)* |
   | Type de partenaire | Partner Type | **Fournisseur** *(Vendor)* |
   | Partenaire | Vendor | **Guinet Group** (id=1) |
   | Montant | Amount | **1 000,00 €** |
   | Devise | Currency | EUR |
   | Date du paiement | Payment Date | (date du jour) |
   | Journal | Journal | **Bank** (BNK1) |
   | Méthode de paiement | Payment Method | **Virement SEPA** *(SEPA Credit Transfer)* |
   | Compte bancaire du destinataire | Recipient Bank Account | **FR76 1780 7000 1795 5219 7114 463** *(auto-rempli depuis Guinet Group)* |
   | Mémo | Memo | **Avance trésorerie GDG vers Guinet Group — Convention de trésorerie de groupe du XX/XX/XXXX** *(remplacer XX/XX/XXXX par la date réelle de signature)* |

5. Cliquer **Confirmer** *(EN : Confirm)* en haut → le statut passe de **Brouillon** *(Draft)* à **En cours** *(In Process)*

**⚠️ Nouveauté Odoo 19 : aucune écriture comptable n'est générée à ce stade.**

En Odoo 17/18, la confirmation créait immédiatement une écriture intermédiaire `Débit 451100 / Crédit 472000` (compte de transit). Cela générait des écritures parasites sur 472000 si le paiement n'était jamais déposé en banque.

En **Odoo 19**, l'état `in_process` signifie "paiement préparé, en attente d'exécution banque". L'écriture comptable n'est créée que **lors du rapprochement bancaire** (étape 2.6), et elle passe **directement** sur le compte définitif :

```
[Brouillon] → [En cours] → génération PAIN.001 → dépôt banque → relevé reçu → [Payé]
                  ↑                                                                ↑
          Aucune écriture                                                  Écriture créée ici :
                                                                          Débit 451100 / Crédit 512001
                                                                          (sans passer par 472000)
```

→ Au stade actuel, **rien n'apparaît dans les écritures comptables** pour ce paiement. C'est normal et voulu — plus propre que les versions antérieures.

### Étape 2.4 — Ajouter le paiement à un paiement par lot et générer le fichier SEPA

Pour générer le fichier PAIN.001, on passe par un **paiement par lot** :

1. Aller dans **Comptabilité** → **Fournisseurs** → **Paiements par lot** *(EN : Accounting → Vendors → Batch Payments)*
2. Cliquer **Nouveau** *(EN : New)*
3. Remplir :

   | Libellé Odoo FR | Libellé Odoo EN | Valeur |
   |---|---|---|
   | Date | Date | (date du jour) |
   | Type de paiement | Payment Type | **Envoyer de l'argent** *(outbound)* |
   | Journal | Journal | **Bank** (BNK1) |
   | Méthode de paiement | Payment Method | **Virement SEPA** *(SEPA Credit Transfer)* |

4. Dans la section **Paiements** *(Payments)* en bas : cliquer **Ajouter une ligne** *(Add a line)* et sélectionner le paiement de 1 000 € créé à l'étape 2.3
5. Cliquer **Valider** *(EN : Validate)* en haut → statut passe à **Validé**
6. Cliquer **Télécharger SEPA** *(EN : Download SEPA)* ou **Imprimer** *(Print)* selon le bouton qui apparaît → un fichier `.xml` PAIN.001 est téléchargé localement (format `pain.001.001.03`)

**À ce stade, l'argent n'a PAS encore quitté GDG.** Le fichier PAIN.001 est juste préparé pour être déposé en banque.

### Étape 2.5 — Upload du fichier PAIN.001 sur le portail Banque Populaire

> ⚠️ Cette étape se passe **hors Odoo**, sur le portail web Banque Populaire entreprise.

1. Se connecter au **portail web entreprise Banque Populaire** (https://www.businessmonline.com/ ou Cyberplus Entreprises selon ton type de contrat) avec le compte GDG (Benoit)
2. Naviguer vers la section **Virements** → **Remise de fichier** *(le libellé exact peut varier selon le portail : "Téléchargement de virements", "Import de fichier", "Remise de virements SEPA")*
3. Sélectionner le fichier PAIN.001 téléchargé à l'étape 2.4
4. Cliquer **Importer** / **Téléverser**
5. Le portail BP affiche le détail du virement à valider :
   - 1 bénéficiaire : Guinet Group, IBAN destinataire, montant 1 000 €
   - Date d'exécution proposée
6. Si BP demande une validation forte : valider avec **MFA Banque Populaire** (code SMS, application Securipass, ou autre selon ta config BP)
7. Si workflow 2 validations est configuré côté BP : la 2e personne (validateur) doit se connecter pour approuver
8. Une fois validé, le virement est **exécuté** par BP (immédiat avec virement instantané, ou à la date d'exécution choisie sinon)

### Étape 2.6 — Rapprochement bancaire côté GDG

Une fois le virement exécuté par BP, le relevé bancaire arrive dans Odoo (via synchronisation bancaire ou import manuel d'un fichier CAMT.053 / OFX).

1. Aller dans **Comptabilité** (tableau de bord) → carte **Bank** (BNK1)
2. Cliquer **Rapprocher les éléments** *(EN : Reconcile Items)* — un compteur affiche le nombre d'opérations à traiter
3. Trouver la nouvelle ligne du relevé : **−1 000,00 €** avec libellé type "VIR INST SAS GUINET GROUP" ou similaire
4. Sur la ligne, Odoo propose automatiquement un **match** avec le paiement créé à l'étape 2.3 → cliquer **Valider** *(EN : Validate)*
5. **Au moment du rapprochement, Odoo 19 crée l'écriture comptable directement** :

| Compte | Débit | Crédit |
|---|---|---|
| **451100 Compte courant Groupe - Guinet Group** | 1 000,00 € | |
| 512001 Bank | | 1 000,00 € |

Et le payment passe à l'état **Payé** *(Paid)*.

→ Imputation directe sur **451100** (sous-compte dédié Guinet Group) via le **workflow SEPA Credit Transfer complet**, sans facture fictive, sans 472000 intermédiaire, sans OD de reclassement.

### Étape 2.7 — Écriture miroir côté Guinet Group (instance `guinet`, company_id=1)

Dans la base **Guinet Group** (company_id=1), il faut **aussi** créer l'écriture miroir pour refléter la dette envers GDG.

⚠️ Odoo 19 en multi-company ne crée PAS automatiquement l'écriture miroir interco. C'est à toi de la faire.

> 💡 **Pour une cohérence parfaite**, il serait pertinent de créer aussi côté Guinet Group un sous-compte **451100 "Compte courant Groupe - Guinet Digital Group"** (en type Payable) dédié à la contrepartie GDG. Voir [§7 — Symétrie côté Guinet Group](#7--sym%C3%A9trie-c%C3%B4t%C3%A9-guinet-group) en bas de note.

1. Basculer la société active en haut à droite → choisir **Guinet Group**
2. Aller dans **Comptabilité** → carte **Compte BP Guinet Group 4463** (journal BNK2)
3. Quand le relevé bancaire BP arrive (synchro ou import) : ligne de **+1 000,00 €** avec libellé type "VIR DE SAS GUINET DIGITAL GROUP"
4. Cliquer **Rapprocher les éléments** *(EN : Reconcile Items)*
5. Sur la ligne, créer l'écriture de contrepartie via **Manuel** *(EN : Manual)* :
   | Champ | Valeur |
   |---|---|
   | Compte | **451100 Compte courant Groupe - Guinet Digital Group** *(à créer côté GG ; sinon utiliser 451000 Group existant)* |
   | Partenaire | **Guinet Digital Group** *(partner GDG dans la base GG — à identifier)* |
   | Libellé | **Avance trésorerie reçue de GDG — Convention de trésorerie de groupe du XX/XX/XXXX** |
   | Montant | 1 000,00 € (auto-rempli) |
6. Cliquer **Valider** *(EN : Validate)*

**Écritures côté Guinet Group :**

| Compte | Débit | Crédit |
|---|---|---|
| 512110 BP Occitane | 1 000,00 € | |
| **451100 Compte courant Groupe - Guinet Digital Group** | | 1 000,00 € |

→ La dette de Guinet Group envers GDG (451100 au crédit côté GG) est miroir de la créance de GDG sur Guinet Group (451100 au débit côté GDG).

---

## 3. Suivi croisé GDG ↔ Guinet Group

Après l'opération, les soldes 451100 de chaque société doivent être **miroirs** :

| Société | Compte | Solde | Sens |
|---|---|---|---|
| GDG (co=4) | 451100 *Compte courant Groupe - Guinet Group* | **+1 000,00 €** (débit) | Créance sur Guinet Group |
| Guinet Group (co=1) | 451100 *Compte courant Groupe - Guinet Digital Group* | **−1 000,00 €** (crédit) | Dette envers GDG |

À chaque clôture comptable, vérifier que la somme algébrique des 451100 cross-companies est = 0 (réconciliation interco).

---

## 4. Points de vigilance

| # | Risque | Mitigation |
|---|---|---|
| 1 | Le compte fournisseur du partner Guinet Group côté GDG est désormais 451100 → impacte toute facture future de GG vers GDG (qui s'imputerait sur 451100 au lieu de 401100) | Si un jour Guinet Group facture une vraie prestation commerciale à GDG : surcharger la ligne de facture sur 401100 manuellement à la création de la facture |
| 2 | Compte 451000 historique reste utilisé pour les flux passés (Guinet Group, Le Petit Cerf) | Garder 451000 en lecture seule pour l'historique ; mettre en place progressivement les sous-comptes 4511xx par contrepartie. À terme, OD de bascule du solde 451000 vers les sous-comptes pour ventiler proprement |
| 3 | Virement dépasse le plafond de la convention de trésorerie | Vérifier le plafond avant exécution (cf. §0) ; si dépassement, signer un avenant à la convention |
| 4 | Le paiement Odoo reste en "En cours" *(In Process)* si pas de retour bancaire | Vérifier la synchro bancaire / relevé, sinon rapprochement manuel |
| 5 | PAIN.001 généré mais jamais déposé sur portail BP | Le paiement reste éternellement non lettré côté Odoo — penser à supprimer le paiement et le batch si on annule |
| 6 | Intérêts éventuels prévus dans la convention non calculés à la clôture | Vérifier les modalités d'intérêts dans la convention ; si prévus, planifier le calcul à la clôture annuelle (modèle inspiré du Acte 6 POC AREC FITEO) |
| 7 | Compte 451100 typé `liability_payable` mais peut être utilisé en débit (créance) | Cohérent avec la pratique Odoo standard pour les comptes 45 ; le bilan retraité reclassera selon le solde réel (débiteur = actif circulant, créditeur = passif) |

---

## 5. Validation post-exécution

À cocher après chaque étape :

- [x] §0 Convention de trésorerie groupe identifiée + plafond non dépassé vérifié
- [x] §2.1 Sous-compte 451100 "Compte courant Groupe - Guinet Group" créé côté GDG en type Payable *(id=3184)*
- [x] §2.2 Partner Guinet Group côté GDG : compte fournisseur = 451100
- [x] §2.3 Paiement SEPA Credit Transfer 1 000 € créé et confirmé *(PAY00001, id=20, état "En cours / In Process")* — pas d'écriture comptable à ce stade (Mode A Odoo 19, voir Annexe A)
- [x] §2.4 Paiement par lot créé, fichier PAIN.001 généré et téléchargé *(SCT-BNK1-20260512114147.xml, conforme pain.001.001.09, validé)*
- [ ] §2.5 PAIN.001 uploadé sur portail BP **OU** virement saisi manuellement dans Cyberplus *(voir Annexe C — service "Suite Entreprise" non actif côté BP)*
- [ ] §2.5 Virement exécuté effectivement par BP (vérifier le relevé)
- [ ] §2.6 Relevé BP reçu dans Odoo et rapproché côté GDG → écriture comptable créée directement (Débit 451100 / Crédit 512001)
- [ ] §2.7 Sous-compte 451100 dédié GDG créé côté Guinet Group (optionnel mais recommandé)
- [ ] §2.7 Écriture miroir créée côté Guinet Group (451100 / 512110) et rapprochée
- [ ] §3 Soldes 451100 cross-companies vérifiés (+1000 GDG / -1000 GG)
- [ ] §0 Relevé bancaire archivé comme justificatif d'exécution de la convention

### Points identifiés à l'usage (Annexes B et C)

- [ ] **Annexe B** : Activer "Lock Outgoing Payments" dans Settings GDG + créer user `factures@guinet-group.com` pour avoir le workflow validation Odoo natif sur les prochains virements
- [ ] **Annexe C** : Souscrire à "Suite Entreprise" chez BP (~5-20 €/mois) OU à Ponto (~4 €/mois + commission) pour pouvoir déposer des fichiers PAIN.001 — sinon saisie manuelle dans Cyberplus

---

## 6. Retour d'expérience attendu

À documenter après exécution pour alimenter le positionnement AREC :

1. **Combien de temps** a pris chaque étape (création paiement, upload BP, validation, réconciliation) ?
2. **Quels frottements** ergonomiques côté Odoo 19 ou portail BP ?
3. **La signature côté BP** : quelle méthode a été demandée (SMS, token, autre) ? Niveau eIDAS effectif ?
4. **La validation à 2 personnes** est-elle activée sur le portail BP entreprise ? Comment se passe le workflow ?
5. **La réconciliation miroir** côté Guinet Group : effort manuel ? Idée pour automatiser via interco ?

Ces retours alimenteront la **note de positionnement AREC** pour la réunion du 21/05.

---

## Annexe A — Workflow paiement Odoo 19 : Mode A vs Mode B (avec/sans outstanding)

> Constat fait lors de l'exécution de §2.3 : aucune écriture comptable n'a été créée à la confirmation du paiement (PAY00001 en état `in_process`). Comportement vérifié et documenté ci-dessous.

### Ce que dit la doc officielle Odoo 19

Citation littérale ([Odoo 19 — Payments](https://www.odoo.com/documentation/19.0/applications/finance/accounting/payments.html)) :

> *"By default, payments in Odoo do not create journal entries, but they can be configured to create journal entries by using outstanding accounts on bank and cash journals."*

→ Il existe **deux modes** de configuration côté journal bancaire (par méthode de paiement) :

### Les 2 modes possibles

| Critère | **Mode A — Sans outstanding** | **Mode B — Avec outstanding** |
|---|---|---|
| Config journal BNK1 → onglet "Paiements sortants" → ligne "Virement SEPA" | Champ **Outstanding Payments account** = `(vide)` | Champ **Outstanding Payments account** = `472000 Comptes de transit` (ou autre suspense) |
| Écriture créée à la confirmation du paiement | **Aucune** | Débit **451100** / Crédit **472000** |
| Écriture créée au rapprochement bancaire | Débit **451100** / Crédit **512001** *(directe)* | Débit **472000** / Crédit **512001** *(lettre le suspense)* |
| Visibilité de l'engagement en attente | Pas visible en compta (juste vue paiements) | Solde du 472000 = somme des paiements en attente |
| Risque d'écriture parasite si paiement jamais exécuté | Aucun | Le 472000 traîne le montant tant que pas annulé |
| Conforme à la doctrine "constatation du fait générateur" | Plus stricte (l'écriture n'apparaît qu'à l'exécution réelle) | Plus large (l'engagement apparaît dès la préparation) |

### Configuration GDG actuelle

Lors de l'audit initial, le payment.method.line "SEPA Credit Transfer" (id=105) sur le journal BNK1 GDG a remonté :

```
payment_account_id : —  (vide)
```

→ **GDG est en Mode A**. C'est pour cela que PAY00001 (créé à §2.3) est en état `in_process` sans aucune écriture comptable associée.

### Comment basculer en Mode B (si jamais on le voulait)

1. **Comptabilité → Configuration → Journaux** → ouvrir **Bank** (BNK1)
2. Onglet **Paiements sortants** *(EN : Outgoing Payments)*
3. Sur la ligne **Virement SEPA** *(SEPA Credit Transfer)*, dans le champ **Compte en attente** *(EN : Outstanding Payments Account)* :
   - Sélectionner un compte de type `current_assets` ou similaire (typiquement 472000 ou 511000 "Effets à l'encaissement")
4. Sauvegarder

> Mais en pratique, **Mode A est préférable pour ce cas** : pas de pollution du 472000, l'écriture comptable n'apparaît qu'à l'exécution effective du virement, ce qui colle mieux à la doctrine PCG ("Une opération est comptabilisée à la date à laquelle elle intervient").

### États du paiement (state machine Odoo 19)

```
┌──────────┐        ┌──────────────┐        ┌──────────────┐        ┌──────┐
│ Brouillon│        │  En cours    │        │  Rapproché   │        │ Payé │
│ (Draft)  │───────▶│ (In Process) │───────▶│ (avec relevé)│───────▶│(Paid)│
└──────────┘  Conf. └──────────────┘  Batch └──────────────┘   Auto └──────┘
                          │   PAIN.001         │                       │
                          │   + Dépôt BP       │                       │
                          ▼                    ▼                       │
                    (rien en compta            (écriture créée :       ▼
                     en Mode A)                Débit 451100        Statut
                                               Crédit 512001)      facture
                                                                   = "Payée"
```

### Note pour la doctrine AREC

Le **Mode A** d'Odoo 19 est une évolution intéressante pour la doctrine comptable :
- En Mode B (comportement Odoo 17/18 par défaut), le seul fait de "préparer" un virement créait une écriture sur le suspense, alors même que l'engagement n'était pas certain
- En Mode A, la comptabilité ne reflète que les opérations effectivement exécutées par la banque, ce qui est plus conforme au principe de **prudence comptable**

→ À mentionner en réunion AREC du 21/05 : Odoo 19 offre désormais une **flexibilité fine sur le moment de constatation comptable** des virements préparés mais pas encore exécutés. C'est un point positif sur leur question "workflow validation virement".

---

## Annexe B — Workflow d'approbation interne Odoo (double validation)

> Point identifié à l'usage : pour ce premier virement, **aucun workflow d'approbation Odoo n'a été mis en place** — le paiement a été créé et confirmé directement par Benoit sans étape "à approuver" par un 2e validateur. Voici comment configurer ça pour les prochains virements.

### Pourquoi ce workflow était attendu

Le plan global [[Workflow-Bancaire-Guinet-Group]] prévoit Phase 2 :
- Préparateur : `factures@guinet-group.com`
- Validateur : Benoit Guinet (dirigeant)
- Règles par montant : < 1 000 € = 1 validation, ≥ 1 000 € = 2 validations

C'est aussi ce qu'AREC souhaite reproduire pour son workflow IBIX → Odoo (CR réunion 7/5, §1).

### Ce qu'Odoo 19 Enterprise propose nativement

**Setting** : Comptabilité → Configuration → Paramètres → section **Paiements fournisseurs** (Vendor Payments) → activer **"Lock Outgoing Payments"** (option Enterprise).

**Workflow résultant** :

```
[Brouillon]  →  [À approuver]  →  [En cours]  →  [Payé]
   ↑                 ↑                ↑              ↑
 Création         Préparateur     Validateur 2   Rapprochement
 par préparateur  clique          clique         bancaire
                  "Envoyer pour   "Approuver"
                   approbation"
```

**Règles** :
- Le préparateur **ne peut pas** approuver son propre paiement (Odoo bloque)
- Le validateur doit être un **autre utilisateur** avec le droit "Approuver paiements"
- Les seuils peuvent être configurés pour exiger 1, 2 ou 3 niveaux selon le montant

**Exemple AREC-style configurable** :
| Montant | Niveaux d'approbation |
|---|---|
| < 1 000 € | 0 (direct) |
| 1 000 € — 10 000 € | 1 (DAF) |
| > 10 000 € | 2 (DAF + Dirigeant) |

### Pourquoi ça n'a pas joué sur PAY00001

Combinaison de 3 raisons :
1. **Option "Lock Outgoing Payments" non activée** dans les Settings GDG
2. **Un seul utilisateur opérationnel sur GDG** (Benoit) → impossible d'avoir 2 validateurs distincts
3. **Le seuil n'aurait probablement pas été dépassé** : 1 000 € sous le seuil typique de 1ère approbation

### Plan d'action pour les prochains virements GDG

| # | Action | Effort |
|---|---|---|
| 1 | Créer un utilisateur `factures@guinet-group.com` dans GDG (rôle préparateur) | 10 min |
| 2 | Activer "Lock Outgoing Payments" dans Settings → Accounting → Vendor Payments | 5 min |
| 3 | Configurer les seuils : ≥ 1 000 € = 1 validation, ≥ 10 000 € = 2 validations | 5 min |
| 4 | Vérifier les droits : `factures@guinet-group.com` = préparateur, Benoit = validateur | 5 min |
| 5 | Refaire un virement de test de ≥ 1 000 € pour valider le workflow complet | — |

### Implications doctrinales (séparation des tâches)

L'activation de ce workflow met en place une **séparation des tâches** (segregation of duties / SoD) conforme aux référentiels de contrôle interne (COSO, AMF) :
- Le préparateur ne peut pas exécuter
- Le validateur ne peut pas préparer
- Trace d'audit complète dans le chatter Odoo (qui a fait quoi, quand)

C'est un point de différenciation fort à porter en réunion AREC du 21/05 : Odoo 19 Enterprise sait nativement reproduire le workflow IBIX actuel d'AREC, sans module tiers.

---

## Annexe C — Limite côté Banque Populaire : service "Remise de virements par fichier"

> Constat lors de l'étape §2.5 : impossible de trouver l'option "Virement par fichier" / "Import PAIN.001" sur le portail Cyberplus standard de GDG.

### Explication

Sur **Banque Populaire**, l'import de fichier SEPA PAIN.001 n'est **pas une fonctionnalité standard** du portail Cyberplus. Elle nécessite la souscription au service **Suite Entreprise** (ou équivalent selon les caisses régionales) :

- **Cyberplus standard** (offre commune PME/pro) → permet uniquement les **virements unitaires** saisis manuellement, ou les modèles enregistrés. Pas d'import fichier.
- **Suite Entreprise / Cyberplus Entreprises** → permet l'**import de fichiers SEPA** (PAIN.001/008), le télépaiement en masse, EBICS, etc. Service payant.

### Procédure pour activer "Remise de virements par fichier" chez BP

1. Contacter le chargé de clientèle pro / entreprise BP (probablement BP Occitane pour GDG)
2. Demander la souscription à **"Suite Entreprise"** ou **"Service Virement multiple par fichier"** (le libellé exact varie)
3. Tarif indicatif : **5 à 20 €/mois** selon options
4. Délai d'activation : ~2-3 jours ouvrés
5. À l'activation, le portail BP propose une nouvelle section "Import de fichier" / "Remise SEPA" dans le menu Virements

### Workaround pour ce virement 1 000 € (sans Suite Entreprise activé)

Trois options :

**Option A — Saisie manuelle dans Cyberplus** (recommandé pour ce 1er test) :
1. Aller sur Cyberplus → Virements → Nouveau virement
2. Saisir manuellement les infos qui sont dans le PAIN.001 généré par Odoo :
   - Bénéficiaire : Guinet Group, IBAN `FR7617807000179552197114463`
   - Montant : 1 000 €
   - Libellé : "Avance trésorerie GDG → Guinet Group — Convention du XX/XX/XXXX"
3. Valider avec MFA
4. Le PAIN.001 généré par Odoo reste utile en **archivage d'audit** (preuve de l'intention de paiement, traçabilité)

**Option B — Souscrire Suite Entreprise** (recommandé pour la suite si volume virements augmente) :
- Voir procédure ci-dessus

**Option C — Activer Ponto** (cf. annexe Plan B du CR AREC) :
- Souscription Ponto via myponto.com → ~4 €/mois + commission par paiement
- Avantage : transmission automatique depuis Odoo, pas de manipulation du fichier
- À tester aussi pour AREC

### Implication pour le retour d'expérience AREC

→ Point important à mentionner en réunion 21/05 : AREC utilise déjà IBIX qui fait le rôle de Suite Entreprise. **S'ils veulent sortir d'IBIX**, ils devront soit :
- Souscrire Suite Entreprise CEMP/BPOC (équivalent fonctionnel pour upload manuel)
- Souscrire un protocole automatisé : EBICS via account_ebics (Noviat) ou Ponto

---

## Sources Odoo 19 officielles consultées

- [Odoo 19 — Payments documentation](https://www.odoo.com/documentation/19.0/applications/finance/accounting/payments.html)
- [Odoo 19 — Pay with SEPA](https://www.odoo.com/documentation/19.0/applications/finance/accounting/payments/pay_sepa.html)
- [Odoo 19 — Batch payments](https://www.odoo.com/documentation/19.0/applications/finance/accounting/payments/batch.html)
- [Odoo 19 — Internal transfers (intra-société uniquement)](https://www.odoo.com/documentation/19.0/applications/finance/accounting/bank/internal_transfers.html)
- [Odoo Forum — Outstanding accounts behavior change](https://www.odoo.com/forum/help-1/v14-change-in-payment-behavior-how-do-the-suspense-and-outstanding-payment-accounts-change-the-journal-entries-posted-177592)
- [Odoo Forum — Custom payment destination account](https://www.odoo.com/forum/help-1/in-odoo-17-how-do-i-override-the-default-accounts-set-in-the-journal-entry-created-by-a-customer-payment-242955)

---

*Mode opératoire — première exécution du workflow bancaire Odoo 19 sur Guinet Digital Group. Tester, mesurer, capitaliser pour AREC.*
