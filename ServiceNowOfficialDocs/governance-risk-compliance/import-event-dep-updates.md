---
title: Adding dependencies of impacted assets
description: You can add the dependencies of the impacted assets in the events and exercises based on the source data and relationships in the CMDB, BIAs, and plans.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/import-event-dep-updates.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Structured workflows for Exercises, Manage, Business Continuity Management, Governance, Risk, and Compliance]
---

# Adding dependencies of impacted assets

You can add the dependencies of the impacted assets in the events and [[exercise-management-uib|exercises]] based on the source data and relationships in the CMDB, BIAs, and plans.

## Configuring the sources in the Event dependency source configuration module

The BCM administrators can configure the sources to get the event dependencies in the Event dependency source configuration module. You can access the Event dependency source configuration module from the [[Administration|Administration]] menu in the Core UI.

The Event dependency source configuration module is shown in the example.\[Omitted image "event-dep-update-config.png"\] Alt text: Updating the Event dependencies.

When the BCM administrators can update the target records, filter condition for the records, and sources to fetch the event dependency.

Dependencies are added in the events only when the user selects the **Update dependencies** UI action. Dependencies are fetched from these sources for the events:

-   BIA upstream dependency
-   BIA downstream dependencies
-   CMDB
-   Plan primary assets
-   Plan related assets

**Note:** In an event, the dependencies of all assets are added manually where the source is Manual.

Setting up the Event dependency source configuration module is a one-time activity. Once the sources are configured in the Event dependency source configuration module, the updates are synchronized in the events.

For more information on setting up the Event dependency source configuration module, see [[conf-event-dep-source-confi-module|Configure Event dependency source configuration record]].

## Roles associated with event dependency updates

Users with these roles check for the dependency updates in an event:

-   The BCM program managers, BCM planners, and BCM managers can update the latest dependencies​.
-   BCM administrators can configure the Event dependency source configuration module.

## Workflow for updating the dependencies manually in the events and exercises

As the BCM application user, when you select the **Update dependencies** UI action in the Event record, the dependencies of all assets are added manually where the source is Manual.

The BCM application executes a workflow to update the impacted assets in the events and exercises as shown in the example.

\[Omitted image "update-dep-manually-f-events.png"\] Alt text: Updating the dependencies manually in the events and exercises.

1.  The BCM planner navigates to the event record.
2.  The BCM planner selects the **Update dependencies** UI action to add the assets manually.
3.  The application checks if the event record matches any configuration filter.

4.  If the event record matches any configuration filter, the system gets the dependencies of the added assets in real time according to the sources defined in the configuration \(Event dependency source configuration module\).
5.  If the event record does not match any configuration filter, the events workflow then continues for the next steps.

For more information on updating the event dependencies manually, see [[update-event-dep-manually|Update the event dependencies]].

## Data Relationships Framework

Beginning with the Australia release, the Data Relationships Framework \(com.sn\_app\_grc\_relationship\_config\) application supports the BCM application with the underlying framework to add the dependencies of the impacted assets in the events and exercises. The Data Relationships Framework application is installed with the BCM application by default.

For more information on the Data Relationships Framework, see [[data-relationship-framework|Data Relationships Framework]].

**Parent Topic:**[[performing-tasks-to-manage-exercise-events|Structured workflows for Exercises]]

## Related

- [[conf-event-dep-source-confi-module|Configure Event dependency source configuration record]]
- [[update-event-dep-manually|Update the event dependencies]]
- [[data-relationship-framework|Data Relationships Framework]]
- [[performing-tasks-to-manage-exercise-events|Structured workflows for Exercises]]
- [[exercise-management-uib|Exercises]]
- [[Administration|Administration]]
