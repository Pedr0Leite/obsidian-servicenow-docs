---
title: "Dynamically Switch Form View Based on Field Value"
aliases:
  - Dynamically Switch Form View Based on Field Value
tags:
  - servicenow-dev-program
  - code-snippet
  - dynamically-switch-form-view-based-on-field-value
  - client-scripts
---

## Dynamically Switch Form View Based on Field Value

This client script demonstrates how to **automatically switch form views** based on the value of a field.

**Use case:**  
For example, if the **Category** field is set to *Hardware*, the form view switches to **ess**.  
You can extend this by updating the mapping object to support additional fields and values (e.g., *Software → itil*, *Network → support*).

**Benefit:**  
Improves user experience by guiding users to the **most relevant form view**, ensuring the right fields are shown for the right scenario.

**Test:**  
- Change the **Category** field to *Hardware* → Form view should switch to **ess**.  
- Update mapping to add new conditions (e.g., *Software → itil*) and verify the view switches accordingly.

**How to Use:**  
1. **Modify the table name** in the `switchView` function to match your target table:
   ```javascript
   switchView("section", "<your_table_name>", targetView);
2. **Modify the view mapping**

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
