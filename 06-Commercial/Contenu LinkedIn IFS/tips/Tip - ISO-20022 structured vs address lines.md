---
tags: ["tipdujour", "ifs", "finance"]
created: 2026-06-01
---

#tipdujour #ifs

## Post (EN)

**Pilier** : E-Invoicing & Compliance

💡 **IFS Cloud tip**

An ISO-20022 gotcha worth knowing *before* you promise a format to a bank: the standard solution doesn't support mixing a **structured address** AND free **address lines** for the same party.

• Choose structured **or** address lines per bank
• Needing both means modifying the XML transformer
• Never edit the **core** transformer — clone it, or you'll pay at every upgrade

Most "the bank rejected our payment file" tickets trace back to address formatting. Decide the format early and you avoid a customization you'd carry forever.

**Hashtags** : #IFS #IFSCloud #ERP #Finance
**Source (1er commentaire)** : https://community.ifs.com/finance-financials-42/iso-20022-set-up-adding-adrline-in-supplier-postel-address-39586
**À vérifier** : néant

#IFS #IFSCloud #ERP #Finance

---
**Source** : best answer d'Eranda — https://community.ifs.com/finance-financials-42/iso-20022-set-up-adding-adrline-in-supplier-postel-address-39586
