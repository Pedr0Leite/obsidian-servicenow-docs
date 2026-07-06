---
title: "pe-maps-ngmap"
aliases:
  - pe-maps-ngmap
tags:
  - servicenow-dev-program
  - code-snippet
  - pe-maps-ngmap
  - serviceportal-widget-library-master
---

# Google Maps with NgMap

## Description

This widget shows us how to use Google Maps through the library Ng-Map

## Screenshots
![](../images/pe-maps-ngmap.gif)

## Additional Information/Notes
> None
---
## Installation
---
Download and install update set **[pe-maps-ngmap.u-update-set.xml](https://github.com/platform-experience/serviceportal-widget-library/blob/master/pe-maps-ngmap/pe-maps-ngmap.u-update-set.xml)** <br/><br/>
After installation, the widget can be accessed via the `Service Portal > Widgets` section for use and customization.<br/>
* SN Product Documentation - ['Load a customization from a single XML file'](https://docs.servicenow.com/bundle/kingston-application-development/page/build/system-update-sets/task/t_SaveAnUpdateSetAsAnXMLFile.html)

---
## Configuration
---
### Widget Option Schema

| Option | Description | Default Value |
| :--- | :--- | :--- |
| `Origin` | Origin or location to search on Google Maps. |  |
| `Destination` | Destination if Google Maps provides the itinerary. |  |
| `Zoom` | Zoom level. | 14 |
| `Transit mode` | Transit mode (Walking, Bicycling, Driving, Transit) if Google Maps provides the itinerary. | Walking |
| `Header Visibility` | This parameter is used to override the visibility behaviour of the header. | True |

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
