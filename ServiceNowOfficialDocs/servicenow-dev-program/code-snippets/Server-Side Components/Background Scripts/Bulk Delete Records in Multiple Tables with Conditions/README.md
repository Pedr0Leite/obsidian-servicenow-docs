---
title: "Bulk Delete Records in Multiple Tables with Conditions"
aliases:
  - Bulk Delete Records in Multiple Tables with Conditions
tags:
  - servicenow-dev-program
  - code-snippet
  - bulk-delete-records-in-multiple-tables-with-conditions
  - background-scripts
---

# Bulk Delete Function Documentation - Use the code/function to bulk-deletes records from multiple tables based on provided encoded queries.

# Function: `bulkDelete(target)`

Deletes records from multiple tables based on provided encoded queries.

## Parameters

- **`target`** (`Object`): An object where each key is the name of a table, and each value is an encoded query string. 
  - The function will delete all records matching the encoded query for each specified table.

## Example Usage

```javascript
bulkDelete({
    'incident': 'priority=1^state=2',
    'change_request': 'state=3^risk=high'
});
```
 

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
