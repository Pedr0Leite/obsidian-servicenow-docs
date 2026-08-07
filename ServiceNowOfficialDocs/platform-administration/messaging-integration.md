---
title: Notifications in messaging applications
description: Enable users to receive their ServiceNow platform notifications in Slack or Microsoft Teams messaging applications. Use the Now Actions app to configure the messaging apps for your instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/messaging-integration.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [System notifications, Notifications, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-concept
---

# Notifications in messaging applications

Enable users to receive their ServiceNow platform [[notifications|notifications]] in Slack or Microsoft Teams messaging applications. Use the Now Actions app to configure the messaging apps for your instance.

## Admin setup

To enable ServiceNow notifications within Slack or Microsoft Teams, you must be an administrator for both ServiceNow and the third-party application.

-   **1. Request Integration Hub**

    The Slack and Microsoft Teams spokes require a Starter subscription to Integration Hub. To activate Integration Hub and view available subscription types, see [Request an Integration Hub plugin](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/integrate-applications/request-integrationhub.md).

-   **2. Request the Messaging Notification plugin**

    To activate this feature, request the Messaging Notification plugin \(com.glide.notification.messaging\) through the HI Customer Service system. This plugin activates related plugins if they are not already active.

-   **3. Install the Now Actions messaging app for Slack or Microsoft Teams**

    As an administrator for both ServiceNow and the third-party application, find and install the Now Actions app. Install the application in ServiceNow to associate the app with your instance.

    **Note:** The primary owner of a Slack workspace or organization owns and manages the application. To avoid losing admin access to the workspace or organization, transfer primary ownership before any administration changes occur. If you transfer primary ownership, update the JSON payload for the Slack installation in the Notification Integration page. For more information about editing the Slack installation, see [[install-now-actions|Install the Now Actions messaging app]].

    If the Now Actions app is uninstalled, the workspace or team displays as inactive in the Notification Integration page. To view the Notification Integration page, navigate to **System Notification** &gt; **Messaging** &gt; **Messaging Integration Configuration**.

-   **4. Configure message content**

    Create a message in the Message Contents \[messaging\_content\] table that you can use in multiple notifications. Messages can be informative, or they can request action from an individual Slack or Teams user. For example, the Approval Request message includes Approve and Reject buttons to take the associated action in ServiceNow. Only users that have linked their Slack or Teams account with their ServiceNow account can take action in ServiceNow from the third-party application.

-   **5. Create a messaging notification**

    Notifications define when a message is sent, who it is sent to, and what it contains. To send a notification to Slack or Teams, add a messaging content record to the notification and configure the notification messaging channel. Notifications that require action must be sent to individual users instead of groups.


**Note:** Message Channel Sync Job can sync more than 1000 channels using pagination.

## User setup

To enable individual ServiceNow notifications in Slack or Microsoft Teams, and to take action on notifications, configure your system settings and link your user accounts.

-   **Link your ServiceNow user account to your Slack or Microsoft Teams account**

    Link your ServiceNow account to your Slack or Teams account to take action on ServiceNow notifications from within Slack or Teams. If you do not link accounts, you can still receive notifications within group channels. However, you cannot to approve ServiceNow requests or take action on notifications from within Slack or Teams.

-   **Configure system settings**

    Each user can enable ServiceNow notifications in a third-party application by configuring the communication channel in their system settings. Opt in to receive approval requests and other actionable notifications in third-party channels.


## Notification channels

In ServiceNow, a notification channel is a method or device for receiving notifications. For example, in the base system you can elect to receive notifications through email or SMS channels. If messaging applications are enabled on your instance, you can enable notifications to Slack and Teams using Notification Channels in your system settings.

## Actions and events

The Message Actions \[messaging\_observer\_handler\] table processes communication channel events, such as adding or deleting a Slack channel, to keep the instance and the third-party application in sync. Only developers creating Slack or Teams applications should add actions to this table. Register new actions with the instance through the Message [[c_EventRegistry|Event Registry]] \[messaging\_observable\] table. To remove a base system action, clear the active flag instead of deleting the record.

## Logging

The Inbound and Outbound message logs contain information on actions, events, and activities between ServiceNow and the third-party application. Use the logs to identify the content, state, and origin of communications to and from your instance.

-   **[[request-messaging-notification|Request the Messaging Notification plugin]]**  
To activate this feature, request the Messaging Notification plugin \(com.glide.notification.messaging\) through the HI Customer Service system. This plugin activates related plugins if they are not already active.
-   **[Install the Now Actions messaging app](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/install-now-actions.md)**  
As an administrator for both ServiceNow and the third-party application, find and install the Now Actions app. Install the application in ServiceNow to associate the app with your instance.
-   **[[configure-message-content|Configure message content]]**  
Create a message in the Message Contents \[messaging\_content\] table that you can use in multiple notifications. Messages can be informative, or they can request action from an individual Slack or Teams user. For example, the Approval Request message includes Approve and Reject buttons to take the associated action in ServiceNow.
-   **[[create-messaging-notification|Create a messaging notification]]**  
Notifications define when a message is sent, who it is sent to, and what it contains. To send a notification to Slack or Teams, add a messaging content record to the notification and configure the notification messaging channel. Notifications that require action must be sent to individual users instead of groups.
-   **[[link-accounts|Link your ServiceNow user account to your Slack or MS Teams account for Now Actions]]**  
Link your ServiceNow account to your Slack or Teams account to take action on ServiceNow notifications from within Slack or Teams. If you do not link accounts, you can still receive notifications within group channels. However, you cannot to approve ServiceNow requests or take action on notifications from within Slack or Teams.
-   **[[unlink-accounts|Unlink your ServiceNow user account from your Slack or MS Teams account for Now Actions]]**  
Unlink your ServiceNow account from your Slack or MS Teams account to stop receiving actionable ServiceNow notifications in Slack or Teams.
-   **[[configure-notif-custom-Slack-app|Set up notifications for a custom Slack app]]**  
Send ServiceNow notifications to users via your own Slack bot.

**Parent Topic:**[[system-notifications-landing|System notifications]]

## Related

- [[install-now-actions|Install the Now Actions messaging app]]
- [[request-messaging-notification|Request the Messaging Notification plugin]]
- [[configure-message-content|Configure message content]]
- [[create-messaging-notification|Create a messaging notification]]
- [[link-accounts|Link your ServiceNow user account to your Slack or MS Teams account for Now Actions]]
- [[unlink-accounts|Unlink your ServiceNow user account from your Slack or MS Teams account for Now Actions]]
- [[configure-notif-custom-Slack-app|Set up notifications for a custom Slack app]]
- [[system-notifications-landing|System notifications]]
- [[notifications|Notifications]]
- [[c_EventRegistry|Event registry]]
