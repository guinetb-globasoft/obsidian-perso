---
tags: ["comptabilité", "guinet-digital-group", "exercice-2025", "claude-code", "brief"]
created: 2026-05-09
---

---
tags: ["comptabilité", "guinet-digital-group", "exercice-2025", "claude-code", "brief"]
created: 2026-05-09
updated: 2026-05-09
---

# Brief Claude Code — Imports relevés BPCE 2025 GDG

> Brief autonome à donner à Claude Code. Tâche : extraire les transactions des PDF BPCE et les injecter dans Odoo via XML-RPC, en évitant les doublons avec ce qui existe déjà.

## Contexte

- Société : **Guinet Digital Group** (GDG, ex-Globasoft), `company_id=4` dans l'instance Odoo `guinet`
- Exercice : 2025 complet
- Fichiers source : `C:/Users/Shadow/Downloads/Releves_BPCE_2025/`

## Identification des comptes

| Compte BPCE | Solde 31/12/2024 | Journal Odoo | Code | Compte comptable |
|---|---:|---|---|---|
| **55621004634** (IBAN FR76 1780 7000 1755 6210 0463 426) | -35,92 € | BNK1 (id=27) | BNK1 | 512001 |
| **95621009495** (IBAN FR76 1780 7000 1795 6210 0949 584) | +6 309,12 € | BNK3 (id=31) | BNK3 | 512003 |
| **CB du 55621004634** | n/a | BNK2 (id=30) | BNK2 | 512002 |

⚠️ **Important** : le journal Odoo BNK1 reçoit déjà des transactions de la connexion bancaire automatique du compte 55621004634. Pour éviter les doublons, vérifier l'existence de la transaction (date + montant + libellé) avant d'insérer.

## Inventaire des fichiers à traiter

### Compte 55621004634 (BNK1 + relevé CB BNK2)

12 extraits de compte (un par mois) :
- `Extrait de compte - 55621004634 - 20250106.pdf` (couvre 06/12/2024 → 06/01/2025)
- `Extrait de compte - 55621004634 - 20250204.pdf` (couvre 06/01/2025 → 04/02/2025)
- `Extrait de compte - 55621004634 - 20250304.pdf`
- `Extrait de compte - 55621004634 - 20250402.pdf`
- `Extrait de compte - 55621004634 - 20250505.pdf`
- `Extrait de compte - 55621004634 - 20250605.pdf`
- `Extrait de compte - 55621004634 - 20250702.pdf`
- `Extrait de compte - 55621004634 - 20250804.pdf`
- `Extrait de compte - 55621004634 - 20250905.pdf`
- `Extrait de compte - 55621004634 - 20251002.pdf`
- `Extrait de compte - 55621004634 - 20251104.pdf`
- `Extrait de compte - 55621004634 - 20251205.pdf` ⚠️ **uniquement jusqu'au 26/11**, **pas de relevé décembre 2025 complet**

12 relevés CB :
- `Relevé CB - 55621004634 - 2025MMDD.pdf` × 12

### Compte 95621009495 (BNK3)

6 extraits seulement (pas d'envoi BPCE quand pas de mouvement) :
- `Extrait de compte - 95621009495 - 20250106.pdf`
- `Extrait de compte - 95621009495 - 20250204.pdf`
- `Extrait de compte - 95621009495 - 20250304.pdf`
- `Extrait de compte - 95621009495 - 20250402.pdf`
- `Extrait de compte - 95621009495 - 20250505.pdf`
- `Extrait de compte - 95621009495 - 20250905.pdf`

**6 mois sans extrait** : jun, juil, août, oct, nov, déc 2025 → vérifier si vraiment aucun mouvement (probable car compte TVA peu utilisé) ou récupérer auprès de la banque.

## État actuel dans Odoo (à comparer avec l'extraction)

### BNK1 (journal id=27, compte 512001) — 494 lignes 2025
- Connexion bancaire active, alimentation auto
- 11 statements existants (jan→oct 2025)
- 78 lignes sans statement (nov+déc 2025)
- ⚠️ statement `20250106` a balance_end (2 358,62) ≠ balance_end_real (610,08) — écart 1 748,54 € à investiguer

### BNK2 (journal id=30, compte 512002) — 231 lignes 2025
- Imports manuels antérieurs incomplets
- 5 statements (août → nov 2025) avec **toutes balance_end ≠ balance_end_real**
- **6 mois manquants** : jan→juin 2025
- 1 mois manquant : décembre 2025

### BNK3 (journal id=31, compte 512003) — 9 lignes 2025
- 6 transactions janvier (TVA) + 3 transactions fin août
- Aucun statement créé

## Spec d'import attendue

### Pour chaque PDF d'extrait

1. **Parser le PDF** (utiliser pdfplumber, pypdf, ou tabula). Extraire :
   - N° de relevé, date début, date fin
   - SOLDE CRÉDITEUR/DÉBITEUR au début et fin
   - Lignes : date_compta, date_operation, date_valeur, libellé (multi-lignes), montant signé
   - Distinguer les "CARTE FACTURETTES CB" (lignes BNK2) des autres (lignes BNK1)

2. **Déduplication** : pour chaque transaction, vérifier dans Odoo via XML-RPC :
   ```python
   # Recherche line existante
   domain = [
       ('company_id', '=', 4),
       ('journal_id', '=', JOURNAL_ID),
       ('date', '=', tx_date),
       ('amount', '=', tx_amount),
       # idéalement payment_ref ~ libellé
   ]
   existing = models.execute_kw(db, uid, password,
       'account.bank.statement.line', 'search', [domain])
   ```
   Si `existing` non vide → skip cette ligne.

3. **Création des bank.statement.line** manquantes :
   ```python
   models.execute_kw(db, uid, password,
       'account.bank.statement.line', 'create', [{
           'journal_id': JOURNAL_ID,
           'date': tx_date,  # YYYY-MM-DD
           'payment_ref': libelle_complet,
           'amount': montant_signe,
           'partner_name': nom_partner_extrait_si_possible,
           # 'statement_id': statement_id_si_un_statement_global_est_cree
       }]
   )
   ```

4. **Création/Mise à jour du statement** au final (un par PDF) :
   ```python
   models.execute_kw(db, uid, password, 'account.bank.statement', 'create', [{
       'journal_id': JOURNAL_ID,
       'date': date_fin_extrait,
       'name': f'Extrait de compte - {NUM_COMPTE} - {DATE_YYYYMMDD}',
       'balance_start': solde_debut,
       'balance_end_real': solde_fin,
   }])
   ```

### Routage par type de ligne

| Pattern libellé | → Journal | Compte |
|---|---|---|
| `CARTE FACTURETTES CB` (montant agrégé du mois) | BNK1 (id=27) | 512001 (vir interne BNK1→BNK2) |
| `COMMISSION FACTURETTE CB` (commission unitaire CB) | BNK1 (id=27) | 512001 (frais bancaires) |
| Autres lignes du `Extrait de compte 55621004634` | BNK1 (id=27) | 512001 |
| Lignes du `Relevé CB 55621004634` | BNK2 (id=30) | 512002 |
| Lignes du `Extrait de compte 95621009495` | BNK3 (id=31) | 512003 |

## Connexion XML-RPC Odoo

```python
import xmlrpc.client

url = 'https://guinet-group.odoo.com'
db = 'guinet-group'  # à confirmer
username = '<l'utilisateur Odoo de Benoit>'
password = '<mot de passe API ou clé>'

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
```

## Validations attendues après chaque import

Pour chaque journal et chaque mois :
1. La somme des montants des `bank.statement.line` du mois = total débits + total crédits du PDF
2. Le `balance_start` du statement = `balance_end_real` du statement précédent (chaînage)
3. Le `balance_end` calculé = `balance_end_real` saisi (équilibre)

Si une validation échoue, **ne pas commit**, logger l'erreur et passer au PDF suivant.

## Étapes recommandées

1. **D'abord** : importer/compléter BNK2 (jan→juin 2025) — le plus gros trou, et nécessaire pour la cohérence amont
2. **Ensuite** : compléter BNK1 (nov+déc 2025 statements de synthèse à créer, lignes déjà là probablement)
3. **Enfin** : compléter BNK2 décembre 2025
4. **Optionnel** : BNK3 — vérifier si les mois manquants ont vraiment 0 mouvement

## Livrables attendus

À la fin de chaque exécution Claude Code :
- Un rapport `import_BPCE_2025_log.md` listant :
  - Fichiers traités
  - Lignes créées (count par journal/mois)
  - Lignes skippées (déjà existantes, count)
  - Erreurs / écarts détectés
- Un script Python réutilisable dans `scripts/import_bpce.py`

## ⚠️ Garde-fous

- **JAMAIS supprimer** une ligne existante. Uniquement créer.
- **TOUJOURS dry-run d'abord** sur un PDF avant batch
- **NE PAS toucher** aux lignes déjà rapprochées (`is_reconciled=True`) — elles sont liées à des factures Odoo
- En cas de doute sur le routage BNK1/BNK2, **demander avant de créer**
- Préserver les `payment_ref` complets (multi-lignes), c'est crucial pour le rapprochement futur

## Liens
- Audit complet : [[01-Audit-Journaux-Bancaires-2025-GDG]]
- Diagnostic : [[00-Diagnostic-GDG-2025]]
