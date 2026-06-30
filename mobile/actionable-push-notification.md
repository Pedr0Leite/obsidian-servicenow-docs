---
title: Configure actionable push notifications
description: Include actions with your push notifications. Users can perform push notification actions without opening the app.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/actionable-push-notification.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Push notifications, Before implementation, Configuration detail, Configuring the Mobile Platform, Mobile Platform]
---

# Configure actionable push notifications

Include actions with your [[sg-mobile-security-push-notif|push notifications]]. Users can perform push notification actions without opening the app.

<table id="table_mtx_yvm_ylb"><tbody><tr><td>

Up to three actions can be associated with a push notification. These actions must refer to an existing mobile function. The following function types of actions are supported:

-   Action item
-   Navigation
-   URL
-   Chat launcher

</td><td>

\[Omitted image "actionable-notifications.png"\] Alt text: Actionable push notifications.

</td></tr></tbody>
</table>## Creating actionable push notifications

Create actionable push notifications using the following process:

1.  Create a push notification that your users will see on their mobile devices.

2.  Add a push action category to determine what actions your users can take in a notification.

3.  Create functions for each push action in the selected action category. These actions perform tasks on your instance based on what the user selects in the notification.

4.  Map functions with push actions on the actionable push notification. Associate functions to the actions in your notification so the instance uses the correct function for each action.

5.  Create push message content by creating a record to determine what information the notification displays to your users.

6.  Create a standard notification on your instance using the platform notifications.


-   **[[actionable-push-notification-1|Create an actionable push notification]]**  
Create a push notification your users will see on their mobile devices.
-   **[[actionable-push-notification-1a|Actionable push notification script example]]**  
You can use this JSON script example to configure an actionable push notification for ServiceNow® mobile apps.
-   **[[actionable-push-notification-2|Add a push action category]]**  
Select a push category to determine what actions your users can take in a notification. This category defines which actions your users can take when viewing a notification.
-   **[[actionable-push-notification-2-3|Create a push action]]**  
Create push actions to suit your needs, when the base system actions do not meet your requirements.
-   **[[actionable-push-notification-3|Create functions for each push action]]**  
Create mobile function for each function in the selected action category. These actions perform tasks on your instance based on what the user selects in the notification.
-   **[[actionable-push-notification-4|Map functions with push actions on the actionable push notification]]**  
Associate functions to the actions in your notification so the instance uses the correct function for each action.
-   **[[actionable-push-notification-5|Create push message content]]**  
Create a record to determine what information the notification displays to your users.
-   **[[actionable-push-notification-6|Create a standard notification]]**  
Create a standard notification on your instance using the platform notifications.

**Parent Topic:**[[sg-mobile-push-notifications|Mobile push notifications]]

## Related

- [[actionable-push-notification-1|Create an actionable push notification]]
- [[actionable-push-notification-1a|Actionable push notification script example]]
- [[actionable-push-notification-2|Add a push action category]]
- [[actionable-push-notification-2-3|Create a push action]]
- [[actionable-push-notification-3|Create functions for each push action]]
- [[actionable-push-notification-4|Map functions with push actions on the actionable push notification]]
- [[actionable-push-notification-5|Create push message content]]
- [[actionable-push-notification-6|Create a standard notification]]
- [[sg-mobile-push-notifications|Mobile push notifications]]
- [[sg-mobile-security-push-notif|Push notifications]]
