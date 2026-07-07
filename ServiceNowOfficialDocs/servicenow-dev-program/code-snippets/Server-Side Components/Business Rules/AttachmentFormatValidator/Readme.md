---
title: "AttachmentFormatValidator"
aliases:
  - AttachmentFormatValidator
tags:
  - servicenow-dev-program
  - code-snippet
  - attachmentformatvalidator
  - business-rules
---

The validator runs automatically on the sys_attachment table during record creation and checks each file extension against an allowed list defined in a system property.
If a file type is not allowed, the upload is blocked, the record creation is aborted, and a descriptive error is logged.
**Key Features:**
Server‑side enforcement (cannot be bypassed through APIs or imports).
Configurable allowed file extensions through a single system property.
Optional restriction to specific business tables.
Lightweight validation for secure instance operation.
**Functionality Summary**
Each attachment upload triggers the Business Rule before insert.
The file name and extension are extracted.
Allowed file extensions are read from the system property attachment.format.allowedExtensions.
The script checks whether the uploaded file complies with this configuration.
If disallowed, the upload is rejected and a clear error message appears in the system log or UI.

**Configuration**
System Property
attachment.format.allowedExtensions -	Defines which file types users are allowed to upload - sample values : pdf,docx,xlsx,png,jpg

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
