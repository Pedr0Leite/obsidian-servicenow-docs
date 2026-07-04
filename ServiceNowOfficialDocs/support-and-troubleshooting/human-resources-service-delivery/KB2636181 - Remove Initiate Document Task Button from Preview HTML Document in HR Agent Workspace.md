---
title: "Remove \"Initiate Document Task\" Button from Preview HTML Document in HR Agent Workspace"
aliases:
  - KB2636181
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2636181
kb_number: KB2636181
last_modified: 2025-12-16
---

## Remove "Initiate Document Task" Button from Preview HTML Document in HR Agent Workspace

  

### Issue

In HR Agent Workspace, the Preview HTML Document page displayed an Initiate Document Task button that needed to be removed. The page is protected in UI Builder, preventing direct deactivation of the button or its functionality. Guidance was requested on best practices for hiding or removing this button.

### Release

Any Release

### Cause

The issue occurred because:

-   The customer was modifying an older page, not the one rendered in the workspace modal.
-   The correct page displayed in the modal is hr-doc-templates-preview-doc-srp, which is part of the CASE SRP record page configuration.

### Resolution

To remove or hide the Initiate Document Task button:

-   Identify the Correct Page

-   -   Use browser Developer Tools to inspect the modal and locate the `sys_ux_macroponent` ID.
    -   Reference this ID in the sys\_ux\_macroponent table to confirm the correct page.

-   Clone the Correct Page

-   -   Clone hr-doc-templates-preview-doc-srp in UI Builder.
    -   Set the cloned page’s order appropriately so it overrides the default page.

-   Hide the Button

-   -   Locate the component for Initiate Document Task.
    -   Set the Hide component property to true.

-   Future Guidance

-   -   Always verify modal pages using Developer Tools before making changes.
    -   For additional customizations, create duplicate variants and maintain correct order below default variants.
