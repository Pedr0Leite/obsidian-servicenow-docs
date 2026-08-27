---
title: "Duplicating additional comments multiple times on the CSM portal and Case record"
aliases:
  - KB0957888
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957888
kb_number: KB0957888
last_modified: 2024-02-24
---

## Duplicating additional comments multiple times on the CSM portal and Case record

  

### Issue

-   Duplicating additional comments multiple times on the CSM portal and Case record when you order an item through the CSM portal. 

### Release

-   All

### Cause

-   A custom BR was on the sc\_req\_item table, however, the BR queries the customer service table and has an update function in it.

### Resolution

-   Deactivating this BR works fine. Furthermore, have to edit/customize the BR in order to solve this issue.
