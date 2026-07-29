---
title: "sn_hr_le_activity sends notification to a random user not in the recipients."
aliases:
  - KB0814002
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814002
kb_number: KB0814002
last_modified: 2024-04-08
---

## sn\_hr\_le\_activity sends notification to a random user not in the recipients.

  

### Issue

sn\_hr\_le\_activity sends notification to a random user not in the recipients.

### Cause

When sys\_user\_grmember has a user with an (empty) group, it is returned in the "Check if there is at least one recipient" IF activity of Lifecycle Event Notification workflow.

### Resolution

1.  Check if sys\_user\_grmember table has a record for that user with an (empty) group
2.  Remove this record if not required or update it with an appropriate group.
