---
title: "After-BR to generate approvals for catalog tasks"
aliases:
  - After-BR to generate approvals for catalog tasks
tags:
  - servicenow-dev-program
  - code-snippet
  - after-br-to-generate-approvals-for-catalog-tasks
  - business-rules
---

This code snippet will help you to generate approvals for catalog tasks via scripting. You just need to create an after insert BR and put this script there.
This script can be used in a workflow run script as well and you can modify the script a little bit and use it for other tables as well. 

Fun fact: When you are playing with Document Id type field. You need to keep a field as dependent for the document ID like we have 'Source table' for 'Approving' field to put the correct table name there and with the help of that you can easily set the document ID field.

For e.g. dependent field name is u_table_name, so your script can be something like below:

- obj.u_table_name = 'Name of the table for your document ID type field';
- obj.u_document_id = 'Sys_id of the correct record from above table';
- obj.update();

where 'obj' is an object of the record you are referring to.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
