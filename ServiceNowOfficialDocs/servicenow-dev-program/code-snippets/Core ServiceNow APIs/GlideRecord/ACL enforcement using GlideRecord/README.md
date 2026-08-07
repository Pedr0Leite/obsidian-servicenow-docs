---
title: "ACL enforcement using GlideRecord"
aliases:
  - ACL enforcement using GlideRecord
tags:
  - servicenow-dev-program
  - code-snippet
  - acl-enforcement-using-gliderecord
  - gliderecord
---

Using GlideRecordSecure to query data with built in access checks is as simple as that! With this class and associated API, you can have confidence that your data is, well, secure!

When utilizing this class and associated API within scripts, the same rules as GlideRecord apply. On the “server side” (like in a Business Rule), the GlideRecordSecure API can only be run from scripts within global or scoped applications. On the “client side” (like in a Client Script), the GlideRecord API can only be run from scripts within global applications.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Add n number of users to n number of groups using server scripts/README|Add n number of users to n number of groups using server scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Archiving Old Incident Records to Improve Performance/readme|Archiving Old Incident Records to Improve Performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/CheckDuplicate-Server/readme|CheckDuplicate-Server]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Choose Window for better performance/README|Choose Window for better performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Compare_2_records/README|Compare_2_records]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Conditional Batch Update/README|Conditional Batch Update]]
