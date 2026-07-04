---
title: "Running Reconciliation and grouping by company does not create different reconciliation records for each company"
aliases:
  - KB0957386
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957386
kb_number: KB0957386
last_modified: 2024-02-17
---

## Running Reconciliation and grouping by company does not create different reconciliation records for each company

  

### Issue

When running reconciliation and grouping by company, the reconciliation results does not show all the companies available for the installations. It shows 1 or 2 companies and the rest are grouped in Any.

### Release

All

### Cause

This is because the company field is assigned at the entitlement level. So, only the company assigned to the entitlement for a specific Software Model will have a separate record in the reconciliation results.    

### Resolution

If there is a specific company you wish to see in the reconciliation results, then separate entitlement assigned to that company will need to be created for this specific Software Model. Then, reconciliation looks for the company field on the "Installed On" CI of the install record. The entitlement will only cover those installs where the company matches the installed on CI's company.
