---
title: "Custom attachment variable"
aliases:
  - Custom attachment variable
tags:
  - servicenow-dev-program
  - code-snippet
  - custom-attachment-variable
  - service-portal-widgets
---

# Attachment variable widget

This widget lets you use the oob attachment picker from the oob catalog item widget as a custom type variable giving you more control over attachment behaviour, you can for example use ui policies to hide and show the attachment picker. 

## Usage example

Create new widget [sp_widget]
Copy template.html in the Body HTML template field
Copy controller.js in the Client controller field
Add custom type variable using newly created widget positioned as last variable
Set hide attachment for catalog item as true
Open cat item in portal and adjust widget as needed

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/Accordion Widget/README|Accordion Widget]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/AngularJS Directives and Filters/README|AngularJS Directives and Filters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/Animated Notification Badge/README|Animated Notification Badge]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/ApplyCSSDynamically/README|ApplyCSSDynamically]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/Batman Animation/README|Batman Animation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/Calendar widget/README|Calendar widget]]
