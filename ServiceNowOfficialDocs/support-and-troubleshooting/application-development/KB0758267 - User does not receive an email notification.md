---
title: "User does not receive an email notification"
aliases:
  - KB0758267
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758267
kb_number: KB0758267
last_modified: 2024-04-20
---

## User does not receive an email notification

  

### Issue

User does not receive an email notification even when all conditions in the notification pass.

### Cause

The logs in the email indicate the reason why the user is excluded. 

Notification 'Incident assigned to group' (6d1e8e18db6e0b407394dbbb5e96190d) excluded recipients because user's device is inactive (see "cmn\_notif\_device.active"): 'Abel Tuter' (e0b351a5dbe357c060af3c8f9d961990)

The user is excluded from the recipient list because the user's 'Primary Email' notification device is inactive. To find the 'Primary Email' notification device, do the following:

1.  Navigate to cmn\_notif\_device.LIST from the filter navigator. 
2.  Filter for the user in the 'User' column AND 'Primary Email' is true. 

### Resolution

1.  Activate the notification device for this user where 'Primary Email' is set to true.
2.  Make sure this is the only device where 'Primary email' is true. 
3.  Make sure the type of this device is 'Email' and not anything else.
