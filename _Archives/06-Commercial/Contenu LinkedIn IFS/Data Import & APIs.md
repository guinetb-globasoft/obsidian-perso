---
tags: ["linkedin", "contenu", "ifs", "integration"]
created: 2026-06-01
---

# Pilier — Data Import & APIs (angle produit fort)

**Pourquoi ça marche** : c'est LE cœur d'ERP Control (imports/exports sans dev). Les fils montrent que l'Excel add-in casse souvent → opportunité de positionnement.

## Brouillon de post (EN)
> **The IFS Cloud Excel Add-in breaks every time Excel updates. There's a better way to move data.**
>
> Three failure modes I see on every project:
> • Add-in stops working after an Office update → migration blocked
> • "InvalidArgument" errors with zero useful context
> • One-off scripts rebuilt from scratch for each environment
>
> What actually scales:
> 1️⃣ Use the **REST/OData APIs** for repeatable imports (e.g. accounting vouchers) instead of manual Excel `[à préciser : exemple endpoint]`
> 2️⃣ Authenticate properly — **OAuth2 authorization code flow / JWT** are supported in IFS Cloud
> 3️⃣ Version your data loads so DEV → TEST → PROD stays in sync
>
> Still living in the Excel add-in? What's your most painful import? 👇

## Fils sources (community.ifs.com)
- IFS Cloud Excel Add-in not working after Excel update — https://community.ifs.com/data-migration-333/ifs-cloud-excel-add-in-not-working-after-excel-update-61180
- Excel Migration InvalidArgument Error — https://community.ifs.com/data-migration-333/excel-migration-invalidargument-error-65755
- Cloud: use API to import accounting vouchers — https://community.ifs.com/finance-financials-42/cloud-use-api-to-import-accounting-vouchers-35995
- OAuth2 authorization code flow integration — https://community.ifs.com/framework-experience-infrastructure-cloud-integration-dev-tools-50/oauth2-authorization-code-flow-integration-58476
- Does JWT authentication support in IFS Cloud — https://community.ifs.com/framework-experience-infrastructure-cloud-integration-dev-tools-50/does-jwt-json-web-token-authentication-supports-in-ifs-cloud-56495
- Test a REST API using Python — https://community.ifs.com/framework-experience-infrastructure-cloud-integration-dev-tools-50/test-a-rest-api-using-python-67490
