---
title: "\"Unable to get task list\" Error for Managers and Mentors in Journey Tasks"
aliases:
  - KB2642177
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2642177
kb_number: KB2642177
last_modified: 2026-01-02
---

## "Unable to get task list" Error for Managers and Mentors in Journey Tasks

  

### Issue

Managers and mentors encounter an "Unable to get task list" error when accessing journey tasks.

-   The error affects manager/mentor personas only, not employees.
-   Issue was previously resolved in development but persists in acceptance environment.
-   Appears linked to changes in HR Task to-do configuration, specifically when excluding HR Tasks with a parent lifecycle event case.

### Release

Any

### Cause

The error occurs due to modification of the out-of-box (OOB) HR Task to-do configuration to exclude parent HR cases with a lifecycle event fulfillment type.

### Resolution

-   Do not modify OOB configurations. Instead, create a new to-do configuration with the required conditions.
-   Revert changes made to the OOB configuration and implement a new configuration for custom conditions.
-   This approach resolved the issue during testing.
-   A defect (PRB1852568) was logged for tracking purposes.
