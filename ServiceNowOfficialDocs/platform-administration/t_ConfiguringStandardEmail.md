---
title: Enable basic email
description: Enable basic email to use ServiceNow - provided email servers and accounts.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/t\_ConfiguringStandardEmail.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Basic email setup, Configure, Email Administration, Notifications, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-task
---

# Enable basic email

Enable basic email to use ServiceNow - provided email servers and accounts.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **[[r_SetArchiveRuleProcessingBehavior|System Properties]]** &gt; **[[c_EmailProperties|Email Properties]]**.

2.  Configure these email properties and select **Save**.

    \[Omitted image "email-properties.png"\] Alt text: Email properties

    |Property section|Label|System property|Setting required|
    |----------------|-----|---------------|----------------|
    |Outbound Email Configuration|Email sending enabled|glide.email.smtp.active|Yes|
    |Inbound Email Configuration|Email receiving enabled|glide.email.read.active|Yes|


**Parent Topic:**[[c_StandardEmailConfiguration|Basic email setup]]

## Related

- [[c_StandardEmailConfiguration|Basic email setup]]
- [[r_SetArchiveRuleProcessingBehavior|System properties]]
- [[c_EmailProperties|Email properties]]
