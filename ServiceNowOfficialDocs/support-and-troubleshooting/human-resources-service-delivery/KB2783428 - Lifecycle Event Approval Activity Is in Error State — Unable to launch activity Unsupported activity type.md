---
title: "Lifecycle Event Approval Activity Is in Error State — \"Unable to launch activity: Unsupported activity type\""
aliases:
  - KB2783428
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2783428
kb_number: KB2783428
last_modified: 2026-04-30
---

## Issue

Approval Workflow and task are not getting attached to HR cases which uses Lifecycle Event - Approval activity. The issue occurs when attempting to launch an LE Approval activity, resulting in an error. The error is observed in the log as 'ERROR: Unable to launch activity: Unsupported activity type'.  
  

## Resolution

The Approval activity references a deprecated **Workflow** fulfiller\_activity configuration. The system no longer recognises this type, causing the activity to error on launch. The fix is to recreate the Approval activity so it references the current **Approval** activity configuration.

1.  Navigate to **HR Administration > Lifecycle Events** and open the affected Lifecycle Event.
2.  Open the **Activity** that is erroring (the Approval type activity).
3.  Check the **Fulfiller Activity** field — if it references the deprecated Workflow configuration, this is the root cause.
4.  Note all current settings of this activity (name, conditions, assignment, etc.), then **delete** the erroring activity record.
5.  Create a new **Approval** type activity with the same settings. The system will automatically link it to the current Approval fulfiller\_activity configuration.
6.  Save the new activity and re-launch the Lifecycle Event to confirm the Approval activity transitions correctly without the "Unsupported activity type" error.
