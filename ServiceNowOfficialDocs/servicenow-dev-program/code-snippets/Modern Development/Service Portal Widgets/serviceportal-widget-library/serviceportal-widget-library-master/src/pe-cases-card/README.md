---
title: "pe-cases-card"
aliases:
  - pe-cases-card
tags:
  - servicenow-dev-program
  - code-snippet
  - pe-cases-card
  - src
---

# Cases Card

## Description

A modern card widget that allows authorized users to visualize the details of active cases.

## Screenshot

![Cases Card](https://raw.githubusercontent.com/platform-experience/serviceportal-widget-library/master/src/pe-cases-card/images/pe-cases-card.png)

## Additional Information/Notes

Please install the Customer Service plugin before uploading the Update Set.

## Installation

Download and install update set **[pe-cases-card.u-update-set.xml](https://github.com/platform-experience/serviceportal-widget-library/blob/master/src/pe-cases-card/pe-cases-card.u-update-set.xml)**

After installation, the widget can be accessed via the `Service Portal > Widgets` section for use and customization.

- SN Product Documentation - ['Load a customization from a single XML file'](https://docs.servicenow.com/bundle/kingston-application-development/page/build/system-update-sets/task/t_SaveAnUpdateSetAsAnXMLFile.html)

### Widget Option Schema

| Option | Description | Default Value |
| :--- | :--- | :--- |
| `Table` | This is for changing the table that the default user is pulled from. | sn_customerservice_case |

## Platform Dependencies

### SN System Tables

> None

### UI Dependencies

> None

## CSS/SASS Variables

_CSS/SASS variables are given default values that can be overridden with theming or portal-level CSS._

> None

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-big-link-to/README|pe-big-link-to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-business-process-visualizer/README|pe-business-process-visualizer]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-card-scroll/README|pe-card-scroll]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-case-and-asset-map/README|pe-case-and-asset-map]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-collapsible-form/README|pe-collapsible-form]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-email-manage-attachment/README|pe-email-manage-attachment]]
