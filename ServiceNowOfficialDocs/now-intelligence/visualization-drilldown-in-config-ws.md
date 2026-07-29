---
title: Data views for different data sources
description: When the chart interaction for a data visualization is set to Go to data, interacting with a data value on the visualization opens different pages depending on the data source.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/now-intelligence/visualization-drilldown-in-config-ws.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Chart interactions in a data visualization, Configure, Data visualizations, Platform Analytics experience, Platform Analytics]
tags:
  - now-intelligence
  - type-reference
---

# Data views for different data sources

When the chart interaction for a data visualization is set to Go to data, interacting with a data value on the visualization opens different pages depending on the data source.

**Note:** For an overview of the data sources that are available for data visualizations, see [[data-sources-visualizations|Data sources for data visualizations]].

## Table data visualizations

**Go to data** chart interactions from table data visualizations open an associated list of table records. When the system property **com.glide.par.pae.drilldown\_to\_core\_ui** is true, the list is a Core UI list. When it is false, the list is a [[c_performanceAnalyticsAndReporting|Platform Analytics]] list. If you are drilling down from a List, you open a table record either in Core UI or in Platform Analytics, again depending on **com.glide.par.pae.drilldown\_to\_core\_ui**. For more information, see [[data-visualization-properties|Data Visualization properties]].

**Note:** This system property does not apply to data visualizations in [[technical-dashboards|technical dashboards]] or other UIB pages, which use manually configured event handlers instead of chart interactions.

\[Omitted image "dv-drilldown-table.gif"\] Alt text: Drilling down from a single score visualization of table data to a list of table records.

## Indicator visualizations

**Go to data** chart interactions from indicator visualizations open the associated KPI Details page. For more information, see [[kpi-details|KPI Details]].

\[Omitted image "dv-drilldown-kpi.gif"\] Alt text: Drilling down from the bar visualization of an indicator to the KPI Details page for that indicator on that date.

## Usage Insights visualizations

**Go to data** chart interactions from [[user-exp-analytics-landing|Usage Insights]] visualizations opens an overview page for the individual application in the visualization. The overview opens on the Data Foundations view that matches the data visualization: event, session, user, or page data. For more information, see [Navigating the Usage Insights application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/usage-insights/user-exp-analytics-dashboard.md).

## Health Log Analytics visualizations

**Go to data** chart interactions from Health Log Analytics data visualizations open the log viewer. For more information, see .

**Note:** You cannot create or edit data visualizations for Health Log Analytics from the [[par-workspace|Platform Analytics experience]], but only from the UI Builder.

## MetricBase visualizations

**Go to data** chart interactions from MetricBase visualizations open the Metrics Explorer. For more information, see MetricBase.

**Important:** **Go to data** chart interactions for MetricBase require the Metric Explorer for Service Operations \(sn\_sow\_metric\_exp\) plugin.

**Parent Topic:**[[dv-chart-interactions|Chart interactions in a data visualization]]

## Related

- [[data-sources-visualizations|Data sources for data visualizations]]
- [[data-visualization-properties|Data Visualization properties]]
- [[kpi-details|KPI Details]]
- [[dv-chart-interactions|Chart interactions in a data visualization]]
- [[c_performanceAnalyticsAndReporting|Platform Analytics]]
- [[technical-dashboards|Technical dashboards]]
- [[user-exp-analytics-landing|Usage Insights]]
- [[par-workspace|Platform Analytics experience]]
