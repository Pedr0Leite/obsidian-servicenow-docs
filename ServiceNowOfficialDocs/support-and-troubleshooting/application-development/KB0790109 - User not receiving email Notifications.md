---
title: "User not receiving email Notifications"
aliases:
  - KB0790109
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790109
kb_number: KB0790109
last_modified: 2026-06-29
---

## User not receiving email Notifications

  

### Issue

A user is not receiving emails from ServiceNow. He has the Primary device enabled and all Notifications set in the system  according to his Notifications preferences. His email is operative and works correctly.

When trying to preview a notification, the user name appears as a not valid recipient:

![](/sys_attachment.do?sys_id=8d26959d47fd0fd43542f24c736d4390)

### Release

 All

### Cause

General notification field for related user record is set to Disabled instead of Enabled

### Resolution

Note that Notification field should be exposed via list mechanic, hence if Disable is shown then should be changed to Enable in order to have affected users receiving notifications.

[https://docs.servicenow.com/csh?topicname=c\_ListConfiguration.html&version=latest](https://docs.servicenow.com/csh?topicname=c_ListConfiguration.html&version=latest)

![List configuration](/sys_attachment.do?sys_id=dd26d59d47fd0fd43542f24c736d431e "List configuration")
