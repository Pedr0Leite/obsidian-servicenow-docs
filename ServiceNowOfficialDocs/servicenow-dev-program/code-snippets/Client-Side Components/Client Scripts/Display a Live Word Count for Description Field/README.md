---
title: "Display a Live Word Count for Description Field"
aliases:
  - Display a Live Word Count for Description Field
tags:
  - servicenow-dev-program
  - code-snippet
  - display-a-live-word-count-for-description-field
  - client-scripts
---

The script enhances a form field (specifically the description field) by:
-Adding a live word counter below the field.
-Visually warning the user if the word count exceeds 150 words.

This client-side script, intended for use in a ServiceNow form (e.g., catalog item or incident form), dynamically appends a custom `<div>` element below the `description` field to display a real-time word count. It leverages the `g_form.getControl()` API to access the field's DOM element and attaches an `input` event listener to monitor user input. The script calculates the word count by splitting the input text using a regular expression (`\s+`) and updates the counter accordingly. It applies conditional styling to the counter (`green` if ≤150 words, `red` if >150), providing immediate visual feedback to the user to enforce input constraints.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
