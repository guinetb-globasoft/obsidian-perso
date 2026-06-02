---
tags: ["tipdujour", "ifs", "procurement"]
created: 2026-06-01
---

#tipdujour #ifs

## Post (EN)
**Pilier** : Procurement / Integration

💡 **IFS Cloud tip**

Setting up a **punch-out catalog** (employee self-service procurement) and the vendor URL won't connect? IFS appends the **endpoint / HOOK_URL automatically** — so you shouldn't include it.

• From the supplier's link, keep everything **up to** `&HOOK_URL`
• Delete `&HOOK_URL` and everything after it
• Let IFS add its own endpoint

Most punch-out connection failures are a **doubled endpoint**. Trim the supplier URL and the handshake usually just works.

**Hashtags** : #IFS #IFSCloud #ERP #Procurement
**Source (1er commentaire)** : https://community.ifs.com/buying-procurement-demand-planner-asc-srm-41/ifs-cloud-employee-self-service-procurement-catalog-punchout-catalog-52455
**À vérifier** : néant
