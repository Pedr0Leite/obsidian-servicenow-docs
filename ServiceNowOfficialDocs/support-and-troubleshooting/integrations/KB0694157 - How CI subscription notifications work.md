---
title: "How CI subscription notifications work"
aliases:
  - KB0694157
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694157
kb_number: KB0694157
last_modified: 2026-02-03
---

## How CI subscription notifications work

  

### Issue

Learn how the Subscribe CI feature notifies users when an incident is reported against a configuration item (CI). This feature helps asset owners and CI owners monitor critical incidents affecting their CIs.

### How CI subscription notifications work

#### Subscription creation

When a user subscribes to a CI, the system creates a record in the Notification Subscription \[sys\_notif\_subscription\] table. This table stores details about the user, notification, device, and table.

![Example of subscription UI](sys_attachment.do?sys_id=9bf3ce1697fe3a905ad8f6e11153af77)

#### Event generation

When an incident is submitted for a CI that a user is subscribed to, the following process occurs:

1.  The Affected ci notifications business rule fires and generates the ci.notification.for.task event.
2.  The event triggers the Handle Affected CIs for Task script action.
3.  The script action calls the handleTaskAffectedCIs method in the CMDBAffectedCINotificationsUtils Script Include, passing the sys\_id of the task record as a parameter.

#### Notification delivery

The handleTaskAffectedCIs method:

1.  Retrieves the affected CIs and subscriptions from the \[sys\_notif\_subscription\] and \[cmn\_notif\_message\] tables.
2.  Generates ci.affected events with parameters including the CI name and sys\_id of the affected CI.
3.  Triggers the **CI affected** notification.

The **CI affected** notification is a subscription-based notification. The notification engine sends email or SMS notifications to all users subscribed to the affected CI.

![Example of CI affected business rule UI](sys_attachment.do?sys_id=dff3ce1697fe3a905ad8f6e11153af72)

"CI Affected" is a subscription notification. Notification engine will trigger notifications ( **email or sms** ) for all the user who are subscribed to the affected CI.

![Example of notification email for subscribed CIs](sys_attachment.do?sys_id=1ff3ce1697fe3a905ad8f6e11153af6d)

### Release

All supported releases

### Resolution

### Troubleshooting

If CI subscription notifications are not working as expected, verify that the following components have not been customized:

-   Affected ci notifications business rule
-   Handle Affected CIs for Task script action
-   CMDBAffectedCINotificationsUtils Script Include
-   CI affected notification

### Related Links

[Subscription-based notifications](https://docs.servicenow.com/search?q=Subscription-based+notifications "Subscription-based notifications")
