---
title: "Emergency Change Cannot be closed without AttachedIncident"
aliases:
  - Emergency Change Cannot be closed without AttachedIncident
tags:
  - servicenow-dev-program
  - code-snippet
  - emergency-change-cannot-be-closed-without-attachedincident
  - business-rules
---

1. This is a Before-Busines rule created on Change Request Table
2. I used GlideAggregate API.
3. only update is checked
4. conditions were Type is Emergency AND State changes to Close.
5. For emergency change Request, if there are no attached incident's to it then we don't let the user to move the state to close.
6. We use glideAggregate to glide Incident table and if we find any incident's user can move the state to close, But if there is no records then user action will be aborted.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
