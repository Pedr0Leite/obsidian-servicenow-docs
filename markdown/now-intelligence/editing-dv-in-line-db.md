---
title: Edit a data visualization in an inline dashboard
description: You can create and edit a data visualization from within the inline dashboard editor. Not all the options are the same as in the Visualization Designer. You can move between the inline editor and the Visualization Designer.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/now-intelligence/editing-dv-in-line-db.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Share, edit, or delete, Data visualizations, Platform Analytics experience, Platform Analytics]
---

# Edit a data visualization in an inline dashboard

You can create and edit a data visualization from within the inline dashboard editor. Not all the options are the same as in the Visualization Designer. You can move between the inline editor and the Visualization Designer.

You can add a data visualization to a dashboard through the **Add new element** menu, as described in [[edit-db-elements-in-ac|Edit in-line Platform Analytics dashboard elements]]. You can edit a visualization in the dashboard by putting the dashboard in edit mode and selecting the visualization. However, some of the behavior may differ:

-   If the visualization is in the library and you own it, you need the itil, report\_user, or viz\_creator role to edit it. When you save your edit, you have the option to save the visualization in the library, which affects all dashboards that show the visualization, or to save a local copy only for the dashboard.
-   If the visualization is in the library and you do not own it, you need the viz\_admin or admin role to edit it. When you save your edit, you have the option to save the visualization in the library, which affects all dashboards that show the visualization, or to save a local copy.
-   If the visualization is in the library and you don't have the necessary roles to edit it, you can "unlink" the visualization by creating a local copy, which you can edit. For more information, see [[editing-local-copy-saved-dv|Edit a copy of a shared dashboard element]].
-   Some options may differ between the inline editor and the Visualization Designer. For example, in the chart interactions, you configure a data visualization to drill down to another visualization only in the Visualization Designer.

**Important:** You cannot place Core UI reports or [[c_Widgets|Performance Analytics widgets]] on a [[c_performanceAnalyticsAndReporting|Platform Analytics]] dashboard. Add data visualizations instead.

The **Actions** menu on the visualization itself provides options for changing the editor. You can also select to **Resize**, **Configure**, **Duplicate** , or **Delete** the visualization from the dashboard. If you have the viz\_admin role or higher, you can also view the visualization's PAR Dashboard Widget \[par\_dashboard\_widget\] record.

\[Omitted image "dv-on-db-more-actions.png"\] Alt text: The More Actions menu on a saved data visualization in the dashboard editor.

**Note:** If you save a Platform Analytics dashboard with appsee data, a single click on that dashboard automatically redirects you to the corresponding UXA dashboard. This provides a quick and efficient way to drill down and explore specific user behavior from your appsee analytics.

## Other topics

-   **[[add-db-data-viz-to-library|Add a dashboard data visualization to the library]]**  
To make a data visualization on a dashboard reusable, or to be able to edit it in the Visualization Designer, add it to the data visualization library.
-   **[[open-dv-on-db-in-vd|Open a visualization in the Visualization Designer from a dashboard]]**  
From the dashboard editor, open a data visualization in the Visualization Designer. You have a different set of options.

**Parent Topic:**[[common-dv-tasks|Common data visualization tasks]]

## Related

- [[edit-db-elements-in-ac|Edit in-line Platform Analytics dashboard elements]]
- [[editing-local-copy-saved-dv|Edit a copy of a shared dashboard element]]
- [[add-db-data-viz-to-library|Add a dashboard data visualization to the library]]
- [[open-dv-on-db-in-vd|Open a visualization in the Visualization Designer from a dashboard]]
- [[common-dv-tasks|Common data visualization tasks]]
- [[c_Widgets|Performance Analytics widgets]]
- [[c_performanceAnalyticsAndReporting|Platform Analytics]]
