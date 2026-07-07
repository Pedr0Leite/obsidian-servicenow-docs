---
title: "CopyAttachmentsFromApprovalToChange"
aliases:
  - CopyAttachmentsFromApprovalToChange
tags:
  - servicenow-dev-program
  - code-snippet
  - copyattachmentsfromapprovaltochange
  - business-rules
---

Copy attahements from Approval Record to corresponding change record.

This BR utilizes GlideSysAttachment API to copy all the attachments at a time. And there is no duplicate prevention enabled as Approval record is generally either approved or rejected one time.

To utilize this script, create an Advanced - After - Insert/Update Business Rule with conditions 
  state :: changes to :: Approved
  state :: changes to :: Rejected

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
