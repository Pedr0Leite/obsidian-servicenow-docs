---
title: "Field Level Audit"
aliases:
  - Field Level Audit
tags:
  - servicenow-dev-program
  - code-snippet
  - field-level-audit
  - gliderecord
---

# GlideRecord Field-Level Audit

## Description
This snippet compares two GlideRecord objects field by field and logs all differences.  
It is useful for debugging, auditing updates, or validating changes in Business Rules, Script Includes, or Background Scripts.

## Prerequisites
- Server-side context (Background Script, Business Rule, Script Include)
- Two GlideRecord objects representing the original and updated records
- Access to the table(s) involved

## Note
- Works in Global Scope
- Server-side execution only
- Logs all fields with differences to system logs
- Does not modify any records
## Usage
```javascript
// Load original record
var oldRec = new GlideRecord('incident');
oldRec.get('sys_id_here');

// Load updated record
var newRec = new GlideRecord('incident');
newRec.get('sys_id_here');

// Compare and log differences
fieldLevelAudit(oldRec, newRec);
```

## Output
```
Field changed: priority | Old: 5 | New: 2
Field changed: state    | Old: 1 | New: 3
Field changed: short_description | Old: 'Old description' | New: 'New description'
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/ACL enforcement using GlideRecord/README|ACL enforcement using GlideRecord]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Add n number of users to n number of groups using server scripts/README|Add n number of users to n number of groups using server scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Archiving Old Incident Records to Improve Performance/readme|Archiving Old Incident Records to Improve Performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/CheckDuplicate-Server/readme|CheckDuplicate-Server]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Choose Window for better performance/README|Choose Window for better performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Compare_2_records/README|Compare_2_records]]
