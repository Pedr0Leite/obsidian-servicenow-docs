---
title: "Hide Interview Question Icon in HR Agent Workspace Conceptual Sidebar"
aliases:
  - KB2636134
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2636134
kb_number: KB2636134
last_modified: 2026-01-01
---

## Hide Interview Question Icon in HR Agent Workspace Conceptual Sidebar

  

### Issue

In HR Agent Workspace, the Interview Question icon on the conceptual sidebar could not be hidden when creating a new interview record. The icon is defined as a Page Collection in UI Builder, and while other tabs can be hidden, no direct option was available to hide this component. Attempts to create a new variant for the Interview Questions page did not provide a workaround.

### Release

Any Release

### Cause

The icon is controlled by a Page Collection configuration in UI Builder. By default, there is no out-of-the-box option to conditionally hide this component without using UX screen conditions.

### Resolution

To hide the Interview Question icon in HR Agent Workspace:

-   Navigate to UX Screen Conditions in UI Builder.
-   Identify the record associated with the Interview Questions page.
-   Use the Script field in the UX Screen Condition to define logic for hiding the icon based on required conditions.
-   Apply the condition and test functionality:
    -   If the interview form fails to load after applying the condition, revert the UX Screen Condition record to the store app and reapply the fix.
-   For customizations:
    -   If additional tabs disappear or edit access to the Case (SRP) page is lost, note that the out-of-the-box CASE SRP variant is read-only.
    -   Create a duplicate variant for customizations and set its order below the default variant to ensure it is used.
