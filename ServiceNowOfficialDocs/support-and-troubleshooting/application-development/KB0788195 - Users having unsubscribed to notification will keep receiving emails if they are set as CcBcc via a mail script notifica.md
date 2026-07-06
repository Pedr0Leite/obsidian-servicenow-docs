---
title: "Users having unsubscribed to notification will keep receiving emails if they are set as Cc/Bcc via a mail script notification"
aliases:
  - KB0788195
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788195
kb_number: KB0788195
last_modified: 2025-01-22
---

## Users having unsubscribed to notification will keep receiving emails if they are set as Cc/Bcc via a mail script notification

  

### Issue

-   Have a user unsubscribe to a notification (Incident commented, for instance)
-   Have the notification use an email template, which will in turn use an email script
-   Have this email script send the notification to the recently created user in Cc
-   Impersonate that user and comment an incident (or do any action that should (not) trigger the associated notification)
-   The user who unsubscribed to the notification will receive that notification anyway

### Release

Tokyo and Above

### Cause

This is due to the fact that the mail script is externally inserting the email address. This is similar to adding the recipient externally with a BR and it is done outside the checks performed by notification engine. Therefore the notification engine would not be able to see if the additional recipient has a filter or not.

### Resolution

This is expected behaviour in the currently supported releases, and it should be taken into account while designing email notifications.

This is considered as an enhancement request.

Ref.: [PRB1588668/KB1122968 - Users are not unsubscribed when unsubscribing to the emails sent by the hr\_integration\_job\_status sys\_script\_email](https://support.servicenow.com/kb_view.do?sysparm_article=KB1122968 "PRB1588668/KB1122968")
