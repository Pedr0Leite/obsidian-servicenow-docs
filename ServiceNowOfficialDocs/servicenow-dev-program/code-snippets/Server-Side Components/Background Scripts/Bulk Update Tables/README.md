---
title: "Bulk Update Tables"
aliases:
  - Bulk Update Tables
tags:
  - servicenow-dev-program
  - code-snippet
  - bulk-update-tables
  - background-scripts
---

# Bulk Update Function Documentation - Use the code/function to bulk change some fields in any tables.

## `bulkUpdate(table, query, data)`

Performs a bulk update on a specified table, applying the given data to all records that match the query.

### Parameters

- **`table`** (`string`): The name of the table where the bulk update is to be performed.
- **`query`** (`string`): The encoded query string that filters which records to update.
- **`data`** (`Object`): An object representing the field-value pairs to update. 
  - Each key is a field name, and the value is the new value for that field.

### Example Usage

```javascript
bulkUpdate('incident', 'priority=1^state=2', { priority: 2, state: 3 });
```
 

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
