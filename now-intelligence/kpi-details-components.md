---
title: Examining indicators with KPI Details
description: The KPI Details feature enables you to delve into the information behind your key performance indicators. Apply forecasts, trends, targets, and thresholds. Filter by breakdown element or apply time series aggregations.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/now-intelligence/kpi-details-components.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [KPI Details, Platform Analytics experience, Platform Analytics]
---

# Examining indicators with KPI Details

The KPI Details feature enables you to delve into the information behind your key performance indicators. Apply forecasts, trends, targets, and thresholds. Filter by breakdown element or apply time series aggregations.

KPI Details has several sections:\[Omitted image "kpi-details-whole.png"\] Alt text: KPI Details page showing the header, visualization, and sidebar sections

## Header

The header contains the name of the indicator, a date selector \(default: last data collection\), and the score on that date. Data snapshots indicators are identified with a badge. The absolute and percentage differences between that score and the previously collected score are shown. If the indicator has Maximize or Minimize set, the color of the score and the score change direction arrow indicates whether the score is improving or getting worse.

The date selector uses whatever calendar the indicator uses.

If [[real-time-scores|real-time scores]] are enabled for the indicator, select in the header whether to view them, using the clock icon \[Omitted image "kpi-details-real-time-icon-off.png"\] Alt text: Real-time scores icon turned off. This icon is transparent when real-time scores are disabled and solid when they are enabled \[Omitted image "real-time-update-icon.png"\] Alt text: Real time icon when real time is activated. For more information, see [Real-time scores](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/performance-analytics/real-time-scores.md).

If a target is set for the selected date, the header shows the target value and the gap between the score on that date and the target, in both absolute and percentage terms. If both target and forecast are shown, as set in [[chart-options|Chart options in KPI Details]], a badge shows whether the indicator is on track or off track to meet the target by the review date.

**Warning:** Real-time scores can differ per viewer and differ from collected scores. Real-time scores are taken directly from the relevant facts tables. Therefore, the [[access-control|Access Control]] Lists \(ACL\) of those facts tables determine the real-time scores that each logged-in user sees.

## Indicator chart

The indicator chart shows:

-   The **Chart options** menu. For more information, see [Chart options in KPI Details](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/chart-options.md).
-   A date picker to choose the date range of the information in the chart. For Industrial Connected Workforce \(ICW\) indicators, this date range can be in shifts or production days.
-   A time series graphic representation of the indicator over time. Click on a point in the graph to see the details for that date.
-   A time series aggregation selector. For more information, see [[select-time-series-aggregation|Select time aggregation in KPI Details]]. \(Does not apply to Industrial Connected Workforce indicators.\)
-   The **Show records** toggle, which shows you the records associated with the indicator score on the selected date. For more information, see [[show-compare-edit-records|Show, compare, create, and edit records in KPI Details]].

**Warning:** In some cases, when you collect second-level breakdowns, the score and the number of records do not agree. When these values do not agree, the score is correct. For more details and an example, see [KB0748969](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748969).

**Important:** Records are not listed for the "Unmatched" breakdown element when you select it in the filter.

## Sidebar

Use the sidebar controls to:

-   Filter by breakdown and element \[Omitted image "icon-filter.png"\] Alt text: Filter icon.
-   [[view-kpi-signals|View KPI Signals]] for the indicator \(\[Omitted image "kpi-details-open-signals.png"\] Alt text: Icon in KPI Details sidebar to open KPI Signals, showing there is a new signal\). See [[process-behavior-charts-for-kpis|KPI Signals]].
-   Set an indicator target or threshold\(\[Omitted image "target-icon.png"\] Alt text: Target icon\). See [[kpi-details-targets|Indicator targets and thresholds in KPI Details]].

## Process analysis

Besides these three sections, a **Run process analysis** button lets you launch a [[process-mining|Process Mining]] analysis on the indicator. For more information, see [Process Mining](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/process-mining/process-mining.md).

## More actions menu

You also have a More actions menu \[Omitted image "icon-menu.png"\] Alt text: More actions menu icon that gives you access to the indicator record and scoresheet. For more information, see [[access-indicator-record-scoresheet|Access indicator record or scoresheet from KPI Details]].

-   **[[view-formula-components|View contributing indicators to a formula in KPI Details]]**  
If you’re viewing a formula indicator in KPI Details, you can list the contributing indicators to that formula. Depending on the KPI Details configuration, you can open the contributing indicators in KPI Details.
-   **[Show, compare, create, and edit records in KPI Details](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/show-compare-edit-records.md)**  
You can view the list of records underlying an indicator score. You can create a record, edit individual records, or compare records. You can also export the list of records.
-   **[Chart options in KPI Details](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/chart-options.md)**  
The KPI Details **Chart options** menu enables you to show, hide, or change aspects of an indicator visualization. Selected chart options persist per user for each indicator. Chart options are divided into analysis, time series, and chart type options.
-   **[Select time aggregation in KPI Details](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/select-time-series-aggregation.md)**  
You can aggregate changes in indicators into discrete time intervals. A time aggregation consists of an AVG or SUM function combined with a time series, such as By quarter.
-   **[[configure-trend-ds-indicator|Configure trend for a native Data snapshots indicator in KPI Details]]**  
Select a calendar and period by which to aggregate scores on the chart. You can also choose whether to include scores from incomplete periods.
-   **[[configure-display-properties-ds-indicator|Configure display properties for a Data snapshots indicator]]**  
Change display properties for viewing a specific native Data snapshots indicator in KPI Details.
-   **[[apply-brkdowns-element-kpi-details|Filter indicator scores by breakdown elements in KPI Details]]**  
Apply breakdowns and elements to filter classic and Data snapshots-enabled indicators. The filter controls are in the KPI Details sidebar.
-   **[[filter-data-snapshots-indicator-scores|Filter native Data snapshots indicator scores in KPI Details]]**  
Filter native Data snapshots indicators by the fields on their Data snapshots sources. For fields that refer to tables with report hierarchies, roll up scores to the parent field.
-   **[Access indicator record or scoresheet from KPI Details](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/access-indicator-record-scoresheet.md)**  
In KPI Details, the More actions menu lets you open the record or the scoresheet of the indicator you are viewing.

**Parent Topic:**[[kpi-details|KPI Details]]

**Related topics**  


[Exploring KPI Details]()

[Indicator targets and thresholds in KPI Details]()

[KPI Details reference]()

[Performance Analytics \(Indicator data sources\)](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown)

## Related

- [[chart-options|Chart options in KPI Details]]
- [[select-time-series-aggregation|Select time aggregation in KPI Details]]
- [[show-compare-edit-records|Show, compare, create, and edit records in KPI Details]]
- [[process-behavior-charts-for-kpis|KPI Signals]]
- [[kpi-details-targets|Indicator targets and thresholds in KPI Details]]
- [[access-indicator-record-scoresheet|Access indicator record or scoresheet from KPI Details]]
- [[view-formula-components|View contributing indicators to a formula in KPI Details]]
- [[configure-trend-ds-indicator|Configure trend for a native Data snapshots indicator in KPI Details]]
- [[configure-display-properties-ds-indicator|Configure display properties for a Data snapshots indicator]]
- [[apply-brkdowns-element-kpi-details|Filter indicator scores by breakdown elements in KPI Details]]
- [[filter-data-snapshots-indicator-scores|Filter native Data snapshots indicator scores in KPI Details]]
- [[kpi-details|KPI Details]]
- [[real-time-scores|Real-time scores]]
- [[access-control|Access control]]
- [[view-kpi-signals|View KPI Signals]]
- [[process-mining|Process Mining]]
