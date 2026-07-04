---
title: "Completing an Activity Request Records as an itil user does not reflect in the Onboarding Activity set state "
aliases:
  - KB2939552
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2939552
kb_number: KB2939552
last_modified: 2026-05-05
---

## Issue

When an ITIL user completes a request (`sc_request`) record created by an activity set in the onboarding lifecycle, the activity state does not change to Complete. This behavior does not occur when an admin user completes the same request, where the activity state updates as expected. The issue persists even after following ServiceNow documentation to add the sn\_hr\_le.activity\_writer role to the ITIL user group. 

## Resolution

ServiceNow's Life Events case handling flows include built-in logic that periodically checks and updates activity statuses, ensuring records remain accurate even when the activity status check Business Rule does not execute. This periodic check runs automatically every 4 hours by default. The interval is configured within the activity set — note that the interval field is hidden by default and must be made visible before it can be modified.

How to speed up the LE activity status check process?

-   Reduce the wait interval to speed up activity status updates. Avoid setting the value too low, as excessively frequent checks may introduce unnecessary system load.
-   Grant ITIL users access to the LE Case.
