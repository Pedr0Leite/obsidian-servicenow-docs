---
title: System and custom notification and delivery channel preferences in Next Experience
description: You can manage and set your own notification preferences, including customized notifications and channels for receiving them.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/advanced-notification-prefrences.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Notification Preferences, Notifications, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-concept
---

# System and custom notification and delivery channel preferences in Next Experience

You can manage and set your own notification preferences, including customized [[notifications|notifications]] and channels for receiving them.

With notification preferences, you can control the [[system-notifications-landing|system notifications]] and custom notifications that you receive and apply conditions to restrict notification delivery and choose how the notifications are delivered to you.

**Note:** Standardized forms across custom notification preferences and delivery channels have been enabled from Yokohama onwards. To use standardized forms, set the property **glide.notification.preference.sn\_form\_enabled** to `true`.

## Search notifications

You can also search for notifications under both system and custom notifications. There are 2 types of searches, search on preferences that only searches if it matches the notification name and [[ia-ai-search|AI search]].

With AI search, the search functionality now goes beyond just looking for notification names. It can also search within fields of notification records, offering a broader and more accurate search experience. To use the AI search, the AI Search for Notifications plugin must be installed and index sources **Platform Notifications V1** and **Platform Notifications V2**, for more information see [[activate-ai-search-for-notifications-plugin|Activate AI Search for Notifications]] and [[index-ai-search-for-notification|Index AI Search for notifications]].

## System notifications

System notifications alert you of record changes that might concern or interest you. You can be notified via email, SMS text messages, [[c_PushNotifications|push notifications]], or messaging applications.

With system notifications, you can:

-   Set your preferences for specific notifications by searching in the list of your notifications or by filtering them by category.
-   Set preferences at a global level.
-   Easily enable or disable all notifications or individual notifications.
-   Use advanced filter options based on categories, delivery channels, active or inactive notifications, email digest, and subscribable notifications.
-   Add or modify a notification schedule for individual delivery channels for each system notification.
-   Set a schedule for all notifications, individual system notifications, or delivery channels.

    For more information, see [[apply-notification-conditions|Apply notification conditions]]


## Custom notifications

A custom notification is a system notification that you can subscribe to and customize by adding conditions.

With custom notifications, you can:

-   Search for a specific notification in the list of your notifications to be able to set your preferences for that notification.
-   Use advanced filter options based on categories, delivery channels, active or inactive subscriptions, and email digest.
-   Create and modify custom notifications, which are subscriptions to notifications that are important to you.
-   Set preferences at a global level.
-   Easily enable or disable all notifications or individual notifications.
-   Enable or disable notification channels.
-   Add or modify a notification schedule for individual delivery channels for each system notification.
-   Set a schedule for all notifications, individual system notifications, or delivery channels.

    For more information, see [Apply notification conditions](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/apply-notification-conditions.md)


**Note:**

Custom notifications for Next Experience do not support notifications that require a related affected record. For these notifications, you have to set the preference in the Core UI. For more information, see [[user-notification-preferences|Setting notification preferences in Core UI]].

**Note:** [[c_SubscriptionBasedNotifications|Subscription-based notifications]] are not domain aware and cannot support domain-specific settings.

## Delivery Channels

Delivery channels is a list of your chosen channels such as email, SMS, instant message and voice channels for receiving notifications.

With Delivery Channels, you can:

-   Enable or disable a particular channel for receiving notifications.
-   Create, edit, or delete notification channels for instant messages, email, SMS, and voice.

    **Note:** Only admins can delete channels from the cmn\_notif\_device table.

-   Choose how notifications are delivered.
-   Set a schedule for the record in the channel and apply to the notifications you want to receive.

-   **[Activate AI Search for Notifications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/activate-ai-search-for-notifications-plugin.md)**  
You can activate the AI Search for Notifications plugin \(com.glide.notification.ais\) for Notifications if you have the admin role. The application includes demo data and installs related ServiceNow® Store applications and plugins if they are not already installed.
-   **[[set-notification-preferences|Set notification preferences]]**  
View, enable, and disable general settings for notification preferences, and delivery channels.
-   **[[create-custom-notifications|Customize system notifications]]**  
Create custom notifications, which are subscriptions to notifications of importance to you, and apply conditions that control specific content included in your custom notification. You can also enable or disable the channels for delivery.
-   **[[modify-notification-schedule|Modify a notification]]**  
Modify a notification by establishing a schedule or setting conditions to control the notifications you receive.
-   **[[create-notification-filter-configuration|Create notification filter configuration for notification preferences]]**  
Control the list of notifications that are displayed to the users under the advanced notification preferences page. This capability can help narrow down and show only relevant notifications based on user criteria.
-   **[[delete-custom-notifications|Delete a custom notification]]**  
Delete custom notifications that you don't need any more.
-   **[[add-email-device|Add a new notification delivery channel]]**  
Add new channels for email, instant message, SMS, and voice to receive notifications and set a schedule for the channel for the notifications you want to receive.
-   **[[edit-or-delete-a-channel|Edit a delivery channel]]**  
Edit an email, instant message, SMS, or voice channel for receiving notifications, and schedule when the channel can receive notifications.

**Parent Topic:**[[preferences-landing|Notification Preferences]]

## Related

- [[activate-ai-search-for-notifications-plugin|Activate AI Search for Notifications]]
- [[index-ai-search-for-notification|Index AI Search for notifications]]
- [[apply-notification-conditions|Apply notification conditions]]
- [[user-notification-preferences|Setting notification preferences in Core UI]]
- [[set-notification-preferences|Set notification preferences]]
- [[create-custom-notifications|Customize system notifications]]
- [[modify-notification-schedule|Modify a notification]]
- [[create-notification-filter-configuration|Create notification filter configuration for notification preferences]]
- [[delete-custom-notifications|Delete a custom notification]]
- [[add-email-device|Add a new notification delivery channel]]
- [[edit-or-delete-a-channel|Edit a delivery channel]]
- [[preferences-landing|Notification Preferences]]
- [[notifications|Notifications]]
- [[system-notifications-landing|System notifications]]
- [[ia-ai-search|AI Search]]
- [[c_PushNotifications|Push notifications]]
- [[c_SubscriptionBasedNotifications|Subscription-based notifications]]
