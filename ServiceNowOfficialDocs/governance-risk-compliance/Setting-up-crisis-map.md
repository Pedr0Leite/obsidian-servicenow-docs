---
title: Setting up the crisis map
description: Before you integrate the crisis management map with the geographical locations of your assets, there are certain configurations that you must do to display the active alerts in the crisis map.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/Setting-up-crisis-map.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Crisis Management map, Using BCM Classic Workspace, Manage, Business Continuity Management, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - type-concept
---

# Setting up the crisis map

Before you integrate the [[crisis-management-map-integration|crisis management map]] with the geographical locations of your assets, there are certain configurations that you must do to display the active alerts in the crisis map.

## Understanding feed, alert, and event

-   **Feed**

    A feed is news content updated frequently and provided on a world-wide website. You can subscribe to a news feed by manually entering the web address or URL of the feed channel in the **Web** field of the Feed form.

-   **Alert**

    An alert is a notification that reports an incident happened at a particular place and time. First, an incident or an event reportedly happens. Then, the alert triggers a notification that reports or notifies the incident to the concerned people to take an action.

-   **Event**

    Based on the severity of the alerts, you can take actions by just notifying the stakeholders of the incident that happened or declare a crisis event. An event can become a crisis event if it disrupts the business operations. In such a case, you can run the [[bcm-recovery-exercise-management|Crisis Management workflow]] to activate the business continuity and disaster recovery plans for the locations impacted by the event.


## Setup steps to integrate crisis map

You require these configurations for the threat and alert feeds to show up in the crisis map visualization.

-   To search locations on the crisis map, [[crisis-map-place-api-configuration|set up the system property]].
-   To manage your threat feed subscriptions sourced internally and externally, [[crisis-map-scheduled-data-imports|configure scheduled data imports]].
-   To plot your organization's assets or resources on the crisis map, [[crisis-map-configure-resource|configure the resources]].
-   To specify the conditions under which a feed should bubble up as an alert on the crisis map, [[crisis-map-alert-configuration|configure alert rules]].
-   Finally, to act on a critical alert from the crisis map dashboard, [[crisis-map-alert-actions|configure an alert action]].

## Related

- [[bcm-recovery-exercise-management|Structured workflows for Exercise and Crisis Management]]
- [[crisis-map-place-api-configuration|Configure search for places in crisis map]]
- [[crisis-map-scheduled-data-imports|Configure scheduled data imports for crisis map]]
- [[crisis-map-configure-resource|Configure a resource for crisis map]]
- [[crisis-map-alert-configuration|Configure alert rules to display alerts in crisis map]]
- [[crisis-map-alert-actions|Configure an alert action]]
- [[crisis-management-map-integration|Crisis Management map]]
