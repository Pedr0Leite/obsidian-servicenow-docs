---
title: "Previous Approval Check"
aliases:
  - Previous Approval Check
tags:
  - servicenow-dev-program
  - code-snippet
  - previous-approval-check
  - business-rules
---

# Previous Approval Check
### Business rule to check for any approval requests by previous approvers and auto approve them.  If an approver had already approved a request, and is later asked to approve the same request again, usually in a different capacity, then the approval will be set as approved by the system automatically. 

Business rule settings:
- Table: sc_req_item
- Advanced: True (Checked)
- When: async
- Order: 1000
- Insert: False (Unchecked)
- Update: True (Checked)
- Delete: False
- Query: True
- Conditions: 
  - Approval is Requested
  - Approval history changes

![image](https://user-images.githubusercontent.com/25243029/136676161-0a842f97-0721-4f28-8b20-a83f52bed949.png)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
