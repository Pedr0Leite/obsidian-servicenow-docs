---
title: "Multiple payloads are getting generated for one push notification"
aliases:
  - KB0818323
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818323
kb_number: KB0818323
last_modified: 2024-04-08
---

## Multiple payloads are getting generated for one push notification

  

### Issue

2 payloads are generated even though there is only 1 notification

![](sys_attachment.do?sys_id=e1b5780ddb4cb8d022e0fb24399619d2)

### Cause

-   User can have different push platforms depending on what device they logged in with.
-   If a push notification is sent to that user, it will use the platform of the user

### Resolution

If the user has 2 devices in “sys\_push\_notif\_app\_install” table then the push notification will be sent to all the 2 devices.
