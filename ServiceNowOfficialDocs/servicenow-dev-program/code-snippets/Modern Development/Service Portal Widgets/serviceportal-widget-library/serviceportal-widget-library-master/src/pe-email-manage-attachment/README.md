---
title: "pe-email-manage-attachment"
aliases:
  - pe-email-manage-attachment
tags:
  - servicenow-dev-program
  - code-snippet
  - pe-email-manage-attachment
  - src
---

# Email Manage Attachment

## Description

A simple widget to allow the management of attachments of a record and being able to email them from ServicePortal. The Update Set also contains a UI action that will copy all the attachments from a record and put them to an email attachment.

## Screenshot

![Email Manage Attachment](https://raw.githubusercontent.com/platform-experience/serviceportal-widget-library/master/src/pe-email-manage-attachment/images/pe-email-manage-attachment.png)

## Additional Information/Notes

> None

## Installation

Download and install update set **[pe-email-manage-attachment.u-update-set.xml](https://github.com/platform-experience/serviceportal-widget-library/blob/master/src/pe-email-manage-attachment/pe-email-manage-attachment.u-update-set.xml)**

After installation, the widget can be accessed via the `Service Portal > Widgets` section for use and customization.

- SN Product Documentation - ['Load a customization from a single XML file'](https://docs.servicenow.com/bundle/kingston-application-development/page/build/system-update-sets/task/t_SaveAnUpdateSetAsAnXMLFile.html)

## Configuration

Install the Update Set and navigate to _Service Portal > Service Portal Configuration_ and select page editor. Find the _Ticket Form_ page in the reference picker and click on it. Now, select the _Edit Ticket Form (ticket) page in Designer_ link. Find the _Manage Attachments_ widget and drag it above the baseline _Ticket Attachments_ widget in the layout. Go to an open ticket in Service Portal and see the new widget. Add an attachment, then select the checkbox next to the attachments you would like to email outside of the platform if you wish to do so.

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
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-cases-card/README|pe-cases-card]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-collapsible-form/README|pe-collapsible-form]]
