---
title: "Auto-Assign Incident Based on Keywords, CI, and Department"
aliases:
  - Auto-Assign Incident Based on Keywords, CI, and Department
tags:
  - servicenow-dev-program
  - code-snippet
  - auto-assign-incident-based-on-keywords-ci-and-department
  - business-rules
---

Auto-Assign Incident Based on Keywords, CI, and Department  using Before Insert Business Rule

Automatically assigns incidents to the correct assignment group based on:

1.Keywords in the short description.

2.Configuration Item (CI) category.

3.Caller’s department.

Incidents should be routed automatically without manual intervention.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
