---
title: "Interaction 'State' Field Not Editable"
aliases:
  - KB2656693
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2656693
kb_number: KB2656693
last_modified: 2025-12-17
---

## Interaction 'State' Field Not Editable

  

### Issue

When creating a new interaction from the Case creation page or the Interaction tab of any HR Case, the state field is not editable. It defaults to Work in Progress and is read-only.

### Release

Xanadu

### Cause

Missing or changed ACLs for the state field on the Interaction table after upgrading to Xanadu P3 (AWHRC v3.3.1).

### Resolution

-   Confirm the issue occurs only after upgrade to Xanadu P3.
-   Review ACLs for the state field on the Interaction table.
-   Apply one of the following fixes:
    -   Upgrade to HR Agent Workspace v4.0 (available since Feb 2025, compatible with Yokohama) or v3.3.4 (released June 2025, compatible with Xanadu), which includes the fix for PRB1832315.
    -   Workaround: Create the required ACL manually for the Interaction table in the AWHRC scope.
-   Validate that the state field becomes editable after applying the fix.
