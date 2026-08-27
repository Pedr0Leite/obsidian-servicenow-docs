---
title: "Hide Dependent Choice field if there no dependent choices"
aliases:
  - Hide Dependent Choice field if there no dependent choices
tags:
  - servicenow-dev-program
  - code-snippet
  - hide-dependent-choice-field-if-there-no-dependent-choices
  - client-scripts
---

Hide the dependent choice field when there are no available options for the selected parent choice.

For example, if a selected category on the incident form has no subcategories, then the subcategory field should be hidden.

The file NumberOfDependentChoices.js is a client callable script include file which has a method which returns number of dependent choices for a selected choice of parent choice field.

HideDepnedentField.js is client script which hides the dependent choice field(ex:subcategory field on incident form) if there are no active choices to show for a selected choices of it's dependent field (example: category on incident form)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
