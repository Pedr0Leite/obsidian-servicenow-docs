---
title: "Undelivered Mail Returned to Sender"
aliases:
  - KB0791883
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791883
kb_number: KB0791883
last_modified: 2026-08-20
---

## Undelivered Mail Returned to Sender

  

### Issue

Emails are not being sent at all & users are not receiving any notifications. 

### Release

### Cause

When checked sys\_user.LIST table, there is only one user in the entire system that has notification = 2 which means Enable.

Hence ONLY one user has been enabled to receive the email notifications.   
  
This is why emails are not getting created, all other users do not have notification = 2 (Enable) in their sys\_user records.

### Resolution

Please make the users enable if they want to get the emails by changing their notification settings from disable to enable.
