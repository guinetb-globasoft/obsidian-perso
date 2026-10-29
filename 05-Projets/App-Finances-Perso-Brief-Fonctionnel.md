---
tags: ["projet", "app", "django", "finances-perso", "brief"]
created: 2026-07-21
type: brief-fonctionnel
---

# Application de gestion des finances personnelles — Brief fonctionnel

> Note destinée à une IA de développement (stack : Django + base de données).
> **Objectif de cette note : décrire le MÉTIER, les DONNÉES et les ANALYSES attendues — pas la technique.**
> Elle est issue d'un long travail réel de mise en ordre de la compta perso de Benoit (fait jusqu'ici dans Odoo). L'app doit reprendre la même logique **mais en beaucoup plus simple**.

---

## 1. Contexte et intention

Aujourd'hui, la gestion se fait dans **Odoo** (logiciel de compta pro), ce qui impose un formalisme lourd et inadapté à un usage personnel : **plan comptable, comptes de classe 6 / 4 / 7, journaux, écritures à double sens, comptes d'attente, comptes de transit…**

👉 **On abandonne totalement cette logique comptable.** Pas de « compte 625200 », pas de « compte 471000 », pas de débit/crédit. On veut un outil **simple et lisible** qui parle en langage humain :

- des **dépenses**,
- des **revenus**,
- des **virements entre mes comptes** (qui ne sont ni des dépenses ni des revenus),
- rangés dans des **catégories** parlantes,
- avec le **commerçant / tiers** quand c'est pertinent,
- pour pouvoir **analyser et comparer** dans le temps.

L'app est **mono-utilisateur** (usage familial privé), pas de multi-tenant, pas de partage public.

---

## 2. L'utilisateur et son foyer

- **Benoit** — titulaire principal, dirigeant d'une société (revenus d'activité).
- **Kwanchanok** — sa conjointe (revenus propres + sa propre carte bancaire).
- **Enfants** : **Vincent** (né fin 2020, **autiste** — nombreux soins spécialisés), **Noah** (né début 2023, crèche).
- **Famille élargie** : parents de Benoit, et la **famille de Kwanchanok en Thaïlande** (à qui on envoie du soutien financier).

Le foyer compte donc **~5 personnes** — élément important pour les comparaisons de budget (voir §7).

---

## 3. Les comptes gérés (multi-banques, multi-cartes)

Point clé : l'argent circule entre **plusieurs comptes** et **plusieurs cartes**. L'app doit gérer une **liste de comptes** paramétrable. Ceux qu'on utilise réellement :

| Compte | Banque | Rôle |
|---|---|---|
| Compte charges principal | Banque Populaire | Charges récurrentes du ménage + revenus |
| Compte joint | Banque Populaire | Loyers reçus de l'appart de Limoges + assurances |
| Compte dépôt secondaire | Banque Populaire | Petit compte + une carte |
| Compte joint Revolut | Revolut | Dépenses courantes du ménage |
| Compte perso Revolut | Revolut | Transit de la rémunération |
| Compte appart Limoges | Caisse d'Épargne | Prêt immobilier de Limoges |
| Compte charges | Caisse d'Épargne | Charges (assurances, box…) |
| Compte perso Benoit | Caisse d'Épargne | Petit compte + carte |
| Carte CB Kwanchanok | — | Dépenses par carte de la conjointe |
| Carte CB Benoit | — | Dépenses par carte de Benoit (a changé de n° en cours de route) |

**Ce qu'il faut retenir pour l'app :**
- Une **transaction est rattachée à un compte** (celui d'où l'argent part/arrive).
- Les **cartes** peuvent être vues comme des comptes ou comme un attribut ; l'important est de pouvoir filtrer « dépenses de la carte de X ».
- Chaque compte a un **solde** qui évolue dans le temps.
- Une même dépense n'apparaît **qu'une seule fois** (attention au « débit différé » des cartes — voir §6).

---

## 4. La donnée centrale : la TRANSACTION

C'est l'objet principal. Une transaction, c'est simplement :

- **Date**
- **Montant** (négatif = sortie d'argent, positif = entrée)
- **Libellé** (le texte brut du relevé, ex. « CARREFOUR LABEGE », « VIR HUMAN IMMOBILIER »)
- **Compte** concerné
- **Commerçant / tiers** (ex. Carrefour, Uber Eats, Human Immobilier, Dr Cheleux…) — normalisé, réutilisable
- **Catégorie** (voir §5)
- **Type de mouvement** : `Dépense` / `Revenu` / `Virement interne` / `Remboursement de crédit` (voir §6)
- **Récurrent ?** (oui/non — loyer, abonnement, assurance, échéance…)
- **Note libre** éventuelle
- **Statut** : catégorisée / à catégoriser (certaines lignes importées restent « à clarifier »)

**Import** : les transactions arrivent en masse (relevés PDF, exports JSON de l'agrégateur bancaire type Bridge). L'app doit permettre un **import en lot** puis une **catégorisation** (idéalement avec des **règles automatiques** : « si le libellé contient CARREFOUR → catégorie Alimentation, tiers Carrefour »). Beaucoup de règles de correspondance libellé→catégorie ont déjà été établies.

**Dédoublonnage** : à l'import, éviter les doublons (même date + même montant + même commerçant, ou même identifiant source).

---

## 5. Les catégories (le cœur du classement)

Liste **plate et lisible**, éventuellement à 2 niveaux (catégorie + sous-catégorie). Voici celles réellement utilisées, à reprendre comme base :

### Dépenses
- **Alimentation / restauration** (courses, boulangerie, restaurants, cafés)
  - sous-catégorie : **Livraison de repas** (Uber Eats, Deliveroo)
- **Shopping / achats divers** (vêtements, maison, déco, jouets, high-tech)
- **Santé** (pharmacie, médecin, parapharmacie, labo)
- **Loisirs / sorties** (parcs, jeux vidéo, activités)
- **Transports en commun** (Tisséo, Vélo Toulouse, métro, SNCF)
- **Péage autoroute**
- **Carburant & entretien véhicule** (+ lavage auto)
- **Abonnements** (Netflix, Canal+, Disney+, Spotify, Amazon, Uber One, presse, logiciels…)
- **Coiffure & soins personnels** (coiffeur, pressing)
- **Jeux & paris** (FDJ, tabac)
- **Stockage** (box de rangement)
- **Voyages / séjours** (hôtels, séjours, dépenses à l'étranger)
- **Dons & œuvres** (Croix-Rouge, Église, associations)
- **Loyer habitation principale**
- **Électricité / gaz**
- **Téléphone mobile** / **Internet box**
- **Assurances** (habitation, vie / prévoyance)
- **Crèche / garde enfant**
- **Garde à domicile** (emploi à domicile déclaré / CESU)
- **Frais bancaires** (agios, commissions d'intervention, frais d'incident, frais de saisie, cotisations)
- **Soutien familial versé** (aide à un proche — à qualifier fiscalement, potentiellement déductible)
- **Frais pro à refacturer** (timbre fiscal, coworking… à rembourser par la société)
- **Soins de Vincent (autisme)** — catégorie spéciale à **suivre par prestataire** (voir §6)

### Revenus
- **Salaire / revenus d'activité** (Benoit, via sa société)
- **Revenus du conjoint** (Kwanchanok)
- **CAF / prestations sociales**
- **CPAM / remboursements santé**
- **Crédit d'impôt / remboursements fiscaux**
- **Loyers perçus** (appartement locatif de Limoges = **revenu foncier**)
- **Autres recettes** (chèques, ventes d'occasion type Vinted, intérêts d'épargne)

### Mouvements « neutres » (ni dépense ni revenu — à exclure des analyses de dépenses)
- **Virements internes** (d'un de mes comptes vers un autre)
- **Transferts en devises** (Wise, vers l'étranger)
- **Retraits espèces**
- **Remboursements de crédit** (voir §6 — sorties d'argent mais pas de la « consommation »)

> ⚠️ **Règle d'or** : quand on additionne « mes dépenses », il faut pouvoir **exclure les virements internes et les remboursements de crédit** (sinon on compte deux fois, ou on gonfle artificiellement). L'app doit clairement distinguer ces types.

---

## 6. Concepts particuliers à modéliser (issus de cas réels)

Ce sont des subtilités rencontrées pendant le travail. Elles doivent être gérées simplement :

1. **Dépense de consommation vs remboursement de crédit vs virement interne**
   Trois natures très différentes qu'il faut séparer :
   - une dépense (courses, resto…) = consommation ;
   - un **remboursement de crédit** (ex. **Creatis** ~914 €/mois, ou l'ancien appartement **SNC Diamant** ~1 162 €/mois) = ça sort du compte mais ça rembourse une **dette**, pas de la consommation ;
   - un **virement interne** entre deux comptes à soi = neutre.

2. **Suivi des crédits / dettes**
   Pour un crédit (ex. Creatis) : connaître la **mensualité**, la **date de souscription**, le **nombre d'échéances restantes**, le **% du remboursement déjà effectué**, la date de fin. (On a calculé tout ça manuellement — l'app devrait le faire.)

3. **Revenu foncier (appartement de Limoges loué)**
   Loyers **reçus** chaque mois (via un gestionnaire, Human Immobilier). À suivre à part : montant, **évolution/indexation annuelle** (le loyer est révisé chaque année), total annuel (utile pour la **déclaration de revenus fonciers**). En face, les **charges de ce bien** (assurance habitation Limoges, syndic, prêt immo, frais de gestion) sont **déductibles** → il faut pouvoir les isoler.

4. **Soins de Vincent (enfant autiste)** — suivi renforcé
   Poste à part entière, à ventiler **par type de soin ET par prestataire** :
   - Équithérapie, Psychomotricité, Musicothérapie, Éducatrice spécialisée, Suivi psychologique, Adhésions associatives.
   - Les paiements sont **irréguliers / groupés** (on paie plusieurs séances d'un coup). L'app doit donner le total par type, par prestataire, par mois, par an. Utile pour les aides (MDPH/AEEH) et le crédit d'impôt.

5. **Débit différé des cartes** (à masquer)
   Les cartes à débit différé génèrent un **règlement mensuel groupé** (« facturette ») sur le compte, ET le détail des achats par ailleurs. **Il ne faut compter la dépense qu'une fois** : afficher le **détail par commerçant**, et neutraliser le règlement groupé. C'est purement technique côté banque — l'utilisateur ne doit **jamais** voir de double comptage.

6. **Commerçants / tiers récurrents**
   Beaucoup d'enseignes reviennent (Carrefour, Uber Eats, Zara, Starbucks, Le Rotisseur, pharmacies, prestataires de Vincent…). Elles doivent être des **entités réutilisables** pour permettre l'analyse « combien j'ai dépensé chez X ». Prévoir la **normalisation** des libellés bruts (ex. « CARREFOUR LABEGE », « CARREFOUR CITY », « CARREFOUR CARBURANTS » → tous « Carrefour », mais le carburant reste catégorie Carburant).

7. **Récurrences**
   Repérer les dépenses récurrentes (loyer, énergie, abonnements, assurances, crèche, échéances de crédit) pour : les prévoir, alerter si un prélèvement habituel manque, suivre leur évolution (ex. hausse d'un abonnement).

8. **Soutien familial**
   Virements réguliers à la famille de la conjointe (Thaïlande). À isoler dans une catégorie dédiée car **potentiellement déductible** fiscalement l'année suivante (pension à un ascendant / aide familiale).

---

## 7. Les analyses & questions à couvrir (LE PLUS IMPORTANT)

Voici, tirées telles quelles de notre travail, **les questions que je pose réellement**. L'application doit permettre d'y répondre facilement (dashboards, filtres, tableaux croisés, graphiques) :

### Vue d'ensemble & suivi
- **« On a des données de quand à quand ? »** → couverture temporelle par compte (dernière transaction, trous éventuels).
- **« Il me reste des choses non catégorisées ? »** → lister les transactions « à clarifier » et leur montant total.
- **« Ma compta du mois est-elle complète ? »** → contrôle par compte + repérage des lignes en attente.

### Dépenses
- **« Combien j'ai dépensé le mois dernier / les 3 derniers mois ? »** — total, **remboursements de crédit inclus ou non** (les deux vues).
- **« Quels sont mes plus gros postes de dépense ? »** — répartition par catégorie, sur une période.
- **« Détaille-moi une catégorie »** (ex. Shopping) — **top des enseignes**, par mois.
- **« Combien chez tel commerçant ? »** (ex. budget **Uber Eats** sur 3 mois).
- **Tableaux croisés** : dépenses **par catégorie × mois**, **par commerçant × mois**, **par prestataire × mois** (cas Vincent). (Sous Odoo on appelait ça des « pivots » — c'est la fonctionnalité clé d'analyse.)
- **« À combien on est sur la carte de X ce mois-ci ? »** — total par carte / par compte.

### Revenus & patrimoine
- **« Comment évoluent les loyers perçus de Limoges sur plusieurs années ? »** — courbe d'évolution + révisions annuelles + totaux annuels.
- Suivi des **revenus** par source et par mois.

### Crédits & dettes
- **« Où en est mon crédit Creatis ? »** — mensualité, échéances restantes, **% remboursé**, date de fin.
- **« Combien il me reste à payer sur l'ancien appartement (SNC Diamant) ? »** — total dû, échéances restantes.

### Soins de Vincent
- **« Combien m'ont coûté les soins de Vincent depuis le début de l'année ? »** — **par type de soin** et **par prestataire**, total + moyenne mensuelle.

### Comparaison & optimisation
- **« Par rapport à la moyenne, est-ce que mes postes de dépense sont logiques pour une famille de 5 ? »** — comparaison à des **repères nationaux** (type INSEE / budgets-types familiaux) par grand poste. Repérer les postes anormalement hauts (ex. frais bancaires) ou bas (ex. transport).
- **« Quelles dépenses pourrais-je basculer sur un moyen de paiement avantageux ? »** — croiser mes commerçants avec une liste d'enseignes éligibles (ex. cartes cadeaux) pour estimer un gain. (Cas réel : chèques culture → cartes multi-enseignes.)

### Contrôles de cohérence
- Vérifier qu'un **règlement groupé de carte** correspond bien à la somme des achats détaillés (repérer un écart = achats manquants).
- Repérer les **doublons**, les montants aberrants, les prélèvements récurrents absents.

---

## 8. Fonctionnalités attendues (synthèse)

1. **Comptes** : créer/gérer la liste des comptes et cartes, voir leur solde et son évolution.
2. **Import de transactions** en lot (fichiers relevés / exports agrégateur), avec **dédoublonnage**.
3. **Catégorisation** : manuelle + **règles automatiques** (libellé → catégorie + commerçant), avec une file « à catégoriser ».
4. **Commerçants / tiers** normalisés et réutilisables.
5. **Catégories** paramétrables (dépense / revenu / neutre), à 2 niveaux, avec la distinction **consommation / remboursement de crédit / virement interne**.
6. **Tableaux de bord & analyses** : totaux par période, répartition par catégorie, **tableaux croisés** catégorie/commerçant/prestataire × mois, top enseignes, graphiques d'évolution.
7. **Suivi des crédits** (échéancier, % remboursé, reste dû).
8. **Module « revenu foncier »** (loyers perçus vs charges déductibles de l'appartement locatif).
9. **Suivi dédié « Soins Vincent »** par type et prestataire.
10. **Récurrences & alertes** (prélèvement attendu manquant, hausse d'un abonnement).
11. **Comparaison à des repères** de budget familial.
12. **Export** (pour préparer les déclarations : revenus fonciers, dons, crédit d'impôt, soutien familial).

---

## 9. Principes directeurs

- **Simplicité avant tout** : langage humain, zéro jargon comptable, zéro plan de comptes.
- Une transaction = un montant + une date + un compte + une catégorie + (un commerçant). Rien de plus obligatoire.
- Toujours pouvoir répondre à : *« combien, quand, pour quoi, chez qui, sur quel compte »*.
- Bien séparer **ce qui est de la vraie dépense** de **ce qui n'en est pas** (virements internes, remboursements de dette).
- Penser **analyse dans le temps** (comparer mois à mois, année à année) dès la conception des données.
- Orientation **fiscale** en tête : pouvoir sortir facilement les chiffres utiles à la déclaration (revenus fonciers, dons, soins/handicap, soutien familial, crédit d'impôt garde d'enfant).

---

## 10. Exemples concrets de restitutions attendues

- Un **écran mensuel** : total dépensé (hors virements/crédits), répartition par catégorie en camembert, top 10 commerçants, comparaison au mois précédent.
- Un **tableau croisé** « catégorie × mois » sur l'année en cours.
- Une **fiche crédit Creatis** : « souscrit le JJ/MM/AAAA, mensualité X €, 135 échéances restantes, 25 % remboursé, fin prévue MM/AAAA ».
- Une **fiche appartement Limoges** : loyers perçus par mois (avec évolution), charges déductibles, résultat foncier de l'année.
- Une **fiche Vincent** : coût des soins par type et par prestataire, par mois et cumul annuel.
- Un **écran de comparaison** : mes postes vs repères d'une famille de 5, avec code couleur (dans la norme / élevé / faible).

---

## 11. Reprise des données existantes depuis Odoo (migration initiale)

Tout l'historique déjà mis en ordre vit dans une instance **Odoo** (`edu-perso-bguinet.odoo.com`, société « Benoit Guinet – Perso »). Il faut **l'extraire une fois** pour amorcer la base de la nouvelle app. On y accède par l'**API XML-RPC d'Odoo** (identifiant / clé API / URL de l'instance) — c'est le canal standard pour lire/exporter en masse.

### Où sont les données dans Odoo

- **Les transactions** = le modèle **`account.move.line`** (les « lignes d'écriture »). C'est la source à extraire. Champs utiles :
  - `date` → date de la transaction
  - `balance` → **montant** (positif/négatif ; c'est le champ à utiliser comme montant signé)
  - `name` → **libellé brut** de l'opération
  - `account_id` → le « compte comptable » Odoo → **à convertir en catégorie** (voir mapping ci-dessous)
  - `partner_id` → le **commerçant / tiers**
  - `journal_id` → le **compte bancaire / la carte** (BNK1…BNK8, CBK, CBB)
  - `parent_state` → ne garder que les écritures **`posted`** (comptabilisées)
- **Les relevés bruts** (avant catégorisation) = **`account.bank.statement.line`** (`date`, `amount`, `payment_ref`, `journal_id`). Moins utile pour la reprise puisque tout est déjà catégorisé côté `account.move.line`, mais c'est la vraie « ligne bancaire » d'origine.
- **Les comptes bancaires / cartes** = modèle **`account.journal`** (type `bank`). Donne la liste des comptes de l'app (nom, code BNKx/CBx, IBAN).
- **Les commerçants / tiers** = modèle **`res.partner`** (nom du commerçant).
- **Le référentiel des « comptes comptables »** (à transformer en catégories) = modèle **`account.account`** (code + libellé).
- **Les analyses déjà définies** (les « pivots ») = modèle **`ir.filters`** : elles décrivent exactement les tableaux croisés voulus (dépenses par catégorie/mois, shopping par commerçant/mois, soins Vincent par prestataire/mois…). À lire comme **spécification des rapports attendus**.

### La transformation clé : « compte comptable » Odoo → concept simple de l'app

C'est le cœur de la migration. Chaque `account_id` d'Odoo se traduit en **(type de mouvement + catégorie)** selon son code :

| Code du compte Odoo | Devient dans l'app |
|---|---|
| commence par **6** (6xxxx) | **Dépense** — la catégorie = le libellé du compte (ex. « Alimentation », « Shopping », « Santé »…) |
| commence par **7** (752, 758…) | **Revenu** — catégorie = libellé (salaire, CAF, loyers perçus, autres recettes…) |
| **580xxx** | **Virement interne** (neutre) |
| **164xxx** (164200 Creatis, 164300 ancien appart SNC Diamant, 164100 prêt immo Limoges) | **Remboursement de crédit** (neutre pour la conso, mais suivi comme dette) |
| **511xxx** (comptes de transit CB) | **Mouvement technique** (débit différé) → **à neutraliser / ignorer** (ne pas recréer en dépense) |
| **512xxx** | Ce sont les **comptes bancaires** eux-mêmes (soldes) — pas des transactions |
| **471000** | Ligne **« à catégoriser »** (compte d'attente Odoo) → à importer avec le statut *non catégorisé* |

> Le **détail exact du mapping libellé → catégorie** (toutes les enseignes, tous les cas particuliers) est déjà documenté dans la note du vault **`04-Comptabilité/Plan-Comptes-Perso-Odoo-v2.md`** et dans les règles de correspondance qu'on a construites. **C'est LA table de référence à reprendre** pour initialiser les règles de catégorisation automatique de l'app (§4).

### Autres correspondances

- **`journal_id`** (Odoo) → **Compte** de l'app (ex. BNK1 = « Compte charges BP », CBK = « Carte Kwanchanok 4561 »…). La liste complète est au §3.
- **`partner_id`** (Odoo) → **Commerçant** de l'app. Les tiers sont déjà normalisés dans Odoo (Carrefour, Uber Eats, les prestataires de Vincent, Human Immobilier…) — à reprendre tels quels.
- **Sous-catégories** : ex. « Livraison de repas » (Uber Eats) est un compte distinct sous Alimentation → devient une **sous-catégorie**.

### Marche à suivre pour l'extraction (fonctionnel)

1. Lire **`account.account`** → construire la table de correspondance *compte → (type, catégorie)* avec la logique ci-dessus.
2. Lire **`account.journal`** (type bank) → créer les **comptes** de l'app.
3. Lire **`res.partner`** → créer les **commerçants**.
4. Lire **`account.move.line`** (état `posted`, tout l'historique) avec les champs `date, balance, name, account_id, partner_id, journal_id` → créer les **transactions**, en appliquant la correspondance de l'étape 1 pour le **type + catégorie**, en rattachant le **compte** (journal) et le **commerçant** (partner).
5. **Écarter** les lignes des comptes **512xxx** (ce sont les côtés « banque » des écritures, redondants — on ne veut qu'une ligne par opération) et **neutraliser** les comptes de transit **511xxx** (débit différé) pour ne pas dédoubler.
6. Contrôler : le **total des dépenses par catégorie/mois** obtenu dans l'app doit **coïncider avec les tableaux croisés (`ir.filters`) d'Odoo** — c'est le test de non-régression de la migration.

### Points de vigilance de la reprise

- **Ne compter chaque opération qu'une fois** : dans Odoo une opération a deux « lignes » (côté banque 512xxx + côté catégorie). **Ne garder que la ligne « catégorie »** (le côté 6/7/580/164), pas le côté 512xxx.
- **Débit différé** : les « facturettes » de carte (comptes de transit 511xxx) ne sont pas des dépenses → ne pas les importer comme telles.
- **Signe du montant** : utiliser `balance` d'Odoo, mais **vérifier la convention de signe** (dans Odoo une dépense apparaît en positif sur un compte de charge) et la **réharmoniser** pour l'app (dépense = négatif, revenu = positif) — c'est un point à tester soigneusement sur quelques cas connus.
- **Lignes « à clarifier »** (compte 471000) : à importer avec le statut *non catégorisé*, pour finir le travail dans la nouvelle app.
- Après reprise, **l'app devient la source de vérité** ; Odoo peut être abandonné.
