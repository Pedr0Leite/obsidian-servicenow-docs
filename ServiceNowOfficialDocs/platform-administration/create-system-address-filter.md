---
title: Create a system address filter
description: Define how email address filters apply to inbound and outbound email.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/create-system-address-filter.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Email service, Create, Email Administration, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Create a system address filter

Define how email address filters apply to inbound and [[ia-outbound-email-il|outbound email]].

## Before you begin

Complete the steps in [[set-email-address-filters|Set email address filters]].

Role required: email\_account\_admin

## About this task

You can use a combination of allowed list and denied list email address filters in a system address filter.

A system address filter blocks a domain or address that appears only on denied lists and never on allowed lists. To ensure that a system address filter effectively blocks a certain domain or address, check for the following:

-   The domain or address is included in at least one denied list
-   The domain or address is not included in any allowed list

## Procedure

1.  Navigate to **All** &gt; **[[c_SystemMailboxes|System Mailboxes]]** &gt; **Administration** &gt; **[[system-address-filters|System Address Filters]]**, and then click **New**.

2.  On the form, fill in the fields.

<table id="table_plg_jv2_jlb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Name

</td><td>

Name of the system address filter.

</td></tr><tr><td>

Active

</td><td>

Option to activate the system address filter.

</td></tr><tr><td>

Type

</td><td>

Type of system address filter. Select one of the following:-   **Outbound**

Control which domains and email addresses can receive email from your instance. Select this option if you plan to use the system address filter for an SMTP server.

-   **Inbound**

Control which domains and email addresses can send email to your instance. Select this option if you plan to use the system address filter for an IMAP or POP3 server.

</td></tr><tr><td>

Application

</td><td>

Application scope of the system address filter.

</td></tr><tr><td>

Default

</td><td>

Option to use this system address filter as the default inbound or outbound filter.

 To control senders and recipients for a specific email account, leave this field cleared.

</td></tr><tr><td>

Short description

</td><td>

Description of the system address filter.

</td></tr><tr><td>

Email Address Filters

</td><td>

Email address filters to apply to the system address filter.

 By default, the maximum number of email address filters that you can associate with a single system address filter is 100. You can reconfigure this limit by setting the **glide.email\_system\_address\_filter.max\_address\_filters** property.

</td></tr></tbody>
</table>3.  Click **Submit**.


## Result

A default outbound filter applies to all active SMTP [[c_EmailAccounts|email accounts]] automatically. A default inbound filter applies to all active IMAP or POP3 email accounts automatically.

For a non-default filter, the next step is to apply the filter to an email account manually. For more information on applying a filter to an email account, see [[t_ConfigureAnEmailAccount|Create an email account]].

**Parent Topic:**[[email-service|Email service]]

## Related

- [[set-email-address-filters|Set email address filters]]
- [[t_ConfigureAnEmailAccount|Create an email account]]
- [[email-service|Email service]]
- [[ia-outbound-email-il|Outbound email]]
- [[c_SystemMailboxes|System mailboxes]]
- [[system-address-filters|System address filters]]
- [[c_EmailAccounts|Email accounts]]
