---
title: "Validate Email on Import"
aliases:
  - Validate Email on Import
tags:
  - servicenow-dev-program
  - code-snippet
  - validate-email-on-import
  - business-rules
---

This business rule can be implemented on any table which is having email type field and we want to validate the email
when we are using the import feature from the list view to upload some data via spreadsheet.

This business rule can be used to validate the email address when 
we are using the OOB 'Import' feature from the list context menu to upload some data from a spreadsheet into the table.

Tables where it could be implemented is the [sys_user] users table's > email field, and [sys_user_group] > 'group email' field.

Note: [u_email_address] this field is just an example, this needs to be replaced by the email field in which this script will run.
For users table it will be 'email' field.


Business Rule will have the below configuration:
When to run: before insert + update
Filter condition: Email[u_email_address] is not empty

In the advance > script section paste the code, it will run when we will import any spreadsheet 
in the table(record will insert/update)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
