---
title: Push notification setup with a custom push application for ServiceNow mobile apps
description: If you are using your own custom mobile or push application, you must configure your app for use and set up the push contents.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/r\_PushNotificationSetupCustom.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Push notifications, System notifications, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Push notification setup with a custom push application for ServiceNow mobile apps

If you are using your own custom mobile or push application, you must configure your app for use and set up the push contents.

Setting up a push notification infrastructure that uses a custom push app involves a push admin \(also called push app developer or mobile app developer\) and system administrator. When push admins create a customized push app, they also configure the app, its push message content \(payload generators\), and optional attributes, such as push action scripts. The admin creates and updates the [[c_PushNotifications|push notifications]] for the custom push app. After users install the custom push app and initially log in to their instance from their mobile device, the system automatically creates a device \(channel\) for the custom app.

**Note:** These instructions are intended for users who develop their own customized push application. You do not need to configure the ServiceNow mobile push application.

This process describes configuration used in the ServiceNow mobile app. Push Notification configuration for the current ServiceNow mobile UI can be found at [Mobile push notifications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/mobile/sg-mobile-push-notifications.md)

\[Omitted image "CustomPushAppSetup.png"\] Alt text: Push notification setup tasks for a custom push app

## Before you begin

Complete the steps in [[t_ActivatePushNotifications|Activate push notifications]].

Assign the push\_admin role to your organization's mobile app developer.

## What to do — push admin

Configure push notifications for your custom push app. This process differs for iOS and Android devices.

1.  \(iOS only\) [[upload-push-cert|Upload a push certificate to your instance]]

    Upload a push certificate to your instance so that you can use it later to connect your iOS device to the [[r_PushMessageArchitecture|push notification system]].

2.  [[t_CreateAMobileApplication|Create a push application record for your custom app]]

    Register your customized mobile application with your instance to receive push notifications for the application. The instance uses this push application record to identify the device + push application combination necessary to determine a push notification recipient.

3.  [[t_CreateAMobileMessageLayout|Create push message content]]

    Create a JSON content payload for different types of push notifications. The content determines how a push notification appears on the push application, and whether the user can send a message in response to the push notification. The push admin can create attribute [[clone-exclusions-preservers-cleanupscripts|definitions]] that specify a default push action script or string, for use in the push message content.

4.  \(Optional\) [[t_CreateAPushMessageAttribute|Create a push message attribute definition]]

    Push message attribute definitions allow you to create reusable properties for push message content specification.

5.  \(Optional\) [[t_CreateAPushMessageAttributeValue|Create an attribute value or action for a push message]]

    You can create attribute values that override the default attribute definitions used in the push message content.

6.  \(Optional\) [[t_CreateAMobileActionScript|Create a push action]]

    A push action is a server-side script that runs when the instance receives a response to an actionable push message.


## What to do — admin

Create the push messages and push notifications: The administrator [[t_CreateAPushMessage|creates the push messages]], [[t_CreatePushNotification|sets up push notifications]] for the custom push app, and if desired, the content.

## Next steps

Use the Push Installation API to opt users in to receive push notifications. For more information, see [Push Installation API](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/pushinstallation-api.md).

## Related

- [[t_ActivatePushNotifications|Activate push notifications]]
- [[upload-push-cert|Upload a push certificate to your instance]]
- [[t_CreateAMobileApplication|Create a push application record for your custom app]]
- [[t_CreateAMobileMessageLayout|Create push message content]]
- [[t_CreateAPushMessageAttribute|Create a push message attribute definition]]
- [[t_CreateAPushMessageAttributeValue|Create an attribute value or action for a push message]]
- [[t_CreateAMobileActionScript|Create a push action]]
- [[t_CreateAPushMessage|Create a push message]]
- [[t_CreatePushNotification|Create a notification using a push message]]
- [[c_PushNotifications|Push notifications]]
- [[r_PushMessageArchitecture|Push notification system]]
- [[clone-exclusions-preservers-cleanupscripts|Definitions]]
