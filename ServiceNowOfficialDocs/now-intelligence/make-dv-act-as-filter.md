---
title: Make a data visualization act as a filter
description: You can set a data visualization to act as a filter on a dashboard that contains it. Only table or indicator data can be so filtered.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/now-intelligence/make-dv-act-as-filter.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Filters, Platform Analytics experience, Platform Analytics]
tags:
  - now-intelligence
  - type-task
---

# Make a data visualization act as a filter

You can set a data visualization to act as a filter on a dashboard that contains it. Only table or indicator data can be so filtered.

## Before you begin

To use a data visualization as a filter, you have to meet these requirements:

-   The visualization can only be of pie/donut or horizontal/vertical bar type.
-   The visualization can show only table or indicator data.
-   The visualization must be on a dashboard that was created in the inline editor. You cannot use a visualization as a filter on a technical dashboard or other UI Builder page.
-   The visualization cannot have a group by value based on a time duration.

Role required: Any internal role and the right to edit the dashboard with the visualization

## Procedure

1.  Navigate to **All** &gt; **[[c_performanceAnalyticsAndReporting|Platform Analytics]]** &gt; **Library** &gt; **Dashboards**.

2.  Find and open the dashboard that contains the data visualization.

3.  Select **Edit** to put the dashboard in edit mode.

    If you do not see an Edit button

4.  Find the pie/donut or bar visualization that you want to use as a filter on the dashboard.

5.  Open the visualization's configuration panel.

6.  Locate the Chart Interactions section.

7.  Select **Apply as filter**.

8.  Save and exit editing mode.


**Related topics**  


[[dv-chart-interactions|Chart interactions in a data visualization]]

[[create-dv-donut-ac|Create a pie or donut data visualization]]

[[create-dv-bar-ac|Create a horizontal or vertical bar data visualization]]

## Related

- [[dv-chart-interactions|Chart interactions in a data visualization]]
- [[create-dv-donut-ac|Create a pie or donut data visualization]]
- [[create-dv-bar-ac|Create a horizontal or vertical bar data visualization]]
- [[c_performanceAnalyticsAndReporting|Platform Analytics]]
