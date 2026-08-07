---
title: Activate Email Retention
description: The Email Retention plugin provides archive and destruction rules for email messages. It is active by default for new instances, but must be activated for upgrades.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/t\_ActivateTheEmailRetentionPlugin.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Email retention, Email and SMS notifications, System notifications, Notifications, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-task
---

# Activate Email Retention

The Email Retention plugin provides archive and destruction rules for email messages. It is active by default for new instances, but must be activated for upgrades.

## Before you begin

Role required: admin

## About this task

The Email Retention plugin requires these plugins:

-   [[c_ArchiveData|Data archiving]]
-   [[c_SystemMailboxes|System Mailboxes]]

## Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the plugin using the filter criteria and search bar.

    You can search for the plugin by its name or ID. If you cannot find a plugin, you might have to request it from ServiceNow personnel.

3.  Select **Install** to start the installation process.

    **Note:** When domain separation and delegated admin are enabled in an instance, the administrative user must be in the **global** domain. Otherwise, the following error appears: `Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>.`

    You will see a message after installation is completed. For information about the components installed with a plugin, see [[find-components|Find components installed with an application]].


**Parent Topic:**[[email-retention|Email retention]]

## Related

- [[c_ArchiveData|System Archive]]
- [[find-components|Find components installed with an application]]
- [[email-retention|Email retention]]
- [[c_SystemMailboxes|System mailboxes]]
