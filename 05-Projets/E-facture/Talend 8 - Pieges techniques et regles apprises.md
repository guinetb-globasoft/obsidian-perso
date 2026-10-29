---
tags: ["talend", "technique", "methode", "IFS", "INT_281"]
created: 2026-07-31
---

# Talend 8 — pièges techniques et règles apprises

Note de travail, alimentée au fil des erreurs réellement commises sur `INT_281`. Chaque entrée décrit un piège vérifié, pas une bonne pratique théorique. Objectif : ne pas repayer deux fois la même erreur.

---

## 1. Le Studio écrase les fichiers depuis sa mémoire

**Le piège.** Éditer un `.item` pendant que le Studio est ouvert ne sert à rien. Le Studio garde le job en mémoire et réécrit le fichier à l'enregistrement ou à la fermeture. La modification disparaît sans aucun message.

**Vécu.** Correction du nom de pièce jointe posée à 16:21. Code généré à 16:52 depuis la mémoire, donc sans la correction. La facture projet est sortie en `FACTURE_.pdf`. Pire : la sauvegarde prise ensuite était déjà amputée, elle ne servait à rien.

**La règle.** Toujours vérifier que le Studio est fermé avant d'écrire :

```powershell
if (Get-Process -Name "Talend-Studio*" -ErrorAction SilentlyContinue) { exit 1 }
```

Et l'ordre est impératif : **fermer le Studio → écrire → rouvrir le Studio**. Jamais l'inverse.

**Corollaire.** À la fermeture, fermer l'onglet du job sans enregistrer si le Studio a une version antérieure en mémoire.

## 2. Vérifier le code généré, pas le `.item`

**Le piège.** Le `.item` est la source, mais ce n'est pas ce qui s'exécute. Croire une modification active parce qu'elle est dans le fichier est une erreur.

**La règle.** Après un run, contrôler le `.java` généré :

```
<workspace>/<projet>/poms/jobs/process/<chemin>/<job>/src/main/java/<paquet>/<Job>.java
```

Comparer son horodatage à celui de l'exécution. S'il est antérieur à la modification, le run n'en tient pas compte.

## 3. Un même libellé peut exister à plusieurs endroits

**Le piège.** Corriger une occurrence et croire le travail fait.

**Vécu.** Le nom de la pièce jointe était construit **deux fois** : dans `tRunJob_16` (paramètre de contexte passé au job fils, qui détermine le nom sous lequel le PDF est écrit sur disque) et dans le code de `tJavaRow_6` (qui relit ce fichier et publie `PDF_LISIBLE_FILENAME`). Corriger l'un sans l'autre casse le flux : le second cherche un fichier au nom que le premier n'écrit plus.

**La règle.** Toujours compter les occurrences avant de remplacer, et refuser d'écrire si le compte ne correspond pas à l'attendu :

```powershell
$n = ([regex]::Matches($t, [regex]::Escape($avant))).Count
if ($n -ne 1) { "ATTENDU 1, trouve $n"; exit 1 }
```

## 4. Les indices de `<connections>` sont positionnels

**Le piège.** Dans un `tXMLMap`, les `outgoingConnections` / `incomingConnections` référencent les connexions par **position**. Supprimer une connexion décale toutes les suivantes et casse silencieusement des liens sans rapport.

**La règle.** Ne jamais supprimer une connexion en éditant le XML. Ajouter en fin de liste, ou passer par le Studio. De même, supprimer un composant est risqué : c'est pourquoi `tRunJob_11`, devenu inutile après la correction de `#BAR#`, a été laissé en place plutôt que supprimé.

## 5. Un composant peut porter plusieurs blocs `metadata`

**Le piège.** Un `tExtractJSONFields` porte un `metadata connector="FLOW"` **et** un `metadata connector="REJECT"`, avec les mêmes colonnes dupliquées. Chercher une colonne par son nom en trouve deux.

**Vécu.** Ajout de `Cf_Traitement_Efacture` : premier essai en échec car la ligne de colonne existait 2 fois dans le nœud (et 2 fois de plus dans un autre composant du job).

**La règle.** Borner la recherche au nœud visé avant de remplacer :

```powershell
$anchor = $t.IndexOf('value="tExtractJSONFields_7"')
$deb = $t.LastIndexOf('<node ', $anchor)
$fin = $t.IndexOf('</node>', $anchor) + 7
```

Et ajouter la colonne dans **les deux** blocs, comme le ferait le Studio.

## 6. `tExtractJSONFields` a deux tables de mapping

`MAPPING` (chemin vide = le nom de colonne sert de chemin) **et** `MAPPING_4_JSONPATH` (chemin explicite entre guillemets). Ajouter une colonne oblige à alimenter les deux, plus le schéma. Trois greffes pour un champ.

## 7. Un groupe de contexte ne se crée pas en éditant les fichiers

**Le piège.** Créer un groupe de contexte `locale_mm` en éditant le XML ne fonctionne pas. Le Studio effectue un câblage interne qui n'apparaît pas dans le fichier.

**Vécu.** Deux tentatives, deux réinitialisations par le Studio — la seconde a touché 8 contextes partagés. Tout a dû être nettoyé.

**La règle.** Pour tester en local sans créer de groupe : **sauvegarder les valeurs, les remplacer temporairement, restaurer avant tout commit**. C'est ce que fait `bascule.ps1`, avec un garde-fou qui refuse de s'exécuter Studio ouvert et un verdict explicite « NE PAS COMMITER ».

## 8. Variables liées au référentiel contre variables built-in

**Le piège.** Une variable de contexte liée à un contexte partagé (`repositoryContextId` ≠ `built-in`) est **resynchronisée par le Studio** depuis l'item partagé à l'ouverture et à l'enregistrement. Toute modification faite dans le job est annulée.

**Vécu.** J'ai affirmé à tort que 4 variables sur 8 étaient surchargeables depuis la vue Run. Elles étaient liées au référentiel.

**La règle.** Avant de vouloir surcharger une variable, vérifier son `repositoryContextId`. Si elle est liée, c'est l'item partagé qu'il faut toucher — en sachant combien de jobs le partagent. `DB_MNTR` est utilisé par **57 jobs**.

## 9. Un contexte partagé peut faire fuiter un secret

**Vécu.** Un mot de passe local (81 caractères chiffrés) s'est retrouvé commité à la place de celui de l'équipe (89 caractères) dans `DB_MNTR_0.1.item`. J'ai cherché la fuite dans le job pendant longtemps alors qu'elle était dans le contexte partagé.

**La règle.** Un arbre de travail propre ne dit rien sur l'écart avec la version de l'équipe. Comparer explicitement à `HEAD` avant de commiter :

```powershell
git -C $depot --no-pager diff -- <fichier>
```

Et se méfier des mots de passe en type `id_String` plutôt que `id_Password` : ils partent en clair dans le `.item` versionné.

## 10. `PROPAGATE_CHILD_RESULT` sur un `tRunJob`

**Le piège.** Un `tRunJob` qui a un flux en entrée **et** un flux en sortie doit avoir `PROPAGATE_CHILD_RESULT` à `true`. Sinon le résultat du job fils est silencieusement perdu — pas d'erreur, juste un flux vide.

**Vécu.** `tRunJob_21` et `tRunJob_22` étaient à `false`. L'`Objkey` remonté par le job fils partait à la poubelle.

**À vérifier aussi :** `DIE_ON_CHILD_ERROR`, qui définit la politique d'erreur par `tRunJob`.

## 11. Un `tRunJob` peut être racine de sous-job

Il n'a pas besoin d'un flux en entrée pour s'exécuter. `tRunJob_19` fonctionne uniquement à partir de `context.PDF_IFS_ResultKey`. Utile pour bifurquer sans transporter de données.

## 12. `OnSubjobOk` se déclenche même à zéro ligne

**Le piège.** `OnSubjobOk` signale la fin du sous-job, pas la présence de données. Il part même si le flux n'a produit aucune ligne. Et il doit partir du **premier composant** du sous-job, pas d'un composant intermédiaire.

**Conséquence pratique.** Ne jamais s'en servir pour dire « il y a eu un résultat ». Pour conditionner, il faut un `RUN_IF` sur une variable explicite.

## 13. Ce qui est hors de la boucle ne s'exécute qu'une fois

**Le piège majeur, et le plus coûteux.** Un `tFileList` avec un lien `ITERATE` fait boucler ce qui en descend. Tout sous-job racine non rattaché à cette chaîne s'exécute **une seule fois**, après la boucle, avec l'état laissé par la dernière itération.

**Vécu.** Sur un lot de 4 factures, une seule a été livrée — la dernière — et les 3 autres sont restées dans le répertoire d'arrivée sans erreur. La livraison et l'archivage pendaient à un sous-job racine indépendant.

**La règle.** Sur un job itératif, tracer explicitement la chaîne depuis le `tFileList` et vérifier que **chaque** étape du traitement en descend. Se le demander composant par composant, pas globalement.

## 14. Les variables mono-valeur survivent aux itérations

**Le piège.** Une variable de contexte ou une clé de `globalMap` posée à l'itération N est toujours là à l'itération N+1. Si elle n'est posée que sur une branche conditionnelle, les itérations qui ne passent pas par cette branche héritent de la valeur précédente.

**Vécu, deux fois.**
- `PDF_IFS_AFP_ResultKey` : identifié et corrigé lors de la tâche 874.
- `PDF_IFS_InvoiceId` : **manqué**, découvert seulement à l'essai multi-fichiers. Une facture projet héritait de l'identifiant de l'instantanée précédente et repartait avec son PDF.

**La règle.** Recenser **toutes** les variables posées sur une branche conditionnelle et les remettre à zéro en début d'itération, dans le `tJava` de tête. En faire une liste exhaustive, pas au cas par cas.

**Et surtout :** une correction qui rend une valeur « plausible » peut masquer une fuite. Le ternaire `FACTURE_ / SITUATION_` a rendu la fuite silencieuse ; sans lui le nom serait resté vide et l'anomalie aurait sauté aux yeux.

## 15. Passer une valeur à un `tXMLMap` sans flux d'entrée

Quand une valeur doit atteindre un `tXMLMap` qui n'a pas le flux concerné en entrée, la publier en `globalMap` en amont et la lire dans l'expression :

```java
(String)globalMap.get("TRAITEMENT_EFACTURE")
```

Bien plus léger que d'ajouter une entrée au mapper. Vérifier l'ordre d'exécution : le composant qui pose la valeur doit être dans un sous-job qui s'achève avant celui du mapper.

## 16. Les expressions de `tXMLMap` sont des expressions, pas des instructions

Pas de déclaration de variable, pas de `;`. Tout doit tenir en une seule expression ternaire imbriquée. Prévoir la robustesse aux `null` directement dans l'expression — `"X".equalsIgnoreCase(y)` accepte un `y` à `null` et renvoie `false`, à préférer à `y.equals("X")`.

## 17. Ne jamais laisser une branche produire `null`

**Vécu.** L'expression de `#BAR#` finissait par `: null`. Si aucune condition ne tombait, la note obligatoire disparaissait purement et simplement.

**La règle.** Toute chaîne de ternaires doit avoir une valeur par défaut réelle. `null` n'est pas une valeur par défaut, c'est un défaut.

## 18. Se méfier des champs concaténés côté IFS

**Vécu.** `Country` renvoyé par `CustomerInfoSet` vaut `FRFRANCE` — le code ISO collé au libellé. Le test `"FR".equals(Country)` était donc **toujours faux**, et la distinction France / international ne pouvait pas fonctionner.

**La règle.** Ne jamais supposer le format d'un champ d'API. Vérifier la valeur réelle sur une réponse, puis normaliser explicitement (`substring(0, 2)` avec garde de longueur).

## 19. `Content-Type: application/json` sans `IEEE754Compatible`

**Le piège.** IFS renvoie les décimaux en chaînes de caractères (`"InvoiceId": "61897"`), mais en attend en **nombres** si l'appel n'annonce pas `IEEE754Compatible=true`.

**Vécu.** `"ScheduledDayNumber":"1"` → HTTP 400 `[INVALID_VALUE_FOR_PROPERTY]`. Corrigé en `"ScheduledDayNumber":1`.

## 20. Vérifier ce qu'un appel API crée en passant

Un appel n'est pas neutre. `VirtualOrderReports` crée un enregistrement avec `Active:true` et `ScheduleOption:Daily` à **chaque** facture projet. L'effet de bord s'accumule.

**La règle.** Pour tout appel en écriture, se demander ce qu'il laisse derrière lui, et si l'objet créé doit être nettoyé ou réutilisé.

---

# Pièges PowerShell rencontrés sur ces fichiers

Ils ont produit de **faux diagnostics**, ce qui est pire qu'une erreur bloquante.

## `$pid` est une variable réservée

`$pid` = identifiant du processus, en lecture seule. L'assigner lève une erreur et fait échouer le bloc — j'ai conclu à tort à l'absence de `PartyIdentification`. **Deux fois.** Nommer autrement.

## `.Name` sur un nœud XML est masqué par l'adaptateur PowerShell

Si un élément a un enfant nommé `Name`, `$noeud.Name` renvoie **le contenu de l'enfant**, pas le nom du nœud. J'ai cru à un élément aberrant `<ARMATURES>` dans `InvoiceLine` alors que `cac:Item` était parfaitement formé.

**La règle.** Sur du XML, utiliser les accesseurs .NET : `get_Name()`, `get_LocalName()`, `get_InnerText()`.

## `Get-Content` lit en ANSI

Sur un fichier UTF-8, les accents deviennent du mojibake et une recherche d'ancre accentuée renvoie 0 occurrence — faux négatif silencieux.

**La règle.** `[System.IO.File]::ReadAllText($f)` en lecture, et en écriture :

```powershell
[System.IO.File]::WriteAllText($f, $t, (New-Object System.Text.UTF8Encoding($false)))
```

Le `$false` supprime le BOM, qu'un `.item` ne doit pas porter.

## `XmlDocument.Save` reformate le fichier

Charger puis sauvegarder un `.item` avec `XmlDocument` réécrit indentation et attributs. Le diff devient illisible et le Studio peut mal réagir.

**La règle.** Manipuler le **texte brut** pour écrire, et n'utiliser `XmlDocument` que pour **vérifier** après coup — ce qui valide au passage que le XML est bien formé.

## `$&` et `$` dans les chaînes de remplacement

`-replace` interprète `$` dans le remplacement. Neutraliser :

```powershell
$valeur -replace '\$', '$$$$'
```

Ou préférer `String.Replace()`, littéral, quand aucune regex n'est nécessaire.

---

# Méthode de travail qui s'est révélée payante

**Écrire, puis relire depuis le XML.** Ne jamais faire confiance à un `Replace` : recharger le fichier avec `XmlDocument` et réafficher la valeur telle que le Studio la lira.

**Refuser d'écrire quand le compte d'occurrences est inattendu.** Cette garde a évité trois modifications fausses ce jour-là.

**Sauvegarder avant chaque modification**, avec un nom qui dit ce qu'on s'apprête à faire (`.item.avant_bar`, `.item.avant_reset_invoiceid`).

**Tester sur un banc local.** SFTP paramiko sur `127.0.0.1:2222` plus base PostgreSQL locale, avec bascule réversible des valeurs. Permet d'itérer sans toucher aux environnements réels.

Détail utile : paramiko 5 ne propose plus `ssh-rsa` (SHA-1), seulement `rsa-sha2-*`. Or JSch 0.1.55, embarqué par Talend 8, ne connaît pas `rsa-sha2-*`. Il faut une clé d'hôte **ECDSA nistp256**, supportée des deux côtés.

**Tester le cas nominal de production, pas seulement le cas unitaire.** Le défaut multi-fichiers n'existe pas en passage unitaire — qui était pourtant le seul mode de test employé jusque-là. Un flux qui traite des lots doit être testé avec des lots, dès le début.
