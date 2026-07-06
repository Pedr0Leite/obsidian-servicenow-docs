---
title: "SLA emails are not sent to assigned to user"
aliases:
  - KB0752062
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752062
kb_number: KB0752062
last_modified: 2025-11-19
---

## SLA emails are not sent to assigned to user

  

### Issue

SLA emails are not sent to assigned to user.

### Release

Any Release

### Cause

'Send to event creator' field is unchecked on the notification record.

### Resolution

If the notification is triggered by an event and that event is performed by an user to whom this notification should be sent, then 'Send to event creator' field should be checked on the notification record.

### Related Links

[https://docs.servicenow.com/bundle/quebec-servicenow-platform/page/administer/notification/task/t\_CreateANotification.html](https://docs.servicenow.com/bundle/quebec-servicenow-platform/page/administer/notification/task/t_CreateANotification.html)
