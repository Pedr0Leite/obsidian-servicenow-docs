---
title: "Adobe SAM - Import Adobe User Subscriptions job is failing even though the OAUTH generated successfully"
aliases:
  - KB1700148
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1700148
kb_number: KB1700148
last_modified: 2024-08-25
---

## Adobe SAM - Import Adobe User Subscriptions job is failing even though the OAUTH generated successfully

  

### Issue

Adobe SAM - Import Adobe User Subscriptions job is failing even though the OAUTH generated successfully.

When validated the system log and we found below error

Error: SamImportUserSubscriptionsAdobe: Failed to run job. Please look into logs for more details.: no thrown error

  
  

### Cause

We have identified that the Organization\_ID entered on the integration profile was missing "@AdobeOrg" at the end.

### Resolution

Please validate Organization\_ID entered on the integration profile and add "@AdobeOrg" at the end.
