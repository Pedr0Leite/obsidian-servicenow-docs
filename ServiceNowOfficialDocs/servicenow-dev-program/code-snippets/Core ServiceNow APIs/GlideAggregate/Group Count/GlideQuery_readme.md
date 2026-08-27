---
title: "Group Count"
aliases:
  - Group Count
tags:
  - servicenow-dev-program
  - code-snippet
  - group-count
  - glideaggregate
---

# Group Count
Redo mostly similar example with GlideQuery

## Example Script
```javascript
var table = "sys_user";
var groupBy = "employee_number";
var minGroupCount = 2;

var countOutputGQ = getGroupCountGQ(
    table, groupBy, minGroupCount
);
gs.info('GlideQuery Output is ' + JSON.stringify(countOutputGQ, null, 4));

```
## Example Result
```json
[
 {
        "group": {
            "employee_number": "321"
        },
        "count": 10
    },
    {
        "group": {
            "employee_number": "657"
        },
        "count": 7
    },
    {
        "group": {
            "employee_number": "831"
        },
        "count": 3
    }
]
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Group Count/README|Group Count]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count All Open Incidents Per Priority/readme|Count All Open Incidents Per Priority]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count Inactive Users with Active incidents/README|Count Inactive Users with Active incidents]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count incidents based on category/README|Count incidents based on category]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count open Incidents per Priority and State using GlideAggregate/README|Count open Incidents per Priority and State using GlideAggregate]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Create Problem based on incident volume/README|Create Problem based on incident volume]]
