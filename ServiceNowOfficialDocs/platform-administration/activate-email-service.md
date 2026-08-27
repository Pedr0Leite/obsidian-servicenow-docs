---
title: Activate Email Service
description: Users with the admin role can activate the Email Service plugin \(com.glide.email.service\) to enable the Email API.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/activate-email-service.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Activate email administration, Configure, Email Administration, Notifications, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-task
---

# Activate Email Service

Users with the admin role can activate the [[email-service|Email Service]] plugin \(com.glide.email.service\) to enable the Email API.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the plugin using the filter criteria and search bar.

    You can search for the plugin by its name or ID. If you cannot find a plugin, you might have to request it from ServiceNow personnel.

3.  Select **Install** to start the installation process.

    **Note:** When domain separation and delegated admin are enabled in an instance, the administrative user must be in the **global** domain. Otherwise, the following error appears: `Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>.`

    You will see a message after installation is completed. For information about the components installed with a plugin, see [[find-components|Find components installed with an application]].


## What to do next

[[create-system-address-filter|Create a system address filter]]

**Parent Topic:**[[activate-email-admin|Activate email administration]]

**Related topics**  


[List of plugins \(Australia\)]()

## Related

- [[find-components|Find components installed with an application]]
- [[create-system-address-filter|Create a system address filter]]
- [[activate-email-admin|Activate email administration]]
- [[email-service|Email service]]
