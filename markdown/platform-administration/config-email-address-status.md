---
title: Configure bounce email address status
description: Configure a bounced email address status according to type, class, subject, and details.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/config-email-address-status.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Email bounce management, Advanced email setup, Configure, Email Administration, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Configure bounce email address status

Configure a bounced email address status according to type, class, subject, and details.

## Before you begin

Role required: admin

## About this task

For detailed information on status codes and explanations of the components, see [RFC Status codes](https://www.rfc-editor.org/rfc/rfc3463).

## Procedure

1.  Navigate to **All** &gt; **[[c_SystemMailboxes|System Mailboxes]]** &gt; **Administration** &gt; **Bounce Email Address Status**.

2.  Select **New**.

3.  Select the **Type** and enter the **Class**, **Subject**, and **Detail**.

    **Note:** For example: Status code patterns for 5.1.\* are blocked by default, if 5, 1, and 2 are entered as the Class, Subject, and Detail, the Type is selected as unblocked then only 5.1.2 is unblocked. All other status codes patterns for 5.1.\* are still blocked.

4.  Select **Submit**.


**Parent Topic:**[[email-bounce|Email bounce management]]

**Related topics**  


[[change-bounce-email-status|Check the status of bounced email addresses]]

## Related

- [[email-bounce|Email bounce management]]
- [[change-bounce-email-status|Check the status of bounced email addresses]]
- [[c_SystemMailboxes|System mailboxes]]
