# 🤝 Argumentaire de négociation IFS

> **Contexte** : IFS demande une facturation supplémentaire pour dépassement de volume sur la base de données IFS Cloud (122 Go).
> **Objectif** : Disposer d'un argumentaire structuré, fondé sur l'analyse technique, pour négocier un ajustement de la base de calcul ou un délai avant facturation.

---

## 1. Position de départ

### Notre constat
> "Sur les 122 Go facturés, nos données métier réelles ne représentent que **~13 Go (11 %)**. Les 109 Go restants relèvent du fonctionnement interne d'IFS (framework, code applicatif, logs, audit) et de la gestion Oracle assurée par IFS Cloud."

### Notre demande
1. **Clarifier la base de calcul** de la facturation (volume alloué ? utilisé ? données client uniquement ?).
2. **Engager des actions techniques** de purge sous responsabilité IFS avant toute facturation supplémentaire (gain potentiel ~30 Go documenté).
3. Si la facturation est maintenue, **discuter d'un périmètre équitable** : facturer uniquement la croissance des données métier client, pas le framework IFS ni l'overhead Oracle.

---

## 2. Arguments structurés par axe

### 🎯 Axe 1 — La majorité du volume n'est pas notre fait

| Argument | Donnée chiffrée |
|----------|-----------------|
| Nos données métier ne représentent qu'une fraction du volume | **13 Go / 122 Go = 11 %** |
| 89 % du volume est généré par IFS ou Oracle, sans contrôle direct de notre part | 109 Go / 122 Go |
| Le framework IFS et son code occupent à eux seuls plus que nos données | 30 Go (framework + PL/SQL) > 13 Go (nos données) |

**Formulation suggérée** :
> *"Nous comprenons la logique de facturation au volume, mais nous souhaitons que la base de calcul reflète notre usage réel. Sur 122 Go, l'analyse détaillée que nous avons menée montre que nos données métier représentent 13 Go. Le reste correspond à l'infrastructure technique d'IFS et au système Oracle que vous administrez en mode Cloud."*

---

### 🎯 Axe 2 — Des défauts d'administration coûtent ~10 Go

**Argument central** : **10,9 Go** du volume sont occupés par une table Oracle (`WRI$_ADV_OBJECTS`) qui devrait être maintenue à quelques Mo en condition normale. C'est un **bug Oracle documenté** dont la responsabilité de purge incombe au DBA, donc à IFS Cloud.

**Références à citer** :
- Oracle Support Note 1281703.1 — "WRI$_ADV_OBJECTS Grows Large"
- Oracle Support Note 2030447.1 — "Auto SQL Tuning Advisor Task Cleanup"

**Formulation suggérée** :
> *"Notre analyse a identifié que la table système Oracle `WRI$_ADV_OBJECTS` occupe 10,9 Go avec ses index. Il s'agit d'un défaut d'administration documenté par Oracle. En tant qu'opérateur Cloud, IFS a la responsabilité de la maintenance Oracle et donc de cette purge. Nous demandons que cette correction soit effectuée avant toute discussion de facturation supplémentaire."*

---

### 🎯 Axe 3 — De la sur-allocation est facturée

**Argument** : **~20 Go d'espace alloué mais vide** dans les datafiles Oracle.

| Tablespace | Vide | Détail |
|------------|------|--------|
| `UNDOTBS1` | 8,3 Go | UNDO Oracle, 95 % vide |
| `AUDIT_DATA_TBSP` | 6,4 Go | Audit Oracle sur-dimensionné |
| `MAINTENIX` | 1,0 Go | Tablespace de module non utilisé |
| `JASPER` | 1,0 Go | Tablespace de module non utilisé |
| Divers | ~3 Go | Marges normales |

**Formulation suggérée** :
> *"Vingt giga-octets d'espace sont alloués mais vides. Ces tablespaces ont été dimensionnés par IFS lors du provisionnement et ne sont pas représentatifs de notre usage. Nous demandons que la facturation soit basée sur le volume effectivement utilisé, pas sur l'espace alloué."*

---

### 🎯 Axe 4 — Le mode debug en production accumule 3,9 Go de logs (clarification à demander)

**Argument** : La table `BPMN_DEBUG_ACTIVITY_LOG_TAB` contient **3,9 Go de logs de debug**. Le mode debug ne devrait pas être actif en production. À clarifier avec IFS : le paramètre se trouve-t-il côté admin client (`Solution Manager › Background Processing` ou équivalent) ou côté IFS Cloud Ops ?

**Formulation suggérée (mode coopératif, sans accusation)** :
> *"La table `BPMN_DEBUG_ACTIVITY_LOG_TAB` contient 3,9 Go de logs de debug, ce qui suggère que le mode debug BPMN est actif sur l'environnement de production.*
>
> *Nous souhaitons clarifier deux points avec vous :*
> *1. **Côté configuration** : ce paramètre se trouve-t-il côté admin client (et dans ce cas, nous le désactivons immédiatement) ou côté IFS Cloud Ops ? Indiquez-nous le chemin exact dans l'UI pour le vérifier.*
> *2. **Côté purge** : les 3,9 Go déjà accumulés ne peuvent être supprimés que par une opération DBA (privilèges sur le schéma `IFSAPP`). Nous demandons cette purge dès que possible, indépendamment de la responsabilité de l'activation initiale."*

**Pourquoi cette formulation** : ne pas se positionner en accusation tant qu'on n'a pas la certitude que le paramètre est hors de notre portée. Si IFS confirme que la config est côté client, on l'aura désactivée et la purge IFS sera quand même nécessaire. Si IFS confirme que c'est côté Ops, l'argument original revient en force.

---

### 🎯 Axe 5 — Le framework IFS lui-même est volumineux

**Argument** : Les tables `FND_MODEL_*` (modèles UI Aurena, doc API) occupent **11,7 Go**. Ce ne sont pas nos données — c'est la structure même du logiciel IFS.

| Objet | Volume | Description |
|-------|--------|-------------|
| `FND_MODEL_DESIGN_TAB` | 5,5 Go | Modèles UI Aurena |
| `FND_MODEL_API_DOC_TAB` | 3,1 Go | Doc API auto-générée |
| `FND_MODEL_DESIGN_DATA_TAB` | 3,0 Go | Données associées aux modèles |

**Formulation suggérée** :
> *"Le framework UI Aurena occupe 11,7 Go. Il s'agit de structures internes du produit IFS, livrées et maintenues par vos équipes. Ce volume croît à chaque mise à jour produit. Si ce framework doit être facturé au stockage, il faudrait que cela soit clairement explicité dans le contrat — et que vous fournissiez en parallèle une procédure de cleanup pour limiter cette croissance."*

---

### 🎯 Axe 6 — Le code IFS est stocké dans la base

**Argument** : ~9 Go du schéma SYS correspondent au **code PL/SQL d'IFS lui-même** (packages, procédures, fonctions stockées).

**Formulation suggérée** :
> *"Environ neuf giga-octets sont occupés par le code source et compilé des packages PL/SQL d'IFS dans le dictionnaire Oracle. Il s'agit du code de votre application, pas de nos données. Facturer le stockage du propre code applicatif d'IFS à son client est difficilement défendable."*

---

### 🎯 Axe 7 — Valider le statut de `Cloud File Storage` et corriger le routage si besoin

**Argument** : IFS Cloud expose nativement la feature **`Cloud File Storage`** (stockage des documents sur Azure Blob hors BDD Oracle). Cette feature est probablement déjà provisionnée sur notre tenant (la doc IFS dit *"A storage account is provisioned automatically per environment"*). Pourtant **les 9,5 Go d'EDM mesurés sont aujourd'hui en BDD Oracle**, ce qui suggère que la feature n'est pas active ou pas paramétrée correctement (repository File Storage absent ou non sélectionné comme default).

Ce n'est donc pas une demande d'activation d'une feature inexistante — c'est une demande de **validation du paramétrage actuel** et de **correction si nécessaire**.

**Citations directes de la doc IFS officielle** (Solution Manager User Guide › Additional IFS Cloud Configuration › Cloud File Storage) :

> *"IFS Cloud File Storage is a platform service which can be used to store and retrieve documents from different storage locations. The service abstracts complexities in the underlying storage mode from the caller of the service."*

> *"**In the Cloud deployment model, the File Storage uses an Azure Blob Storage Account to store files.** A storage account is provisioned automatically per environment."*

> *"Setting up IFS Cloud File Storage is an easy task."*

Et pour la migration des fichiers existants (doc *"Cloud File Storage Migration Tool"*) :

> *"For 'smaller' installations, where the full source database can be moved into the managed cloud environment as is, there are two IFS Cloud Web assistants for moving document files and media items to IFS Cloud File Storage: Transfer Documents / Transfer Media. **That option is fully automatic and is preferable to using this tool.**"*

→ On est exactement dans ce cas (déjà en IFS Cloud, base déjà gérée par IFS) : la migration des 9,5 Go existants se ferait via un **Web Assistant intégré, "fully automatic"**, sans recourir au FS Mig Tool externe.

**Volumétrie EDM mesurée (mai 2026, PROD)** :

| Source | Documents | Volume Mo | % volume | Nature |
|--------|-----------|-----------|----------|--------|
| **TT (Talend, automatique)** | 5 774 | 7 368 | **78 %** | PJ factures fournisseurs depuis mars 2026 (obligation légale 10 ans) |
| **NELGRA (manuel)** | 1 494 | 941 | 10 % | Factures clients depuis avril 2025 (~100 docs/mois) |
| Autres utilisateurs (70 comptes) | 2 472 | 1 162 | 12 % | Uploads manuels divers (PJ commandes, BL, CRM, etc.) |
| **TOTAL EDM** | **9 740** | **9 471 Mo** | **100 %** | |

**Trajectoire** : ~+36 Go/an pour Talend, ~+0,8 Go/an pour NELGRA, marginal pour les autres. Soit **~37 Go/an de croissance documentaire** dont 97 % adressables par Cloud File Storage.

**Notre choix initial** : nous avions fait le choix de ne pas activer cette feature au provisionnement initial du tenant. Avec l'évolution du volume documentaire (×6 sur 12 mois grâce à Talend + NELGRA), ce choix est à reconsidérer.

**Formulation suggérée** :
> *"Notre volume documentaire EDM atteint 9,5 Go aujourd'hui en PROD, avec une trajectoire de croissance de ~37 Go/an dominée par le flux d'archivage légal des factures fournisseurs (Talend, démarré mars 2026). Vos propres tables `EDM_FILE_STORAGE_TAB` montrent que ces documents sont actuellement stockés en BDD Oracle.*
>
> *Votre documentation Solution Manager (`Cloud File Storage` et `Cloud File Storage Migration Tool`) décrit exactement la feature qui adresse ce cas : stockage des documents sur Azure Blob hors BDD Oracle, avec un Web Assistant 'fully automatic' pour migrer les fichiers existants. La doc précise par ailleurs que 'A storage account is provisioned automatically per environment' — donc le storage Azure Blob est probablement déjà alloué côté notre tenant.*
>
> *Nous demandons :*
> *1. **Vérification du statut actuel** de `Cloud File Storage` sur notre tenant :*
>    - *Le storage account Azure Blob est-il bien provisionné ?*
>    - *Un repository de type `File Storage` est-il configuré dans Document Management › Repositories ?*
>    - *Sinon, quel est le blocage technique ?*
> *2. **Si la feature n'est pas active**, son activation conformément à votre doc :*
>    - *Object Properties › LU `MediaItem` › property `REPOSITORY` = `FILE_STORAGE`*
>    - *Document Management › Repositories : nouveau repository Type=`File Storage`, Status=`Generating`*
> *3. **Migration des 9,5 Go d'EDM existants** via le Web Assistant `Transfer Documents` que vous décrivez comme 'fully automatic'.*
> *4. **Garantie de continuité pour nos intégrations tierces** qui consomment les pièces jointes — notamment Ootary, qui génère les mails sortants en y intégrant les PJ factures. Nous comprenons que votre service File Storage abstrait le storage sous-jacent via API REST (la doc le précise explicitement) ; nous demandons confirmation que les endpoints DocMan utilisés actuellement par nos intégrations continueront à renvoyer les PJ après migration.*
>
> *C'est une feature standard d'IFS Cloud, prête à l'emploi. Une fois opérationnelle, les ~37 Go/an de croissance documentaire iront sur Azure Blob plutôt qu'en BDD Oracle, et la question du dépassement de volume sur l'EDM disparaîtrait mécaniquement."*

**Bénéfice mutuel** :
- Pour nous : maîtrise du coût stockage BDD sur le long terme malgré l'archivage légal des PJ factures.
- Pour IFS : déchargement de la BDD Oracle (plus performante), promotion d'une de leurs features récentes, argument commercial pour les autres clients.

---

## 3. Scénarios de négociation possibles

### Scénario A — Refacturation sur la base d'un périmètre clarifié

**Demande** :
> *"La facturation au Go supplémentaire devrait porter uniquement sur la croissance des données métier client (schéma applicatif, hors framework, hors logs IFS, hors Oracle système). Cela représente ~13 Go aujourd'hui, ce qui est bien en-deçà du quota contractuel."*

**Avantage client** : Reflète l'usage réel et incite IFS à maîtriser son framework.
**Avantage IFS** : Maintient la logique de facturation à l'usage tout en étant équitable.

---

### Scénario B — Plan d'actions de purge avant facturation

**Demande** :
> *"Suspendre la facturation supplémentaire pendant 60 jours, le temps que les actions de purge identifiées (cf. document `03_Plan_purge.md`) soient mises en œuvre. Si après ces actions le volume reste élevé, nous reprendrons la discussion."*

**Gain potentiel attendu après actions** : ~30 Go (122 Go → ~90 Go).

**Avantage client** : Délai pour mesurer l'impact réel.
**Avantage IFS** : Démonstration de bonne foi, possibilité de récupérer du volume sans investissement.

---

### Scénario C — Forfait étendu vs facturation à l'usage

**Demande** :
> *"Si la facturation au Go est confirmée, nous demandons que le quota inclus dans le contrat soit ré-évalué pour tenir compte du fait que le framework IFS représente seul ~30 Go à minima. Le quota de base devrait donc être augmenté en conséquence, sans coût supplémentaire."*

---

### Scénario D — Engagement contractuel sur le framework

**Demande** :
> *"IFS s'engage par avenant à maintenir le volume du framework (`FND_MODEL_*`, `SYS` PL/SQL, etc.) sous un plafond défini (par exemple 25 Go). Au-delà, le surcoût est à la charge d'IFS, pas du client."*

---

## 3 bis. Anticipation d'une attaque IFS : *"Votre flux Talend gonfle le volume, c'est de votre fait"*

**Risque** : IFS pourrait répondre que **nous** sommes à l'origine de la croissance documentaire (Talend dépose 3 Go/mois), et que c'est donc à nous de payer.

**Notre réponse** :
> *"Effectivement, depuis mars 2026, nous archivons les PJ factures fournisseurs dans IFS via Talend. C'est un processus légitime et nécessaire (obligation légale 10 ans). Nous ne contestons pas le fait de stocker ce volume.*
>
> *Ce que nous contestons, c'est de devoir le faire en **stockage BDD Oracle**, alors qu'**IFS Cloud propose nativement la feature `Cloud File Storage`** qui stocke les documents sur Azure Blob hors BDD relationnelle. Cette feature est **documentée dans votre propre Solution Manager User Guide** ('Cloud File Storage' et 'Cloud File Storage Migration Tool'), et votre doc précise même que 'A storage account is provisioned automatically per environment' — donc le storage Azure Blob est probablement déjà provisionné côté notre tenant. Nous demandons une **vérification du paramétrage actuel** et, si besoin, la finalisation de l'activation + migration via les Web Assistants 'fully automatic' Transfer Documents / Transfer Media.*
>
> *Nous avions fait le choix de ne pas activer cette feature au provisionnement initial. Avec l'évolution de notre usage (archivage légal des factures fournisseurs depuis mars 2026), ce choix est à reconsidérer — et c'est précisément le scénario que votre doc anticipe."*

→ Ce point est crucial : il évite le piège *"c'est votre faute, payez"* et déplace le débat sur **l'activation d'une feature standard IFS existante**, pas sur une demande exotique. Voir aussi l'**Axe 7** (section 2).

---

## 4. Anticipation des contre-arguments IFS

### "Le volume facturé correspond à la base totale, c'est notre standard contractuel"

**Réponse** :
> *"Nous comprenons le principe, mais le contrat ne précise probablement pas la décomposition. Un standard contractuel ne devrait pas inclure des défauts d'administration comme `WRI$_ADV_OBJECTS` (10,9 Go) ou de la sur-allocation (20 Go). Nous demandons une révision sur ces points."*

---

### "Tous nos clients ont la même structure"

**Réponse** :
> *"Justement — si tous vos clients ont 30 Go de framework, ce coût devrait être inclus dans la licence, pas dans la facturation au stockage. Vous ne facturez probablement pas la place de Windows sur le serveur."*

---

### "Vous pouvez nettoyer vos documents et vos données"

**Réponse** :
> *"Nos documents font 10 Go sur 122 Go. Même en les supprimant tous, nous serions à 112 Go — toujours au-dessus du quota. Le problème n'est pas notre usage, c'est la structure IFS.*
>
> *Par ailleurs, ~78 % de ces 10 Go (soit 7,4 Go) sont des **pièces justificatives de factures fournisseurs** déposées automatiquement par notre connecteur Talend depuis mars 2026, dans le cadre d'une politique d'archivage légale obligatoire. Elles sont soumises à une **obligation de conservation de 10 ans** (Code de Commerce L.123-22). Toute suggestion de les purger expose notre entreprise à un risque fiscal et juridique majeur — ce n'est donc pas une option."*

---

### "C'est l'usage normal d'Oracle"

**Réponse** :
> *"Un usage normal d'Oracle ne stocke pas 10,9 Go dans `WRI$_ADV_OBJECTS`. C'est un défaut d'administration documenté par Oracle lui-même. Si IFS Cloud assume la responsabilité de l'administration, il assume aussi la responsabilité des correctifs."*

---

### "La facturation est automatique, basée sur des métriques globales"

**Réponse** :
> *"Une métrique globale qui inclut le système Oracle, le framework IFS et l'espace alloué vide n'est pas une métrique d'usage client. Nous demandons soit une métrique plus fine, soit un crédit reflétant les éléments hors usage."*

---

## 5. Documents à présenter

Lors de l'échange avec IFS, présenter dans cet ordre :

1. **`00_Synthese_executive.md`** — Vue d'ensemble en une page.
2. **`02_Responsabilite_volumes.md`** — Document central, ce qui appartient à qui.
3. **`03_Plan_purge.md`** — Démontre notre bonne foi et le gain possible côté IFS.
4. **`01_Analyse_volumetrie_complete.md`** — Pour répondre aux questions techniques détaillées.

---

## 6. Préparation de la réunion

### Avant la réunion
- [ ] Relire ce document et les références techniques.
- [ ] Identifier qui côté IFS sera l'interlocuteur (commercial ? technique ? account manager ?).
- [ ] Préparer 2-3 questions précises pour engager le dialogue : *"Pouvez-vous nous confirmer ce qui est inclus dans le calcul des 122 Go ?"*, *"Avez-vous une procédure documentée de cleanup `WRI$_ADV_OBJECTS` pour vos clients ?"*

### Pendant la réunion
- [ ] Commencer par exposer les chiffres factuellement, sans dramatiser.
- [ ] Insister sur le ratio 11 % données utiles / 89 % infrastructure.
- [ ] Mettre en avant le plan de purge comme solution gagnant-gagnant.
- [ ] Ne pas accepter un *"c'est comme ça"* — demander la justification technique de chaque ligne contestée.

### Après la réunion
- [ ] Envoyer un compte-rendu écrit récapitulant les engagements pris.
- [ ] Demander un délai écrit pour la mise en œuvre des actions de purge avant toute facturation.
- [ ] Programmer un point de suivi à 30-60 jours pour mesurer l'impact.

---

## 7. Position de repli

Si IFS refuse toute négociation sur la base de calcul :

1. **Demander une facturation au prorata** : seuls les Go au-delà du quota qui correspondent à des données métier client sont facturés.
2. **Demander un engagement de purge** documenté par IFS sur les 10,9 Go de `WRI$_ADV_OBJECTS` avant toute facturation.
3. **Obtenir un délai** d'au moins 3 mois pour la mise en œuvre du plan de purge interne.
4. À défaut, **escalader auprès du Customer Success Manager** ou de l'Account Executive IFS, voire envisager une médiation contractuelle.

---

## 8. Indicateurs à demander à IFS

Pour clarifier la base de calcul, demander officiellement à IFS :

1. La décomposition exacte des **122 Go** qu'ils facturent (par tablespace, par schéma).
2. La **méthode de mesure** : volume alloué ? volume utilisé ? snapshot à quel moment ?
3. La **politique de purge appliquée** par IFS Cloud sur les tables système Oracle.
4. Les **seuils de rétention par défaut** pour : AWR, audit Oracle, BPMN debug, IAM events.
5. Les **procédures de cleanup officielles** pour `FND_MODEL_*` et autres tables framework.

Si IFS ne peut pas fournir ces informations, c'est un argument supplémentaire pour contester la facturation.
