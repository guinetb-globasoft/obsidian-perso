---
titre: Brief Claude Excel — correctifs post-phases 1 et 2
statut: à exécuter
date: 2026-08-18
cible: INVENTAIRE - Applicatifs Métier.xlsx, onglet « FLUX inter-APPS »
tags: [referentiel, excel, brief, correctif]
---

# Brief Claude Excel — correctifs

Deux corrections courtes après les phases 1 et 2. **43 cellules**, aucune structure à changer.

## Pourquoi la correction A

En phase 2, la colonne `Support & Protocole d'échange` a été remplie avec les **connexions
techniques de la tâche Talend** (`BDD + REST + SFTP`) au lieu du **protocole d'échange métier**
entre les deux applications.

Vérification faite sur les ressources réelles des 17 tâches : **toutes échangent par fichier
déposé sur SFTP**, sans exception —
`stgprodsftpv2.blob.core.windows.net:/SFTPGANEW/...` et `sftp-ne7.ondemand.esker.com:/...`.
Le « REST » correspond à l'endpoint *Talend Monitoring* et à la variable *Commun URL interfaces* ;
le « BDD » à `Database_Connection`, la base interne de Talend pour les logs et la
transcodification. Ce sont des composants de l'orchestrateur, pas le canal d'échange.

La bonne valeur métier est donc `fichier via SFTP` pour les 17 lignes — c'est d'ailleurs ce que
le référentiel portait déjà sur 10 d'entre elles avant l'écrasement.

---

## ⬇️ À COPIER À PARTIR D'ICI ⬇️

Deux corrections dans l'onglet `FLUX inter-APPS`. Mêmes règles que précédemment : travaille sur
une copie ou vérifie qu'une sauvegarde existe, ne modifie que ce qui est listé, ne trie pas, ne
reformate pas, n'insère ni ne supprime de ligne.

**Repère les colonnes par leur libellé d'en-tête** (ligne 1). Lettres attendues après les
insertions de la phase 2, à confirmer avant d'écrire :

| Libellé d'en-tête | Lettre attendue |
|---|---|
| `Code` | **A** |
| `Support & Protocole d'échange` | **AI** |
| `Commentaires` | **AQ** |

### Correction A — remettre le protocole métier (17 lignes)

Dans la colonne `Support & Protocole d'échange`, **remplace la valeur actuelle par** :

```
fichier via SFTP
```

sur ces 17 lignes — identifiées par leur code, le n° de ligne est donné en repère :

| Code (colonne A commence par) | Ligne | Valeur actuelle attendue |
|---|---:|---|
| `INT-185-` | 173 | BDD + REST + SFTP |
| `INT-187-` | 174 | BDD + REST + SFTP |
| `INT-189-` | 175 | BDD + SFTP |
| `INT-199-` | 182 | SFTP |
| `INT-209-` | 186 | BDD + REST + SFTP |
| `INT-213-` | 189 | REST + SFTP |
| `INT-217-` | 190 | BDD + REST + SFTP |
| `INT-222-` | 193 | BDD + REST + SFTP |
| `INT-225-` | 196 | REST + SFTP |
| `INT-233-` | 204 | BDD + REST + SFTP |
| `INT-251-` | 222 | BDD + SFTP |
| `INT-252-` | 223 | BDD + SFTP |
| `INT-253-` | 224 | BDD + SFTP |
| `INT-255-` | 226 | BDD + SFTP |
| `INT-256-` | 227 | BDD + SFTP |
| `INT-257-` | 228 | BDD + SFTP |
| `INT-258-` | 229 | BDD + SFTP |

**Ne touche pas à la colonne `Fréquence`** : les valeurs de la phase 2 sont correctes et ont
remplacé des planifications périmées. Ne touche pas non plus à `Tâche Talend`.

### Correction B — corriger la date des commentaires (26 lignes)

En phase 1, la trace ajoutée en fin de colonne `Commentaires` porte une date erronée.

Dans la colonne `Commentaires`, **remplace la chaîne** :

```
13/08/2026 - MAJ d'apres releve Talend PROD
```

**par** :

```
18/08/2026 - MAJ d'apres releve Talend PROD
```

Ne remplace que cette chaîne, en conservant le reste du contenu de la cellule et les crochets
qui l'entourent. Les lignes concernées sont celles de la phase 1 : 10, 11, 12, 13, 27, 38, 55,
73, 120, 135, 138, 168, 169, 170, 171, 172, 182, 186, 187, 189, 193, 196, 222, 224, 226, 231.
Aucune autre ligne de l'onglet ne contient cette chaîne — un remplacement global sur la seule
colonne `Commentaires` est donc sûr, mais vérifie le compte.

### Compte rendu attendu

1. Nombre de cellules modifiées (attendu : 17 + 26 = **43**).
2. Toute ligne dont la valeur actuelle ne correspondait pas à l'attendu.
3. Confirmation que `Fréquence` et `Tâche Talend` n'ont pas été touchées.
4. Confirmation que la table est toujours en `A1:AR251`.

## ⬆️ À COPIER JUSQU'ICI ⬆️

---

## Option C — à faire seulement si tu la juges utile

Ajouter l'**expression cron brute** à la fin de la colonne `Fréquence`, après le libellé en
clair, sur les 17 lignes. Exemple pour INT-217 :

```
Toutes les 10 min, 12 h/j, lun-ven — 10/10 8-11,14-21 ? * 2-6 *
```

**Pourquoi ça vaut le coup** : c'est précisément parce que l'ancien référentiel contenait le
cron brut que j'ai pu comparer le déclaré au réel et établir que **4 planifications sur 12
avaient dérivé** — dont `INT-187-188` qui tourne désormais **sept jours sur sept** (`? * * *`)
alors que le référentiel le disait du lundi au vendredi. Une prose seule n'aurait pas permis
cette comparaison.

| Code | Cron réel à ajouter |
|---|---|
| `INT-185-` | `5 7,10,11,14,16 ? * 2-6 *` |
| `INT-187-` | `8/5 8-21 ? * * *` |
| `INT-189-` | (non planifié — déclenché par la tâche amont) |
| `INT-199-` | `3/5 7-20 ? * 2-6 *` |
| `INT-209-` | `3/5 7-11,14-20 ? * 2-6 *` |
| `INT-213-` | `2/10 7-11,14-20 ? * 2-6 *` |
| `INT-217-` | `10/10 8-11,14-21 ? * 2-6 *` |
| `INT-222-` | `7/5 7-20 ? * 2-6 *` |
| `INT-225-` | `0 13,18 ? * 2-6 *` |
| `INT-233-` | `6 7,10,14,18 ? * 2-6 *` |
| `INT-251-` `252-` `256-` `257-` `258-` | `5/30 7-12,14-20 ? * 2-6 *` |
| `INT-253-` | `5/10 7-11,14-20 ? * 2-6 *` |
| `INT-255-` | `5/10 8-11,14-21 ? * 2-6 *` |

---

## Ce qu'on abandonne volontairement

Les **connexions techniques des tâches** (`Database_Connection`, `Talend Monitoring`,
`SFTP GA TLDIFS`, `Commun URL interfaces`…) ne sont **pas** versées au référentiel : elles
décrivent l'intérieur de l'orchestrateur, pas les échanges entre applications. Elles restent
disponibles dans `Talend-PROD-inventaire.csv` et `_inv_prod.json` si un besoin d'exploitation
se présente.
