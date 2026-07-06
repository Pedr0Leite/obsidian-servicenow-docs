---
title: "Delete Attachments - Closed Approvals"
aliases:
  - Delete Attachments - Closed Approvals
tags:
  - servicenow-dev-program
  - code-snippet
  - delete-attachments---closed-approvals
  - background-scripts
---

Many organizations still prefer copying over the attachments from RITM or any ticket type that has approval required to its corresponding approvals by using GlideSysAttachment.copy() 
This ideally makes sense till the time approval is needed however, when approvals are actioned (approved/rejected) there is no need for attachments to stay on the approval record till eternity (it will be stored at its ticket level). Use this script as a scheduled script to remove attachments from closed (approved/rejected) approval records and help consume less storage.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
