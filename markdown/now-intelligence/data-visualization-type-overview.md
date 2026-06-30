---
title: Overview of data visualization types
description: When you create a data visualization, you select the type of visualization to display. Each visualization type is suited to show different data.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/now-intelligence/data-visualization-type-overview.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 11
breadcrumb: [Create, Data visualizations, Platform Analytics experience, Platform Analytics]
---

# Overview of data visualization types

When you create a data visualization, you select the type of visualization to display. Each visualization type is suited to show different data.

## Score visualizations

This type of data visualization shows a single value or score as a number or percentage. Scores are often used to show how a particular value or metric compares to a target or benchmark. They can be useful for tracking progress or identifying areas for improvement, for example showing a company's or division's overall performance.

<table id="table_sth_yqq_5x"><thead><tr><th>

Visualization

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[create-dv-sing-sc-ac|Single score visualization]] \[Omitted image "inline-data-vis-single-score.png"\] Alt text:

</td><td>

Single-score visualizations display a single aggregate value that is important to your business.[[dv-example-single-score|Single score data visualization example]]

</td></tr><tr><td>

[[create-dv-dial-ac|Dial visualization]] \[Omitted image "inline-data-vis-dial.png"\] Alt text:

</td><td>

Dial visualizations show where a single value lies across a range from minimum to maximum expected values. Visually, a "needle" points to the value, and the dial is colored in for values up to the needle.[[dv-example-dial|Dial visualization example]]

</td></tr><tr><td>

[[create-dv-gauge-ac|Gauge visualization]] \[Omitted image "inline-data-vis-gauge.png"\] Alt text:

</td><td>

Like dials, gauges show where a single value lies across a range from minimum to maximum expected values. In addition to dial functionality, you can set colored data ranges to help users understand what the value represents.[[dv-example-gauge|Gauge visualization example]]

</td></tr></tbody>
</table>## Time series visualizations

Time Series visualizations show data over time. All time series visualization types share configuration options. They differ in use case, depending on whether you want to emphasize data trends or the differences between individual data points. For more information about these use cases, see [[create-dv-time-series-ac|Create time series data visualizations]].

**Note:** In addition to data from within your instances and imported data sources, you can also use MetricBase data in time series visualizations. For more information, see MetricBase application.

<table id="table_time-series"><thead><tr><th>

Visualization

</th><th>

Description and use case

</th></tr><tr><th class="sub-head" colspan="2">

Visualizing trends in a data source

</th></tr></thead><tbody><tr><td>

Line\[Omitted image "inline-data-vis-line.png"\] Alt text: line visualization

</td><td>

Shows how one or more values change over time by connecting a series of data points with straight lines. Use a line visualization to emphasize the trend in the data. Consider line visualizations to be the default choice for showing a time series. If you’re unsure of which visualization to use, use a line.

</td></tr><tr><td>

Spline\[Omitted image "inline-data-vis-spline.png"\] Alt text: spline visualization

</td><td>

Shows how one or more values change over time by connecting a series of data points with a fitted curve. The curve emphasizes the trend over individual data points. Spline visualizations let you take a limited set of known data points and approximate intervening values.

</td></tr><tr><td>

Scatter\[Omitted image "inline-data-vis-trend.png"\] Alt text: scatter visualization - med

</td><td>

Shows unconnected points for values in the Y-axis against time in the X-axis. Usually the trend line is also shown. Use with a spread of data that can’t be usefully connected with a line.

</td></tr><tr><td class="sub-head" colspan="2">

Comparing scores in a data source

</td></tr><tr><td>

Column\[Omitted image "inline-data-vis-bar-column.png"\] Alt text: column visualization

</td><td>

Shows changes in data over time by showing values as proportional vertical columns. Use either to visualize changes in one data source or to compare data sources. To compare data sources with a column visualization, either add data sources to the visualization, or place several column visualizations next to each other in a dashboard.

</td></tr><tr><td>

Step\[Omitted image "inline-data-vis-stepline.png"\] Alt text:

</td><td>

Emphasizes changes in a data source between discreet points in time. Use to show small incremental changes, especially when a line visualization smudges the data.

</td></tr><tr><td class="sub-head" colspan="2">

Comparing scores or trends between data sources

</td></tr><tr><td>

Area\[Omitted image "inline-data-vis-area.png"\] Alt text:

</td><td>

Resembles a line visualization, but the area between the axis and line is emphasized with colors. Use with [[multiple-data-sources|multiple data sources]] to highlight the relative contribution that each data source makes to the whole.

</td></tr></tbody>
</table>## Bar visualizations

Bar visualizations enable you to [[scorecard-compare-tab|compare scores]] across data dimensions. Horizontal and vertical bar visualization types are available. They share all configuration options. In general, use horizontal bars for nominal or categorical data. Use vertical bars for ordinal or sequential data. Use different colors or patterns to distinguish different groups or categories. For more information, see [[create-dv-bar-ac|Create a horizontal or vertical bar data visualization]].

<table id="table_js4_h4f_s5b"><thead><tr><th>

Visualization

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[Horizontal bar visualization](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/create-dv-bar-ac.md) \[Omitted image "inline-data-vis-bar-horizontal.png"\] Alt text:

</td><td rowspan="3">

Bar visualizations show categories labeled on one axis and values on the other. Use vertical bars to compare ordinal data, especially when there aren’t too many categories, such as sales numbers grouped into buckets. Use horizontal bar charts with nominal data, such as incident severity or assignment group.-   [[dv-example-h-bar|Horizontal bar visualization example]]
-   [[dv-example-v-bar|Vertical bar visualization example]]

Pareto bar visualizations help you identify the most important dimension in a large set of dimensions. Columns show data in descending order. A line shows cumulative percentage. Pareto visualizations contain both bar and line graphs. The bars display the data in descending order from left to right, and the line graph shows the cumulative totals from each category in the same order. The left Y axis is the record count, and the right Y axis is the cumulative percentage of the total number of records evaluated.

</td></tr><tr><td>

[Vertical bar visualization](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/create-dv-bar-ac.md) \[Omitted image "inline-data-vis-bar-vertical.png"\] Alt text: Data visualization vertical bar type- med

</td></tr><tr><td>

[[create-dv-pareto-vd|Pareto bar visualization]]\[Omitted image "inline-data-vis-pareto.png"\] Alt text: Data visualization pareto bar type

</td></tr></tbody>
</table>## Pie and Donut visualizations

Pie and donut visualizations show the relationship between parts and the whole of a data set. The segments of these visualizations should total to 100%. For more information, see [[create-dv-donut-ac|Create a pie or donut data visualization]].

<table id="table_vks_frf_s5b"><thead><tr><th>

Visualization

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[Pie visualizations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/create-dv-donut-ac.md) \[Omitted image "inline-data-vis-pie.png"\] Alt text:

</td><td rowspan="3">

Pie visualizations are best when comparing 5–7 segments that total 100%, when no two segments have a value within 10% of each other.

 Donut visualizations are best for comparing no more than five segments that total 100%, when no two segments have a value within 10% of each other. The center of the donut can be used to show additional information.

 Semi-donut visualizations are best for comparing no more than four segments that total 100%, when no two segments have a value within 10% of each other.

 -   [[dv-example-pie|Pie visualization example]]
-   [[dv-example-donut|Donut visualization example]]

</td></tr><tr><td>

[Donut visualizations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/create-dv-donut-ac.md) \[Omitted image "inline-data-vis-donut.png"\] Alt text:

</td></tr><tr><td>

[Semi-donut visualizations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/create-dv-donut-ac.md) \[Omitted image "inline-data-vis-semi-donut.png"\] Alt text:

</td></tr></tbody>
</table>## Multidimensional charts

Multidimensional visualizations enable you to show multiple variables in a single chart, and it can be useful for showing the relationships between different variables. They are useful when you have a lot of data, and you want to find patterns or trends that might not be immediately obvious. They're also good to use when you want to show the relationship between three or more variables.

<table id="table_uyz_dtf_s5b"><thead><tr><th>

Visualization

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[create-dv-pivot-ac|Pivot table visualization]] \[Omitted image "inline-data-vis-pivot-table.png"\] Alt text: Data visualization pivot table type - med

</td><td>

[[c_PivotTables|Pivot tables]] allow for several kinds of aggregation between its fields. You can also filter the data. The columns represent one field or [breakdown](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/performance-analytics/performance-analytics-glossary.md), while a hierarchy of rows represents multiple other fields or breakdowns.[[dv-example-pivot|Pivot visualization example]]

</td></tr><tr><td>

[[create-dv-heatmap-ac|Heatmap visualization]] \[Omitted image "inline-data-vis-heatmap.png"\] Alt text: Data visualization heatmap type - med

</td><td>

Heatmaps show the relationship between two table fields or [[c_CreatingBreakdowns|indicator breakdowns]]. The changes in color as you move along the axes reveal patterns in the value of one or both fields/breakdowns.[[dv-example-heatmap|Heatmap visualization example]]

</td></tr><tr><td>

[[create-dv-bubble-ac|Bubble chart visualization]] \[Omitted image "inline-data-vis-bubble.png"\] Alt text: Data visualization bubble chart - med

</td><td>

Bubble charts are circles of different sizes along an x-y axis. The x and y axes represent different numeric fields, such as values or amounts. Use the relative size and position of the circles to compare fields and see their relationships. You can also group the data by a third field, which can be qualitative. The third field is differentiated by color. Use bubble charts to answer binary questions, such as whether two fields have a relationship, and to highlight patterns.[[dv-example-bubble|Bubble data visualization example]]

</td></tr></tbody>
</table>## Other visualizations

Data visualizations can also show calendars, simple lists, indicator scorecards, and location.

<table id="table_bcx_f2r_g5b"><thead><tr><th>

Visualization

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[create-dv-calendar-ac|Calendar report visualization]] \[Omitted image "inline-data-vis-calendar-days.png"\] Alt text: Data visualization calendar type - med

</td><td>

Displays data-driven events in a calendar format.

</td></tr><tr><td>

[[create-dv-indicator-scorecard|Indicator scorecard]] \[Omitted image "inline-data-vis-scorecard.png"\] Alt text: Analytics center scorecard report-med

</td><td>

The Indicator scorecard component enables you to visualize and compare data between multiple [[c_Indicators|Performance Analytics indicators]].[Create an Indicator Scorecard](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/create-dv-indicator-scorecard.md)

</td></tr><tr><td>

[[create-dv-analytics-list|List]]\[Omitted image "inline-data-vis-list.png"\] Alt text: Data visualization list type - med

</td><td>

Shows a list of table records.

</td></tr><tr><td>

[[create-dv-box-plot|Box plot]]\[Omitted image "inline-data-vis-box.png"\] Alt text:

</td><td>

Use a box plot to show the median and lower and upper quartiles of numeric data along with outliers. You can also compare the distribution of different groups of this data.

</td></tr><tr><td>

[[create-dv-geomap-ac|Geomap]]\[Omitted image "inline-data-vis-geomap.png"\] Alt text: Geomap data visualization

</td><td>

Displays data by country, state, or city. Users can use table data that contains location information to visualize in the chart.

</td></tr></tbody>
</table>**Parent Topic:**[[creating-data-visualizations|Creating data visualizations]]

## Related

- [[create-dv-sing-sc-ac|Create a single score data visualization]]
- [[dv-example-single-score|Single score data visualization example]]
- [[create-dv-dial-ac|Create a dial data visualization]]
- [[dv-example-dial|Dial visualization example]]
- [[create-dv-gauge-ac|Create a gauge data visualization in the Visualization Designer]]
- [[dv-example-gauge|Gauge visualization example]]
- [[create-dv-time-series-ac|Create time series data visualizations]]
- [[create-dv-bar-ac|Create a horizontal or vertical bar data visualization]]
- [[dv-example-h-bar|Horizontal bar visualization example]]
- [[dv-example-v-bar|Vertical bar visualization example]]
- [[create-dv-pareto-vd|Create a Pareto bar data visualization]]
- [[create-dv-donut-ac|Create a pie or donut data visualization]]
- [[dv-example-pie|Pie visualization example]]
- [[dv-example-donut|Donut visualization example]]
- [[create-dv-pivot-ac|Create a pivot table data visualization in the Visualization Designer]]
- [[dv-example-pivot|Pivot visualization example]]
- [[create-dv-heatmap-ac|Create a heatmap data visualization]]
- [[dv-example-heatmap|Heatmap visualization example]]
- [[create-dv-bubble-ac|Create a bubble data visualization in the Visualization Designer]]
- [[dv-example-bubble|Bubble data visualization example]]
- [[create-dv-calendar-ac|Create a calendar report data visualization]]
- [[create-dv-indicator-scorecard|Create an Indicator Scorecard]]
- [[create-dv-analytics-list|Create a list visualization in the Visualization Designer]]
- [[create-dv-box-plot|Create a box plot data visualization]]
- [[create-dv-geomap-ac|Create a geomap data visualization]]
- [[creating-data-visualizations|Creating data visualizations]]
- [[multiple-data-sources|multiple data sources]]
- [[scorecard-compare-tab|Compare scores]]
- [[c_PivotTables|Pivot tables]]
- [[c_CreatingBreakdowns|Indicator breakdowns]]
- [[c_Indicators|Performance Analytics indicators]]
