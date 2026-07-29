---
title: "Field Completion Counter"
aliases:
  - Field Completion Counter
tags:
  - servicenow-dev-program
  - code-snippet
  - field-completion-counter
  - client-scripts
---

# Field Completion Counter

## Use Case / Requirement
Display a simple message showing how many fields are completed vs total fields on a form. This helps users track their progress while filling out forms.

## Solution
A simple onLoad client script that:
- Counts filled vs empty fields
- Shows completion status in an info message
- Updates when fields are modified

## Implementation
Add this as an **onLoad** client script on any form.

## Notes
- Excludes system fields and read-only fields
- Updates in real-time as users fill fields
- Simple and lightweight solution

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
