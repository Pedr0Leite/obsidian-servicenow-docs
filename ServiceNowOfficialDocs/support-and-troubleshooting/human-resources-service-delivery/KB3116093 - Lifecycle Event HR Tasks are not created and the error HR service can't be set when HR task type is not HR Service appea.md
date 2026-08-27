---
title: "Lifecycle Event HR Tasks are not created and the error \"HR service can't be set when HR task type is not HR Service\" appears when submitting a request in ESC"
aliases:
  - KB3116093
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3116093
kb_number: KB3116093
last_modified: 2026-06-25
---

## Issue

When submitting a LE Case through the Employee Service Center (ESC), the Lifecycle Event (LE) case is created but the expected HR Tasks are not generated. One or more Activity Sets on the LE case land in an Error state, and the following message is displayed:

> _HR service can't be set when HR task type is not HR Service_

## Resolution

1.  Identify the HR Templates (`sn_hr_core_template`) used by the Lifecycle Event Activity Set activities.
2.  For any template where the HR Task Type is not "HR service" (e.g., "Mark when completed"), remove the value in the "HR service" field. This clears the conflict with the OOB "Prevent setting HR service" Business Rule and allows the HR Task to be created.
3.  Repeat for all HR Templates associated with the  LE types — not only the first one found — so every Activity Set can complete.
4.  Re-test by submitting a new LE case in ESC and confirm the HR Tasks are now generated and visible LE case, with all Activity Sets reaching a non-error state.
