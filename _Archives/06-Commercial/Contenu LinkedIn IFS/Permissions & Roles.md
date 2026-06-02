---
tags: ["linkedin", "contenu", "ifs", "permissions"]
created: 2026-06-01
---

# Pilier — Permissions & Roles (angle produit fort)

**Pourquoi ça marche** : sujet ultra-récurrent (cf. aussi l'échange LinkedIn avec Nilla Cijntje, Bang & Bonsomer — « set up rights from scratch in Cloud 22R2 »). Pile sur le pain point que ton produit adresse.

## Brouillon de post (EN)
> **Setting up permissions in IFS Cloud from scratch? The Navigator tree is your best friend — and most teams ignore it.**
>
> A pattern I keep seeing:
> • Permission sets built field-by-field → unmaintainable in 6 months
> • No mapping between *what a role does* and *what it can access*
> • Rights rebuilt manually in every environment → drift between DEV/TEST/PROD
>
> A cleaner approach:
> 1️⃣ Export the **Navigator tree** as the basis for functional + end-user roles, then derive permission sets from it `[à préciser : étapes exactes]`
> 2️⃣ Keep **Service Users** separate from named users (integration ≠ people)
> 3️⃣ Watch **Row Level Security** on custom entities — it can silently block Query Designer
> 4️⃣ Export/import user profiles in bulk instead of clicking one by one
>
> How do you keep your IFS roles clean across environments? 👇

## Fils sources (community.ifs.com)
- Export the Navigator tree as the basis for functional roles / permission sets — https://community.ifs.com/framework-experience-infrastructure-cloud-integration-dev-tools-50/export-the-navigator-tree-as-the-basis-for-functional-roles-and-end-user-roles-for-the-permission-sets-66882
- Service Users IFS Cloud — https://community.ifs.com/framework-experience-infrastructure-cloud-integration-dev-tools-50/service-users-ifs-cloud-67547
- Allow Query Designer to display add-on custom entities without mandatory Row Level Security — https://community.ifs.com/framework-experience-infrastructure-cloud-integration-dev-tools-50/allow-query-designer-to-display-add-on-custom-entities-without-mandatory-row-level-security-configuration-67379
- How can I export/import multiple user profiles in one action — https://community.ifs.com/framework-experience-infrastructure-cloud-integration-dev-tools-50/how-can-i-export-import-multiple-user-profiles-in-one-1-action-52884
