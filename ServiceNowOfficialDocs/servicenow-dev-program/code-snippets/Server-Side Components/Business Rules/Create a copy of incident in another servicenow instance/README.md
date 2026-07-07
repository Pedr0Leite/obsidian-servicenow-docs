---
title: "Create a copy of incident in another servicenow instance"
aliases:
  - Create a copy of incident in another servicenow instance
tags:
  - servicenow-dev-program
  - code-snippet
  - create-a-copy-of-incident-in-another-servicenow-instance
  - business-rules
---

# Create incident copy

**Use case** : Whenever a new incident is created in servicenow production instance, a copy of that incident should be created in backup instance.

*info* : This method is to achieve the above use-case just with business rule and without creating a record in sys_rest_message table.

**Solution** : Create a `After` business rule on incident table with `insert` checkbox checked. Follow the script present in [script.js](script.js) 

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
