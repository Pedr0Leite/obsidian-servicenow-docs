---
title: "How to verify the push service received a notification"
aliases:
  - KB0551644
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551644
kb_number: KB0551644
last_modified: 2026-08-20
---

## How to verify the push service received a notification

  

### Issue

After the instance sends a push notification to the push service, it changes its **state** in the queue to **Success**. If ServiceNow successfully sends a push notification but users are not receiving it, there may be an issue with the push service. Push providers such as Apple and Google make no guarantees of delivery even though they have acknowledged receipt of a push notification.

### Resolution

1.  Login to the instance.
2.  Navigate to **System Logs > Push Notifications**.
3.  Verify that the push notification is in the queue with a state of **Success**.
4.  Copy the request ID and search for it on Splunk at https://search.servicenow.net/
5.  Logs should show, starting from the bottom, the push notification being received and then sent to APNs  
      
    ![](/sys_attachment.do?sys_id=1b5b32bbdb912590770be6be13961981)
