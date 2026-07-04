---
title: "Closing child case task does not closed parent case"
aliases:
  - KB0998441
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998441
kb_number: KB0998441
last_modified: 2024-09-24
---

## Closing child case task does not closed parent case

  

### Issue

The user wanted to know if there was anything like Service Catalog's _sc\_req\_item_ "Close Parent if Required" Business Rule (where when child RITMs are closed, the parent REQ is also closed) for Case.

### Resolution

There is not currently anything in the platform shipped Out of Box (OOB) as of Rome within Case which has this same idea/functionality.

The user was encouraged that if they needed this sort of functionality in their instance, they could simply review the Service Catalog "Close Parent if Required" Business Rule and modify it for the Case table according to their business needs. That way, whenever all Case Tasks (CSTASK) on a Case were closed, the parent case would close also.
