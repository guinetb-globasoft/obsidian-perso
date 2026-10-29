---
tags: ["ia", "agents", "skills", "claude", "daf", "compta", "architecture"]
created: 2026-09-13
---

---
type: note
domaine: IA / Direction financière
statut: brouillon
créé: 2026-09-13
tags: [ia, agents, skills, claude, daf, compta, architecture]
---

# Architecture agents & skills pour une direction financière multi-équipes

> Retour d'expérience tiré de la construction du skill `compta-groupe` (groupe Guinet).
> Public visé : DAF avec plusieurs équipes, majorité sur **Claude web**, 1-2 personnes sur **Claude Code**.

## 1. Principe fondateur — séparer 4 couches

La plupart des setups empilent « instructions + procédures + accès + rôle » dans un seul prompt. À l'échelle d'une DAF, ça devient ingérable. Il faut séparer :

| Couche | C'est quoi | Où ça vit | Qui la touche |
|---|---|---|---|
| **1. Socle / référentiel** | Invariants du groupe : règle d'or (l'entité = la banque qui paie), mapping sociétés↔banques↔instances↔drive, règles TVA, conventions de nommage, garde-fous | 1 skill « socle », versionné en git | 1 owner (DAF) |
| **2. Playbooks** | Le « comment faire X » par domaine : saisir une facture fournisseur, lettrer une carte, faire une déclaration TVA, un cut-off | 1 skill par domaine, qui charge le socle | 1 référent par domaine |
| **3. Rôles / agents** | Qui fait quoi, avec quel périmètre | Projects (web) / subagents (Code) | Chaque équipe |
| **4. Mains** | Accès réels : Odoo, Drive, Gmail, banque | Connectors (MCP) | IT / DAF, en droits **minimaux** |

**Idée clé** : le savoir (couches 1-2) est partagé et versionné ; les mains (couche 4) sont scopées par droits ; les rôles (couche 3) ne font que combiner les deux. Un changement de règle (ex. correction TVA G/S) se fait **une fois dans le socle** et se propage à tout le monde.

## 2. Découper la DAF par domaine (= par équipe)

Ne pas faire un skill par société — les mappings d'entité sont de la **donnée** dans le socle, pas une frontière. Découper par **domaine métier**, car c'est ce qui correspond à une équipe et à un owner :

- **AP** — comptabilité fournisseurs (saisie, rapprochement, paiement)
- **AR** — clients (facturation, encaissement, relances, lettrage)
- **Trésorerie / banque** — import relevés, rapprochement, prévi
- **TVA / fiscal** — déclarations, contrôles
- **Clôture / reporting** — cut-off, FNP/CCA, liasse, conso groupe
- **NDF / paie**

Chaque domaine = **1 skill (playbook + fiches par entité) + 1 Project sur le web**. Tous chargent le socle.

## 2 bis. Bien comprendre les agents (le morceau flou)

Un skill se visualise (« un manuel ») ; un agent est plus abstrait. L'analogie qui débloque :

- **Skill = un manuel de procédure sur l'étagère.** Durable, partagé, écrit une fois, tout le monde peut l'ouvrir. Passif.
- **Agent = un employé avec une fiche de poste.** Il a un **mandat**, un **badge qui ouvre certaines portes**, et il **pioche dans les manuels** (skills) dont il a besoin. Actif.

On **écrit les manuels une fois** (skills) ; on **« recrute » des employés par rôle** (agents). Un agent sans skill = un intérimaire sans méthode ; un skill sans agent = un manuel que personne n'ouvre.

### Ce qui *définit* un agent — 4 attributs

| Attribut | Question | Exemple (agent Fournisseurs) |
|---|---|---|
| **Mandat** | Il fait quoi, point final | Comptabiliser et préparer le paiement des factures fournisseurs |
| **Périmètre** | Sur quoi il a le droit d'agir | Sociétés GDG + ESN, journaux d'achat + banque **en lecture** |
| **Outils / droits** | Quelles mains, en lecture ou écriture | Odoo : écriture sur les bills ; Gmail : lecture ; Drive : dépôt |
| **Autonomie / passe-plat** | Jusqu'où seul, quand il s'arrête et à qui il passe | Prépare en `dry_run`, s'arrête avant de poster/payer → validation |

> Crucial en finance : **c'est le périmètre + les droits qui rendent un agent sûr**, pas son intelligence. Un agent « super-comptable » qui touche tout sur toutes les sociétés est un danger ; un agent au mandat étroit est prévisible et auditable.

### La relation agent ↔ skill

- **Le skill dit COMMENT.** L'agent dit **QUI peut, et SUR QUOI**.
- Un agent **charge** un ou plusieurs skills : toujours le **socle** + le playbook de son domaine.
- Les **skills sont partagés** (même playbook pour tous) ; les **agents sont scopés** (AP-GDG et AP-ESN chargent le même skill mais n'ont ni le même périmètre ni les mêmes droits).
- **Les droits suivent l'agent, jamais le skill.** Le manuel de virement existe pour tous ; seul l'agent « trésorier » a le badge qui déclenche un paiement.
- Conséquence : **les skills sont le capital durable, les agents sont reconfigurables/jetables.** Un agent = une combinaison **{skills + périmètre + droits}** pour un job ; on peut monter un agent « Clôture Q3 » le temps d'une campagne puis le jeter.

### Cartographie des agents d'une DAF

Un agent par domaine/équipe (le « faiseur » spécialiste), plus 1-2 transverses :

| Agent | Mandat | Skills chargés |
|---|---|---|
| **Fournisseurs (AP)** | Saisir/rapprocher/préparer paiement fournisseurs | socle + `ap-fournisseurs` |
| **Clients (AR)** | Facturer, encaisser, relancer, lettrer clients | socle + `ar-clients` |
| **Banque / Trésorerie** | Importer relevés, rapprocher, prévi | socle + `banque-lettrage` |
| **TVA / Fiscal** | Préparer déclarations, contrôler | socle + `tva-fiscal` |
| **Clôture** | Cut-off, FNP/CCA, liasse (transverse) | socle + tous les playbooks en lecture |
| **Contrôle** (relecteur) | Vérifier avant validation — **séparation des tâches** | socle, **lecture seule partout** |

L'agent **Contrôle** est le plus sous-estimé : il n'écrit rien, il relit le travail d'un autre agent avant validation humaine (« 4 yeux » porté dans l'archi).

### Les 3 modes de collaboration

1. **Solo** (le quotidien) : 1 agent + validation humaine. ~90 % des cas.
2. **Faiseur + Relecteur** : sur ce qui poste ou paie, l'agent métier prépare (dry-run), l'agent Contrôle relit, l'humain valide.
3. **Orchestrateur + spécialistes** : à la clôture, un agent Clôture séquence AP → AR → banque → TVA. (Multi-agents réel = surface Code ; ailleurs, **l'humain est l'orchestrateur**.)

### La règle de conception

**Un mandat = un agent.** Comme un skill unique pour tout est ingérable, un agent unique pour tout est ingérable *et* dangereux. On préfère 6 agents à mandat étroit qu'un « agent compta » omnipotent. **Un agent naît d'un besoin** (« qui fait les fournisseurs GDG ? »), **jamais d'un outil** (« l'agent Odoo » ← à proscrire).

## 3. La contrainte réelle : web ≠ Code

C'est ce qui doit piloter l'archi. « Agent » ne veut pas dire la même chose des deux côtés :

| Capacité | Claude web (la majorité) | Claude Code (1-2 power users) |
|---|---|---|
| Skills | ✅ (dans un Project / Capabilities) | ✅ |
| Connectors distants (Odoo/Drive/Gmail en MCP remote) | ✅ | ✅ |
| Système de fichiers local, scripts (pdftotext, zip, dédoublonnage) | ❌ | ✅ |
| Sous-agents / orchestration multi-agents / workflows | ❌ | ✅ |
| Hooks, tâches récurrentes, mémoire fichier | ❌ | ✅ |
| Traitement de masse (ventiler 300 lignes, lettrer un mois) | 🟡 laborieux | ✅ |

**Web = le quotidien de la majorité.** Chaque équipe a son **Project** = rôle + skill de son domaine + socle + connectors en **lecture seule ou écriture limitée**. Parfait pour : poser une question, retrouver une pièce, saisir *une* facture, préparer une relance, sortir un reporting, vérifier un lettrage. Conversationnel, zéro install.

**Code = poste « opérateur lourd » + « mainteneur ».** Les 1-2 personnes en Code font : imports/ventilations/lettrages en masse, clôtures, tout ce qui touche du fichier local — et **surtout elles sont propriétaires des skills** (elles écrivent et versionnent le socle et les playbooks que le web consomme).

> Piège à éviter : vouloir faire faire à Claude web ce que seul Code sait faire (masse, fichiers locaux, multi-agents) → frustration garantie.

## 4. Gouvernance & garde-fous (crucial en finance)

- **Source unique versionnée.** Socle + playbooks dans un dépôt git. Web et Code y font référence ; on ne recopie pas les règles dans dix Projects. Une modif = une PR = validée (ex. règle TVA validée par l'EC) → propagée partout.
- **La mémoire n'est PAS de la politique partagée.** Mémoire = préférences perso + état local d'un poste. Toute règle de groupe va dans le socle/skill, sinon deux personnes divergent sans le savoir.
- **Moindre privilège sur les connectors.** Analystes web en lecture ; écriture (poster, payer, lettrer) réservée aux rôles opérateurs. Séparation des tâches : celui qui prépare ≠ celui qui poste.
- **`dry_run` par défaut + validation humaine** sur tout ce qui poste ou paie.
- **« Pas de règle de repli ».** Quand on ne peut pas trancher → **s'arrêter et signaler**, jamais de `else` par défaut. C'est la règle qui protège une DAF d'un agent trop zélé.
- **Piste d'audit.** Chaque écriture référence sa pièce ; le nommage Drive daté d'import sert exactement à ça.

## 5. Feuille de route — par quoi commencer

1. **Promouvoir `compta-groupe` en socle** : en extraire les invariants (règle d'or, aiguillage, TVA, nommage, garde-fous) → skill `socle-finance-groupe`.
2. **Sortir 2 playbooks** de ce qu'on maîtrise déjà : `ap-fournisseurs` et `banque-lettrage`. Chacun charge le socle.
3. **Créer 1 Project web par équipe** avec le bon playbook + le socle + connectors en lecture, et observer ce que le web fait bien / bute → ça dira quels domaines méritent un vrai poste Code.
4. **Versionner le tout en git** et nommer un owner par skill.

**Fil directeur : le web pour le flux quotidien et les questions, Code pour le lourd et pour maintenir la connaissance, le socle git comme cerveau commun.**
