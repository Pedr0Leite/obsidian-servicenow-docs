---
title: "Flow Activity Not Displayed in Playbook Timeline"
aliases:
  - KB2656784
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2656784
kb_number: KB2656784
last_modified: 2025-12-17
---

## Flow Activity Not Displayed in Playbook Timeline

  

### Issue

A task created from an activity type Flow (e.g., _Verify ELM's overall performance rating_) does not appear in the Playbook timeline. The activity set includes a fulfiller task and a flow activity, but only the fulfiller task is visible.

### Release

Any

### Cause

Activities of type Flow, Container, or Content are not supported for display in the Playbook timeline. Only certain activity types, such as Fulfiller tasks, are shown.

### Resolution

-   Confirm that the behavior is as designed; flow activities will not appear in the Playbook timeline.
-   Use supported activity types (e.g., Fulfiller tasks) if visibility in the Playbook is required.
