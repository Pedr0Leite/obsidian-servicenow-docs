---
title: Crisis map interface
description: You can integrate Crisis map with the BCM application and initiate the response workflows for crisis management. After installing the Crisis map application, you can view the Threat and Alert Data Feeds module in your BCM application instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/threats-feeds-alerts-crisis-map.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Explore, Business Continuity Management, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - type-concept
---

# Crisis map interface

You can integrate Crisis map with the BCM application and initiate the response workflows for crisis management. After installing the Crisis map application, you can view the **Threat and Alert Data Feeds** module in your BCM application instance.

## Feeds, alerts, and events in BCM

When you integrate the Crisis map application with the BCM application, you can view and analyze the feeds, alerts, and events from different locations in the Crisis map view.

-   **Feed**

    A feed is news content updated frequently and provided on a worldwide website. You can subscribe to a news feed by manually entering the URL of the feed channel in the **Web** field of the Feed form.

-   **Alert**

    An alert is a notification that reports an incident happened at a particular place and time. First, an incident, or an event reportedly happens. Then, the alert triggers a notification that reports or notifies the incident to the concerned people to take an action.

-   **Event**

    Based on the severity of the alerts, you can take actions such as notifying the stakeholders of the incident or declaring a crisis event. An event can become a crisis event if it disrupts the business operations. For information on the [[crisis-management-uib|crisis events]], see [[crisis-map-uib-ws|Crisis map view]]. You can then activate the business continuity plans for the locations that are impacted by the event.


## Threat and Alert Data Feeds module in BCM

The **Threat and Alert Data Feeds** module in BCM displays details:

-   **Feeds**
-   **Alerts**
-   **[[Administration|Administration]]**

The **Threat and Alert Data Feeds** module is shown in the example.

\[Omitted image "threat-alert-data-feeds-admin-tasks.png"\] Alt text: Threat alerts and data feeds.

## Feeds module in BCM

A threat feed is the data intelligence information of a potential or current threat that can pose a danger to an organization. It can disrupt the business routine or disable its business processes. The Crisis map application receives the feeds from third-party sources such as GDAC Feeds and Weather Gov Alerts.

The **Feeds** module in BCM displays types of feeds:

-   **Active feeds**
-   **Archived feeds**

A sample view of the active feeds is displayed in the example.

\[Omitted image "feeds.png"\] Alt text: Active feeds view.

You can use the **Personalize List** icon to configure the list columns in the **Feeds** module. For example, you can display additional details on the alert:

-   Headline
-   Event
-   Severity
-   Certainty
-   Category
-   Response type
-   Data source
-   Process state

Threat feeds include information about real-time disruptive events as shown in the sample list:

-   Civil unrest or riots
-   Flood advisory
-   Flood warning
-   Drought area
-   Earthquake
-   Hurricane
-   Wildfire or red flag warnings
-   War or military conflict
-   Volcano eruption

## Alerts module in BCM

An alert is a notification that reports an incident happened at a particular place and time. First, an incident or an event reportedly happens. Then, the alert triggers a notification that reports or notifies the incident to the concerned people to take an action.

The **Alerts** module in BCM displays types of feeds:

-   **Active alerts**
-   **Dismissed alerts**
-   **Alert responses**

A sample view of the active alerts is shown in the example.

\[Omitted image "alerts.png"\] Alt text: Active alerts.

You can use the **Personalize List** icon to configure the list columns in the **Alerts** module. For example, you can display these details on the alert:

-   Title
-   Severity
-   Feed
-   Source
-   Alert rule
-   Impact type
-   Updated

## Administrative tasks in the Threat and Alert Data Feeds module

If you have the BCM administrator role, see [[crisis-map-admin-tasks|Setup for Crisis map]] for information on the setup tasks.

The **Administration** module in BCM displays types of feeds:

-   **Scheduled imports**

    To manage your threat feed subscriptions that are sourced internally and externally, you must schedule a data import from the data source at defined intervals. For more information on scheduled imports, see [[sched-data-imports-crisis-map-uib-ws|Configure Scheduled Data Imports records]].

-   **Resource configuration**

    To plot your organization's assets or resources on the Crisis map, you must configure the resources in the application. For more information on resource configuration, see [[conf-resource-for-crisis-map-uib-ws|Configure Resource Configuration records]].

-   **Alert rules**

    To display the feeds as alerts on the Crisis map, configure the alert rules. For more information on alert rules, see [[conf-alert-rule-uib-ws|Configure alert rules]].

-   **Alert actions**

    To act on a critical alert from the Crisis map dashboard, see [[configure-alert-action-uib-ws|Configure alert actions]].


-   For information on the administrative tasks for Crisis map, see [Setup for Crisis map](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/crisis-map-admin-tasks.md).
-   To search for locations on the Crisis map, you must set the **sn\_bcm\_map.use\_google\_places\_lib** system property. For more information, see [[properties-bcm|Properties installed with BCM]].

## Crisis map

For information on managing the alerts in Crisis map, see [[crisis-map-collective-tasks|Structured workflows for Crisis map]].

## Related

- [[crisis-map-uib-ws|crisis map uib ws]]
- [[crisis-map-admin-tasks|Setup for Crisis map]]
- [[sched-data-imports-crisis-map-uib-ws|Configure Scheduled Data Imports records]]
- [[conf-resource-for-crisis-map-uib-ws|Configure Resource Configuration records]]
- [[conf-alert-rule-uib-ws|Configure alert rules]]
- [[configure-alert-action-uib-ws|Configure alert actions]]
- [[properties-bcm|Properties installed with BCM]]
- [[crisis-map-collective-tasks|Structured workflows for Crisis map]]
- [[crisis-management-uib|Crisis events]]
- [[Administration|Administration]]
