---
title: "AI agents/workflows are not being automatically triggered, even when all configured trigger configuration/conditions are met."
aliases:
  - KB3132271
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3132271
kb_number: KB3132271
last_modified: 2026-07-01
---

## AI agents/workflows are not being automatically triggered, even when all configured trigger configuration/conditions are met.

  

### Issue

Example: In this KB, we are using the example of "Help manage software request" AI workflow, which comes with Now Assist for Software Asset Management plugin

  
The 'Help manage software request' AI workflow setup in the any instance is not autotriggering the agent when following the steps in the documentation. The agent requires a manual prompt in the NA Panel/Virtual Agent to run after executing the steps. The issue was observed when raising a software request for Adobe, approving the RITM, and impersonating user Abraham Lincoln with correct roles{itil, procurement\_user, and now\_assist\_panel\_user} to access the RITM in the asset workspace. The OOTB trigger was not functioning as expected, while custom triggers created with similar conditions worked.  
  

### Release

Yokohama, Zurich, Australia

### Cause

The issue was caused by the 'Help manage software requests' AI agent configuration override and the associated Trigger (Sys Hub Flow) being created in the Global scope. Activation failed when attempting to use the trigger within the Now Assist for Software Asset Management (SAM) scope due to a scope mismatch.  
  

### Resolution

  
1\. Delete the 'Help manage software requests' AI agent configuration override and associated Trigger (Sys Hub Flow) records from the Global scope.

NOTE: To find the AI agent configuration override

-   Go to sn\_aia\_trigger\_configuration and look for Trigger configuration overrides Related List OR sn\_aia\_trigger\_config\_override table and find your AI agent using the use case column

2\. Reactivate the trigger from the Now Assist for Software Asset Management (SAM) scope to allow the records to be correctly regenerated in the appropriate scope.

3\. Verify the trigger execution history to confirm the resolution. The triggers are now activated and functioning as expected.
