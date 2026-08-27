---
title: "Validate JSON Property"
aliases:
  - Validate JSON Property
tags:
  - servicenow-dev-program
  - code-snippet
  - validate-json-property
  - business-rules
---

Usage : Executes a business rule to verify if the JSON object saved in the property is a valid JSON. 

Steps for Creating the Business Rule:

Navigate to Business Rules:
  - Go to System Definition > Business Rules in ServiceNow.
  - Create a New Business Rule:
  - Click New to create a new business rule.

Fill in Basic Information:
 - Name: Provide a name like Validate JSON in Properties Table.
 - Table: Set the table to properties(sys_properties).
 - When to Run: Choose Before so that it validates before the record is saved.
 - Insert: Select True to run on insert.
 - Update: Select True to run on update (if needed).
   
Add Conditions (optional):
 - Set conditions if you only want to validate the JSON under certain circumstances. For instance, you can add conditions like

   value "starts with" { OR
   value "starts with" [ AND
   value "ends with" } OR
   value "ends with" ] OR

  to check specific fields.

Add the Script:

Under the Advanced tab, write the script to validate the JSON object. The script is mentioned in the jsonPropertyValidator.js file.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
