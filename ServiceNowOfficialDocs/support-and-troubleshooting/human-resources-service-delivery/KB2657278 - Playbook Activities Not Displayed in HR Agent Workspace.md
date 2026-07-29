---
title: "Playbook Activities Not Displayed in HR Agent Workspace"
aliases:
  - KB2657278
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657278
kb_number: KB2657278
last_modified: 2025-12-17
---

## Playbook Activities Not Displayed in HR Agent Workspace

  

### Issue

Playbook in HR Agent Workspace does not reflect all activities for Lifecycle Events (LE) cases.  
The issue occurs in instances running Playbook Experience v25.1.2, while production or other environments with newer versions display activities correctly.

### Release

Any

### Cause

A known out-of-the-box (OOTB) issue in Playbook Experience v25.1.2 prevents activities from displaying correctly in the playbook. Errors related to `now-playbook-data-broker` may appear in the console.

### Resolution

-   Upgrade the Playbook Experience plugin to version 25.2 or above, where the issue is resolved.
-   Verify that all activities are visible in the playbook after the upgrade.
