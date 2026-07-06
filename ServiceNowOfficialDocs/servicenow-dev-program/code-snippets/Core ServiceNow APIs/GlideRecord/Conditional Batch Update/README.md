---
title: "Conditional Batch Update"
aliases:
  - Conditional Batch Update
tags:
  - servicenow-dev-program
  - code-snippet
  - conditional-batch-update
  - gliderecord
---

# GlideRecord Conditional Batch Update

## Description
This snippet updates multiple records in a ServiceNow table based on a GlideRecord encoded query.  
It logs all updated records and provides a safe, controlled way to perform batch updates.

## Prerequisites
- Server-side context (Background Script, Script Include, Business Rule)
- Access to the table
- Knowledge of GlideRecord and encoded queries

## Note
- Works in Global Scope
- Server-side execution only
- Logs updated records for verification
- Can be used for maintenance, bulk updates, or automated scripts

## Usage
```javascript
// Update all active low-priority incidents to priority=2 and state=2
batchUpdate('incident', 'active=true^priority=5', {priority: 2, state: 2});
```

## Sample Output
```
Updated record: abc123
Updated record: def456
Updated record: ghi789
Batch update completed. Total records updated: 3
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/ACL enforcement using GlideRecord/README|ACL enforcement using GlideRecord]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Add n number of users to n number of groups using server scripts/README|Add n number of users to n number of groups using server scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Archiving Old Incident Records to Improve Performance/readme|Archiving Old Incident Records to Improve Performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/CheckDuplicate-Server/readme|CheckDuplicate-Server]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Choose Window for better performance/README|Choose Window for better performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Compare_2_records/README|Compare_2_records]]
