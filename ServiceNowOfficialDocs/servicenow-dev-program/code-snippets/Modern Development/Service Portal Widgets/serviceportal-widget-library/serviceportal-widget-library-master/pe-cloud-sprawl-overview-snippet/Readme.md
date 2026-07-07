---
title: "pe-cloud-sprawl-overview-snippet"
aliases:
  - pe-cloud-sprawl-overview-snippet
tags:
  - servicenow-dev-program
  - code-snippet
  - pe-cloud-sprawl-overview-snippet
  - serviceportal-widget-library-master
---

# Cloud Sprawl Overview Snippet

## Description

This snippet can be used to quickly obtain a card containing quick reference data and chart(s).

## Screenshots
![alt text](../images/pe-cloud-sprawl-overview-snippet.png "Tabs Selector - No tab selection")

## Additional Information/Notes
> None
---
## Installation
---
Download and install update set **[pe-cloud-sprawl-overview-snippet.u-update-set.xml](https://github.com/platform-experience/serviceportal-widget-library/blob/master/pe-cloud-sprawl-overview-snippet/pe-cloud-sprawl-overview-snippet.u-update-set.xml)** <br/><br/>
After installation, the widget can be accessed via the `Service Portal > Widgets` section for use and customization.<br/>
* SN Product Documentation - ['Load a customization from a single XML file'](https://docs.servicenow.com/bundle/kingston-application-development/page/build/system-update-sets/task/t_SaveAnUpdateSetAsAnXMLFile.html)

---
## Configuration
---
Widget Option Schema parameters:

**"Card Data"** JSON Data object

Example:

```javascript
    {
      "title": "Retail POS",
      "sluged": "retail_pos",
      "sub_title": "Marketing",
      "right_percent": "98%",
      "type": "aws",
      "thumbs": "up",
      "progress": "60%",
      "bottom_dollor": "$12,100",
      "right_attn_count": "3",
      "right_attn_color": "red"
    }
```
---
## Platform Dependencies
---
> None
---
## Sample Data and Data Structures
---
> See 'Configuration' above
---
## API Dependencies
---
<i>Dependencies are included and configured as part of the provided Update Set.</i>
> None
---
## CSS/SASS Variables
---
_CSS/SASS variables are given default values that can be overridden with theming or portal-level CSS._
> None

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/README|serviceportal-widget-library-master]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/docs/CONTRIBUTING|Widget Contribution]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/docs/help|help]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/pe-app-analytics/README|pe-app-analytics]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/pe-appointment-list/README|pe-appointment-list]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/pe-appointment-scheduler/README|pe-appointment-scheduler]]
