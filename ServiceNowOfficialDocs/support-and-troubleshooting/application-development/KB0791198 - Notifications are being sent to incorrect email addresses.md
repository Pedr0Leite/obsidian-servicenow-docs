---
title: "Notifications are being sent to incorrect email addresses"
aliases:
  - KB0791198
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791198
kb_number: KB0791198
last_modified: 2024-05-01
---

## Notifications are being sent to incorrect email addresses

  

### Issue

When we send emails to users , emails are not sent to the email set on the user profile in sys\_user table instead it is sent to different email address

### Cause

Different email set for this user in the "cmn\_notif\_device" table when compared with sys\_user table

### Resolution

We need to sync email address between "user profile" (sys\_user)  and "cmn\_notif\_device" table. This will fix the issue. There is already a BR that does this sync initially when the user is created in sys\_user table. But if the email address in these tables vary later due to manual intervention, make sure both are in sync in both these tables.
