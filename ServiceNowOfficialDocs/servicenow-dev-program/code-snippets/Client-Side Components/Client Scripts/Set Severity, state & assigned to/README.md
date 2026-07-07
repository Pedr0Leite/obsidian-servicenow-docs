---
title: "Set Severity, state & assigned to"
aliases:
  - Set Severity, state & assigned to
tags:
  - servicenow-dev-program
  - code-snippet
  - set-severity-state--assigned-to
  - client-scripts
---

Use the script provided in script_include.js and script.js to set fetch multiple values from server to client side by passing an
object from server to the client side and setting values on your form. This can be used to pass multiple parameters from server to
client side.

Use Case:
Consider you have a reference field on your form referring to "sn_si_incident" and you need to set Severity, state and assigned to
onChange of the reference field.

Solution:
Create a client callable script include as mentioned in script_include.js and pass the required values to your client script.
Then use the onChange client script in script.js to set values on the form.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
