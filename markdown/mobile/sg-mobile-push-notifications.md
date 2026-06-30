---
title: Mobile push notifications
description: Mobile push notifications are configurable pushed messages that appear directly in a mobile app. These push notifications are non-actionable or actionable, and are configured by administrators to meet the needs of their users.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/sg-mobile-push-notifications.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Before implementation, Configuration detail, Configuring the Mobile Platform, Mobile Platform]
---

# Mobile push notifications

Mobile push notifications are configurable pushed messages that appear directly in a mobile app. These [[sg-mobile-security-push-notif|push notifications]] are non-actionable or actionable, and are configured by administrators to meet the needs of their users.

Non-actionable notifications are created by configuring a mobile push notification and then using the mobile deep link generator to generate links that navigate users into any screen type within a mobile app. To learn more about the mobile deep link generator, see [[deep-link-mobile|Deep linking for mobile]].

Actionable push notifications require you to perform additional steps, such as mapping functions for each push action. For more information about actionable notifications, see [[actionable-push-notification|Configure actionable push notifications]].

Define push notifications as critical when you require users to be immediately alerted to an event. Critical alerts override Do Not Disturb or Silent mode settings on your users' mobile device. For more information, see [[mobile-critical-alerts-create|Mobile critical alerts]].

You can target mobile push notifications for any of the specific ServiceNow [[mobile-config-navigation|Mobile Platform]] mobile apps.

## Push notifications structure overview

\[Omitted image "SNMobileAppPushNotificationStructureOverview.png"\] Alt text: Diagram showing how push notifications are created in an instance and sent directly to users to interact with on the device of their choice.

You must configure mobile push notifications in your ServiceNow instance before they can be sent to users on their mobile devices.

## Add push notifications to mobile apps with Mobile App Builder

In the Washington DC family release and later, you can now add push notifications to your mobile apps with Mobile App Builder:

\[Omitted image "push-notif-in-mab.png"\] Alt text: Mobile app builder menu showing available push notifications

Select **[[mobile-notifications|Mobile notifications]]** in the menu and then select the push notification you want to use. For more information about Mobile App Builder, see [[mab-concept|Mobile App Builder]].

-   **[[configure-mobile-push-notifications|Mobile push notification components]]**  
Configure mobile push notifications to target a specific screen in one of the ServiceNow Mobile Platform applications.
-   **[[add-push-notifications-mobile-apps|Reuse push notifications across mobile apps]]**  
Reuse push notifications across mobile apps with Mobile App Builder \(MAB\). Push notifications are configurable pushed messages that appear directly in mobile apps. Using MAB to manage push notifications streamlines your mobile application development into one tool.
-   **[[sg-push-setup-ios|Configure push applications for iOS branded apps using certificate based authentication]]**  
Install an iOS push certificate to use push notifications on your branded ServiceNow mobile apps for iOS.
-   **[[config-push-ios-token|Configure push applications for iOS branded apps using a token]]**  
Use push notifications on your branded ServiceNow mobile apps for iOS using token-based authentication.
-   **[[config-push-setup-android-httpv1|Configure push applications for Android branded apps using HTTP v1]]**  
Enter your Google Firebase Cloud Messaging push token authentication in your push application record to use push notifications on your branded ServiceNow mobile apps for Google Android.
-   **[Configure actionable push notifications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/mobile/actionable-push-notification.md)**  
Include actions with your push notifications. Users can perform push notification actions without opening the app.
-   **[[notification-activity-stream|Configure notifications for mobile activity stream mentions]]**  
Configure your instance to send an email notification or a push notification when a user mentions a contact’s name within a mobile activity stream record.
-   **[Mobile critical alerts](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/mobile/mobile-critical-alerts-create.md)**  
Send your users critical alerts, even if they set their mobile device to Do Not Disturb or Silent mode. Configure these visual and audio alerts to be sent when an issue needs immediate attention. Example scenarios can be to inform the user of an essential update, or to publicize a major incident that requires a speedy response.

**Parent Topic:**[[imp-considerations|Considerations before implementation]]

## Related

- [[deep-link-mobile|Deep linking for mobile]]
- [[actionable-push-notification|Configure actionable push notifications]]
- [[mobile-critical-alerts-create|Mobile critical alerts]]
- [[mab-concept|Mobile App Builder]]
- [[configure-mobile-push-notifications|Mobile push notification components]]
- [[add-push-notifications-mobile-apps|Reuse push notifications across mobile apps]]
- [[sg-push-setup-ios|Configure push applications for iOS branded apps using certificate based authentication]]
- [[config-push-ios-token|Configure push applications for iOS branded apps using a token]]
- [[config-push-setup-android-httpv1|Configure push applications for Android branded apps using HTTP v1]]
- [[notification-activity-stream|Configure notifications for mobile activity stream mentions]]
- [[imp-considerations|Considerations before implementation]]
- [[sg-mobile-security-push-notif|Push notifications]]
- [[mobile-config-navigation|Mobile Platform]]
- [[mobile-notifications|Mobile notifications]]
