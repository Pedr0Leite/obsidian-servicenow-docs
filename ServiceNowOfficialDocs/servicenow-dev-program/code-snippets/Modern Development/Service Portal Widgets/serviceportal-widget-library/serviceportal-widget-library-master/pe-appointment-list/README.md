---
title: "pe-appointment-list"
aliases:
  - pe-appointment-list
tags:
  - servicenow-dev-program
  - code-snippet
  - pe-appointment-list
  - serviceportal-widget-library-master
---

# PE Appointment List

## Description

This widget is used to display the appointments scheduled through widget **[PE Appointment Scheduling](https://github.com/platform-experience/serviceportal-widget-library/pe-appointment-scheduling)**.

## Screenshot

![PE appointment list](../images/pe-appointment-list.png)

## Additional Information/Notes


## Installation

Download and install update set in **[PE Appointment Scheduling](https://sc.service-now.com/snds?state=widget-detail&sys_id=612ff60adbbc6f403eb8f4bbaf96190a)**

After installation, **Appointment List** can be accessed via the `Service Portal > Widgets` section for use and customization.

* SN Product Documentation - ['Load a customization from a single XML file'](https://docs.servicenow.com/bundle/kingston-application-development/page/build/system-update-sets/task/t_SaveAnUpdateSetAsAnXMLFile.html)

## Configuration

### Widget Option Schema

| Option | Description |
| :--- | :--- |
| `Title` | Give the widget a Title that will appear above the widget. |
| `Task Appointment Definition` | Set the Task Appointment record to use from step 1. |
| `Show short description` | If you would like to collect Short Description when creating appointments, check the applicable box(s). |
| `Show location` | If you would like to collect Location info when creating appointments, check the applicable box(s). |



## Platform Dependencies

### SN System Tables

> None

## Sample Data and Data Structures

> See 'Configuration' above

## Dependencies

* [PE Appointment Scheduling](https://sc.service-now.com/snds?state=widget-detail&sys_id=612ff60adbbc6f403eb8f4bbaf96190a)


## CSS/SASS Variables

_CSS/SASS variables are given default values that can be overridden with theming or portal-level CSS._

**`$icon-color`**

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/README|serviceportal-widget-library-master]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/docs/CONTRIBUTING|Widget Contribution]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/docs/help|help]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/pe-app-analytics/README|pe-app-analytics]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/pe-appointment-scheduler/README|pe-appointment-scheduler]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/pe-appointment-scheduling/README|pe-appointment-scheduling]]
