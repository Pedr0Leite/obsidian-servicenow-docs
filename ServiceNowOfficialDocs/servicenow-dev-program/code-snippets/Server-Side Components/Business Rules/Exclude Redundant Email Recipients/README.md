---
title: "Exclude Redundant Email Recipients"
aliases:
  - Exclude Redundant Email Recipients
tags:
  - servicenow-dev-program
  - code-snippet
  - exclude-redundant-email-recipients
  - business-rules
---

# Exclude Redundant Email Recipients
### This business rule is designed to intercept new comment notifications and modify the recipients to mitigate redundant notifications in response to email replies that users were previously included on as a direct or copied recipient.

Initial Settings (modify as needed for your purposes)
- Table: sys_email
- Advanced: true
- When: before
- Insert: true
- Update: true
- Conditions:
  - Type > changes to > send-ready
  - Subject > contains > comment

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
