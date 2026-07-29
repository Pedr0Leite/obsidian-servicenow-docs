---
title: "Use_case_Base64-Encode-Before-Save-And-Decode-on-Display"
aliases:
  - Use_case_Base64-Encode-Before-Save-And-Decode-on-Display
tags:
  - servicenow-dev-program
  - code-snippet
  - use-case-base64-encode-before-save-and-decode-on-display
  - business-rules
---

Base64 Encode/Decode Business Rule
Overview

This setup demonstrates how to store field data securely in Base64 format in the database, while still displaying it as human-readable text to end users in ServiceNow.

It uses two Business Rules:

Before Insert/Update Rule : Encodes plain text into Base64 before saving to the database.

Display Rule  : Decodes the Base64 value back into readable text when loading the record form.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
