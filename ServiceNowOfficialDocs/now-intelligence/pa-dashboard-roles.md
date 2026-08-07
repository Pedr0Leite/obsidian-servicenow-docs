---
title: Platform Analytics dashboard roles
description: Platform Analytics dashboards have few role restrictions. Editing rights are granted by sharing, independent of role.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/now-intelligence/pa-dashboard-roles.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Reference, Dashboards, Platform Analytics experience, Platform Analytics]
tags:
  - now-intelligence
  - type-concept
---

# Platform Analytics dashboard roles

[[c_performanceAnalyticsAndReporting|Platform Analytics]] dashboards have few role restrictions. Editing rights are granted by sharing, independent of role.

Users with any role can create dashboards and share them with groups, users, and roles. These users can share a dashboard that has been shared with them if sharing rights were also granted. They can pass along editing rights if granted.

The dashboard\_admin role allows a user to configure, edit, or delete any dashboards, regardless of ownership or editing rights. Certain configuration tasks also require dashboard\_admin, as described in [[configuring-dashboards|Configuring dashboards]].

Tasks that integrate dashboards with [[process-mining|Process Mining]] require the sn\_process\_optimization\_analyst role. These tasks are listed in [Configuring dashboards](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/configuring-dashboards.md).

Users with the analytics\_categories\_admin role can create, edit, or delete dashboard categories.

For a full guide to roles connected to Platform Analytics dashboards, see [[platform-analytics-roles|Platform Analytics roles]].

<table id="table_d1r_2vc_k2c"><thead><tr><th>

Use case

</th><th>

Required role

</th></tr></thead><tbody><tr><td>

Create a dashboard

</td><td>

Any role

</td></tr><tr><td>

Share a dashboard

</td><td>

Any role to share a data visualization that you created or that was shared with you with sharing rights. With the viz\_admin role or higher, you can share any data visualization on the instance. When you share a data visualization, you can pass along the rights to share that visualization further. You also decide whether to share with editing rights or only viewing rights. If a data visualization has been shared with you with sharing and editing rights, you can also pass along editing rights.dashboard\_admin to share any dashboard

A role with read access to the Roles \[sys\_user\_role\] table to share with roles

</td></tr><tr><td>

Edit a dashboard

</td><td>

Any role, if you created the dashboard or have had it shared with you with editing rights.dashboard\_admin or higher for any dashboard

[[technical-dashboards|Technical dashboards]] also require ui\_builder\_admin

</td></tr><tr><td>

Duplicate a dashboard

</td><td>

Any role, if you can view the dashboard. You cannot duplicate technical dashboards.

</td></tr><tr><td>

Create a printer-friendly copy of a dashboard

</td><td>

Any role, if you can view the dashboard.

</td></tr><tr><td>

Export a dashboard

</td><td>

Any role, if you can view the dashboard.

</td></tr><tr><td>

Schedule the export of a dashboard

</td><td>

par\_scheduler for dashboards that you own or that have been shared with you.dashboard\_admin or higher for any dashboard

</td></tr><tr><td>

Delete the scheduled export of a dashboard

</td><td>

sn\_par\_sche\_export.par\_scheduler\_admin \(contained in dashboard\_admin\)

</td></tr><tr><td>

Bookmark a dashboard

</td><td>

Any role, if you can view the dashboard.

</td></tr><tr><td>

Delete a dashboard

</td><td>

Any role, if you created the dashboard.dashboard\_admin or higher for any dashboard

</td></tr><tr><td>

[[config-db-in-ac|Configure dashboard details]]

</td><td>

Any role, if you created the dashboard or have had it shared with you with editing rights.dashboard\_admin or higher for any dashboard

</td></tr><tr><td>

[[configure-ac-db-settings|Configure dashboard settings]] except scheduled refreshes

</td><td>

Any role, if you created the dashboard or have had it shared with you with editing rights.dashboard\_admin or higher for any dashboard

</td></tr><tr><td>

[Schedule dashboard refreshes](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/configure-ac-db-settings.md)

</td><td>

dashboard\_admin or higher

</td></tr><tr><td>

[[configure-ac-db-timeout|Configure dashboard tab cache timeout]]

</td><td>

admin

</td></tr><tr><td>

[[db-categories|Create dashboard categories]]

</td><td>

analytics\_categories\_admin or higher

</td></tr><tr><td>

[Assign categories to a dashboard](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/db-categories.md)

</td><td>

Any role, if you can edit the dashboard.analytics\_categories\_admin or higher to assign a category to any dashboard.

</td></tr></tbody>
</table>**Parent Topic:**[[dashboard-reference-page|Dashboard reference]]

## Related

- [[configuring-dashboards|Configuring dashboards]]
- [[platform-analytics-roles|Platform Analytics roles]]
- [[config-db-in-ac|Configure Platform Analytics dashboard details]]
- [[configure-ac-db-settings|Configure Platform Analytics dashboard settings]]
- [[configure-ac-db-timeout|Configure Platform Analytics dashboard tab cache timeout]]
- [[db-categories|Platform Analytics experience dashboard categories]]
- [[dashboard-reference-page|Dashboard reference]]
- [[c_performanceAnalyticsAndReporting|Platform Analytics]]
- [[process-mining|Process Mining]]
- [[technical-dashboards|Technical dashboards]]
