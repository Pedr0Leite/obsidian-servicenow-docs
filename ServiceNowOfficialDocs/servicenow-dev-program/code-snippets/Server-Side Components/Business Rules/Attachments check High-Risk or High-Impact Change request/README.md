---
title: "Attachments check High-Risk or High-Impact Change request"
aliases:
  - Attachments check High-Risk or High-Impact Change request
tags:
  - servicenow-dev-program
  - code-snippet
  - attachments-check-high-risk-or-high-impact-change-request
  - business-rules
---

This Before Update business rule acts as a safeguard in a Change management process, 
ensuring that critical changes(those marked as high impact or high risk)
are properly documented before progressing to key implementation stages.

**BR Type**: 'Before', 'Update'
**Table**: Change Request (change_request)
**Condition**: 'State' 'changes to' 'Scheduled' OR 'State' 'changes to' 'Implement'

**What It Does**:
-The BR triggers before a change request record is updated, specifically when the state changes to either Scheduled or Implement.

-It checks whether the change is classified as high impact or high risk.

-If the change meets either of those criteria, it verifies that at least two attachments are present on the record. 
 These attachments are expected to be essential supporting documents like an Implementation Plan or Backout Procedure.

-If the required documentation is missing, the rule blocks the state change and displays an error message to the user, 
 preventing the change from moving forward until compliance is met.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
