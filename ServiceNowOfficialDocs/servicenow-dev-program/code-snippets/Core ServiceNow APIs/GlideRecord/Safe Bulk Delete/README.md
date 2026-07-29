---
title: "Safe Bulk Delete"
aliases:
  - Safe Bulk Delete
tags:
  - servicenow-dev-program
  - code-snippet
  - safe-bulk-delete
  - gliderecord
---

# GlideRecord Bulk Delete with Safety Checks

## Description
This snippet allows you to safely delete multiple records from a ServiceNow table based on an encoded query.
It logs all records that match the query so you can review them before actually deleting anything.  
Helps prevent accidental mass deletion of important data.

## Note 
- Works in Global Scope by default
- Can be executed in Background Scripts or Script Includes
- **ALWAYS REVIEW LOGS BEFORE ENABLING DELETION**
## Prerequisites
- Server-side context (Background Script, Business Rule, Script Include)
- Access to the target table
- Basic understanding of GlideRecord and Encoded Queries

## Usage
```javascript
// Logs all active low-priority incidents that would be deleted
safeDelete('incident', 'active=true^priority=5');

// To perform actual deletion, uncomment gr.deleteRecord() inside the function
```

## Output
```
Records matching query: 3
Record sys_id: 12345abcdef would be deleted.
Record sys_id: 23456bcdef would be deleted.
Record sys_id: 34567cdefg would be deleted.
Bulk delete preview complete. Verify logs before enabling deletion.
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/ACL enforcement using GlideRecord/README|ACL enforcement using GlideRecord]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Add n number of users to n number of groups using server scripts/README|Add n number of users to n number of groups using server scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Archiving Old Incident Records to Improve Performance/readme|Archiving Old Incident Records to Improve Performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/CheckDuplicate-Server/readme|CheckDuplicate-Server]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Choose Window for better performance/README|Choose Window for better performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Compare_2_records/README|Compare_2_records]]
