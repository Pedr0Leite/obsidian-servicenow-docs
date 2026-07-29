---
title: "The Variable Editor is not showing on sc_task records for users with certain roles"
aliases:
  - KB0814952
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814952
kb_number: KB0814952
last_modified: 2024-04-08
---

## The Variable Editor is not showing on sc\_task records for users with certain roles

  

### Issue

When users who have a certain role open sc\_task records with variables on them (verifiable via viewing the same record as admin), they cannot see the Variable Editor.

### Resolution

The reason users with the certain role are seeing this issue is that there is a custom _before_\-query Business Rule (BR) on sc\_req\_item (RITM) which they are failing.  
  
Disabling the custom BR resolves the issue, and those users are once again able to see both the Variable Editor and the variables within it on sc\_task records.
