---
title: Configure alert actions
description: Configure an alert action from the Crisis map interface in the BCM Configurable Workspace.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/configure-alert-action-uib-ws.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Setup for Crisis map, Configure, Business Continuity Management, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - type-task
---

# Configure alert actions

[[crisis-map-alert-actions|Configure an alert action]] from the [[threats-feeds-alerts-crisis-map|Crisis map interface]] in the [[bcm-workspace|BCM Configurable Workspace]].

## Before you begin

Role required: sn\_bcm.program\_manager

## About this task

You can open or dismiss an alert from the Crisis map interface. For more information, see [[manage-alerts-in-crisis-map-interface-uib-ws|Manage alerts from the map interface]].

## Procedure

1.  Navigate to **Threat and Alert Data Feeds** &gt; **[[Administration|Administration]]** &gt; **Alert Actions**.

    These alert actions are available within the base system.

    |Name|Description|
    |----|-----------|
    |Notify|Used to send email notifications to stakeholders and the asset managers that are within the impact radius.|
    |Declare Crisis|Used to declare a combination of alert and critical assets as a crisis event.|

2.  To add a new alert action, select **New**.

3.  On the form, fill in the fields.

    For more information on the fields, see [[alert-action-form|Alert Action form]].

4.  Select **Submit**.

    You can follow up on the alert actions from the Crisis map dashboard.


## Result

The alert action is displayed in the **Alert Actions** record page.

-   **[Alert Action form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/alert-action-form.md)**  
Use the Alert Action form in BCM UIB Workspace to add details about the alert actions.

**Parent Topic:**[[crisis-map-admin-tasks|Setup for Crisis map]]

## Related

- [[manage-alerts-in-crisis-map-interface-uib-ws|Manage alerts from the map interface]]
- [[alert-action-form|Alert Action form]]
- [[crisis-map-admin-tasks|Setup for Crisis map]]
- [[crisis-map-alert-actions|Configure an alert action]]
- [[threats-feeds-alerts-crisis-map|Crisis map interface]]
- [[bcm-workspace|BCM Configurable Workspace]]
- [[Administration|Administration]]
