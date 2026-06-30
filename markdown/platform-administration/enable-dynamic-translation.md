---
title: Enable dynamic translation for email notifications
description: Enable dynamic translation for a notification to send dynamically translated emails to recipients in their preferred language.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/enable-dynamic-translation.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Dynamic translation, Multilingual email notifications, Email and SMS notifications, System notifications, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Enable dynamic translation for email notifications

Enable dynamic translation for a notification to send dynamically translated emails to recipients in their preferred language.

## Before you begin

An email notification must exist. For more information, see [[t_CreateANotification|Create an email notification]].

You must activate the Glide Notification Translation \(com.glide.notification.translation\) plugin.

Set the system property for the dynamic translation. For more information see, [[enable-email-notification-translation|Enable dynamic translation]].

Role required: admin

## About this task

Notification recipients must be defined as active users in the User \[sys\_user\] table. They must also have a valid email address defined for their primary channel \(device\) in the Notification Device \[cmn\_notif\_device\] table.

## Procedure

1.  Navigate to **All** &gt; **[[system-notifications-landing|System Notifications]]** &gt; **Email** &gt; **[[notifications|Notifications]]**.

2.  Select the name of the email notification you want to send.

3.  Select the **What it will contain** tab.

4.  If **Advanced view** is not already selected, select it.

5.  Select the **Enable Dynamic Translation** check box.


## What to do next

[[t_PreviewingNotifications|Preview email notifications]]

**Parent Topic:**[[dynamic-translation|Dynamic translation]]

**Related topics**  


[Enable dynamic translation]()

[Configure the note banner for translated emails]()

## Related

- [[t_CreateANotification|Create an email notification]]
- [[enable-email-notification-translation|Enable dynamic translation]]
- [[t_PreviewingNotifications|Preview email notifications]]
- [[dynamic-translation|Dynamic translation]]
- [[system-notifications-landing|System notifications]]
- [[notifications|Notifications]]
