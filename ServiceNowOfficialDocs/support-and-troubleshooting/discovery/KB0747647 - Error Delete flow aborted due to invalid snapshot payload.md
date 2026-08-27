---
title: "Error: Delete flow aborted due to invalid snapshot payload"
aliases:
  - KB0747647
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747647
kb_number: KB0747647
last_modified: 2024-04-10
---

## Issue

Error: Delete flow aborted due to invalid snapshot payload.

**Symptoms**

-   Error at the end of pattern payload processing:
-   "Delete flow aborted due to invalid snapshot payload"
-   Says the pattern failed

  

  

## Resolution

1) Go to table "sa\_payload\_snapshot":

-   https://<instance-name>.service-now.com/sa\_payload\_snapshot\_list.do?sysparm\_query=

2) Find the via the pattern name and CI, for the CI you are trying to discover.

3) Delete that snapshot.

4) Run discovery again.
