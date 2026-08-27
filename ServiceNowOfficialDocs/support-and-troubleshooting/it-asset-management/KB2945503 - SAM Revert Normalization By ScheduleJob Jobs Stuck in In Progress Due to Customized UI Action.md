---
title: "SAM: \"Revert Normalization By ScheduleJob\" Jobs Stuck in \"In Progress\" Due to Customized UI Action"
aliases:
  - KB2945503
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2945503
kb_number: KB2945503
last_modified: 2026-04-27
---

## Issue

Jobs triggered by the UI Action "Revert Normalization" > "SAM - revert Normalization By ScheduleJob from UI" remain permanently stuck in "In Progress" status in `samp_job_log`, preventing Software Discovery Models from transitioning out of their current normalization state. Each subsequent click of the Revert Normalization button creates additional stuck jobs, causing further pile-up.

## Resolution

Revert the UI Action "SAM - revert Normalization By ScheduleJob from UI" to its OOB version if its customised
