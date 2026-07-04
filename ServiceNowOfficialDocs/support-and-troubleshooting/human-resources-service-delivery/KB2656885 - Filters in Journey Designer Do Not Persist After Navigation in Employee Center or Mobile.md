---
title: "Filters in Journey Designer Do Not Persist After Navigation in Employee Center or Mobile"
aliases:
  - KB2656885
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2656885
kb_number: KB2656885
last_modified: 2025-12-17
---

## Filters in Journey Designer Do Not Persist After Navigation in Employee Center or Mobile

  

### Issue

Filters such as Assigned to, Type, and Journey Stage in Journey Designer do not persist after navigating between tasks and the journey overview page. Issue occurs in both portal and mobile views.

### Release

Any

### Cause

Defect in filter persistence logic within Journey Designer prior to version 5.3.

### Resolution

-   Upgrade to Journey Designer v5.3 (released May 25) to apply the fix for filter persistence issues.
-   Track PRB1848941 for reference; fix included in SR - HR - Journey Designer v5.3.
