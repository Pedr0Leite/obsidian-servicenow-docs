---
title: "Custom Greetings in portal homepage"
aliases:
  - Custom Greetings in portal homepage
tags:
  - servicenow-dev-program
  - code-snippet
  - custom-greetings-in-portal-homepage
  - service-portal-widgets
---

This code snippet will help you to provide customize greetings to end user when they login to the portal. And the time will be reflected as browser's time zone. By default javascript uses browser's time zone and which is further converted into hours as per the method I used in my clint script code. Below steps needs to be performed to achive this.
1. Clone Homepage-search widget of portal.
2. Update the client script of the cloned widget as per the code prvided in homepage-search-clint.js.
3. Update the HTML as per homepage-search.html.
4. Replace the Homepage-search widget with Custom Homepage-search widget from portal home page by going to Page in designer.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/Accordion Widget/README|Accordion Widget]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/AngularJS Directives and Filters/README|AngularJS Directives and Filters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/Animated Notification Badge/README|Animated Notification Badge]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/ApplyCSSDynamically/README|ApplyCSSDynamically]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/Batman Animation/README|Batman Animation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/Calendar widget/README|Calendar widget]]
