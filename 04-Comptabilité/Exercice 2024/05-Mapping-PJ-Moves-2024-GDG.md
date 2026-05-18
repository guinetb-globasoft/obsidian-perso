---
tags: ["comptabilité", "guinet-digital-group", "exercice-2024", "reconstruction", "pieces-jointes"]
created: 2026-05-09
---

---
tags: ["comptabilité", "guinet-digital-group", "exercice-2024", "reconstruction", "pieces-jointes"]
created: 2026-05-09
updated: 2026-05-09
---

# Mapping PJ ↔ Moves 2024 GDG — Avant détachement

> Référence pour re-rattacher les 71 PJ orphelinées après reconstruction de l'à-nouveau 2024.
> Phase 3a : `update_record` sur `ir.attachment` mettant `res_id=False` et `res_model=False`.

## Procédure de re-rattachement (post-reconstruction)

1. Reconstruire les moves 2024 dans Odoo (à-nouveau + reprise détaillée).
2. Pour chaque PJ ci-dessous : identifier le nouveau `move_id` correspondant (par date + partenaire + montant + ref).
3. `update_record` sur `ir.attachment` avec `res_model="account.move"` et `res_id=<nouveau_id>`.

## Indexation par attachment_id

| PJ ID | Nom fichier | Mimetype | Taille (octets) | Move ID original | Nom move | Date | Partenaire | Ref facture | Montant TTC | État |
|---|---|---|---:|---:|---|---|---|---|---:|---|
| 2799 | 2024_04_16.pdf | pdf | 308 267 | 1977 | FACTU/2024/04/0001 | 2024-04-30 | Transform Partner | PP2024/0021 | 50,00 | posted |
| 2800 | 2024_05_15.pdf | pdf | 302 667 | 2025 | FACTU/2024/05/0001 | 2024-05-31 | Transform Partner | PP2024/0027 | 50,00 | posted |
| 2801 | 2024_06_17.pdf | pdf | 297 365 | 1997 | FACTU/2024/06/0001 | 2024-06-30 | Transform Partner | PP2024/0033 | 50,00 | posted |
| 2802 | 2024_07_19.pdf | pdf | 335 692 | 1960 | FACTU/2024/07/0001 | 2024-07-19 | Transform Partner | PP2024/0038 | 125,00 | posted |
| 3555 | Canva_invoice_may.pdf | pdf | 113 175 | 2042 | FACTU/2024/06/0002 | 2024-06-30 | Canva | 04169-19335410 | 27,00 | posted |
| 3558 | facture_FACVE2024051.pdf | pdf | 219 169 | 2043 | FACTU/2024/04/0002 | 2024-04-30 | Bureaux and co verdier | FACVE2024051 | 58,80 | posted |
| 3568 | 2024-05-15_FA_347279.pdf | pdf | 35 627 | 2044 | FACTU/2024/05/0002 | 2024-05-31 | Digidom | FA-347279 | 28,80 | posted |
| 3571 | F202406-0104.pdf | pdf | 30 496 | 2046 | FACTU/2024/06/0005 | 2024-06-30 | Etincelle Coworking | F202406-0104 | 168,00 | posted |
| 3572 | F202406-0151.pdf | pdf | 30 507 | 2045 | FACTU/2024/06/0003 | 2024-06-30 | Etincelle Coworking | F202406-0151 | 168,00 | posted |
| 3576 | GCFRD0006212921.pdf | pdf | 45 153 | 2051 | FACTU/2024/05/0003 | 2024-05-31 | Google Cloud France SARL | GCFRD0006212921 | 40,26 | posted |
| 3577 | GCFRD0005529940.pdf | pdf | 45 964 | 2050 | FACTU/2024/02/0001 | 2024-02-29 | Google Cloud France SARL | GCFRD0005529940 | 16,50 | posted |
| 3578 | GCFRD0005656090.pdf | pdf | 45 809 | 2049 | FACTU/2024/03/0001 | 2024-03-31 | Google Cloud France SARL | GCFRD0005656090 | 18,64 | posted |
| 3579 | GCFRD0005940560.pdf | pdf | 45 931 | 2048 | FACTU/2024/04/0003 | 2024-04-30 | Google Cloud France SARL | GCFRD0005940560 | 18,64 | posted |
| 3584 | Invoice FA047-240672.pdf | pdf | 166 482 | 2054 | FACTU/2024/05/0006 | 2024-05-31 | Mwpi | FA047-240672 | 105,60 | posted |
| 3585 | Invoice FA047-240648.pdf | pdf | 166 867 | 2053 | FACTU/2024/05/0005 | 2024-05-31 | Mwpi | FA047-240648 | 105,60 | posted |
| 3586 | Invoice FA047-240671.pdf | pdf | 166 761 | 2052 | FACTU/2024/05/0004 | 2024-05-31 | Mwpi | FA047-240671 | 153,60 | posted |
| 3590 | in_1PCHcqCcKlYJxALVnCdh0uRv.pdf | pdf | 94 810 | 2056 | FACTU/2024/05/0007 | 2024-05-31 | Notion | in_1PCHcqCcKIYJxALVnCdh0uRv | 704,70 | posted |
| 3591 | in_1P1PJYCcKlYJxALVDmLG3Kxb.pdf | pdf | 90 064 | 2055 | FACTU/2024/04/0004 | 2024-04-30 | Notion | in_1P1PJYCCKIYJXALVDmLG3Kxb | 180,00 | posted |
| 3594 | FR2024-1272613.pdf | pdf | 119 549 | 2059 | FACTU/2024/06/0007 | 2024-06-30 | Patreon | FR2024-1272613 | 23,40 | posted |
| 3595 | FR2024-847179.pdf | pdf | 119 956 | 2058 | FACTU/2024/04/0008 | 2024-04-30 | Patreon | FR2024-847179 | 17,40 | posted |
| 3596 | FR2024-1009910.pdf | pdf | 119 546 | 2057 | FACTU/2024/05/0009 | 2024-05-31 | Patreon | FR2024-1009910 | 23,40 | posted |
| 3600 | Facture FC10005539.pdf | pdf | 108 503 | 2060 | FACTU/2024/03/0002 | 2024-03-31 | New Top Gramont | FC10005539 | 47,98 | posted |
| 3605 | Invoice FA047-240541.pdf | pdf | 166 575 | 2062 | FACTU/2024/04/0006 | 2024-04-30 | Mwpi | FA047-240541 | 105,60 | posted |
| 3606 | Invoice FA047-240530.pdf | pdf | 166 835 | 2061 | FACTU/2024/04/0005 | 2024-04-30 | Mwpi | FA047-240530 | 105,60 | posted |
| 3617 | 2024-04-09_FA_337320.pdf | pdf | 35 313 | 2067 | FACTU/2024/04/0007 | 2024-04-09 | Digidom | FA-337320 | 28,80 | posted |
| 3618 | 2024-05-09_FA_345630.pdf | pdf | 35 531 | 2066 | FACTU/2024/05/0008 | 2024-05-31 | Digidom | FA-345630 | 28,80 | posted |
| 3619 | 2024-02-09_FA_320650.pdf | pdf | 35 930 | 2065 | FACTU/2024/02/0002 | 2024-02-29 | Digidom | FA-320650 | 28,80 | posted |
| 3620 | 2024-06-09_FA_354166.pdf | pdf | 35 577 | 2064 | FACTU/2024/06/0006 | 2024-06-30 | Digidom | FA-354166 | 28,80 | posted |
| 3621 | 2024-07-09_FA_362790.pdf | pdf | 36 291 | 2063 | FACTU/2024/07/0002 | 2024-07-31 | Digidom | FA-362790 | 28,80 | posted |
| 3633 | F-000715965.pdf | pdf | 461 208 | 2068 | FACTU/2024/06/0008 | 2024-06-30 | Up France | F-000715965 | 152,00 | posted |
| 3634 | F-000734436.pdf | pdf | 455 599 | 2069 | FACTU/2024/07/0003 | 2024-07-31 | Up France | F-000734436 | 80,00 | posted |
| 3635 | F-000734322.pdf | pdf | 455 119 | 2070 | FACTU/2024/07/0004 | 2024-07-31 | Up France | F-000734322 | 160,00 | posted |
| 3663 | 2024_07_01_patreon.pdf | pdf | 39 629 | 2074 | FACTU/2024/07/0005 | 2024-07-31 | Patreon | 987179597 | 23,40 | posted |
| 3697 | F240701384.pdf | pdf | 237 626 | 2086 | FACTU/2024/07/0006 | 2024-07-31 | Super Compteur | F240701384 | 166,80 | posted |
| 3698 | F240701367.pdf | pdf | 237 747 | 2085 | FACTU/2024/07/0007 | 2024-07-31 | Super Compteur | F240701367 | 1 659,60 | posted |
| 4794 | 2024_06_18_Gandi_invoice_2024061800316.pdf | pdf | 25 775 | 2213 | FACTU/2024/06/0009 | 2024-06-30 | Gandi | 2024061800316 | 38,94 | posted |
| 4796 | F-000759409.pdf | pdf | 459 742 | 2215 | FACTU/2024/08/0002 | 2024-08-31 | Up France | F-000759409 | 224,00 | posted |
| 4797 | F-000757110.pdf | pdf | 456 457 | 2214 | FACTU/2024/08/0001 | 2024-08-31 | Up France | F-000757110 | 368,00 | posted |
| 4800 | 2024_09_01_Github.pdf | pdf | 58 890 | 2216 | FACTU/2024/09/0001 | 2024-09-01 | GitHub | ch_3PuH28JFr6CCHwli1sDM4AmT | 12,00 | posted |
| 4802 | 2024_08_09_FA_371446.pdf | pdf | 36 203 | 2217 | FACTU/2024/08/0003 | 2024-08-31 | Digidom | FA-371446 | 28,80 | posted |
| 4976 | Facture334.pdf | pdf | 8 012 | 2276 | FACTU/2024/08/0004 | 2024-08-31 | Le Tire Bouchon | 334 | 46,00 | posted |
| 4977 | Ticket30424.pdf | pdf | 4 454 | 2277 | FACTU/2024/04/0009 | 2024-04-30 | Le Tire Bouchon | T30424 | 53,50 | posted |
| 4978 | Facture Notion 3 juillet 2024.pdf | pdf | 67 913 | 2278 | FACTU/2024/06/0010 | 2024-06-30 | Notion | in_1PYOhFCcKIYJxALVG0a9znwR | 146,48 | posted |
| 4980 | Invoice-4D19CFCB-0001.pdf | pdf | 40 149 | 2282 | FACTU/2024/07/0008 | 2024-07-31 | ChatGPT | 4D19CFCB-0001 | 60,00 | posted |
| 4981 | fnac_23_07.pdf | pdf | 307 007 | 2283 | FACTU/2024/07/0009 | 2024-07-31 | Fnac | 2420580134 | 209,99 | posted |
| 4982 | 94251c19-abce-4f1a-b9df-635bb332af27.pdf | pdf | 118 515 | 2284 | FACTU/2024/07/0010 | 2024-07-31 | Canva | EU372042198 | 27,00 | posted |
| 4983 | 3f430962-5e0a-4423-8e7b-9251b5f43cbc.pdf | pdf | 48 127 | 2285 | FACTU/2024/07/0011 | 2024-07-31 | GitHub | ch_3PXgHxJFr6CCHwli1ipZYiiY | 8,00 | posted |
| 4986 | VOTRE FACTURE (1) (1).pdf | pdf | 50 688 | 2288 | FACTU/2024/03/0003 | 2024-03-31 | But International | 1311858 | 169,98 | posted |
| 4999 | github-Globasoft-receipt-2024-08-01.pdf | pdf | 59 023 | 2330 | FACTU/2024/08/0005 | 2024-08-31 | GitHub | ch_3Pj2pnJFr6CCHwli1ssrDyfL | 8,00 | posted |
| 5024 | 20240909013229.jpg | jpg | 175 652 | 2337 | FACTU/2024/09/0003 | 2024-09-09 | Guinet Benoit | Indigo 06/09/24 | 5,50 | posted |
| 5025 | 20240909013252.jpg | jpg | 171 841 | 2338 | FACTU/2024/09/0002 | 2024-09-09 | Guinet Benoit | Indigo 02/09/24 | 23,20 | posted |
| 5041 | 20240909034004.jpg | jpg | 261 652 | 2341 | FACTU/2024/09/0004 | 2024-09-02 | La cote et l'arrête | 0012213/002 | 204,80 | posted |
| 5042 | 20240909034022.jpg | jpg | 234 631 | 2342 | FACTU/2024/09/0005 | 2024-09-09 | Dicapo | 0064162 | 22,00 | posted |
| 5081 | 20240911082405.jpg | jpg | 194 184 | 2354 | / | 2024-05-31 | 2C2S | 0013209/002 | 47,10 | **draft** |
| 5082 | 20240911082423.jpg | jpg | 203 038 | 2355 | FACTU/2024/05/0010 | 2024-05-31 | La Gina Ristorante | 17/05/2024 | 38,00 | posted |
| 5083 | 20240911082453.jpg | jpg | 229 068 | 2356 | FACTU/2024/05/0011 | 2024-05-31 | La pecora nera | A5967-278662 | 16,20 | posted |
| 5105 | 20240913114236.jpg | jpg | 217 220 | 2359 | FACTU/2024/06/0011 | 2024-06-30 | Dicapo | 0059041/18 | 51,00 | posted |
| 5106 | 20240913115241.jpg | jpg | 286 031 | 2360 | FACTU/2024/07/0013 | 2024-07-31 | La Cuisine à Mémé | 10 | 32,00 | posted |
| 5107 | 20240913115259.jpg | jpg | 255 384 | 2361 | FACTU/2024/07/0012 | 2024-07-31 | O PAISIBLE | 225752 | 39,50 | posted |
| 5113 | note de frais.pdf | pdf | 77 542 | 2362 | FACTU/2024/07/0014 | 2024-07-31 | API RESTAURATION | 020 | 50,00 | posted |
| 5334 | Facture pro - 55621004634 - 20240329.pdf | pdf | 87 497 | 3047 | FACTU/2024/03/0004 | 2024-03-31 | Banque Populaire Occitane | 24030000000000039185 | 39,66 | posted |
| 5335 | Facture pro - 55621004634 - 20240430.pdf | pdf | 84 817 | 3048 | FACTU/2024/04/0010 | 2024-04-30 | Banque Populaire Occitane | 24040000000000054440 | 39,66 | posted |
| 5336 | Facture pro - 55621004634 - 20240531.pdf | pdf | 87 737 | 3049 | FACTU/2024/05/0012 | 2024-05-31 | Banque Populaire Occitane | 24050000000000039114 | 45,18 | posted |
| 5337 | Facture pro - 55621004634 - 20240628.pdf | pdf | 85 089 | 3050 | FACTU/2024/06/0012 | 2024-06-30 | Banque Populaire Occitane | 24060000000000038312 | 60,39 | posted |
| 5338 | Facture pro - 55621004634 - 20240731.pdf | pdf | 85 098 | 3051 | FACTU/2024/07/0015 | 2024-07-31 | Banque Populaire Occitane | 24070000000000054304 | 40,74 | posted |
| 5339 | Facture pro - 55621004634 - 20240830.pdf | pdf | 87 481 | 3052 | / | 2024-08-31 | — | 24080000000000038125 | 49,69 | **draft (doublon de 3159)** |
| 5349 | 20240922120003.jpg | jpg | 240 537 | 3063 | FACTU/2024/05/0013 | 2024-05-31 | Au Pois Gourmand | 122885 | 245,50 | posted |
| 5443 | Gandi_Invoice_2024092900358.pdf | pdf | 43 901 | 3107 | FACTU/2024/09/0009 | 2024-09-29 | Gandi | 2024092900358 | 60,00 | posted |
| 5536 | Facture pro - 55621004634 - 20240930.pdf | pdf | 87 488 | 3158 | FACTU/2024/09/0008 | 2024-09-30 | Banque Populaire Occitane | 24090000000000038297 | 45,46 | posted |
| 5537 | Facture pro - 55621004634 - 20240830.pdf | pdf | 87 481 | 3159 | FACTU/2024/08/0007 | 2024-08-31 | Banque Populaire Occitane | 24080000000000038125 | 49,69 | posted |
| 7499 | Facture334.pdf | pdf | 8 012 | 3433 | / | 2024-08-31 | Le Tire Bouchon | 334 | 68,50 | **draft (doublon partiel de 2276)** |

## Statistiques

- **71 PJ** au total : **60 PDF + 11 JPG** (~9,7 Mo)
- **68 PJ** sur moves posted (registrées en compta), **3 PJ** sur drafts
- Plage `attachment_id` : 2799 → 7499
- Plage `move_id` : 1960 → 3433
- Plage de dates : 2024-02-29 → 2024-09-30

## Anomalies repérées

### A1 — Doublon Facture334.pdf (Le Tire Bouchon ref "334")

Deux PJ avec le même nom `Facture334.pdf` mais montants différents :
- PJ 4976 → move 2276 (posted, 46,00€)
- PJ 7499 → move 3433 (draft, 68,50€)

Les deux sont en août 2024. Soit deux factures distinctes du même fournisseur portant la même référence (peu probable), soit une facture rebaissée et reretranscrite, soit un bug de saisie. **À investiguer pendant la reconstruction.**

### A2 — Doublon BPO 24080000000000038125 (49,69€)

Deux moves avec la même référence et le même montant :
- Move 3052 (draft) avec PJ 5339 (`Facture pro - 55621004634 - 20240830.pdf`)
- Move 3159 (posted, FACTU/2024/08/0007) avec PJ 5537 (même nom de fichier `Facture pro - 55621004634 - 20240830.pdf`)

Le draft 3052 est probablement le brouillon initial qui a été recréé en 3159 pour validation. À supprimer pendant la reconstruction. **Conserver la PJ 5537 prioritairement** (rattachée au posted).

### A3 — Move draft 2354 (2C2S 47,10€)

Move `draft` sans contrepartie posted. PJ 5081 (`20240911082405.jpg`) — note de frais visiblement non finalisée. À traiter dans la reprise détaillée.

## Liste indexée par move_id (utile pour reconstruction)

| Move ID | Nom move | PJ ID(s) attachées |
|---:|---|---|
| 1960 | FACTU/2024/07/0001 | 2802 |
| 1977 | FACTU/2024/04/0001 | 2799 |
| 1997 | FACTU/2024/06/0001 | 2801 |
| 2025 | FACTU/2024/05/0001 | 2800 |
| 2042 | FACTU/2024/06/0002 | 3555 |
| 2043 | FACTU/2024/04/0002 | 3558 |
| 2044 | FACTU/2024/05/0002 | 3568 |
| 2045 | FACTU/2024/06/0003 | 3572 |
| 2046 | FACTU/2024/06/0005 | 3571 |
| 2048 | FACTU/2024/04/0003 | 3579 |
| 2049 | FACTU/2024/03/0001 | 3578 |
| 2050 | FACTU/2024/02/0001 | 3577 |
| 2051 | FACTU/2024/05/0003 | 3576 |
| 2052 | FACTU/2024/05/0004 | 3586 |
| 2053 | FACTU/2024/05/0005 | 3585 |
| 2054 | FACTU/2024/05/0006 | 3584 |
| 2055 | FACTU/2024/04/0004 | 3591 |
| 2056 | FACTU/2024/05/0007 | 3590 |
| 2057 | FACTU/2024/05/0009 | 3596 |
| 2058 | FACTU/2024/04/0008 | 3595 |
| 2059 | FACTU/2024/06/0007 | 3594 |
| 2060 | FACTU/2024/03/0002 | 3600 |
| 2061 | FACTU/2024/04/0005 | 3606 |
| 2062 | FACTU/2024/04/0006 | 3605 |
| 2063 | FACTU/2024/07/0002 | 3621 |
| 2064 | FACTU/2024/06/0006 | 3620 |
| 2065 | FACTU/2024/02/0002 | 3619 |
| 2066 | FACTU/2024/05/0008 | 3618 |
| 2067 | FACTU/2024/04/0007 | 3617 |
| 2068 | FACTU/2024/06/0008 | 3633 |
| 2069 | FACTU/2024/07/0003 | 3634 |
| 2070 | FACTU/2024/07/0004 | 3635 |
| 2074 | FACTU/2024/07/0005 | 3663 |
| 2085 | FACTU/2024/07/0007 | 3698 |
| 2086 | FACTU/2024/07/0006 | 3697 |
| 2213 | FACTU/2024/06/0009 | 4794 |
| 2214 | FACTU/2024/08/0001 | 4797 |
| 2215 | FACTU/2024/08/0002 | 4796 |
| 2216 | FACTU/2024/09/0001 | 4800 |
| 2217 | FACTU/2024/08/0003 | 4802 |
| 2276 | FACTU/2024/08/0004 | 4976 |
| 2277 | FACTU/2024/04/0009 | 4977 |
| 2278 | FACTU/2024/06/0010 | 4978 |
| 2282 | FACTU/2024/07/0008 | 4980 |
| 2283 | FACTU/2024/07/0009 | 4981 |
| 2284 | FACTU/2024/07/0010 | 4982 |
| 2285 | FACTU/2024/07/0011 | 4983 |
| 2288 | FACTU/2024/03/0003 | 4986 |
| 2330 | FACTU/2024/08/0005 | 4999 |
| 2337 | FACTU/2024/09/0003 | 5024 |
| 2338 | FACTU/2024/09/0002 | 5025 |
| 2341 | FACTU/2024/09/0004 | 5041 |
| 2342 | FACTU/2024/09/0005 | 5042 |
| 2354 | / (draft) | 5081 |
| 2355 | FACTU/2024/05/0010 | 5082 |
| 2356 | FACTU/2024/05/0011 | 5083 |
| 2359 | FACTU/2024/06/0011 | 5105 |
| 2360 | FACTU/2024/07/0013 | 5106 |
| 2361 | FACTU/2024/07/0012 | 5107 |
| 2362 | FACTU/2024/07/0014 | 5113 |
| 3047 | FACTU/2024/03/0004 | 5334 |
| 3048 | FACTU/2024/04/0010 | 5335 |
| 3049 | FACTU/2024/05/0012 | 5336 |
| 3050 | FACTU/2024/06/0012 | 5337 |
| 3051 | FACTU/2024/07/0015 | 5338 |
| 3052 | / (draft) | 5339 |
| 3063 | FACTU/2024/05/0013 | 5349 |
| 3107 | FACTU/2024/09/0009 | 5443 |
| 3158 | FACTU/2024/09/0008 | 5536 |
| 3159 | FACTU/2024/08/0007 | 5537 |
| 3433 | / (draft) | 7499 |

## Historique opération

- **2026-05-09** : note créée juste avant l'exécution Phase 3a.
- **2026-05-09** : ✅ exécution Phase 3a réussie — `update_record` sur les 71 attachments avec `res_id=False, res_model=False`. Vérification effectuée sur l'échantillon `[2799, 5081, 5339, 7499, 5537]` : tous orphelinés (`res_id=0`, `res_model` vide). Les 71 PJ survivront au unlink des moves.
- *(à compléter après reconstruction)* : nouveaux IDs de re-rattachement.

## Liens

- Brief GDG : [[Brief-Comptable-Odoo]]
- Diagnostic 2024 : [[Exercice 2024/04-Diagnostic-GDG-Odoo-vs-SuperCompteur]]
- Brief transverse : [[Brief-Compta-Transverse]]
