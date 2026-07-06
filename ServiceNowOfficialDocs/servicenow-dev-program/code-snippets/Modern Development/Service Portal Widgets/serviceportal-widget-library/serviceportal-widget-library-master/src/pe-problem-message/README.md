---
title: "pe-problem-message"
aliases:
  - pe-problem-message
tags:
  - servicenow-dev-program
  - code-snippet
  - pe-problem-message
  - src
---

# Problem Message

## Description

This widget can be used to quickly craft a problem message with configuration.

## Screenshot

![Problem Message](https://raw.githubusercontent.com/platform-experience/serviceportal-widget-library/master/src/pe-problem-message/images/pe-problem-message.png)

## Additional Information/Notes

A sample problem record is created and displayed by default. To display another problem, set the problem number option.

## Installation

Download and install update set **[pe-problem-message.u-update-set.xml](https://github.com/platform-experience/serviceportal-widget-library/blob/master/src/pe-problem-message/pe-problem-message.u-update-set.xml)**

After installation, the widget can be accessed via the `Service Portal > Widgets` section for use and customization.

* SN Product Documentation - ['Load a customization from a single XML file'](https://docs.servicenow.com/bundle/kingston-application-development/page/build/system-update-sets/task/t_SaveAnUpdateSetAsAnXMLFile.html)

## Configuration

### Widget Option Schema

| Option | Description | Default Value |
| :--- | :--- | :--- |
| `Problem Number` | Sets the problem number which is used to display problem data. | SIR0001932 |

## Platform Dependencies

### SN System Tables

* problem
* sys_ui_message

### UI Dependencies

* PE Incident Module
* PE Incident Service

## CSS/SASS Variables

_CSS/SASS variables are given default values that can be overridden with theming or portal-level CSS._

```scss
$pe-status-color-danger: #6b0022 !default;
$pe-badge-danger: #a40034 !default;
$pe-background-header-danger: #dd0047 !default;
$pe-background-body-danger: #be003d !default;
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-big-link-to/README|pe-big-link-to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-business-process-visualizer/README|pe-business-process-visualizer]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-card-scroll/README|pe-card-scroll]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-case-and-asset-map/README|pe-case-and-asset-map]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-cases-card/README|pe-cases-card]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-collapsible-form/README|pe-collapsible-form]]
