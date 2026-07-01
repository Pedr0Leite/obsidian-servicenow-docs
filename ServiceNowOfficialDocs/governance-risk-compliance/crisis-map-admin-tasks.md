---
title: Setup for Crisis map
description: BCM administrators perform the administrative tasks to set up the Crisis map interface.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/crisis-map-admin-tasks.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configure, Business Continuity Management, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - type-concept
---

# Setup for Crisis map

BCM administrators perform the administrative tasks to set up the [[threats-feeds-alerts-crisis-map|Crisis map interface]].

BCM administrators perform the administrative tasks to set up the threat alerts and data feeds in Crisis map. The administrative tasks are displayed under **[[Administration|Administration]]** in the **Threat and Alert Data Feeds** module as shown in the example.

**Note:** Prior to enabling the Crisis Map feature, verify that you have purchased and set up Google Maps API.

\[Omitted image "threat-alert-data-feeds-admin-tasks.png"\] Alt text: Threat alerts and data feeds.

With the BCM administrator role, you can perform the administrative tasks to set up the Crisis map:

-   **Scheduled Imports**: Configure a Scheduled Data Imports record for the Crisis map application. For more information, see [[sched-data-imports-crisis-map-uib-ws|Configure Scheduled Data Imports records]].
-   **Resource Configuration**: Configure a Resource Configuration record for the Crisis map application. For more information, see [[conf-resource-for-crisis-map-uib-ws|Configure Resource Configuration records]].
-   **Alert Rules**: Configure an alert rule in Crisis map so that you can specify the conditions under which a feed can be displayed in the dashboard as an alert. For more information, see [[conf-alert-rule-uib-ws|Configure alert rules]].
-   **Alert Actions**: [[crisis-map-alert-actions|Configure an alert action]] in UIB Workspace for the Crisis map application. For more information, see [[configure-alert-action-uib-ws|Configure alert actions]].

-   **[[crisis-map-customization-properties-for-g-maps|Customization properties for Google Maps]]**  
The Crisis map application users can configure the customization properties for Google Maps in the **Google Maps Properties** module.
-   **[[g-maps-api-in-fam-map-component|Google Maps APIs used in Fam-map component]]**  
The Fam-map component in Crisis map utilizes various Google Maps APIs to provide interactive mapping functionalities. This section lists the Google Maps APIs that are integrated into the Fam-map component, along with their usage information.
-   **[Configure Scheduled Data Imports records](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/sched-data-imports-crisis-map-uib-ws.md)**  
Configure a Scheduled Data Imports record for the Crisis map application. You can then manage your subscriptions to the threat feeds from an internal or external source in the [[bcm-workspace|BCM Configurable Workspace]].
-   **[Configure Resource Configuration records](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/conf-resource-for-crisis-map-uib-ws.md)**  
Configure a Resource Configuration record for the Crisis map application in UIB Workspace. You can then plot the assets of your organization on the Crisis map. The assets can be locations, employees, datacenters, suppliers, and others. Configuring resources is also required as an input to set up the alert rules.
-   **[Configure alert rules](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/conf-alert-rule-uib-ws.md)**  
Configure an alert rule in the Crisis map so that you can define when a feed is displayed as an alert on the dashboard. You can also specify the conditions under which an alert is no longer valid and dismiss it from the dashboard.
-   **[Configure alert actions](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/configure-alert-action-uib-ws.md)**  
Configure an alert action from the Crisis map interface in the BCM Configurable Workspace.

**Parent Topic:**[[configuring-business-continuity-management|Configuring Business Continuity Management]]

## Related

- [[sched-data-imports-crisis-map-uib-ws|Configure Scheduled Data Imports records]]
- [[conf-resource-for-crisis-map-uib-ws|Configure Resource Configuration records]]
- [[conf-alert-rule-uib-ws|Configure alert rules]]
- [[configure-alert-action-uib-ws|Configure alert actions]]
- [[crisis-map-customization-properties-for-g-maps|Customization properties for Google Maps]]
- [[g-maps-api-in-fam-map-component|Google Maps APIs used in Fam-map component]]
- [[configuring-business-continuity-management|Configuring Business Continuity Management]]
- [[threats-feeds-alerts-crisis-map|Crisis map interface]]
- [[Administration|Administration]]
- [[crisis-map-alert-actions|Configure an alert action]]
- [[bcm-workspace|BCM Configurable Workspace]]
