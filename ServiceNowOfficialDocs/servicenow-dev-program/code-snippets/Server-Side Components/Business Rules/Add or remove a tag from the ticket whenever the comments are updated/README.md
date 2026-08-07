---
title: "Add or remove a tag from the ticket whenever the comments are updated"
aliases:
  - Add or remove a tag from the ticket whenever the comments are updated
tags:
  - servicenow-dev-program
  - code-snippet
  - add-or-remove-a-tag-from-the-ticket-whenever-the-comments-are-updated
  - business-rules
---

The purpose of this code is to conditionally apply a specific label (label_entry) to an Incident when the person updating the record is the same as the caller. If the update is made by someone else, the label is removed.
This mechanism helps fulfillers quickly identify caller driven updates, enabling faster and more targeted responses. Additionally, it can be leveraged in reporting to track caller engagement.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add woknotes for 75 percent SLA/README|Add woknotes for 75 percent SLA]]
