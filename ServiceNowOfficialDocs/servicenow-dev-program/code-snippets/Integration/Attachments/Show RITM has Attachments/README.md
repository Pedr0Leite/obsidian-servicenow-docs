---
title: "Show RITM has Attachments"
aliases:
  - Show RITM has Attachments
tags:
  - servicenow-dev-program
  - code-snippet
  - show-ritm-has-attachments
  - attachments
---

This feature requires a "Display" Business rule on [sc_task] to pass true/false to the scratchpad and then an "onLoad" Client Script to display a message on the Catalog Task form if the RITM has attachments.

The result is a message on the Catalog Task form (below the RITM field) indicating when a RITM has attachments.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to Base64/README|Attachment to Base64]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to base64 in scope/README|Attachment to base64 in scope]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Base 64 to Attachment/README|Base 64 to Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/CSVParser/README|CSVParser]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Calculate attachment hash code/README|Calculate attachment hash code]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Convert KnowledgePage to PDF/README|Convert KnowledgePage to PDF]]
