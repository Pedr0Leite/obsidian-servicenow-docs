---
title: Configuring Subscription Management
description: Set up and configure Subscription Management.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/configuring-subscription-management-v2.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Subscription Management, Get started, Administer the ServiceNow AI Platform]
---

# Configuring Subscription Management

Set up and configure Subscription Management.

## Configuration overview

Subscription Management is free and active by default for all production instances and non-production instances. You don't have to [[t_ActivateAPlugin|activate a plugin]].

1.  [[assign-usage-admin-v2|Create a Subscription Management administrator]]

    Assign the usage\_admin role to at least one user who will manage subscriptions for your organization.

2.  [[share-subscription-data|Share subscription data from another instance]]

    View subscription data from other production instances in areas of Subscription Management that provide account-level summaries of subscription usage.

3.  [[configure-subscription-allocation-status-v2|Configure subscription allocation status in Subscription Management]]

    Configure the allocation status threshold using a percentage value that represents what near capacity means for your instance.


-   **[Create a Subscription Management administrator](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/assign-usage-admin-v2.md)**  
Create a Subscription Management administrator by assigning the usage\_admin role to an administrator.
-   **[Share subscription data from another instance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/share-subscription-data.md)**  
View subscription data from another instance by enabling data sharing on that instance.
-   **[Configure subscription allocation status in Subscription Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/configure-subscription-allocation-status-v2.md)**  
Identify when you're close to allocating all of your subscriptions by configuring an allocation status threshold if you prefer a threshold other than the default value of 90 percent in Subscription Management.
-   **[[manage-subscriptions-on-prem|Manage subscriptions in an on-premise installation]]**  
Download licensing and usage definition data to view and manage subscriptions for your on-premise installation.

**Parent Topic:**[[subscription-management-landing-page-v2|Subscription Management]]

## Related

- [[assign-usage-admin-v2|Create a Subscription Management administrator]]
- [[share-subscription-data|Share subscription data from another instance]]
- [[configure-subscription-allocation-status-v2|Configure subscription allocation status in Subscription Management]]
- [[manage-subscriptions-on-prem|Manage subscriptions in an on-premise installation]]
- [[subscription-management-landing-page-v2|Subscription Management]]
- [[t_ActivateAPlugin|Activate a plugin]]
