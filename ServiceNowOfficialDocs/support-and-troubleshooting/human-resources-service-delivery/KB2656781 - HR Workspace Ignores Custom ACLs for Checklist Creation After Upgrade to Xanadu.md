---
title: "HR Workspace Ignores Custom ACLs for Checklist Creation After Upgrade to Xanadu"
aliases:
  - KB2656781
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2656781
kb_number: KB2656781
last_modified: 2025-12-17
---

## HR Workspace Ignores Custom ACLs for Checklist Creation After Upgrade to Xanadu

  

### Issue

After upgrading from Vancouver to Xanadu, agents in HR Agent Workspace can create and edit checklists using Add item and Edit buttons, even when ACLs are set to prevent this. Custom ACLs on checklist and checklist\_item tables work in BackOffice but are ignored in the workspace.

### Release

Any

### Cause

The hr\_ChecklistUtil Script Include uses GlideRecord instead of GlideRecordSecure, causing ACLs to be bypassed in HR Agent Workspace.

### Resolution

-   Duplicate the Checklist - SRP page collection.
-   Add a transform data broker to check ACLs and set the allow editing property based on the broker output.
-   Set the duplicated page’s order lower than the OOTB page.
-   Change GlideRecord to GlideRecordSecure in hr\_ChecklistUtil to enforce ACLs.
