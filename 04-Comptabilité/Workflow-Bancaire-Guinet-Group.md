---
tags: ["compta", "odoo", "guinet-group", "workflow-bancaire", "interne"]
created: 2026-05-12
parent: "[[Plan-Comptes-Perso-Odoo-v2]]"
liens_externes:
  - "[[Propositions-commerciales/2026/AREC-Occitanie - Impl ERP Gestion Affaires/_cr-demo-2026-05-07]]"
---

# Mise en place workflow bancaire — Guinet Group

> **Objectif** : déployer un workflow bancaire complet sur Guinet Group (instance Odoo `guinet`, company_id=1) — virements fournisseurs avec validation à étages + prélèvements clients récurrents en SDD + distribution multi-banque.
>
> **Bénéfice direct** : industrialiser les paiements Guinet Group (aujourd'hui partiellement manuels côté portail BP).
>
> **Bénéfice indirect** : valider en mains propres les capacités Odoo sur les 4 sujets que AREC nous a posés le 7 mai — pour les répondre solidement à la démo du 21 mai.

---

## Sujets de fond couverts

| # | Sujet | Usage Guinet Group | Usage attendu AREC |
|---|---|---|---|
| 1 | **Workflow validation virement** | Préparation factures fournisseurs + validation paiement avant émission | Idem côté AREC sur les paiements de leurs partenaires FITEO |
| 2 | **SEPA distribué multi-banque** | Routage des virements entre Banque Populaire et un 2e établissement (Qonto / Revolut Business) selon le journal | Routage entre CEMP et BPOC selon le compte payeur |
| 3 | **Sécurité forte** (FIDO / Certigref / eIDAS) | MFA Odoo + signature EBICS T côté BP | Idem |
| 4 | **Prélèvement SDD automatisé** | Recouvrement clients récurrents — 1er cas : Globasoft 300 €/mois | Recouvrement loyers FITEO, intérêts CCA, etc. |

---

## Choix de l'entité : **Guinet Group (instance `guinet`, company_id=1)**

### État actuel des comptes bancaires (inspecté 12/05)

| Instance / Société | Banque(s) | Verdict |
|---|---|---|
| `globasoft` Globasoft (co=1) | **Revolut x3** comptes (principal, TVA, FR7628233...) | ❌ Mono-banque néobanque UK, pas d'EBICS, ICS Créancier SEPA non natif, distribution multi-banque impossible |
| `guinet` Guinet Group (co=1) | **Banque Populaire Occitane x3** (compte 4463, CB 8343, générique) | ✅ Banque française traditionnelle, EBICS T supporté, ICS facile à obtenir, multi-comptes opérationnel |
| `guinet` GDG (co=4) | Config partielle / bancale (un journal "GLOBASOFT XX7328" douteux) | ⚠️ À nettoyer avant de l'utiliser |

### Pourquoi Guinet Group plutôt que Globasoft

1. **Banque Populaire** = banque française traditionnelle, environnement le plus proche de **CEMP + BPOC** chez AREC — protocoles EBICS T, SDD complet avec ICS Créancier, PAIN.001/008 standard
2. **Revolut limité côté Odoo** : connecteur en lecture statements OK, **émission SDD / virements par lot non supportée nativement**. Le workflow validation passe par l'app Revolut Web, pas par Odoo → impossible à industrialiser.
3. **3 comptes BP déjà actifs** sur Guinet Group → distribution intra-banque opérationnelle dès J0
4. **Volume réel** : Guinet Group a déjà du flux fournisseurs et client → le workflow industrialisé sert immédiatement, pas juste pour la démo

---

## Plan de mise en place

### Phase 1 — Préparation (J1-J3)

| # | Action | Pré-requis | Durée |
|---|---|---|---|
| 1.1 | Activer modules Enterprise : `account_accountant`, `account_sepa`, `account_sepa_direct_debit`, `account_batch_payment` | Licence Enterprise active | 15 min |
| 1.2 | **Demande d'ICS Créancier SEPA** auprès de Banque Populaire | Démarche externe (2-3 j bancaires) | 30 min de paperasse + délai BP |
| 1.3 | Ouvrir / activer un **2e compte banque** (Qonto Pro ou Revolut Business) — utile pour la distribution multi-banque réelle et pour ne plus mettre tous les œufs chez BP | Décision dirigeants Guinet Group | Variable (Qonto = quelques jours, Revolut = 1 j) |
| 1.4 | Nettoyer le journal BNK1 "Bank" générique sans IBAN sur Guinet Group | — | 5 min |

### Phase 2 — Workflow validation virement (J4)

| # | Action | Critère d'acceptation |
|---|---|---|
| 2.1 | Activer **double validation paiements** : Settings → Accounting → Outgoing Payments | Champ "Double Validation" visible sur les paiements |
| 2.2 | Configurer **règles par montant** : `< 1 000 € = 1 validation, ≥ 1 000 € = 2 validations` | Une facture fournisseur ≥ 1 000 € exige 2 utilisateurs distincts pour valider |
| 2.3 | Définir les **rôles** sur Guinet Group : **préparateur** = compte fonctionnel `factures@guinet-group.com` (compta), **validateur** = Benoit Guinet (dirigeant) | Groupes Odoo paramétrés, droits cohérents. Workflow à 2 étapes (préparation + validation) puisqu'on est sur une PME — on simulera la 2e validation si nécessaire pour démontrer la mécanique AREC à 3 niveaux |
| 2.4 | Premier batch réel : 3-5 virements fournisseurs Guinet Group à différents montants → workflow complet | Statusbar du paiement reflète les étapes (`draft → validated_1 → validated_2 → sent`) |

### Phase 3 — Distribution multi-banque (J5)

| # | Action | Critère d'acceptation |
|---|---|---|
| 3.1 | Ajouter le 2e journal banque (Qonto / Revolut) dans Odoo Guinet Group | Journal `BNK4` actif avec IBAN renseigné |
| 3.2 | Préparer un **batch de paiements** mélangeant BP + 2e banque (selon nature du paiement / fournisseur) | Batch contient des paiements avec `journal_id` différents |
| 3.3 | Générer le fichier **PAIN.001** depuis le batch | 1 fichier PAIN.001 par banque (pas un fichier mixte), avec `<DbtrAgt>` correct |
| 3.4 | Déposer le fichier BP côté **portail BP** (ou EBICS si configuré) + 2e banque côté son propre canal | Confirmation visuelle des virements émis sur les 2 banques |

### Phase 4 — Prélèvement SDD client (J6-J7) — 1er cas : Globasoft 300 €/mois

| # | Action | Critère d'acceptation |
|---|---|---|
| 4.1 | Créer `res.partner` **GLOBASOFT** dans Guinet Group (si pas déjà) avec IBAN Revolut + BIC | Partner actif, données bancaires complètes |
| 4.2 | Créer **mandat SEPA SDD** Globasoft → Guinet Group, type "récurrent (RCUR)", date signature, UMR unique | Mandat `state=valid` avec ICS Guinet Group |
| 4.3 | Créer **abonnement Odoo** : 300 € HT/mois, échéance le 5 du mois, mode paiement "SEPA Direct Debit" | Subscription `state=in_progress`, prochaine facture programmée |
| 4.4 | Au déclenchement (le 5 du mois courant ou en avance manuelle pour la démo) : facture générée + batch SDD | Facture posted, batch créé, fichier PAIN.008 généré |
| 4.5 | Valider PAIN.008 : `CdtrAgt`=BP, `DbtrAgt`=Revolut, montant 300 €, date d'exécution conforme SEPA (D-2 ou D-5 selon FRST/RCUR) | XML conforme PAIN.008.001.02 (norme SDD CORE) |
| 4.6 | Dépôt côté BP (portail ou EBICS) | Confirmation prélèvement sur Globasoft sous 2 j ouvrés |

### Phase 5 — Sécurité forte (J8 — exploratoire)

> Voir analyse détaillée plus bas dans **[Annexe — Sécurité forte : qu'est-ce qui est réellement faisable ?](#annexe--sécurité-forte--qu'est-ce-qui-est-réellement-faisable)**

| # | Action | Critère |
|---|---|---|
| 5.1 | **MFA TOTP natif Odoo 19** déjà actif sur les utilisateurs validateurs Guinet Group | Connexion à Odoo exige le 2e facteur (Google Authenticator) — déjà en place |
| 5.2 | Documenter la **chaîne complète Odoo → BP** : auth utilisateur Odoo (TOTP) + validation côté portail BP web (manuelle, niveau 1) | Schéma capturé pour la démo AREC |
| 5.3 | Identifier **les gaps explicites** entre les besoins AREC et ce que Odoo 19 + BP fournissent — produire la note de positionnement | Document remis à AREC pour la réunion 21/05 |

---

## Livrables

À l'issue de la mise en place (avant **20 mai 2026**) :

1. **Workflow bancaire opérationnel** sur Guinet Group — validation virement industrialisée + 1er prélèvement Globasoft 300 € exécuté
2. **Note de positionnement AREC** sur les 4 sujets — réponse argumentée à intégrer dans la propale et en réunion 21/05
3. **Captures écran Odoo** : workflow validation, batch payment, fichier PAIN.001/008, dashboard trésorerie multi-comptes
4. **Démo live possible le 21/05** avec données réelles Guinet Group
5. **Gap analysis** : natif Odoo / custom Odoo / non faisable / délégué au canal banque

---

## Risques / dépendances

| Risque | Impact | Mitigation |
|---|---|---|
| ICS Créancier SEPA pas obtenu avant le 20/05 | SDD non démontrable, prélèvement Globasoft 300 € reporté | **Lancer la démarche BP dès le 12/05** (J-9) |
| 2e banque pas ouverte / activée à temps | Multi-banque non démontrable en live, fallback sur journal fictif | Démarche Qonto Pro = ~3 jours, Revolut Business = 1 jour ouvré |
| Module `account_sepa_direct_debit` non installé / payant | SDD non opérationnel | Vérifier dès J1, installer/acquérir |
| 1er prélèvement SDD Globasoft trop tardif pour la démo 21/05 | Pas de cycle complet à montrer | Déclencher manuellement une facture 300 € hors cycle pour la démo |
| Subscription Odoo récurrente non synchronisée avec mandat | Risque double facturation | Vérifier `next_invoice_date` cohérent + UMR du mandat lié à la subscription |

---

## Implications business

> Ce déploiement n'est pas une démo jetable — c'est un **outil opérationnel pérenne** pour Guinet Group. À terme, tous les recouvrements clients récurrents et les virements fournisseurs passent par ce flow.
>
> **Premier cas réel** : prélèvement mensuel Globasoft 300 € (refacturation interne).
>
> **Cas suivants à industrialiser** : autres clients récurrents Guinet Group, virements fournisseurs habituels (loyer, prestataires, charges).
>
> En miroir, ce déploiement vivant nous met dans la peau de l'utilisateur AREC — on saura exactement ce qui marche / ce qui demande du custom / ce qui frotte côté ergonomie. C'est la meilleure préparation possible pour la démo du 21/05 et pour la phase d'implémentation AREC.

---

## Annexe — Sécurité forte : qu'est-ce qui est réellement faisable ?

> **Question AREC du 7/5** : "Sur la sécurité : Clé FIDO ? Certigref ? eIDAS ?"
>
> Recherche menée le 12/05/2026 sur les modules Odoo, les protocoles bancaires français et les solutions middleware. Cette section vise à arbitrer ce qu'on déploie réellement sur Guinet Group et à préparer la réponse argumentée pour AREC.

### Le malentendu à clarifier en premier

**La "sécurité forte" pour un virement bancaire couvre deux mécanismes distincts** qu'il faut traiter séparément :

| Mécanisme | Qu'est-ce qu'il authentifie ? | Où ça se passe ? |
|---|---|---|
| **A. Authentification utilisateur dans l'ERP** | "C'est bien Pierre Dupont qui a cliqué *Valider* à 14h32" | Connexion Odoo |
| **B. Signature cryptographique du fichier de virement** | "Le fichier PAIN.001 déposé en banque a bien été signé par Pierre Dupont (preuve non-répudiable)" | À la sortie d'Odoo / Avant dépôt banque |

Ces deux mécanismes sont **complémentaires** mais ils utilisent des technologies différentes et n'ont pas les mêmes exigences réglementaires.

→ **Question à poser à AREC** : sur les 2 plans, quel est le besoin réel ? Aujourd'hui IBIX couvre-t-il les deux ou juste B ?

---

### Plan A — Authentification utilisateur dans Odoo 19

#### Ce qui est natif dans Odoo 19 (déjà disponible, déjà utilisé chez Guinet Group)

- **MFA TOTP** : application Google Authenticator / Authy / Microsoft Authenticator → code à 6 chiffres renouvelé toutes les 30 sec
- Configurable directement dans le module utilisateur (`Mon profil → Préférences → Two-Factor Authentication`)
- Activable par chaque utilisateur, désactivable par l'admin
- **Audit log** sur les actions sensibles (modification paiement, validation) — niveau Enterprise

> **Vérifié sur la doc officielle Odoo 19** : MFA TOTP est la **seule méthode native**. Pas de support natif FIDO2 / WebAuthn / Passkeys / clés physiques dans Odoo 19 standard.

#### Ce qui demande un module ou un middleware (pour aller au-delà de TOTP)

| Solution | Source | Ce qu'elle apporte | Pertinence pour nous |
|---|---|---|---|
| **SSO Odoo ↔ IdP entreprise** (via `auth_oauth` natif Odoo) | Module Odoo natif + IdP type Keycloak / Azure AD / Google Workspace | Délègue l'auth à l'IdP qui lui fait du FIDO2/WebAuthn/Passkeys/MFA selon ses propres règles | **C'est le pattern recommandé** pour les ETI — l'auth forte est gouvernée par la DSI au niveau IdP, pas par chaque application |
| **Module Odoo Apps `auth_passkey`** (si existe en 19) ou équivalent | Marketplace Odoo / OCA | Ajoute WebAuthn / Passkeys directement à la page de login Odoo | À évaluer si la maturité Odoo 19 est suffisante — sinon préférer SSO |
| **MasterKey Connector** (Odoo Apps Store, payant) | Éditeur tiers | Passwordless FIDO2 sur Odoo | Plutôt pour des cas de niche, prudence en prod |

#### Niveau eIDAS — où on se situe

- **MFA TOTP natif Odoo 19** = authentification simple renforcée (DSP2 SCA compatible) → **suffit pour 95% des usages opérationnels**, y compris la validation de virements à montants courants
- **SSO Odoo ↔ IdP avec FIDO2/Passkeys** = authentification forte (niveau eIDAS "substantiel" si l'IdP est configuré pour)
- **eIDAS "élevé"** (certificat qualifié sur support matériel type carte CNIE ou token CertEurope qualifié) = pas dans le scope d'un ERP métier, ça concerne la signature de documents engageants, pas la connexion à Odoo

#### Verdict côté Guinet Group

- **État actuel** : MFA TOTP natif Odoo 19 actif sur le compte Benoit Guinet → à étendre au compte fonctionnel `factures@guinet-group.com` lors de la mise en place du workflow validation virement
- **À étudier si besoin futur** : SSO Google Workspace ↔ Odoo via `auth_oauth` si on veut centraliser l'auth de toutes nos apps Globasoft/Guinet
- **À ne pas faire** : pas de module FIDO2/Passkeys spécifique à Odoo aujourd'hui — pas justifié, et risque maintenance sur les modules tiers

#### Verdict côté AREC

- AREC ETI = très probablement déjà équipée d'un **IdP entreprise** (Azure AD / Entra ID, Okta, ou autre)
- **Recommandation à porter en réunion 21/05** : SSO Odoo ↔ IdP AREC via `auth_oauth` natif Odoo 19, avec MFA et FIDO2/Passkeys gérés par leur IdP existant
- **Avantages** :
  - Gouvernance auth centralisée (DSI AREC gère un seul endroit)
  - Conforme à leurs politiques sécurité actuelles (probablement déjà alignées eIDAS substantiel)
  - Pas besoin de module FIDO2 dans Odoo → moins de surface de maintenance
  - Compatible avec leur SI existant (provisionnement automatique des utilisateurs Odoo depuis l'AD)
- **Question à AREC** : quel IdP utilisez-vous aujourd'hui pour vos autres applications métier ?

---

### Plan B — Signature cryptographique du fichier de virement

C'est ici que ça se complique vraiment. Odoo génère un fichier `PAIN.001` (virements) ou `PAIN.008` (prélèvements) — un fichier XML standardisé. **Mais Odoo ne signe pas ce fichier nativement.** La signature électronique cryptographique se fait par un autre composant.

#### Les 3 niveaux de communication banque

| Niveau | Protocole | Comment c'est signé ? | Validité légale |
|---|---|---|---|
| **1. Portail web banque** | Upload manuel du PAIN.001 sur le portail BP / CEMP / Qonto | Validation utilisateur dans le portail web banque (login + MFA banque) — **pas de signature sur le fichier** | Suffisant en pratique pour PME et même ETI |
| **2. EBICS T** ("Transport") | Transmission automatisée du fichier par EBICS, **sans signature dans le fichier** | Validation finale **séparée** via le portail web banque (par le même utilisateur ou un autre) | Idem niveau 1 — automatise juste la transmission |
| **3. EBICS TS** ("Transport + Signature") | Transmission automatisée + **signature électronique XML attachée au fichier** | Signature avec **certificat qualifié sur support matériel** (USB token) avant transmission → non-répudiable et immédiatement exécutable côté banque | Niveau supérieur, équivalent eIDAS "avancé" voire "qualifié" selon le certificat |

#### Quels certificats pour EBICS TS ?

Banque Populaire (et la plupart des banques françaises) accepte plusieurs autorités de certification :

| Certificat | Émetteur | Particularité | Durée | Coût indicatif |
|---|---|---|---|---|
| **SWIFT 3SKey** | SWIFT (groupe interbancaire) | USB token, accepté par toutes les banques signataires de la convention 3SKey (~90% des grandes banques fr) | 3 ans | ~150 € / token + activation |
| **CertEurope** | Filiale CertEurope (groupe Oodrive) | Certificat sur USB token, **certifié RGS 2-étoiles** (signature qualifiée niveau intermédiaire) — proposé directement par BP | 3 ans | À demander BP (~200-400 € selon nb signataires) |
| **Keyneticks / ClicNTrust** | Autres prestataires français | Variantes équivalentes | 3 ans | Similaire |

"**Certigref**" mentionné par AREC : pas trouvé en tant qu'autorité de certification — probablement une appellation interne AREC ou une confusion avec **Certinomis** (autre AC française). À leur demander de préciser.

#### Modules Odoo pour EBICS

**Module `account_ebics` (Noviat / OCA)** — Odoo 17/18/19 disponible :

- Échange de fichiers PAIN.001/PAIN.008/CAMT.053 via EBICS
- Téléchargement automatique des statements bancaires
- **Couvre EBICS T** (transport sans signature) ✅
- **EBICS TS (avec signature)** : à confirmer dans le code/doc — la signature requiert un token physique branché sur la machine, ce qui complique l'intégration dans un Odoo Cloud (Odoo.sh ou SaaS). Plutôt **non supporté nativement**.

**Pour EBICS TS, il faut un middleware externe** :

| Middleware | Fournisseur | Usage typique |
|---|---|---|
| **Sage XRT** (anciennement XRT, racheté par Sage) | Sage | Le standard du marché trésorerie multi-banques, EBICS TS complet, intégration ERP possible (y compris Odoo via fichier ou API) |
| **Cegid Trésorerie** | Cegid | Concurrent direct de Sage XRT |
| **JeBICS** (open source) | Communauté | Bibliothèque Java EBICS, peut être wrappée dans un middleware custom — utilisé par certaines équipes IT internes |
| **BancStar** | Mata-IO et autres | Solution dédiée à la communication bancaire avec signature TS |
| **IBIX** (utilisé par AREC) | Editeur français | Équivalent fonctionnel à Sage XRT — c'est probablement le rôle qu'il joue chez AREC |

#### L'architecture cible réaliste

```
                    ┌─────────────┐
                    │    Odoo     │ ← prépare PAIN.001/008
                    └──────┬──────┘
                           │ fichier XML standard
                           ▼
                  ┌─────────────────┐
                  │   Middleware    │ ← signe le fichier avec
                  │  (Sage XRT,     │   le certificat USB
                  │   IBIX, etc.)   │   (3SKey / CertEurope)
                  └────────┬────────┘
                           │ fichier signé EBICS TS
                           ▼
                  ┌─────────────────┐
                  │   Banque        │ ← vérifie la signature,
                  │   (BP, CEMP,    │   exécute immédiatement
                  │   BPOC...)      │
                  └─────────────────┘
```

**Pour Guinet Group** : on n'a pas besoin de cette architecture (volume virements faible). On reste sur **niveau 1 (portail BP web)** ou **niveau 2 (EBICS T via account_ebics)**.

**Pour AREC** : si IBIX joue le rôle de middleware EBICS TS, l'architecture cible est :

```
Odoo (génère PAIN) → IBIX (signe TS) → CEMP/BPOC
```

→ **Faisable techniquement**, mais nécessite de qualifier l'API IBIX (fichier dropbox ? API REST ? upload manuel ?). À demander à AREC en réunion 21/05.

#### Alternative pour AREC sans IBIX

Si AREC veut se débarrasser d'IBIX et faire tout en natif Odoo, la solution serait :

1. Module **`account_ebics`** (Noviat) → couvre EBICS T (transport)
2. **Validation manuelle** côté portail web CEMP/BPOC pour les ordres ≥ seuil
3. Ou **développement custom** d'un module Odoo EBICS TS qui sait piloter un USB token branché sur un serveur — **non trivial**, ~30-40 j/h dev minimum

C'est probablement **le scope d'un avenant éventuel** si AREC veut sortir d'IBIX à terme.

---

### Plan B — Signature électronique des documents (autre sujet)

À ne pas confondre avec la signature des virements : il existe aussi le besoin de signature électronique de **documents** (contrats, mandats SEPA, conventions CCA...).

| Outil | Niveau eIDAS | Usage Guinet Group / AREC |
|---|---|---|
| **Odoo Sign** (natif) | Niveau 1 (simple) | Mandats SEPA internes, accusés de réception → suffit |
| **Yousign** (intégré dans le POC FITEO) | Niveau 1 à 2 (simple à avancée selon offre) | Contrats commerciaux, factures, mandats opposables → notre cas standard |
| **DocuSign Identify / Universign** | Niveau 3 (qualifiée) | Actes engageants à fort enjeu (cessions, actes notariés) → rare en pratique chez nos clients |

→ Pour Guinet Group, **Odoo Sign + Yousign** couvre tout. Pas besoin de niveau 3.

---

### Synthèse — Ce qu'on fait sur Guinet Group, ce qu'on dit à AREC

#### Pour Guinet Group (déploiement réel)

| Plan | Action concrète | Quand | Coût |
|---|---|---|---|
| Plan A — Auth | **MFA TOTP natif Odoo 19** actif sur Benoit Guinet | ✅ Fait | 0 € |
| Plan A — Auth | Activer TOTP sur le compte fonctionnel `factures@guinet-group.com` (préparateur) | J1 (5 min) | 0 € |
| Plan B — Signature virement | **Niveau 1** : génération PAIN.001 dans Odoo + dépôt manuel portail BP + validation BP web | J0 | 0 € |
| Plan B — Évolution future | Évaluer EBICS T via `account_ebics` Noviat si volume virements > 20/mois | T+3 mois | Module gratuit, mais demande configuration EBICS BP (~200 € setup) |
| Plan B — Signature document | Odoo Sign natif pour les mandats SEPA internes | J0 | 0 € |

→ **Pas de certificat 3SKey / CertEurope sur Guinet Group** : pas justifié pour notre volume actuel.
→ **Pas de module FIDO2 / U2F** : TOTP natif suffit pour notre besoin sécurité.

#### Pour la réponse à AREC le 21/05

**Message en 3 temps :**

1. **Clarifier le besoin** (Plan A vs Plan B) : "Quand vous parlez de sécurité forte, vous adressez l'authentification de la personne qui valide dans l'ERP, ou la signature cryptographique du fichier transmis à la banque ? Ou les deux ?"

2. **Sur Plan A (auth Odoo)** :
   - **MFA TOTP natif Odoo 19** (Google Authenticator) — suffit pour la majorité des usages opérationnels, c'est ce qu'on utilise nous-mêmes sur Guinet Group
   - **SSO Odoo ↔ IdP AREC** (Azure AD / Okta / autre) via le module `auth_oauth` natif Odoo → c'est l'IdP qui impose FIDO2/Passkeys/MFA selon votre politique sécurité existante. **C'est le pattern recommandé pour vous** : gouvernance auth centralisée DSI, pas de module tiers Odoo à maintenir.
   - **Pas de blocage technique** — c'est cadré dès l'install Odoo 19

3. **Sur Plan B (signature fichier)** :
   - Odoo génère PAIN.001/008 conformes
   - **Odoo ne signe pas le fichier** : la signature TS (avec 3SKey/CertEurope) est faite par un middleware externe (votre IBIX actuel joue ce rôle)
   - Architecture cible : Odoo → IBIX (signature TS) → CEMP/BPOC (inchangée par rapport à aujourd'hui)
   - **Question à AREC** : voulez-vous garder IBIX comme middleware EBICS TS, ou souhaitez-vous étudier sa suppression (sortie IBIX = scope d'avenant à chiffrer si oui)
   - **Question à AREC** : "Certigref" est-il un nom interne ? = Certinomis ou CertEurope ? Quel(s) certificat(s) vos signataires détiennent-ils aujourd'hui ?

#### Incidence sur nos sociétés (Globasoft / Guinet Group)

**Côté authentification (Plan A) :**
- **Odoo 19 Guinet Group** : MFA TOTP natif actif sur Benoit Guinet — à étendre à `factures@guinet-group.com` (compte fonctionnel compta) lors du déploiement
- *Note de périmètre* : Mahdi Zouaoui n'a pas accès à l'instance `guinet` (il est sur `globasoft1` uniquement) → toute la mise en place workflow Guinet Group est portée côté `factures@guinet-group.com` (préparateur) + Benoit (validateur)
- **Pas de YubiKey / FIDO2 prévu** : surdimensionné pour une petite structure, le TOTP couvre largement le besoin
- **SSO Google Workspace ↔ Odoo** envisageable à terme si on veut centraliser l'auth de toutes les apps Globasoft/Guinet (config `auth_oauth` natif Odoo) → à étudier hors scope court terme

**Côté signature virement (Plan B) :**
- **Globasoft (Revolut)** : Revolut n'a pas d'EBICS TS, et la validation Revolut passe par leur portail web → workflow validation Odoo non transposable directement. **C'est pour ça qu'on ne déploie pas la mise en place sur Globasoft.**
- **Guinet Group (BP)** : on déploie le **niveau 1** (Odoo génère PAIN.001 + dépôt manuel portail BP + validation BP web par 2e personne) — robuste et suffisant pour notre volume. Si Guinet Group grandit, on pourra basculer sur EBICS T (module `account_ebics`) plus tard.
- **À terme** : si on veut une vraie signature TS interne (par exemple si Guinet Group facture des montants à 5 chiffres récurrents), on prend un token CertEurope chez BP. Coût ~300 € + 200 €/an renouvellement. Inutile pour l'instant.

---

## Sources externes consultées

- [Odoo 19 — Two-factor authentication (doc officielle)](https://www.odoo.com/documentation/19.0/applications/general/users/2fa.html)
- [EBICS TS — Mata-IO](https://www.mata-io.com/comment-fonctionne-le-protocole-ebics-ts/)
- [Banque Populaire — CertEurope](https://www.banquepopulaire.fr/entreprises/comptes-flux/le-certificat-electronique-certeurope/)
- [Module account_ebics — Noviat sur GitHub](https://github.com/Noviat/account_ebics)
- [Odoo Sign — documentation officielle](https://www.odoo.com/documentation/18.0/applications/productivity/sign.html)
- [Vox-Fi — Sécurisation paiements EBICS TS](https://www.finance-gestion.com/vox-fi/securisation-des-paiements-debics-ts/)
- [Caisse d'Epargne — Vérification bénéficiaire EBICS TS](https://www.caisse-epargne.fr/faq-entreprises/virements/realisation-dun-virement/pro-comment-fonctionne-le-service-de-verification-du-beneficiaire-pour-les-virements-teletransmis-via-les-protocoles-ebics-ts-ou-swiftnet-fileact/)
- [Newsroom BPCE — Natixis 3SKey](https://newsroom.groupebpce.fr/actualites/natixis-1re-banque-a-commercialiser-3skey-sur-tous-les-protocoles-de-communication-bancaire-04a6-7b707.html)
- [Sage XRT EBICS](https://sxbe-onlinehelp.sage.com/PDF/SXBE/SXBE.12.1.EBICS.3.0.UserGuide_FR.pdf)
- [Xperdoo — Signature électronique Odoo niveau eIDAS](https://www.xperdoo.fr/blog/pme-2/la-signature-electronique-sur-odoo-21)

---

*Note interne — déploiement opérationnel Guinet Group, lancé en parallèle de la préparation démo AREC du 21/05/2026.*
