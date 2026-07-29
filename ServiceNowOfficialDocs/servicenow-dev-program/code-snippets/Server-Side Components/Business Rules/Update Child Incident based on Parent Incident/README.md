---
title: "Update Child Incident based on Parent Incident"
aliases:
  - Update Child Incident based on Parent Incident
tags:
  - servicenow-dev-program
  - code-snippet
  - update-child-incident-based-on-parent-incident
  - business-rules
---

UseCase : Update child incident when parent incident is updated.

What do we want to achieve ? --> Real-time update of child incident based on parent incident update
What fields do we want to update? --> We can dynamically configure it out in my script I have created an array called 'monitorFields' which will hold all the fields which should get updated when it gets updated on the parent record (Inn the ideal case you can put these values on the system property)
How we will get all the changed values on the record? --> These values will be extracted as a part of the array 'changedFields' which will be derived by comparing the current and previous values for that field

Solution :
Create an On After Business rule on the incident table
Define the trigger condition based on the fields you wanna monitor. In our case monitored fields are as given: 'caller_id','state','impact','description' (You can add or remove as per your use case)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
