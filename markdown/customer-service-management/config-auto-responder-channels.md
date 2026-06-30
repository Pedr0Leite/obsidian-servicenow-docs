---
title: Include cases logged using specified communication channels in Auto-Responder notifications
description: Send Auto-Responder email notifications for customer service cases logged using a communication channel.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/config-auto-responder-channels.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure Auto-Responder notifications, Machine learning solutions, Implement Intelligence, Configure, Customer Service Management]
---

# Include cases logged using specified communication channels in Auto-Responder notifications

Send Auto-Responder email notifications for customer service cases logged using a communication channel.

## Before you begin

Role required: admin

Perform the following tasks.

-   Activate the Predictive [[intelligence-csm|Intelligence]] for [[c_CustomerServiceManagement|Customer Service Management]] plugin \(com.snc.csm\_ml\). For more information, see [Activate a plugin](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_ActivateAPlugin.md) and [[predictive-intelligence-for-csm|Predictive Intelligence for CSM solution definitions]].
-   Set the application scope to Customer Service using the application picker. For more information, see [Application picker](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/c_ApplicationPicker.md).
-   Ensure that the required channel is already set up for use. For more information, see [[enable-comm-channels|Enable communication channels]].

## About this task

By default, the Case auto-responder recommendations notification is configured to send Auto-Responder email notifications for customer service cases logged using emails. You can configure it to include other communication channels such as web, phone, chat, social, community, alert, and virtual agent.

## Procedure

1.  Navigate to **All** &gt; **System Notification** &gt; **Notifications**.

2.  Search for `Case auto-responder recommendations`.

3.  In the **Name** column, click the **Case auto-responder recommendations** link.

4.  In the **Conditions** field, click **Add Filter Condition** or **Add "Or" Clause** to set the filter condition for a communication channel.

    **Note:** The default filter condition is **\[Channel\] \[is\] \[Email\] AND \[Active\] \[is\] \[true\]**.

    For example, to send Auto-Responder notifications for customer service cases logged using a mobile phone in addition to email, you would click **Add Filter Condition** and create the condition **\[Channel\] \[is\] \[Phone\] AND \[Active\] \[is\] \[true\]**.

## Related

- [[predictive-intelligence-for-csm|Predictive Intelligence for CSM solution definitions]]
- [[enable-comm-channels|Enable communication channels]]
- [[intelligence-csm|Intelligence]]
- [[c_CustomerServiceManagement|Customer Service Management]]
