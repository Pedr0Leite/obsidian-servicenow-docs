---
title: "Planned Maintenance does not create work orders and service orders after upgrading"
aliases:
  - KB0779990
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779990
kb_number: KB0779990
last_modified: 2024-05-16
---

## Planned Maintenance does not create work orders and service orders after upgrading

  

### Issue

Planned Maintenance does not create work orders and service orders after upgrading.

### Resolution

This issue is caused due to custom business rule running on the Work Order table.

Upon inactivating this custom business rule the issue is no longer reproducible. 

We would suggest commenting out code, line by line to better understand which line of code is breaking functionality.
