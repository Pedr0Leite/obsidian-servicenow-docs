---
title: "pe-push-notification"
aliases:
  - pe-push-notification
tags:
  - servicenow-dev-program
  - code-snippet
  - pe-push-notification
  - serviceportal-widget-library-master
---

# Push Notification

## Description

This widget allows you to emulate for demo purposes a mobile (iOs based) push notification alert.
The most important feature is the availability of settings for easily and quickly configuring it.

**NOTE:** this widget only works on mobile.

## Screenshots
<kbd><img src="../images/pe-push-notification.png" /></kbd>

---
## Installation
---
Download and install update set **[pe-push-notification.u-update-set.xml](https://github.com/platform-experience/serviceportal-widget-library/blob/master/pe-push-notification/pe-push-notification.u-update-set.xml)** <br/><br/>
After installation, the widget can be accessed via the `Service Portal > Widgets` section for use and customization.<br/>

* SN Product Documentation - ['Load a customization from a single XML file'](https://docs.servicenow.com/bundle/kingston-application-development/page/build/system-update-sets/task/t_SaveAnUpdateSetAsAnXMLFile.html)

---
## Configuration
---
Widget Option Schema parameters:

- Time shown in the home page / locked screen, and if not specified the default is the current time
- Date shown in the home page / locked screen, and if not specified the default is the current date
- Notification Title
- Notification Time
- Body Title
- Body Text
- Background Image
- Landing Page

---
## Platform Dependencies
---
> None

---
## Sample Data and Data Structures
---
No sample data provided.

---
## API Dependencies
---
<i>Dependencies are included and configured as part of the provided Update Set.</i>

---
## CSS/SASS Variables
---

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/README|serviceportal-widget-library-master]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/docs/CONTRIBUTING|Widget Contribution]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/docs/help|help]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/pe-app-analytics/README|pe-app-analytics]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/pe-appointment-list/README|pe-appointment-list]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/pe-appointment-scheduler/README|pe-appointment-scheduler]]
