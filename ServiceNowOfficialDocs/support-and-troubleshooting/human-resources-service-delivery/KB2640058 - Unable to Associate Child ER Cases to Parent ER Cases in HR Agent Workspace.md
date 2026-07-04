---
title: "Unable to Associate Child ER Cases to Parent ER Cases in HR Agent Workspace"
aliases:
  - KB2640058
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2640058
kb_number: KB2640058
last_modified: 2026-01-03
---

## Unable to Associate Child ER Cases to Parent ER Cases in HR Agent Workspace

  

### Issue

Certain users are unable to associate child Employee Relations (ER) cases to parent ER cases within the HR Agent Workspace.  
The issue occurs when users create a child ER case from the Child Cases tab, but the association between parent and child is not established.  
This problem is intermittent and affects only specific users and environments, notably when users are not impersonated.

### Release

Any Release

### Cause

-   The Parent field was missing from the Workspace UIB view in some instances, preventing proper association.
-   HR Agent Workspace functionality changed in version 4.0.0, deprecating the New button and introducing Add and Remove options for child cases.

### Resolution

-   Verify if the Parent field is present in the Workspace UIB view. If missing, add the field to the form.
-   Update the HR Agent Workspace plugin to version 4.0.1 to enable the new Add and Remove functionality for child cases.
-   Note: The New button is deprecated and will not work in versions 4.0.0 and above.
-   A product defect (PRB1882774) has been logged to restore the New button in a future release (v4.2, scheduled for August).
-   After updating the plugin, configure and use the new functionality for child case association.
