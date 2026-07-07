---
title: "isValidGlideRecord"
aliases:
  - isValidGlideRecord
tags:
  - servicenow-dev-program
  - code-snippet
  - isvalidgliderecord
  - gliderecord
---

# Description

Many developers are building functions which expect any GlideRecord reference as a function parameter but within these functions they do no check whether the passed value really represents a valid GlideRecord. However to test a function parameter for a valid GlideRecord reference is pretty tricky and extensive. Therefore I built a small helper function `isValidGlideRecord` which will do the job. As a second optional parameter you can specify a table name which will be considered for an additional validation.

# Usage

```
var grIncident = new GlideRecord('incident');

grIncident.get('12345678901234567890123456789012');

gs.info(isValidGlideRecord(grIncident, 'incident'));
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/ACL enforcement using GlideRecord/README|ACL enforcement using GlideRecord]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Add n number of users to n number of groups using server scripts/README|Add n number of users to n number of groups using server scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Archiving Old Incident Records to Improve Performance/readme|Archiving Old Incident Records to Improve Performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/CheckDuplicate-Server/readme|CheckDuplicate-Server]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Choose Window for better performance/README|Choose Window for better performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Compare_2_records/README|Compare_2_records]]
