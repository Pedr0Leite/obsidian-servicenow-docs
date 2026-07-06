---
title: "Remove HTML Tags from a String in a Flow"
aliases:
  - Remove HTML Tags from a String in a Flow
tags:
  - servicenow-dev-program
  - code-snippet
  - remove-html-tags-from-a-string-in-a-flow
  - flow-actions
---

# Remove HTML Tags from a String in a Flow

## Use Case / Requirement
Normalize HTML-rich content such as email-derived descriptions by stripping markup before continuing through a Flow Designer action.

## Solution
Create a reusable subflow action that accepts an HTML string, removes all tags with a regular expression, and returns clean text ready for downstream logic.

## Implementation
1. Create a new custom Flow action with an input named htmlValue and an output named plainString.
2. Paste the contents of removeHtmlTags.js into the script step of the action.
3. Publish the action and invoke it in your flows wherever you need to sanitize user-provided HTML.

## Notes
- The regular expression removes any markup tag; adjust the pattern if you need to preserve specific tags.
- The script trims leading and trailing whitespace generated after stripping tags.
- Combine with HTML entity decoding if your inputs contain encoded characters.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Add signature and update fields to a fillable PDF document/README|Add signature and update fields to a fillable PDF document]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Adhoc Assessment Generator Flow Action/README|Adhoc Assessment Generator Flow Action]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Assign Role/README|Assign Role]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Calculate Ticket Age/README|Calculate Ticket Age]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Check MID Server Availability/README|Check MID Server Availability]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Create Student Weekday Pickup Schedule/README|Create Student Weekday Pickup Schedule]]
