---
title: "\"New\" Button Missing from HR Task Related List in Agent Workspace"
aliases:
  - KB2639682
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2639682
kb_number: KB2639682
last_modified: 2025-12-16
---

## "New" Button Missing from HR Task Related List in Agent Workspace

  

### Issue

The "New" button is missing from the HR Task Related List in Agent Workspace, preventing users from creating HR Tasks directly from a case.  
This occurs when viewing any ER Case record and accessing the HR Tasks tab in Agent Workspace.  
The missing button impacts workflow efficiency for HR case management.

### Release

Any Release

### Cause

The global Declarative Action responsible for the "New" button was overridden by a similar action for the Source-to-Pay Workspace, due to script conditions returning false.

### Resolution

-   Update Agent Workspace for HR Case Management to the latest version (initial step).
-   Enable the Experience Restricted checkbox for the Source-to-Pay Workspace Declarative Action.
    -   This ensures the global "New" button displays correctly in the HR Task Related List.
-   Validate the fix by checking the HR Task tab in Agent Workspace after applying the change
