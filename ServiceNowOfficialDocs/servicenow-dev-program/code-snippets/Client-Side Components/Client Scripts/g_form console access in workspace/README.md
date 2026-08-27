---
title: "g_form console access in workspace"
aliases:
  - g_form console access in workspace
tags:
  - servicenow-dev-program
  - code-snippet
  - g-form-console-access-in-workspace
  - client-scripts
---

# Access g_form instance inside Agent Workspace from DevTools Console
When developing forms in ServiceNow it can be useful to try stuff out directly in the DevTools Console.
In UI16 this was pretty straightforward because g_form was available globally, Agent Workspace makes this a little bit more complicated.
So this script provides access to the g_form object of the currently active tab in a Workspace.

Just copy the Script in the DevTools Console and run `var g_form = getGlideFormAW()` 
now you should be able to do stuff like `g_form.setValue("short_description", "Lorem ipsum")`

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
