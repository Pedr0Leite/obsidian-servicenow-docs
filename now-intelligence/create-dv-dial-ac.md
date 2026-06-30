---
title: Create a dial data visualization
description: Use a dial visualization to show where a value lies between expected minimum and maximum values. Use the dial visualization to show how a value compares to a target or benchmark, track progress, or to identify areas for improvement.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/now-intelligence/create-dv-dial-ac.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 9
keywords: [Create dial report, Create dial visualization]
breadcrumb: [Create, Data visualizations, Platform Analytics experience, Platform Analytics]
---

# Create a dial data visualization

Use a dial visualization to show where a value lies between expected minimum and maximum values. Use the dial visualization to show how a value compares to a target or benchmark, track progress, or to identify areas for improvement.

## Before you begin

Role required: Anyone with access to data can create a visualization of that data on any dashboard that they can edit. Users with the itil, report\_user, admin, or viz\_creator role can create a visualization in the Visualization Designer. When you create a visualization in the Visualization Designer, it is saved to the Library. For more information on access, see [Report\_view access control](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/reporting/report-view-access-control.md) and [[platform-analytics-roles|Platform Analytics roles]].

## About this task

For information about the use of a Dial visualization in a dashboard, see [the Developer Site.](https://developer.servicenow.com/dev.do#!/reference/now-experience/xanadu/shared-components/now-vis-dial-wrapper/usage) This site gives information about Dial data visualization components in the UI Builder, and some configuration options may differ from the Visualization Designer.

**Note:** Workflow Data Fabric sources do not support real-time update on single score, dial, and gauge visualizations.

## Procedure

1.  Navigate to **All** &gt; **[[c_performanceAnalyticsAndReporting|Platform Analytics]]** &gt; **Library** &gt; **Data Visualizations**, or open an in-line dashboard and select **Edit**.

2.  Select **Create data visualization**.

3.  Select the Dial \(\[Omitted image "inline-data-vis-dial.png"\] Alt text: Data visualization dial type\) visualization type.

4.  Configure the **Header and border**. Header and border options are the same for all data sources.

<table id="table_ly5_djk_c5b"><thead><tr><th>

Header and border fields

</th><th>

Description

</th></tr></thead><tbody><tr id="ac-dv-showborder"><td>

Show border

</td><td>

Option to display a line around the component.

</td></tr><tr id="ac-dv-showheader"><td>

Show header

</td><td>

The visualization header, including title and icons.

</td></tr><tr id="ac-dv-showheadersep"><td>

Show header separator

</td><td>

Option to display a line separating the header from the rest of the component.

</td></tr><tr id="ac-dv-charttitle"><td>

Chart title

</td><td>

Title of the visualization.

</td></tr><tr id="ac-dv-title-align"><td>

Title alignment

</td><td>

Choose Start to align the title with the start of line, End to align it with the end of the line, or Center for center alignment.

</td></tr><tr id="ac-dv-chartdesc"><td>

Description

</td><td>

A short overview about the visualization that the end user sees. Descriptions help users find the visualization.

</td></tr><tr id="ac-dv-wraptitle"><td>

Wrap title

</td><td>

Option to wrap long titles onto a second line. If false, displays an ellipsis to truncate long titles.

</td></tr><tr id="ac-dv-wraplabels"><td>

Wrap labels

</td><td>

Select to wrap long elements labels on the axis.

</td></tr><tr id="ac-dv-maxlabelsize"><td>

Max label size, px

</td><td>

Specify the maximum label size for element names on the axis. Default=100 px.

</td></tr><tr id="ac-dv-truncationtype"><td>

Line of truncation

</td><td>

Specify where to truncate long labels with an ellipsis. Options are 1, 2, and 3.

</td></tr><tr id="ac-dv-bare"><td>

Bare

</td><td>

Option to remove padding around data visualization to provide more compact positioning on the page. Only available when **Show border** is turned off.

</td></tr><tr id="ac-dv-showrefreshoption"><td>

Show refresh option

</td><td>

Option to show or hide the refresh option from data visualizations. If cache is enabled on a dashboard, the Refresh option is always hidden.

</td></tr><tr id="ac-dv-show-export-option"><td>

Show export options

</td><td>

Option to show or hide the visualization's export types.

</td></tr><tr><td>

Header background color

</td><td>

Specify the color behind the title of the visualization.

</td></tr><tr><td>

Title color

</td><td>

Specify the text color of the title. The default title color is black, but you can choose a color that contrasts better with the header background. Only available when **Header background color** is selected.

</td></tr></tbody>
</table>5.  Choose a data source.

    For general descriptions of the data sources, see [[data-sources-visualizations|Data sources for data visualizations]].

    -   Table \(available in the base system\). When you select a table, you can filter it by custom or preconfigured conditions. Custom conditions can include questions or Service Catalog variables.

        Configured [[c_ReportSources|report sources]] appear in the **Predefined conditions** list. For more information, see [Report sources](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/reporting/c_ReportSources.md).

        To help you create a custom filter, there is a preview list of records that would be included in the visualization. You can change which fields are shown as columns and the width of columns in the list actions.

        \[Omitted image "dv-preview-edit-cols.png"\] Alt text: Preview record list for table source data visualization with list actions shown.

    -   Indicator \(available in the base system\). You can filter the indicator scores by breakdowns and elements. [[automated-indicators|Automated indicators]] can be configured with selected breakdowns. [[formula-indicators|Formula indicators]] inherit their breakdowns from the parent indicators. Data snapshots [[c_CreatingBreakdowns|indicator breakdowns]] are configured in the indicator. In both cases, only those breakdowns are available when you configure a visualization based on those indicators.

        **Note:** Benchmark indicators are not supported.

        \[Omitted image "dv-ind-source-con-filter.png"\] Alt text: Conditional filter for indicator data source on data visualization.

        **Note:**

        You might have a multiple select \(is one of\) or dynamic \(is \(dynamic\)\) operator on the breakdown element filter. These operators require the indicator and breakdown to support them. For more information about the configurations that support these operators, see ["Is one of" and "Is \(Dynamic\)" operators on breakdown conditions in data visualizations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/performance-analytics/condition-operators-ind-bkdowns.md).

        Indicator types include Automated, Formula, and [[t_CreateAManualIndicator|Manual indicators]] as well as Automated and Formula Data Snapshots. The Indicator Preview shows an example of the visualization and a list of the indicator's properties.

        \[Omitted image "dv-indicator-source-preview.png"\] Alt text: Indicator preview example with visualization example and list of properties including source type, indicator source, indicator type, additional conditions and available breakdowns.

    -   [[user-exp-analytics-landing|Usage Insights]] \(available with the User Experience PAR Integration application, to users with a required role\). Choose one of up to three KPIs included with this application, depending on the visualization type. For more information, see [[uxa-data-sources|Usage Insights data sources for data visualizations]].
6.  Select the options for your data source.

    -   If your visualization represents table data, go to [[config-dv-dial-table-data|Table data options for dial visualizations]].
    -   If your visualization represents indicator data, go to [[config-dv-dial-ind-data|Indicator data options for dial data visualizations]].
    -   If your visualization represents Usage Insights data, go to [[config-dv-dial-uxa-data|Usage Insights data options for dial data visualizations]].
7.  Under **Presentation**, provide display and color information.

<table id="table_gvk_2mr_qtb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td class="sub-head" colspan="2">

Display settings

</td></tr><tr><td>

Value label size

</td><td>

Characters that represent dynamic sizes: small \(S\), medium \(M\), or large \(L\). The actual size of the type changes in proportion to the size of the chart.

</td></tr><tr><td>

Min value

</td><td>

Set the lowest value shown on the visualization. If not specified, zero is the default.

</td></tr><tr><td>

Max value

</td><td>

Set the highest value shown on the visualization.

</td></tr><tr><td>

Inner radius

</td><td>

Specify the ratio of the visualization's inner radius to the outer. Allowed values are 0.7–0.95.

</td></tr><tr><td>

Show data table

</td><td>

Shows a table with chart and graph data for easier screen reader access. Data includes the percentage of the total for each value, when appropriate.

</td></tr><tr><td class="sub-head" colspan="2">

Colors

</td></tr><tr><td>

Set color type

</td><td>

-   Default: A color or set of colors that come from the UX Theme that is applied to the instance. For more information, see .
-   Single color/Colors per metric: Select a single color in the **Set value color** field. Interacting with that field opens a selector where you can choose the color from either a set of icons or from a list. You can also search for a color. Entering a search value has the selector show you a list of colors filtered by that search value.

Alternatively, you can add a rule to define a dynamic color. For more information, see [[colors-dv|Create coloring rules for data visualizations]].

</td></tr></tbody>
</table>8.  Under **Chart interaction**, set what if anything happens when a viewer clicks a chart or a chart segment on the visualization.

<table id="table_qnp_d2d_b1c"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Allow chart interaction

</td><td>

Enable an event to occur when a user clicks in a visualization or one of its segments.

</td></tr><tr><td>

Action

</td><td>

Choose the event that occurs when a user clicks in a visualization or one of its segments. Choices depend on the visualization type and data source. Applies only when **Allow chart interaction** is on. For more information, see [[dv-chart-interactions|Chart interactions in a data visualization]].

-   **Go to data view** opens a list view, [[kpi-details|KPI Details]] page, or Usage Insights overview page relevant to the associated segment or visualization. For table data, a system property determines whether a Core UI list or a Platform Analytics list opens. For more information, see [[visualization-drilldown-in-config-ws|Data views for different data sources]].
-   **Go to URL** opens the specified URL, which can be on the instance or external. You have the option of specifying a page name to appear in the tooltip, for those visualizations with tooltips.
-   **Drill down to chart** \(Visualization Designer only\) Opens a different data visualization that is filtered by the selected data. You can add a drill-down visualization for each metric on the parent visualization.

**Note:** The last level of drill down in the [[par-workspace|Platform Analytics experience]] is always a Core UI list. Records do not open in Workspace embedded lists.

**Drill down to chart** supports only table data sources.

</td></tr></tbody>
</table>9.  Select **Save** to continue editing the visualization, or **Save and close** to return to the Analytics Overview main screen.


## What to do next

-   [[add-dv-new-db|Add a visualization to a dashboard from the Visualization Designer]]
-   [[share-dv-ac|Share a data visualization in the Visualization Designer]]
-   [[bookmark-dv-ac|Bookmark a visualization in the Visualization Designer]]

-   **[Table data options for dial visualizations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/config-dv-dial-table-data.md)**  
When you select a table data source for a dial visualization, the following Data configuration options are available.
-   **[Indicator data options for dial data visualizations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/config-dv-dial-ind-data.md)**  
When you select an indicator data source for a dial visualization, the following Data configuration options are available.
-   **[Usage Insights data options for dial data visualizations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/config-dv-dial-uxa-data.md)**  
When you select a Usage Insights data source for a dial visualization, the following Data configuration options are available.
-   **[[dv-example-dial|Dial visualization example]]**  
Dial visualizations show where a single value lies across a range from minimum to maximum expected values. Visually, a "needle" points to the value, and the dial is colored in for values up to the needle.

**Parent Topic:**[[creating-data-visualizations|Creating data visualizations]]

## Related

- [[platform-analytics-roles|Platform Analytics roles]]
- [[data-sources-visualizations|Data sources for data visualizations]]
- [[uxa-data-sources|Usage Insights data sources for data visualizations]]
- [[config-dv-dial-table-data|Table data options for dial visualizations]]
- [[config-dv-dial-ind-data|Indicator data options for dial data visualizations]]
- [[config-dv-dial-uxa-data|Usage Insights data options for dial data visualizations]]
- [[colors-dv|colors dv]]
- [[dv-chart-interactions|Chart interactions in a data visualization]]
- [[visualization-drilldown-in-config-ws|Data views for different data sources]]
- [[add-dv-new-db|Add a visualization to a dashboard from the Visualization Designer]]
- [[share-dv-ac|Share a data visualization in the Visualization Designer]]
- [[bookmark-dv-ac|Bookmark a visualization in the Visualization Designer]]
- [[dv-example-dial|Dial visualization example]]
- [[creating-data-visualizations|Creating data visualizations]]
- [[c_performanceAnalyticsAndReporting|Platform Analytics]]
- [[c_ReportSources|Report sources]]
- [[automated-indicators|Automated indicators]]
- [[formula-indicators|Formula indicators]]
- [[c_CreatingBreakdowns|Indicator breakdowns]]
- [[t_CreateAManualIndicator|Manual indicators]]
- [[user-exp-analytics-landing|Usage Insights]]
- [[kpi-details|KPI Details]]
- [[par-workspace|Platform Analytics experience]]
