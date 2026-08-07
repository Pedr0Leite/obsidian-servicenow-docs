---
title: "Determining if field type is causing issues with ODBC queries"
aliases:
  - KB0542651
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0542651
kb_number: KB0542651
last_modified: 2025-04-07
---

## Determining if field type is causing issues with ODBC queries

  

### Issue

Determining if field type is causing issues with ODBC queries

Symptoms

* * *

-   Query has empty result
-   Query returns no data

   
Cause

* * *

While querying for **internal\_type** field, no data is returned because the field is hidden.

Resolution

* * *

This field is hidden to protect customers from creating errors in their sys\_dictionary records. Unhide the field and submit the query again.
