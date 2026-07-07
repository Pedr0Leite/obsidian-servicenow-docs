---
title: "Enforce Percentage"
aliases:
  - Enforce Percentage
tags:
  - servicenow-dev-program
  - code-snippet
  - enforce-percentage
  - business-rules
---

# Objective
A Business Entity has multiple owners who are individuals. 
Each indivisual owns a percentage of the business.
This business rule insures that the total of all ownership percentage does not exceed 100%.

# Challenge
The aggregate function calculates the sum by using the values that are stored in the database. However we need to calculate the sum using the values that are in the database for all owners and use the value that the user is trying to update for the owner that is currently being udpated.

# Solution
1. Use the sum function from the [Calculator Script Include](https://github.com/ServiceNowDevProgram/code-snippets/tree/main/Script%20Includes/Calculator).
2. Calculate the sum using the values in the database
3. Substract the previous value and then add the current value to calculate what the future sum would be

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
