---
title: "Update Variable Choices"
aliases:
  - Update Variable Choices
tags:
  - servicenow-dev-program
  - code-snippet
  - update-variable-choices
  - server-side
---

Programatically update add a new choice for a service catalog variable and reorder all choices alphabetically. Can be helpful as part of a workflow where a fulfiller chooses logic to "update the list" variable, such as a small product or category list that may require ongoing updates as a result of fulfilling the request. Often unlisted choices are handled with an "Other" option and a text field to include the unlisted option. This script will take the value from the "Other" variable and add it to the choice list in the workflow.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CallScriptIncludeWithParameters/README|CallScriptIncludeWithParameters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CheckTableExtension/README|CheckTableExtension]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Admin Users/README|Create Admin Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Tiny Url with API's/README|Create Tiny Url with API's]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CreateUpdateCIThroughIRE/README|CreateUpdateCIThroughIRE]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Custom Relationship/README|Custom Relationship]]
