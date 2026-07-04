---
title: "Determining if a secondary view is causing issues with ODBC database tables"
aliases:
  - KB0542671
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0542671
kb_number: KB0542671
last_modified: 2024-04-30
---

## Determining if a secondary view is causing issues with ODBC database tables

  

### Issue

Determining if a secondary view is causing issues with ODBC database tables

Symptoms

* * *

-   Cannot view database tables
-   Only system schema tables are viewed

   
Cause

* * *

The user is trying to view the database from a secondary view.

Resolution

* * *

Make sure that you do not have a view of a view on itself. This causes problems with the schema processor that is used to generate the table list.
