---
title: Configuring Activity Management
description: Install and configure the necessary plugins for enabling Activity Management features.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/configuring-activity-management.html
release: australia
topic_type: concept
last_updated: "2026-04-30"
reading_time_minutes: 2
keywords: [configure]
breadcrumb: [Lead and opportunity management apps, Configure, Sales Customer Relationship Management]
tags:
  - order-management
  - fulfillment
  - catalog
  - orchestration
  - type-concept
---

# Configuring Activity Management

Install and configure the necessary plugins for enabling Activity Management features.

**Important:**

To use personal email mailbox in Activity Management, you must install the User Mailbox Integration plugin \(com.glide.email.user\_mailbox.integration\) on your ServiceNow instance. For setup instructions, see [Personal corporate mailbox](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/personal-corporate-mailbox.md).

You must also install the Omnichannel Callback for Customer Service Management \(com.sn\_omnichannel\_callback\) application to enable the click-to-call feature, so agents can call customers from the touchpoint record.

## Configuring CRM Touchpoints

Install and configure the [[explore-crm-touchpoints|CRM Touchpoints]] application. It provides a unified system for capturing and tracking customer engagements for your sales and service teams while providing leadership with visibility into representative activity and engagement effectiveness.

1.  [[install-crm-touchpoints|Install CRM Touchpoints]]

    You can install the CRM Touchpoints application \(com.sn\_crm\_touchpoint\) if you have the admin role.

2.  [[create-custom-touchpoint-types|Create custom touchpoint types]]

    Create touchpoint types tailored to your sales organization's workflow to capture activities beyond the standard Discovery, Demo, and CBR types.


## Configuring CRM Outlook Add-in

Install and configure the [[explore-crm-outlook-add-in|CRM Outlook Add-in]] application to make the ServiceNow CRM for Outlook add-in available to your users.

1.  [[install-crm-outlook-add-in|Install CRM Outlook Add-in]]

    You can install the CRM Outlook Add-in application \(com.sn\_crm\_outlook\) if you have the admin role.

2.  [[add-crm-outlook-add-in|Configure CRM access from Microsoft Outlook]]

    Download and install the ServiceNow CRM for Outlook add-in to access and manage CRM records directly from your Outlook inbox, eliminating the need to switch between applications.

3.  [[promote-crm-outlook-emails|Make emails associated through the CRM Outlook Add-in visible to agents]]

    Configure email promotion so that emails associated with CRM records through the ServiceNow CRM for Outlook add‑in are promoted from the Staged Email \[sys\_email\_staging\] table to the Email \[sys\_email\] table, making them visible to agents in the workspace.


**Related topics**  


[[using-activity-management|Using Activity Management]]

[[explore-activity-management|Activity Management]]

## Related

- [[install-crm-touchpoints|Install CRM Touchpoints]]
- [[create-custom-touchpoint-types|Create custom touchpoint types]]
- [[install-crm-outlook-add-in|Install CRM Outlook Add-in]]
- [[add-crm-outlook-add-in|Configure CRM access from Microsoft Outlook]]
- [[promote-crm-outlook-emails|Make emails associated through the CRM Outlook Add-in visible to agents]]
- [[using-activity-management|Using Activity Management]]
- [[explore-activity-management|Activity Management]]
- [[explore-crm-touchpoints|CRM Touchpoints]]
- [[explore-crm-outlook-add-in|CRM Outlook Add-in]]
