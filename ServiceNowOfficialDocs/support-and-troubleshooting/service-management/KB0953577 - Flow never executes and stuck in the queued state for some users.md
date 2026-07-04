---
title: "Flow never executes and stuck in the queued state for some users"
aliases:
  - KB0953577
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0953577
kb_number: KB0953577
last_modified: 2025-10-29
---

## Flow never executes and stuck in the queued state for some users

  

### Issue

The flow never executes and stuck in the queued state for some users

### Release

All Versions

### Cause

-   The User ID field in the sys\_user table is set to more than a length of 40 \[Example: cde.junior.@servicenow.com.br\]
-   The created by field on sys\_flow\_context table TRUNCATES the id and then saves it as 40 characters.
-   When the flow actually tries to execute, it doesn't find the user and hence fails to execute.
-   This is causing empty flow names in flow-context - causing the original flow to appear to be hung/queued state and never execute  
    

### Resolution

Please reduce the length of the impacted user's user\_id
