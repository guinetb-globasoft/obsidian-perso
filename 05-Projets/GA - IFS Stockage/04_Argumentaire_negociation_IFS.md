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

### 🎯 Axe 4 — Le mode debug en production est anormal

**Argument** : La table `BPMN_DEBUG_ACTIVITY_LOG_TAB` contient **3,9 Go de logs de debug**. Le mode debug ne devrait jamais être actif en production.

**Formulation suggérée** :
> *"Quatre giga-octets de logs de debug sont stockés alors que nous sommes en production. Soit le mode debug a été oublié activé lors du déploiement par les équipes IFS, soit la purge automatique n'est pas paramétrée correctement. Dans les deux cas, c'est une situation de configuration à corriger côté IFS."*

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
> *"Nos documents font 10 Go sur 122 Go. Même en les supprimant tous, nous serions à 112 Go — toujours au-dessus du quota. Le problème n'est pas notre usage, c'est la structure IFS."*

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
