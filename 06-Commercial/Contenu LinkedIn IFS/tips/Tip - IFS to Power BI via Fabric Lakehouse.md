---
tags: ["tipdujour", "ifs", "analytics"]
created: 2026-06-01
---

#tipdujour #ifs

## Post (EN)
**Pilier** : Insights & Analytics

💡 **IFS Cloud tip**

Connecting IFS Cloud analytics data to **Power BI** without standing up on-prem infrastructure?

• IFS lands **Parquet** data in **ADLS Gen2** (the supported extraction mechanism)
• Instead of Power BI hitting ADLS directly, ingest into a **Fabric Lakehouse** to secure, type and model it
• Power BI then connects to **Fabric** — no on-prem gateway required

Treat ADLS as the landing zone and Fabric as the modelling layer. It's the cleaner, gateway-free path for IFS → BI, and it keeps governance where it belongs.

**Hashtags** : #IFS #IFSCloud #ERP #PowerBI
**Source (1er commentaire)** : https://community.ifs.com/insights-business-reporter-and-analysis-models-eoi-51/adls-gateway-question-66001
**À vérifier** : détails archi selon ta version [à vérifier]
