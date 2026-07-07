---
title: "pe-foexp-401k"
aliases:
  - pe-foexp-401k
tags:
  - servicenow-dev-program
  - code-snippet
  - pe-foexp-401k
  - serviceportal-widget-library-master
---

# FOEXP 401k Enrollment

## Description

This widget allows users to register their 401k contribution level. Simply clicking the buttons will register their contribution level.

## Screenshots
![FOEXP 401k Enrollment](../images/pe-foexp-401k.png "FOEXP 401k Enrollment")

## Additional Information/Notes

Update set installs the table '401k Enrollments' (u_401k_enrollments) with sample data.

---
## Installation
---
Download and install update set **[pe-foexp-401k-update-set.u-update-set.xml](https://github.com/platform-experience/serviceportal-widget-library/blob/master/pe-foexp-401k/pe-foexp-401k-update-set.u-update-set.xml)** <br/><br/>
After installation, the widget can be accessed via the `Service Portal > Widgets` section for use and customization.<br/>
* SN Product Documentation - ['Load a customization from a single XML file'](https://docs.servicenow.com/bundle/kingston-application-development/page/build/system-update-sets/task/t_SaveAnUpdateSetAsAnXMLFile.html)

---
## Configuration
---
Widget Option Schema parameters:
> None
---
## Platform Dependencies
---
> None
---
## Sample Data and Data Structures
---
Sample data is provided by the update set installed table '401k Enrollments' (u_401k_enrollments)

---
## API Dependencies
---
<i>Dependencies are included and configured as part of the provided Update Set.</i>
> None
---
## CSS/SASS Variables
---
_CSS/SASS variables are given default values that can be overridden with theming or portal-level CSS._

```scss
$button-bg: #ffffff !default;
$button: #1aa5be !default;
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/README|serviceportal-widget-library-master]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/docs/CONTRIBUTING|Widget Contribution]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/docs/help|help]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/pe-app-analytics/README|pe-app-analytics]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/pe-appointment-list/README|pe-appointment-list]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/pe-appointment-scheduler/README|pe-appointment-scheduler]]
