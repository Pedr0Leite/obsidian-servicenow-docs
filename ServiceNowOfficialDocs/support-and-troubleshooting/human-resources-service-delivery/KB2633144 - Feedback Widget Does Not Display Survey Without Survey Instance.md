---
title: "Feedback Widget Does Not Display Survey Without Survey Instance"
aliases:
  - KB2633144
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2633144
kb_number: KB2633144
last_modified: 2026-01-01
---

## Feedback Widget Does Not Display Survey Without Survey Instance

  

### Issue

The feedback widget does not display an existing survey unless the logged-in user has a corresponding survey instance record. Manual creation of survey instances for all users is impractical, and the requirement is to make the survey visible to all Employee Center visitors.

### Release

Any Release

### Cause

This is out-of-the-box (OOTB) behavior. The widget logic requires a survey instance for visibility. Survey visibility is controlled by audience configuration and trigger conditions; the widget only delivers the survey and does not override these rules.

### Resolution

 **Confirm that survey visibility depends on:**

-   Audience configuration of the survey.
-   Trigger conditions defined in the survey setup.

 **To make surveys visible to all users:**

-   Configure the survey audience to include all Employee Center visitors.
-   Ensure trigger conditions allow survey generation for all users.

 **Note:** The feedback widget cannot bypass these rules; this is intended product design.
