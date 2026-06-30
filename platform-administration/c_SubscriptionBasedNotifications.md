---
title: Subscription-based notifications
description: Subscription-based notifications enable users to proactively subscribe to items that interest them and unsubscribe from messages that are not mandatory.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/c\_SubscriptionBasedNotifications.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Preferences in Core UI, Notification Preferences, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Subscription-based notifications

Subscription-based notifications enable users to proactively subscribe to items that interest them and unsubscribe from messages that are not mandatory.

Users can also specify additional notification channels that each of their [[notifications|notifications]] can be configured to use.

Before users can manage the notifications that are sent to them, administrators must create email notifications to which users can subscribe. Administrators can also make subscription-based notifications mandatory so users cannot unsubscribe to them. Then users can subscribe or unsubscribe to the notifications, and add [[c_UseSchedules|schedules]] and filters to the subscription to limit the notifications that can be received.

Notifications that administrators mark as subscribable are automatically available in user notification settings. Users are limited to one subscription per notification.

Administrators should create subscription-based notifications when they do not want to specify users for a notification and want to let users proactively subscribe to the notification.

**Note:** Subscription-based notifications are not domain aware and cannot support domain-specific settings.

## Subscriptions 2.0 plugin

The Subscription Based Notifications 2.0 plugin must be active to use subscribable notifications. This plugin is active by default on all new and upgraded instances.

The plugin installs the Notification Subscription \[sys\_notif\_subscription\] table, which holds user subscriptions to all notifications.

## Subscriptions and notification preferences

Users can subscribe to notifications available to them through their [[preferences-landing|notification preferences]]. In the Core UI interface, all users can set and modify their notification preferences through the **Notifications** tab of the System Settings window.

-   **[[create-personal-notifications|Create personal notifications]]**  
Create personal notifications, which are subscriptions to notifications of importance to you. You can apply conditions that control specific content included in your personal notification, and also enable or disable the channels for delivery.
-   **[[t_CreateAServiceProvider|Create a service provider]]**  
Administrators can configure service providers for devices that use SMS.
-   **[[t_MakingANotificationMandatory|Make a notification mandatory]]**  
To prevent users from turning off or deleting a subscription to a notification, make the notification mandatory.
-   **[[t_ForcingANotificationToBeSent|Force a notification to be sent]]**  
To force a notification to be sent to the specified users, enable forced delivery.
-   **[[t_NotificationFilters|Create a notification filter]]**  
Notification filters enable a user to control the delivery of messages by creating special conditions on multiple tables in a single, reusable filter.

**Parent Topic:**[[user-notification-preferences|Setting notification preferences in Core UI]]

## Related

- [[create-personal-notifications|Create personal notifications]]
- [[t_CreateAServiceProvider|Create a service provider]]
- [[t_MakingANotificationMandatory|Make a notification mandatory]]
- [[t_ForcingANotificationToBeSent|Force a notification to be sent]]
- [[t_NotificationFilters|Create a notification filter]]
- [[user-notification-preferences|Setting notification preferences in Core UI]]
- [[notifications|Notifications]]
- [[c_UseSchedules|Schedules]]
- [[preferences-landing|Notification Preferences]]
