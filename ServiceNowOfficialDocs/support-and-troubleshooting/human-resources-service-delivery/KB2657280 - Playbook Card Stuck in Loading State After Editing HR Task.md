---
title: "Playbook Card Stuck in Loading State After Editing HR Task"
aliases:
  - KB2657280
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657280
kb_number: KB2657280
last_modified: 2025-12-17
---

## Playbook Card Stuck in Loading State After Editing HR Task

  

### Issue

In HR Agent Workspace, when an HR task is added and its short description is edited, the playbook card remains stuck in a "Loading" state instead of refreshing automatically.  
This prevents updated task information from displaying as expected during HR lifecycle event cases.

### Release

Any

### Cause

The issue is a defect tracked under PRB1844302. It occurs due to logic at the Java layer that fails to refresh the playbook card after task updates.

### Resolution

-   Upgrade the instance to one of the following versions where the fix is applied:
    -   Washington DC Patch 10 (available 2025-02-07)
    -   Xanadu Patch 6 (available 2025-02-13)
-   Verify that playbook cards refresh correctly after editing HR tasks.
