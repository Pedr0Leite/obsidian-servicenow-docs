---
title: "Attachment Variable from Activity Stream to Clip Icon"
aliases:
  - Attachment Variable from Activity Stream to Clip Icon
tags:
  - servicenow-dev-program
  - code-snippet
  - attachment-variable-from-activity-stream-to-clip-icon
  - business-rules
---

When attaching a file via an attachment type variable, on the target record the attachment appears in the Activity Stream instead of at the top associated with the paper clip icon, where one typically looks for / notices attachments.  This Business Rule will convert the entry in the sys_attachment table so that the attachment added via an attachment type variable appears at the top of the record, associated with the paper clip icon.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
