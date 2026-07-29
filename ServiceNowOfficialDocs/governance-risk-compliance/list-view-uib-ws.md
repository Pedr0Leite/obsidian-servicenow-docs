---
title: List view
description: The List view in the BCM Configurable Workspace displays BIA, planning, exercise, and crisis event records along with their key metrics. You can filter records, create new ones, and open them to display the scope of all BCM functional components and their key metric information.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/list-view-uib-ws.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [BCM Configurable Workspace, Explore, Business Continuity Management, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - type-concept
---

# List view

The List view in the [[bcm-workspace|BCM Configurable Workspace]] displays BIA, planning, exercise, and crisis event records along with their key metrics. You can filter records, create new ones, and open them to display the scope of all BCM functional components and their key metric information.

Use the List view to know the count and status of the business impact analysis, planning, exercise, and crisis event records. It provides a structured view to help you:

-   Assess potential disruptions to business services or applications.
-   Manage continuity plans and their dependencies.
-   Create and track exercise events.
-   Respond to crisis events with relevant continuity tasks.

A typical List view in the BCM Configurable Workspace is shown in the example.

\[Omitted image "list-view-bcm.png"\] Alt text: List view in BCM UIB Workspace.

The records from each group are listed according to their current state and the record details are configurable. You can create a record by selecting **New**. You can select the link of a record in the **Name** column and view its details.

Use the List view in the BCM Configurable Workspace to complete these business continuity tasks:

-   Assess the impact of a possible disruption on your business services, processes, and applications. For more information on performing a business impact analysis, see [[bia-uib|Business impact analysis]].
-   Create business continuity plans to mitigate the risk at the time of an event. For more information on managing your business continuity planning tasks, see [[bcp-uib|Business continuity planning]].
-   Create an event to exercise the plan in a simulated crisis. For more information on exercising an event, see [[exercise-management-uib|Exercises]].
-   Apply the plan in an actual crisis. For more information on managing a crisis event, see [[crisis-management-uib|Crisis events]].

For information on managing business continuity tasks in the BCM Configurable Workspace, see [[manage-bcm-with-uib-workspace|Managing BCM workflow tasks]].

## Monitoring 360° relationship data for a record

You can view 360° relationship data for BIAs, plans, exercises, and crisis events. This view shows upstream and downstream dependencies, helping you understand how assets relate to one another. Administrators configure these views using the **360° View Configurations** menu.

The configurations for the 360° view are stored in **360° View Configurations** &gt; **Configure 360° Views**. If you have the BCM administrator role, you can configure the relationships for the records in **360° View Configurations** &gt; **Relationship Registries**.

-   For information on configuring 360° relationship registries and views, see [[configure-relationship-registries-views|Configure 360° relationship registries and views]].
-   For information on how to view 360º relationships of a business impact analysis, see [[visualize-360-degree-view-for-bia|Visualize 360° relationships for BIAs]].
-   For information on how to view 360º relationships of a business continuity plan, see [[relationship-view-bcp|Visualize 360° relationships for the BCP]].
-   For information on how to view 360º relationships of an exercise or crisis event, see [[relationship-view-exercise-crisis|View 360° relationships for exercises and crises]].

## Related

- [[bia-uib|Business impact analysis]]
- [[bcp-uib|Business continuity planning]]
- [[exercise-management-uib|Exercises]]
- [[crisis-management-uib|Crisis events]]
- [[manage-bcm-with-uib-workspace|Managing BCM workflow tasks]]
- [[configure-relationship-registries-views|Configure 360° relationship registries and views]]
- [[visualize-360-degree-view-for-bia|Visualize 360° relationships for BIAs]]
- [[relationship-view-bcp|Visualize 360° relationships for the BCP]]
- [[relationship-view-exercise-crisis|View 360° relationships for exercises and crises]]
- [[bcm-workspace|BCM Configurable Workspace]]
