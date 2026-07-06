---
title: "Remove element from list field"
aliases:
  - Remove element from list field
tags:
  - servicenow-dev-program
  - code-snippet
  - remove-element-from-list-field
  - background-scripts
---

This script can be used to remove a specific element from a list field across multiple records in a table that match a query condition.

It requires 3 variables to be set:
- table {string}: the name of the table to run on, e.g. 'kb_knowledge_block'
- listField {string}: the name of the list field on the above table to remove an element from, e.g. 'can_read_user_criteria'
- whatToRemove {sysId}: the sys_id of the element to remove from the list field, e.g. sys_id of a specific user critria

The script contains additional inline comments about what it does while runnning.

Further context annd use case can be read in the [related community post](https://www.servicenow.com/community/developer-forum/glide-list-type-field-need-to-remove-one-value-in-bulk/m-p/2431257#M947276) where this code was used as the solution by yours truly.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
