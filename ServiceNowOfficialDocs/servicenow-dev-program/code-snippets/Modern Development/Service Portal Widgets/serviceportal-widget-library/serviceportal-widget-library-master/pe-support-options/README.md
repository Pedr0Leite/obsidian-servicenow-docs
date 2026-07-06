---
title: "pe-support-options"
aliases:
  - pe-support-options
tags:
  - servicenow-dev-program
  - code-snippet
  - pe-support-options
  - serviceportal-widget-library-master
---

# Support Options

## Description

This can be used to quickly craft a configurable widget with a list items fed from a catalog.

## Screenshot
![](../images/pe-support-options-1.png)

## Additional Information/Notes

Uses ServiceNow® [Service Catalog](https://docs.servicenow.com/bundle/istanbul-it-service-management/page/product/service-catalog-management/concept/c_ServiceCatalogManagement.html)

---
## Installation
---
Download and install update set **[pe-support-options.u-update-set.xml](https://github.com/platform-experience/serviceportal-widget-library/blob/master/pe-support-options/pe-support-options.u-update-set.xml)** <br/><br/>
After installation, the widget can be accessed via the `Service Portal > Widgets` section for use and customization.<br/>
* SN Product Documentation - ['Load a customization from a single XML file'](https://docs.servicenow.com/bundle/kingston-application-development/page/build/system-update-sets/task/t_SaveAnUpdateSetAsAnXMLFile.html)

---
## Configuration
---
### Widget Option Schema

| Option | Description | Default Value |
| :--- | :--- | :--- |
| `Title` | Widget Title. | Support Options |
| `Category` | Sets a category. | PE Support Options |
| `Fields` | Sets the field items to display for the catalog item, using a comma separated list. | sc_cat_item.name, sc_cat_item.icon, sc_cat_item.short_description |
| `Items` | Sets the catalog items for display. | Live Chat with Customer Support, Call Customer Support, How to reset your Okta cookie, Run Health Check |
| `Show Title` | Shows the title if checked (true). | true |
| `Show All Catalog Items` | Displays all catalog items for a category, if checked (true). | false |

---
## Platform Dependencies
---
### SN System Tables
* sc_cat_item
* sc_category
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

_CSS/SASS variables are given default values that can be overridden with theming or portal-level CSS._
> None

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/README|serviceportal-widget-library-master]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/docs/CONTRIBUTING|Widget Contribution]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/docs/help|help]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/pe-app-analytics/README|pe-app-analytics]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/pe-appointment-list/README|pe-appointment-list]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/pe-appointment-scheduler/README|pe-appointment-scheduler]]
