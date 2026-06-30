---
title: Activate AI Search for Notifications
description: You can activate the AI Search for Notifications plugin \(com.glide.notification.ais\) for Notifications if you have the admin role. If the application does NOT include demo data or it does NOT install related applications and plugins, delete or revise the following sentence:The application includes demo data and installs related ServiceNow Store applications and plugins if they are not already installed.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/activate-ai-search-for-notifications-plugin.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Preferences in Next Experience, Notification Preferences, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Activate AI Search for Notifications

You can activate the [[ia-ai-search|AI Search]] for [[notifications|Notifications]] plugin \(com.glide.notification.ais\) for Notifications if you have the admin role. The application includes demo data and installs related ServiceNow® Store applications and plugins if they are not already installed.

## Before you begin

Role required: admin

## About this task

The following items are installed with Notifications:

## Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the AI Search for Notifications plugin \(com.glide.notification.ais\) using the filter criteria and search bar.

    You can search for the plugin by its name or ID. If you cannot find a plugin, you might have to request it from ServiceNow personnel.

3.  Select **Install** to start the installation process.

    **Note:** When domain separation and delegated admin are enabled in an instance, the administrative user must be in the **global** domain. Otherwise, the following error appears: `Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>.`

    You will see a message after installation is completed. For information about the components installed with a plugin, see [[find-components|Find components installed with an application]].


## What to do next

[[index-ai-search-for-notification|Index AI Search for notifications]]

-   **[Index AI Search for notifications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/index-ai-search-for-notification.md)**  
Make content from multiple internal indexed sources searchable by performing a full table index. This procedure indexes existing records from the source tables and any child tables configured for indexing.

**Parent Topic:**[[advanced-notification-prefrences|System and custom notification and delivery channel preferences in Next Experience]]

## Related

- [[find-components|Find components installed with an application]]
- [[index-ai-search-for-notification|Index AI Search for notifications]]
- [[advanced-notification-prefrences|System and custom notification and delivery channel preferences in Next Experience]]
- [[ia-ai-search|AI Search]]
- [[notifications|Notifications]]
