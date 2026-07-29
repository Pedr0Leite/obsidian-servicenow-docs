---
title: "ExportAttachmentsToMidServer"
aliases:
  - ExportAttachmentsToMidServer
tags:
  - servicenow-dev-program
  - code-snippet
  - exportattachmentstomidserver
  - attachments
---

The snippet can be used to export all attachments within any record in ServiceNow to the mid server. You could specify a relative file path within the server's agent folder and it will copy them into it.

Sample Usage

exportAttachmentsToMid("66a4daff2f9ff810ba1b52492799b6f1", "\\Incident\\INC00293930", "Mid Server 01");

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to Base64/README|Attachment to Base64]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to base64 in scope/README|Attachment to base64 in scope]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Base 64 to Attachment/README|Base 64 to Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/CSVParser/README|CSVParser]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Calculate attachment hash code/README|Calculate attachment hash code]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Convert KnowledgePage to PDF/README|Convert KnowledgePage to PDF]]
