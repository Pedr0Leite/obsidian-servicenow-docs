---
title: "Tasks Displayed for Other Users on HRM Ticket Page in Employee Center"
aliases:
  - KB2639300
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2639300
kb_number: KB2639300
last_modified: 2025-12-16
---

## Tasks Displayed for Other Users on HRM Ticket Page in Employee Center

  

### Issue

On the onboarding portal, end users can see tasks on the `hrm_ticket_page` that are not assigned to them, especially when they have no tasks of their own. On page load, the portal displays tasks belonging to other users in the tasks/to-dos section, which is not the expected behavior.

### Release

Any Release

### Cause

By default, the HRM Case Header widget (out-of-the-box) displays all active HR tasks related to a case, regardless of assignment. If the filter panel is hidden or customized, the default behavior is to show all tasks.

### Resolution

·  Understand Default Behavior

-   The HRM Case Header widget is designed to show all active tasks for a case, not just tasks assigned to the logged-in user.

·  Enable or Configure the “MINE\_BADGE” Filter

-   If the filter panel is visible, set the default filter to MINE\_BADGE to restrict tasks to those assigned to the logged-in user.
-   If the filter panel is hidden or customized, update the widget configuration to apply MINE\_BADGE by default.

·  Modify Client Controller (Optional)

-   In the HRM Case Header widget, adjust the client controller logic to enforce the MINE\_BADGE filter on load.
-   Example: Add logic in the controller to set the filter before rendering tasks.

·  Upgrade Employee Center Applications

-   Navigate to System Definition > Plugins.
-   Upgrade Employee Center and related HR applications to the latest versions to ensure compatibility and access to recent fixes.

·  Test in Sub-Production

-   Validate changes in a development or test environment before deploying to production.
