---
title: "How to verify that notification record conditions are met"
aliases:
  - KB0528655
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0528655
kb_number: KB0528655
last_modified: 2026-03-24
---

## How to verify that notification record conditions are met

  

### Issue

Beginning with the Berlin release, email notifications are triggered by conditions in the notification record rather than specific events. If you do not receive expected notifications, verify that the notification record conditions are correctly configured.

### Release

Beginning with the Berlin release

### Resolution

1.  Go to System Policy > Email > Notifications.
2.  Select the notification you want to test. For example, select the Incident Commented notification if you expect a notification from an incident comment.
3.  Confirm the notification conditions in the record are valid.
4.  Select Update if you made any changes to the notification record.
5.  Test the notification by performing an action that meets the record conditions.
