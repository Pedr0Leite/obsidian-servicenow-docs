---
title: "Outbound Email addressed to wrong email address"
aliases:
  - KB0785131
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785131
kb_number: KB0785131
last_modified: 2024-04-16
---

## Outbound Email addressed to wrong email address

  

### Issue

Outbound emails are sent to the wrong email address. When you check the email logs, it shows the recipient is included but in the email header, it is addressed to different email address.

### Cause

The email address mentioned in the cmn\_notif\_device is different than the email address in the sys\_user profile.

System always checks the cmn\_notif\_device to get the email address of a user.

### Resolution

Change the email address in cmn\_notif\_device to match the email address in sys\_user.
