---
title: "HR Tasks Not Visible in Portal To-Do List "
aliases:
  - KB2656909
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2656909
kb_number: KB2656909
last_modified: 2025-12-17
---

## HR Tasks Not Visible in Portal To-Do List

  

### Issue

After the Yokohama upgrade, HR tasks are not visible in the Portal To-Do list, although the task count appears in MyTask. Users cannot open assigned tasks from the portal.

### Release

Yokohama

### Cause

Two Business Rules on HR Task and HR Case tables added restrictive queries, preventing tasks from appearing in the portal To-Do list.

### Resolution

-   Navigate to Business Rules for HR Task and HR Case tables.
-   Identify the two restrictive Business Rules causing the issue.
-   Deactivate these Business Rules in the sub-production instance to restore task visibility.
-   Validate that tasks appear in the Portal To-Do list after deactivation.

Permanent Fix:

-   Track under PRB1926146 (associated with PRB1922171) for future release.
