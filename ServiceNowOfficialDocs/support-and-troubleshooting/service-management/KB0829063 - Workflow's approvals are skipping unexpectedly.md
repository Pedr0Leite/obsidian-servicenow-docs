---
title: "Workflow's approvals are skipping unexpectedly"
aliases:
  - KB0829063
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0829063
kb_number: KB0829063
last_modified: 2024-04-08
---

## Workflow's approvals are skipping unexpectedly

  

### Issue

The user's _vulnerability_ workflow's approvals were skipping unexpectedly and they needed to know why.

### Resolution

The root of the issue was found to be a custom query Business Rule. What was happening is that the logic within the workflow approval scripts was trying to reach out against the sn\_vul\_vulnerable\_item table. However, when it tried to do so, the custom query Business Rule tacked on additional information to the query and would not allow correct information to return - hence the system could not resolve the returned result, and because of that, it took the skipped condition path.
