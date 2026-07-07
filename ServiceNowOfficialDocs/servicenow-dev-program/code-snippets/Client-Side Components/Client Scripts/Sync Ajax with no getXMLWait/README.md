---
title: "Sync Ajax with no getXMLWait"
aliases:
  - Sync Ajax with no getXMLWait
tags:
  - servicenow-dev-program
  - code-snippet
  - sync-ajax-with-no-getxmlwait
  - client-scripts
---

# onSubmit Ajax validation with no getXMLWait

Using getXMLWait() ensures the order of execution, but can cause the application to seem unresponsive, significantly degrading the user experience of any application that uses it.

Also, the getXMLWait method is not available in scoped applications.

This snippet simulates the behavior of the getXMLWait method.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
