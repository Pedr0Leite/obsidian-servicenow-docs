---
title: "Set Variables By Url"
aliases:
  - Set Variables By Url
tags:
  - servicenow-dev-program
  - code-snippet
  - set-variables-by-url
  - service-portal-widgets
---

## Use case
Sometimes you want to share a link to a catalog item on the portal and you want to pre-set some variables.  Like when you make documentation and you want to pre-categorize a ticket with information but you dont show all that.

So you build your link `https://{{instance}}/sp?id=sc_cat_item&sys_id={{itemSysID}}&description=I'cant%20access%20ServiceNow`

Which would set the description variable to "I can't access ServiceNow"

## Set up

1.  Create the widget
2.  Goto the https://{{instance}}/nav_to.do?uri=sp_page.do?sysparm_query=id=sc_cat_item
3.  Click the "Open in Designer" link at the bottom
4.  Add your widget anywhere as it has no html it will not render any elements.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/Accordion Widget/README|Accordion Widget]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/AngularJS Directives and Filters/README|AngularJS Directives and Filters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/Animated Notification Badge/README|Animated Notification Badge]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/ApplyCSSDynamically/README|ApplyCSSDynamically]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/Batman Animation/README|Batman Animation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/Calendar widget/README|Calendar widget]]
