---
title: "Remove Option from Choice List"
aliases:
  - Remove Option from Choice List
tags:
  - servicenow-dev-program
  - code-snippet
  - remove-option-from-choice-list
  - client-scripts
---

**Purpose:**
This onChange function automatically reacts when the "Category" field is changed. If the new category selected is "inquiry," the function removes the options for "Impact" and "Urgency" that have a value of 1.
Whenever a user selects a new category, the script checks if it’s set to "inquiry." If so, it removes the specified options for "Impact" and "Urgency".
**How to Use This Function**
You can use this Onchange client script on any form and maanage your field choice options.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
