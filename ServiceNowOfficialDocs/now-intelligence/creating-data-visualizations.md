---
title: Creating data visualizations
description: See how to create data visualizations using different data sources.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/now-intelligence/creating-data-visualizations.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
keywords: [Create visualization, Create data visualization]
breadcrumb: [Data visualizations, Platform Analytics experience, Platform Analytics]
tags:
  - now-intelligence
  - type-concept
---

# Creating data visualizations

See how to create data visualizations using different data sources.

\[Omitted video\] Description: How to create a data visualization in the Visualization Designer.

**Note:** In the Australia release, visualizations are based on Highcharts version 12.3.0.

Anyone with access to data can create a visualization of that data on any dashboard that they can edit. Users with the itil, report\_user, admin, or viz\_creator role can create a visualization in the Visualization Designer. When you create a visualization in the Visualization Designer, it is saved to the Library. For more information on access, see [Report\_view access control](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/reporting/report-view-access-control.md) and [[platform-analytics-roles|Platform Analytics roles]].

## Creating data visualizations in a dashboard editor

To create a data visualization from a dashboard, select **Add new element** and then choose **New visualization**. You can then configure the visualization as described in the topic for the selected visualization type.\[Omitted image "new-dv-from-dashboard.png"\] Alt text: Open dashboard in edit mode with the Add new element and New visualization buttons highlighted

## Creating data visualizations in the Visualization Designer

To create data visualizations in the Visualization Designer, navigate to **All** &gt; **[[c_performanceAnalyticsAndReporting|Platform Analytics]]** &gt; **Library** &gt; **Data Visualizations** and select **New**. You can then configure the visualization as described in the topic for the selected visualization type.

\[Omitted image "new-dv.png"\] Alt text: Data visualizations selected in filter navigator and New button highlighted

Use the Condition Builder to filter the information displayed in your visualization. For more information, see [[filter-dv-condition-builder|Filter data visualizations with the condition builder]].

## Instructions for creating data visualizations by type

-   **[[data-visualization-type-overview|Overview of data visualization types]]**  
When you create a data visualization, you select the type of visualization to display. Each visualization type is suited to show different data.
-   **[[create-dv-sing-sc-ac|Create a single score data visualization]]**  
Use a single score to show a value as a number or percentage. Visualize how the value compares to a target or benchmark, to track progress, or to identify areas for improvement.
-   **[[create-dv-box-plot|Create a box plot data visualization]]**  
Use a boxplot to show the median and lower and upper quartiles of numeric data along with outliers. You can also compare the distribution of different groups of this data.
-   **[[create-dv-bubble-ac|Create a bubble data visualization in the Visualization Designer]]**  
Use bubble visualizations to show multiple separate metrics on a single visualization and to answer binary questions, such as whether two fields have a relationship, and to highlight patterns.
-   **[[create-dv-dial-ac|Create a dial data visualization]]**  
Use a dial visualization to show where a value lies between expected minimum and maximum values. Use the dial visualization to show how a value compares to a target or benchmark, track progress, or to identify areas for improvement.
-   **[[create-dv-gauge-ac|Create a gauge data visualization in the Visualization Designer]]**  
A gauge visualization shows where a value lies between expected minimum and maximum values. Use the gauge visualization to follow progress with color-coded value ranges.
-   **[[create-dv-geomap-ac|Create a geomap data visualization]]**  
A geomap visualization shows the geographical distribution of data for a world, country, region, or province/state. Use Geomaps to show table data that contains location information.
-   **[[create-dv-heatmap-ac|Create a heatmap data visualization]]**  
Use a heatmap visualization to show the relationship between two table fields or [[c_CreatingBreakdowns|indicator breakdowns]]. The changes in color as you move along the axes reveal patterns in the value of one or both fields/breakdowns.
-   **[[create-dv-bar-ac|Create a horizontal or vertical bar data visualization]]**  
Use bar visualizations to show information in segments that are proportional to the values they represent. Vertical bar and horizontal bar visualizations compare numeric values that represent either nominal or ordinal data.
-   **[[create-dv-donut-ac|Create a pie or donut data visualization]]**  
Use pie, donut, and semi-donut visualizations to compare the size of parts of a data set to the whole. The segments of these visualizations should total to 100%.
-   **[[create-dv-pareto-vd|Create a Pareto bar data visualization]]**  
Use a Pareto bar visualization to Identify the most important dimension in a large set of dimensions. Pareto bar visualization columns show data in descending order. A line shows the cumulative percentage.
-   **[[create-dv-pivot-ac|Create a pivot table data visualization in the Visualization Designer]]**  
Create a pivot table visualization to summarize large data sets by breaking them down by multiple dimensions in a single table. Cells show each row and column value combination and can also show subtotals.
-   **[[create-dv-time-series-ac|Create time series data visualizations]]**  
Show changes in data over time. Use different time series visualizations to emphasize different aspects of the data, such as trends or individual values.
-   **[[create-dv-calendar-ac|Create a calendar report data visualization]]**  
Create calendar report visualizations to show and highlight date-driven events.
-   **[[create-dv-analytics-list|Create a list visualization in the Visualization Designer]]**  
Create a list of table records that can be drilled down to from chart interactions. List visualizations display table data in columns. By default, the columns match the default list view of the table.
-   **[[create-dv-indicator-scorecard|Create an Indicator Scorecard]]**  
The Indicator Scorecard component enables users to visualize and compare data between multiple [[c_Indicators|Performance Analytics indicators]]. It highlights the information regarding the last score collected, the change from the previous data point, the trend over time, and the value of the target to achieve.​
-   **[[create-data-viz-from-list|Create a data visualization from a list]]**  
You can create a Platform Analytics vertical bar or pie data visualization from inside a Core UI list. If you have a data visualization role, you can save, share, export, or duplicate the visualization.

**Parent Topic:**[[analytics-center-data-visualizations|Data visualizations in Platform Analytics]]

**Related topics**  


[Exploring the Data Visualizations library]()

[Common data visualization tasks]()

[View data visualizations]()

[Configure data visualizations]()

[Data visualization reference]()

## Related

- [[platform-analytics-roles|Platform Analytics roles]]
- [[filter-dv-condition-builder|Filter data visualizations with the condition builder]]
- [[data-visualization-type-overview|Overview of data visualization types]]
- [[create-dv-sing-sc-ac|Create a single score data visualization]]
- [[create-dv-box-plot|Create a box plot data visualization]]
- [[create-dv-bubble-ac|Create a bubble data visualization in the Visualization Designer]]
- [[create-dv-dial-ac|Create a dial data visualization]]
- [[create-dv-gauge-ac|Create a gauge data visualization in the Visualization Designer]]
- [[create-dv-geomap-ac|Create a geomap data visualization]]
- [[create-dv-heatmap-ac|Create a heatmap data visualization]]
- [[create-dv-bar-ac|Create a horizontal or vertical bar data visualization]]
- [[create-dv-donut-ac|Create a pie or donut data visualization]]
- [[create-dv-pareto-vd|Create a Pareto bar data visualization]]
- [[create-dv-pivot-ac|Create a pivot table data visualization in the Visualization Designer]]
- [[create-dv-time-series-ac|Create time series data visualizations]]
- [[create-dv-calendar-ac|Create a calendar report data visualization]]
- [[create-dv-analytics-list|Create a list visualization in the Visualization Designer]]
- [[create-dv-indicator-scorecard|Create an Indicator Scorecard]]
- [[create-data-viz-from-list|Create a data visualization from a list]]
- [[analytics-center-data-visualizations|Data visualizations in Platform Analytics]]
- [[c_performanceAnalyticsAndReporting|Platform Analytics]]
- [[c_CreatingBreakdowns|Indicator breakdowns]]
- [[c_Indicators|Performance Analytics indicators]]
