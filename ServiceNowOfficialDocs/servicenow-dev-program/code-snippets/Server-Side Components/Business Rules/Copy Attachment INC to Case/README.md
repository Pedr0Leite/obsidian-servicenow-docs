---
title: "Copy Attachment INC to Case"
aliases:
  - Copy Attachment INC to Case
tags:
  - servicenow-dev-program
  - code-snippet
  - copy-attachment-inc-to-case
  - business-rules
---

Copy attahements from Sc task  table to case table, using custom function to avaoid duplicate copies.

Attachment file will have one or more entries in the sys_attachment_doc table.
When we upload an attachment file to ServiceNow, a record is created in the Attachments table with some metadata, including the file name,
content type, and the size of the attached file.
the sys_attachment record essentially just contains metadata about the attachment. 
The actual binary data of the file is split into chunks, which are then saved into the Data field of the Attachment Documents table. 
The Attachment Documents table also contains a reference field (sys_attachment), which points to the parent record in the Attachments table. 

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
