---
title: "Smart Attachment Size Limiter"
aliases:
  - Smart Attachment Size Limiter
tags:
  - servicenow-dev-program
  - code-snippet
  - smart-attachment-size-limiter
  - business-rules
---

Smart Attachment Size Limiter
This Business Rule limits attachment sizes uploaded to ServiceNow records by enforcing a maximum size configured via the system property com.glide.attachment.max_size (in bytes). If the attachment exceeds the configured limit, the upload is blocked with an error message shown to the user. You can create or modify this system property to change the max size and update the property name in the script accordingly.

Scoped Application Note:
If deploying in a scoped application, configure Cross-Scope Access under System Applications > Application Cross-Scope Access to allow your app permission to access the sys_attachment table and related resources, avoiding security restrictions.

This approach keeps your instance performant by managing attachment size transparently without hardcoded limits.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
