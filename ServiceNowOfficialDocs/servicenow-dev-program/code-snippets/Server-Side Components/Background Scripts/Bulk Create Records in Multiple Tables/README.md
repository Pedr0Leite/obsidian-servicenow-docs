---
title: "Bulk Create Records in Multiple Tables"
aliases:
  - Bulk Create Records in Multiple Tables
tags:
  - servicenow-dev-program
  - code-snippet
  - bulk-create-records-in-multiple-tables
  - background-scripts
---

# Function: `bulkCreateRecords(target)`

Creates multiple records in specified tables based on provided data.

## Parameters

- **`target`** (`Object`): An object where each key is the name of a table, and each value is an array of objects representing the records to be created. Each object in the array should contain field-value pairs for the respective table.

## Example Usage

```javascript
bulkCreateRecords({
    'incident': [
        { short_description: 'Network issue', caller_id: '681ccaf9c0a8016401c5a33be04be441', priority: 2 },
        { short_description: 'Email outage', caller_id: '681ccaf9c0a8016401c5a33be04be442', priority: 1 }
    ],
    'change_request': [
        { short_description: 'Server upgrade', assigned_to: '681ccaf9c0a8016401c5a33be04be443', state: 'new' }
    ]
});

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
