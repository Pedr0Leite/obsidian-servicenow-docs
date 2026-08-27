---
title: Create a notification filter
description: Notification filters enable a user to control the delivery of messages by creating special conditions on multiple tables in a single, reusable filter.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/t\_NotificationFilters.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Subscription-based notifications, Preferences in Core UI, Notification Preferences, Notifications, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-task
---

# Create a notification filter

Notification filters enable a user to control the delivery of messages by creating special conditions on multiple tables in a single, reusable filter.

## Before you begin

Role required: admin

## About this task

For example, you can create a filter that controls message delivery when active incidents, problems, and change requests for network issues reach a critical state. For Core UI, filters for [[notifications|notifications]] or channels are set through the Notifications tab of the System Settings window. For details, see [[apply-notification-conditions|Apply notification conditions]].

**Note:** The system applies the user's filter conditions after the administrator's conditions have been evaluated. If the administrator's conditions fail, the system ignores notification filters.

## Procedure

1.  Navigate to **All** &gt; **System Notification** &gt; **Email** &gt; **Notification Filters** and create a record.

2.  In the Notification conditions related list of the new record, create and submit filter conditions on one or more tables.

3.  Repeat the procedure to create additional conditions on other tables for this filter.


-   **[[t_FiltDeviceNotifUsingASchedule|Filter device notifications using a schedule]]**  
You can associate devices, such as Email, SMS, and Voice, to [[c_UseSchedules|schedules]] that define when the devices can and cannot receive notifications.
-   **[[t_EditSchedOrFiltNotifMessage|Edit the schedule or filter of an existing notification message]]**  
You can update a schedule or filter that was previously created for an email notification.

**Parent Topic:**[[c_SubscriptionBasedNotifications|Subscription-based notifications]]

## Related

- [[apply-notification-conditions|Apply notification conditions]]
- [[t_FiltDeviceNotifUsingASchedule|Filter device notifications using a schedule]]
- [[t_EditSchedOrFiltNotifMessage|Edit the schedule or filter of an existing notification message]]
- [[c_SubscriptionBasedNotifications|Subscription-based notifications]]
- [[notifications|Notifications]]
- [[c_UseSchedules|Schedules]]
