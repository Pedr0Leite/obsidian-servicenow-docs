---
title: Configuring dashboards
description: Configure your dashboard and perform admin tasks. Most tasks are performed in either the dashboard details or the dashboard settings UI.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/now-intelligence/configuring-dashboards.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Dashboards, Platform Analytics experience, Platform Analytics]
tags:
  - now-intelligence
  - type-concept
---

# Configuring dashboards

Configure your dashboard and perform admin tasks. Most tasks are performed in either the dashboard details or the dashboard settings UI.

## Common configuration tasks

The following tasks do not require a special role, though they may be limited to the dashboard owner or a user with editing rights.

-   [[config-db-in-ac|Change dashboard name or description]]

    Provide an informative description of your dashboard for other users.

-   [Specify dashboard requester](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/config-db-in-ac.md)

    Specify the user who requested that this dashboard be created. Specifying the user automatically gives them editing rights to the dashboard.

-   [Transfer ownership of a dashboard](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/config-db-in-ac.md)

    By default, the creator of the dashboard is the dashboard owner. If you are the owner of a dashboard, you can transfer this ownership to another user or to a user group.

-   [[configure-ac-db-settings|Set background colors]]

    Select the background colors for one or more tabs on the dashboard.

-   [See who created a dashboard](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/config-db-in-ac.md)
-   [See who the dashboard is shared with](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/config-db-in-ac.md)

## Admin configuration tasks

The following tasks require at least the dashboard\_admin if not the admin role.

-   [Set data refresh options](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/configure-ac-db-settings.md)

    Set whether the dashboard is refreshed on a schedule and whether data caching is used. Requires the dashboard\_admin or admin role. For more information, see [[data-caching-pa|Data caching in Platform Analytics]].

-   [[certify-db-ac|Certify a dashboard]]

    Certify that a dashboard has been officially approved for use by your organization. Requires the admin role.

-   [[configure-ac-db-timeout|Configure Platform Analytics dashboard tab cache timeout]]

    Set the number of minutes that dashboard tab content is retained before being refreshed. Applies to all dashboard tabs on the instance. Requires the admin role.

-   [Manage which workspaces are allowed to contain the dashboard](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/config-db-in-ac.md)

    Specify the workspaces on the instance other than the [[par-workspace|Platform Analytics experience]] that this dashboard can be added to. Requires the admin or dashboard admin role. For more information about dashboards in workspaces, see [[add-dashboard-to-workspace|Add a dashboard to a Dashboards page]].

-   [[move-pae-db-with-update-set|Move a Platform Analytics dashboard with an update set]]

    Moves the dashboard structure to an update set, so it can be put on another instance. Does not include dashboard contents. Requires the admin role.


## Process Mining integration tasks

-   [[configure-po-map|Configure a Process Mining map on a dashboard]]

    Map the different states that are part of your process and the transitions between those states. See which states the objects of the process are in and the speed with which they change state. Requires the sn\_process\_optimization\_analyst role.

-   [Creating Process Mining projects from Proactive Analytics suggestions](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/proactive-analytics/pm-projects-insights-suggestions.md)

    The Insights panel can include suggestions for [[process-mining|Process Mining]] projects to create. Creating the projects requires the sn\_process\_optimization\_analyst role.

## Related

- [[config-db-in-ac|Configure Platform Analytics dashboard details]]
- [[configure-ac-db-settings|Configure Platform Analytics dashboard settings]]
- [[data-caching-pa|Data caching in Platform Analytics]]
- [[certify-db-ac|Certify a Platform Analytics dashboard]]
- [[configure-ac-db-timeout|Configure Platform Analytics dashboard tab cache timeout]]
- [[add-dashboard-to-workspace|Add a dashboard to a Dashboards page]]
- [[move-pae-db-with-update-set|Move a Platform Analytics dashboard with an update set]]
- [[configure-po-map|Configure a Process Mining map on a dashboard]]
- [[par-workspace|Platform Analytics experience]]
- [[process-mining|Process Mining]]
