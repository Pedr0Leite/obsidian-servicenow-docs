---
title: "Why Request / Requested Item / SCTASK records can not be seen on list view"
aliases:
  - KB0779116
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779116
kb_number: KB0779116
last_modified: 2024-04-08
---

## Why Request / Requested Item / SCTASK records can not be seen on list view

  

### Issue

When the user views any of the below three tables, they can't see any records:

-   sc\_request
-   sc\_req\_item
-   sc\_task

**Note**, they are _not_ seeing the typically ACL-related security restraints in the list-view.

### Resolution

Within each of the reported tables (sc\_request, sc\_req\_item, and sc\_task) there is a custom query Business Rule called "Query Business Rule" which is filtering all records out from being visible. This is causing the issue, and why the user is not able to see any records on the reported tables.

Therefore, to stop the issue, kindly suggest that the user disable their custom query Business Rule so that they can see the list-views for those tables properly.
