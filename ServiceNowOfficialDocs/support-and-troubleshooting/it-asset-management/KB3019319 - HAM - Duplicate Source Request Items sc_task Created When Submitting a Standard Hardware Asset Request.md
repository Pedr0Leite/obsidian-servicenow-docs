---
title: "HAM - Duplicate \"Source Request Items\" sc_task Created When Submitting a Standard Hardware Asset Request"
aliases:
  - KB3019319
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3019319
kb_number: KB3019319
last_modified: 2026-05-14
---

## Issue

When a Standard Hardware Asset Request is submitted, two sc\_tasks with the short description "Source Request Items" are created instead of one. The two tasks are typically created a few seconds apart.

## Resolution

Deactivate the legacy "Source Request" workflow in the Workflow Editor. The Flow Designer flow should remain active and will continue to create the single expected sc\_task.

Steps:

1.  Navigate to the Workflow Editor on the affected instance.
2.  Locate the legacy "Source Request" workflow.
3.  Deactivate or retire the published version of the workflow.
4.  Verify by submitting a new Standard Hardware Asset Request and confirming that only a single "Source Request Items" sc\_task is created.

The Flow Designer flow is controlled by the system property com.sn\_itam.enable\_flow\_designer.source\_request. Confirm this is set to true before making any changes.
