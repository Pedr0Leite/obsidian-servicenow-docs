---
title: "Updating a record in the sys_user table"
aliases:
  - Updating a record in the sys_user table
tags:
  - servicenow-dev-program
  - code-snippet
  - updating-a-record-in-the-sys-user-table
  - background-scripts
---

# update a record in sys_user table

If we use the command below to update a record, it can lead to a problem.

grUser.get('grUser.get('62826bf03710200044e0bfc8bcbe5df9')');

If the record is not found in the table, the script will create a new one. 

To make sure we are updating and not inserting, it is better to wrap up the get method with an If statement.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
