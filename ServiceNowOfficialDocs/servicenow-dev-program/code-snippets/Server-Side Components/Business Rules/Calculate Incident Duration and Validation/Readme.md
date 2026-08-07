---
title: "Calculate Incident Duration and Validation"
aliases:
  - Calculate Incident Duration and Validation
tags:
  - servicenow-dev-program
  - code-snippet
  - calculate-incident-duration-and-validation
  - business-rules
---

Calculate Incident Duration and Validation.

Script Type : Business Rule Trigger: before update Table: incident Condition: Resolved Changes or Opened Changes

Goal : To calculate the duration of a particular record and how much time has been spent on a particular ticket.

Walk through of code :
So when the Resolved Changes or Opened Changes in a particular record to calculate the duration will this Business rule will pull those values
And then check whether the Opened Data/Time is lesser than the Resolved Date/Time the will calculate the duration 
Else it will throw the Error Message and then Abort that action and won't save the record and will clear the values.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
