---
title: Configure a push notification message
description: Configure the message displayed to users when they receive their push notification.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/configure-push-notification-message.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Components, Push notifications, Before implementation, Configuration detail, Configuring the Mobile Platform, Mobile Platform]
tags:
  - mobile
  - now-mobile
  - apps
  - platform
  - type-task
---

# Configure a push notification message

Configure the message displayed to users when they receive their push notification.

## Before you begin

To create a push notification message, you must first configure the push notification message content. For more information, see [[config-push-notification-message-content|Configure push notification message content]].

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **System Notification** &gt; **Push** &gt; **Push Messages**.

2.  Click **New**.

3.  In the Push Message form, fill in the following fields:

<table id="table_nqf_pwh_wpb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Name

</td><td>

The string value for this record. **Note:** This name is not visible in the notification, it is only a reference for use during configuration.

</td></tr><tr><td>

Push app

</td><td>

References the mobile app you want to send a notification to.-   Use ServiceNow mobile Application for Mobile Agent.
-   Use ServiceNow Request Application for [[now-mobile-app|Now Mobile app]].


</td></tr><tr><td>

Push message

</td><td>

References the push message content record.

</td></tr><tr><td>

Table

</td><td>

Table selector to choose the table the message originates from. For example, if you want to send notifications when new incidents are created, select the Incident \[incident\] table.

</td></tr><tr><td>

Message

</td><td>

The string value used as the message. This field can contain a simple string, but also supports displaying field values from the source table.**Note:**

To use a field value, wrap the desired column name with `${}`, such as "Change `${number}` has been assigned to you."

</td></tr></tbody>
</table>4.  Click **Submit** to create the record.


## Result

You configured a push notification message and paired it with a push notification message content record.

## What to do next

To complete the notification, an event is required to determine when the push notification is sent and who receives it. For more information, see [[configure-push-notification-event|Configure a push notification event]].

**Parent Topic:**[[configure-mobile-push-notifications|Mobile push notification components]]

## Related

- [[config-push-notification-message-content|Configure push notification message content]]
- [[configure-push-notification-event|Configure a push notification event]]
- [[configure-mobile-push-notifications|Mobile push notification components]]
- [[now-mobile-app|Now Mobile app]]
