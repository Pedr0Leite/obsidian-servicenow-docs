---
title: "SAM Pro Renewal Calendar – Personalize Option Shows Permission Error for Admin"
aliases:
  - KB2949078
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2949078
kb_number: KB2949078
last_modified: 2026-04-10
---

## Text

## Issue

In the Software Asset Management Professional (SAM Pro) workspace, the Personalization (gear) icon in the Renewal Calendar displays a permission error, even for users with admin or elevated roles.

![](/sys_attachment.do?sys_id=77390c2f4740c71030fba325126d43f2)

## Cause

This behavior is expected and by design.

The Personalize option is not supported in the SAM Pro workspace. However, the icon is still visible due to a limitation of the shared Roadmap component used across multiple workspaces.

## Explanation

-   The Personalize (gear) icon appears because the Renewal Calendar leverages a shared Roadmap component.
-   This component is also used in:
    -   Strategic Planning Workspace
    -   Portfolio Planning Workspace
-   In those workspaces, personalization is fully functional and supported, allowing users to:
    -   Configure grouping
    -   Apply color coding
    -   Define metrics
    -   Manage milestones
-   However, in the SAM Pro (Software Asset Workspace):
    -   The roadmap is read-only
    -   Personalization functionality is intentionally disabled
    -   The icon cannot be hidden due to a current platform limitation

## Observed Behavior

-   Clicking the Personalize icon results in a permission error
-   This occurs even for users with:
    -   `admin`
    -   `maint` roles

## Expected Behavior

-   The Personalize option is non-functional in SAM Pro.
-   The icon remains visible but should not be used.
-   This is intentional platform behavior due to a limitation of the shared Roadmap component.
-   The feature is supported in Strategic Planning Workspace and Portfolio Planning Workspace.

## Resolution / Additional Information

-   There is no workaround to enable or hide the Personalize option in SAM Pro.
-   Users are advised to ignore the Personalize icon in this workspace.
-   For roadmap personalization details, refer to:  
    [https://www.servicenow.com/docs/r/it-business-management/scenario-planning-in-spw/personalize-a-roadmap.html](https://www.servicenow.com/docs/r/it-business-management/scenario-planning-in-spw/personalize-a-roadmap.html)
-   To request enhancements, submit via Idea Management:  
    [https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0755878](/kb?id=kb_article_view&sysparm_article=KB0755878)
-   This behavior is a known limitation and any change would require a future product enhancement.
