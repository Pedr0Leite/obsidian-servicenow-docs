---
title: "Get all users whose email is empty"
aliases:
  - Get all users whose email is empty
tags:
  - servicenow-dev-program
  - code-snippet
  - get-all-users-whose-email-is-empty
  - gliderecord
---

# Get all users without email

Use the script in script.js file to get the list of all users in sys_user table who do not have an email.
This GlideRecord script can be used in multiple places. For example in background scripts.

### Did some optimization in the code
1. Used different variable name instead of gr to reference a GlideRecord object.
2. Used addActiveQuery() method to filter out just the active records.
3. Used getDisplayValue() method to push string values in the array instead of using dot notation.
4. Used self executing function to wrap the code in a function for reducing variable scoping issues.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/ACL enforcement using GlideRecord/README|ACL enforcement using GlideRecord]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Add n number of users to n number of groups using server scripts/README|Add n number of users to n number of groups using server scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Archiving Old Incident Records to Improve Performance/readme|Archiving Old Incident Records to Improve Performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/CheckDuplicate-Server/readme|CheckDuplicate-Server]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Choose Window for better performance/README|Choose Window for better performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Compare_2_records/README|Compare_2_records]]
