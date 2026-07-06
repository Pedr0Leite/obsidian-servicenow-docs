---
title: "pe-gantt-chart"
aliases:
  - pe-gantt-chart
tags:
  - servicenow-dev-program
  - code-snippet
  - pe-gantt-chart
  - src
---

# Gantt Chart

## Description

This is used to create a simple Gantt Chart.

## Screenshots

![Gantt Chart](https://raw.githubusercontent.com/platform-experience/serviceportal-widget-library/master/src/pe-gantt-chart/images/pe-gantt-chart.png)

![Gantt Chart Options](https://raw.githubusercontent.com/platform-experience/serviceportal-widget-library/master/src/pe-gantt-chart/images/gantt-chart-options.png)

## Additional Information/Notes

> None

## Installation

Download and install update set **[pe-gantt-chart.u-update-set.xml](https://github.com/platform-experience/serviceportal-widget-library/blob/master/src/pe-gantt-chart/pe-gantt-chart.u-update-set.xml)**

After installation, the widget can be accessed via the `Service Portal > Widgets` section for use and customization.

- SN Product Documentation - ['Load a customization from a single XML file'](https://docs.servicenow.com/bundle/kingston-application-development/page/build/system-update-sets/task/t_SaveAnUpdateSetAsAnXMLFile.html)

## Configuration

Widget Options Schema:

| Option    | Description       | Default Value |
| :-------- | :---------------- | :------------ |
| `Project` | List of projects. |               |

## API Dependencies

_Dependencies are included and configured as part of the provided Update Set._

- DHTMLX Gantt Chart API (v 6.1 - Recommended) w/Export and No Data plug-ins
  <br/>Latest version(s) available from [DHTMLX Gantt](https://docs.dhtmlx.com/gantt/)

## CSS/SASS Variables

_CSS/SASS variables are given default values that can be overridden with theming or portal-level CSS._

> None

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-big-link-to/README|pe-big-link-to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-business-process-visualizer/README|pe-business-process-visualizer]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-card-scroll/README|pe-card-scroll]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-case-and-asset-map/README|pe-case-and-asset-map]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-cases-card/README|pe-cases-card]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-collapsible-form/README|pe-collapsible-form]]
