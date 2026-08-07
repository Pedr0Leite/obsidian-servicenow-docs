---
title: Configure wrap-up codes for email interactions
description: Configure internal wrap-up codes that agents use to categorize email interactions when closing them. Wrap-up codes work with both AWA-routed and CCaaS-routed email interactions.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/configure-wrap-up-codes-email-interactions-eaai.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Email Interaction, Email channel, Enable communication channels, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Configure wrap-up codes for email interactions

Configure internal wrap-up codes that agents use to categorize email interactions when closing them. Wrap-up codes work with both AWA-routed and CCaaS-routed email interactions.

## Before you begin

Default wrap-up codes are read-only. The system uses ACLs to restrict list-edit operations and data policies to restrict edits in form view. You can’t configure multiple default wrap-up codes for different use cases. For more information on wrap-up codes, see [[wrap-up-codes-email-interactions-r|Wrap-up codes for email interactions]].

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Interaction** &gt; **Wrap Up Codes**.

2.  Select **New**.

3.  Enter the required details.

4.  Select the **Active** check box.

5.  Select **Submit**.


## Result

The wrap-up code is created. To make it available to agents, associate it with the [[email-as-an-interaction|email interaction]] wrap-up configuration. See [[associate-wrap-up-codes-email-interactions|Associate wrap-up codes with email interactions]].

## Related

- [[wrap-up-codes-email-interactions-r|Wrap-up codes for email interactions]]
- [[associate-wrap-up-codes-email-interactions|Associate wrap-up codes with email interactions]]
- [[email-as-an-interaction|Email Interaction]]
