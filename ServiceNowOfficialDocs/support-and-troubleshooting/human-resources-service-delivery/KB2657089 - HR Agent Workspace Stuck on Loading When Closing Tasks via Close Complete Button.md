---
title: "HR Agent Workspace Stuck on Loading When Closing Tasks via Close Complete Button"
aliases:
  - KB2657089
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657089
kb_number: KB2657089
last_modified: 2025-12-17
---

## HR Agent Workspace Stuck on Loading When Closing Tasks via Close Complete Button

  

### Issue

In HR Agent Workspace, clicking the Close Complete button displays a perpetual loading indicator and does not navigate to the next item or update the screen. The issue occurs when closing ad hoc HR tasks generated via Flow activities.  
  

### Release

Any

### Cause

A defect in the Playbook/HR integration prevents proper task closure in HR Agent Workspace. This issue is tracked under PRB1844302.

### Resolution

To resolve the issue:

-   Upgrade the instance to Washington DC Patch 10 or Xanadu Patch 6 (or later).
-   Update the following plugins to their latest versions:
    -   Playbook Experiences
    -   Playbook Experiences Components
-   Validate the fix in a lower environment before applying to production.
-   Refer to PRB1844302 for tracking the permanent fix and patch details.
