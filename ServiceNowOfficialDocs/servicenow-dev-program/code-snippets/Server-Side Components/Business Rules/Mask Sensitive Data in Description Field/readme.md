---
title: "Mask Sensitive Data in Description Field"
aliases:
  - Mask Sensitive Data in Description Field
tags:
  - servicenow-dev-program
  - code-snippet
  - mask-sensitive-data-in-description-field
  - business-rules
---

This script scans the description field of a record for patterns that resemble sensitive personal data and masks them to ensure privacy and compliance. It targets the following data types using regular expressions:

Credit Card Numbers: Detects both continuous digits (13–16 digits) and spaced/dashed formats (e.g., 1234-5678-9012-3456).
Social Security Numbers (SSNs): Matches the standard US format (XXX-XX-XXXX).
Phone Numbers: Identifies various formats including international and local styles.

If any of these patterns are found, the script replaces them with masked placeholders (e.g., ****-****-****-**** for credit cards) and updates the description field accordingly. It also logs messages to the system and displays info messages to notify users of the masking actions taken.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
