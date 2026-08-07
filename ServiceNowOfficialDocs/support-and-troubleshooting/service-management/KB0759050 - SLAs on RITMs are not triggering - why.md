---
title: "SLAs on RITMs are not triggering - why?"
aliases:
  - KB0759050
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759050
kb_number: KB0759050
last_modified: 2024-04-07
---

## SLAs on RITMs are not triggering - why?

  

### Issue

SLAs on RITMs are not triggering per the SLA Definition's Start conditions, and the user would like to know why.

### Resolution

The reported behavior was experienced because, while the SLA Definition was on the correct table for a RITM record (sc\_req\_item), updates were being made on the child sc\_task record and then pushed to the parent. The reason then that SLAs are not triggering on the RITM based on those child updates is because an update needs to be pushed to the RITM for those updates to register on the back-end.  
  
For example, after making updates to the child sc\_task record, pushing even a minor update to the RITM (e.g. like adding a '.' to the short description field on the RITM) will trigger the Run SLAs Business Rule and the SLA will attach immediately. Until that update is made, however, the SLA will not attach.

Therefore, it is recommended that if such an implementation must stay in place, it would be best for the user to create a custom Business Rule to push an update to the parent RITM when the update is made to the child sc\_task.  
  
Ideally, however, the method which is recognized as best practice is to create SLA Definitions explicitly on the table where updates are being made (e.g. if RITM-level SLAs are needed, all relevant updates are made on the RITM record itself, not a child or associated record).
