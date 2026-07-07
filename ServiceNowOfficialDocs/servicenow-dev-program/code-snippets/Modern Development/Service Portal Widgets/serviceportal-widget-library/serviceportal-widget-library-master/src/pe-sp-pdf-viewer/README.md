---
title: "pe-sp-pdf-viewer"
aliases:
  - pe-sp-pdf-viewer
tags:
  - servicenow-dev-program
  - code-snippet
  - pe-sp-pdf-viewer
  - src
---

# SP PDF Viewer

## Description

A simple and quick way to show a PDF within Service Portal.

## Screenshot

![SP PDF Viewer with a classic A4 PDF](https://raw.githubusercontent.com/platform-experience/serviceportal-widget-library/master/src/pe-sp-pdf-viewer/images/pe-sp-pdf-viewer-01.png)

![SP PDF Viewer ](https://raw.githubusercontent.com/platform-experience/serviceportal-widget-library/master/src/pe-sp-pdf-viewer/images/pe-sp-pdf-viewer-02.png)

## Additional Information/Notes

> None

## Installation

Download and install update set **[pe-sp-pdf-viewer.u-update-set.xml](https://github.com/platform-experience/serviceportal-widget-library/blob/master/src/pe-sp-pdf-viewer/pe-sp-pdf-viewer.u-update-set.xml)**

After installation, the widget can be accessed via the `Service Portal > Widgets` section for use and customization.

* SN Product Documentation - ['Load a customization from a single XML file'](https://docs.servicenow.com/bundle/newyork-application-development/page/build/system-update-sets/task/t_SaveAnUpdateSetAsAnXMLFile.html)

## Configuration

In input the component needs the attachment sys_id from sys_attachment table, and it can be used with a companion widget too which is showing a list of PDFs having in input a table, and/or the sys_id of the associated record where the attachments are dragged on. In this case, the PDFs are opened inside a modal.

## Platform Dependencies

### SN System Tables

sys_attachment

### UI Dependencies

PDF.js and Angular PDF Viewer

## CSS/SASS Variables

_CSS/SASS variables are given default values that can be overridden with theming or portal-level CSS._

Bootstrap variables

```sass
$link-color
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-big-link-to/README|pe-big-link-to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-business-process-visualizer/README|pe-business-process-visualizer]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-card-scroll/README|pe-card-scroll]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-case-and-asset-map/README|pe-case-and-asset-map]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-cases-card/README|pe-cases-card]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-collapsible-form/README|pe-collapsible-form]]
