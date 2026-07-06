---
title: "Fetching reference field value from higher-level parents"
aliases:
  - Fetching reference field value from higher-level parents
tags:
  - servicenow-dev-program
  - code-snippet
  - fetching-reference-field-value-from-higher-level-parents
  - business-rules
---

This is a "**before insert/update**" Business Rule
We are fetching a reference field value from higher-level parents in hierarchy 
when there is a field containing the parent record in the children and 
our use-case reference field is present in all the tables in hierarchy

In the code, we are referring to "reference field name we want to populate" as "_r1_"
In the code, we are referring to "reference field containing parent record" as "_parent_"

The "**JSUtil.nil**" is being used to check for empty/null value for the field.


Through the code we are checking the empty value of the use-case reference field and dot walking to parents and fetching the value from them if it exists

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
