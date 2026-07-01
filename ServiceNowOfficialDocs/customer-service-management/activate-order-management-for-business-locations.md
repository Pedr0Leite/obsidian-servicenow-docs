---
title: Activate Order Management for Business Locations
description: Activate the Order Management for Business Location plugin to manage the complete order lifecycle.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/activate-order-management-for-business-locations.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Business location plugin, Activate plugins, Configure Service Model Foundation, Data models, Set up your environment, Configure, Customer Service Management]
---

# Activate Order Management for Business Locations

Activate the Order Management for Business Location plugin to manage the complete order lifecycle.

## Before you begin

Role required: admin

## About this task

The following items are installed with Order Management for Business Locations:

-   Plugins
-   Store applications
-   Roles
-   Scheduled jobs
-   Tables

For more information, see [[personas-roles-and-tables-post-integration|Roles and responsibilities]].

## Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the Order Management for Business Locations plugin \(sn\_bus\_org\_orm\) using the filter criteria and search bar.

    You can search for the plugin by its name or ID. If you cannot find a plugin, you might have to request it from ServiceNow personnel.

3.  Select **Install** to start the installation process.

    **Note:** When domain separation and delegated admin are enabled in an instance, the administrative user must be in the **global** domain. Otherwise, the following error appears: `Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>.`

    You will see a message after installation is completed. For information about the components installed with a plugin, see [Find components installed with an application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/find-components.md).


**Related topics**  


[[order-managment-for-business-location|Order Management for business location]]

## Related

- [[personas-roles-and-tables-post-integration|Roles and responsibilities]]
- [[order-managment-for-business-location|Order Management for business location]]
