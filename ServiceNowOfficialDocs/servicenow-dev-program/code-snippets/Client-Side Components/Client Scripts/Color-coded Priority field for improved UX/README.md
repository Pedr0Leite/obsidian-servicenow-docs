---
title: "Color-coded Priority field for improved UX"
aliases:
  - Color-coded Priority field for improved UX
tags:
  - servicenow-dev-program
  - code-snippet
  - color-coded-priority-field-for-improved-ux
  - client-scripts
---

# Field Color-Coding Based on Choice Values

## Purpose
Dynamically change the background color of any choice field on a form based on the selected backend value.

## How to Use
1. Create an OnChange client script on the desired choice field.
2. Replace `'your_field_name'` in the script with your actual field name.
3. Update the `colorMap` with relevant backend choice values and colors.
4. Save and test on the form.

## Key Points
- Works with any choice field
- Uses backend values of choices for mapping colors.

## Demo

<img width="1710" height="557" alt="image" src="https://github.com/user-attachments/assets/9fb9e68a-1ade-4eb5-81cc-c947c970bd6f" />

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
