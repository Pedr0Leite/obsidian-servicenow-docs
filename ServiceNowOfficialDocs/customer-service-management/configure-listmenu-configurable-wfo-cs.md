---
title: Configure a list menu to display in the Learning tab in Workforce Optimization for Customer Service
description: Add list or list categories to modify the list menu for Coaching with Learning in the Coaching application in Workforce Optimization for Customer Service.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/configure-listmenu-configurable-wfo-cs.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Setting up Workforce Optimization Coaching, Optimize workforce operations, Extend capabilities, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Configure a list menu to display in the Learning tab in Workforce Optimization for Customer Service

Add list or list categories to modify the list menu for Coaching with Learning in the Coaching application in [[configurable-wfo-cs|Workforce Optimization for Customer Service]].

## Before you begin

**Important:** This feature is available with the Workforce [[optimization|Optimization]] for [[csm-workspaces-configure|CSM Configurable Workspace]] \(sn\_csm\_wfo\_workspa\) from the ServiceNow Store. To enable this feature, see [[request-configurable-wfo-cs|Activate Workforce Optimization for CS configurable workspace]].

Set the map application scope to **Coaching With Learning**. For information on how to set the scope, see [Set map application scope](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/set-map-application-scope.md).

Role required: admin

## Procedure

1.  In the application navigator, enter `sys_ux_list_menu_config.list`.

2.  Select **Learning list** record.

3.  Under UX list category, select **New**.

4.  Enter the following field values.

    |Field|Value|
    |-----|-----|
    |Title|Enter the name of the list category.|
    |Description|Enter a short description about the list category.|
    |Order|Enter a value to set the position of the list category in the current list.|
    |Active|Select the check box to make the list category visible.|

5.  Select **Submit**.

6.  Under UX [[migration-lists|Lists]], select **New** to create lists under that list category.

7.  Enter the following field values.

    |Field|Value|
    |-----|-----|
    |Title|Enter the name of the list.|
    |Table|Select the table for the data that you want to display in the list.|
    |Configuration|Select **Learning List**.|
    |Columns|Select the columns that you want to display for the table.|

8.  Select **Submit**.

9.  Select **Update**.


**Parent Topic:**[[setup-coaching-configurable-wfo-cs|Setting up Coaching in Workforce Optimization for Customer Service]]

## Related

- [[request-configurable-wfo-cs|Activate Workforce Optimization for Customer Service]]
- [[setup-coaching-configurable-wfo-cs|Setting up Coaching in Workforce Optimization for Customer Service]]
- [[configurable-wfo-cs|Workforce Optimization for Customer Service]]
- [[optimization|Optimization]]
- [[csm-workspaces-configure|CSM Configurable Workspace]]
- [[migration-lists|Lists]]
