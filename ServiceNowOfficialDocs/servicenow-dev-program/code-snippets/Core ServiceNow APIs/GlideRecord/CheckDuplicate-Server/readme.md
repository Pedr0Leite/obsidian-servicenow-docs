---
title: "CheckDuplicate-Server"
aliases:
  - CheckDuplicate-Server
tags:
  - servicenow-dev-program
  - code-snippet
  - checkduplicate-server
  - gliderecord
---

Scan all Servers (cmdb_ci_server). For each one, check if there is another CI in cmdb_ci_computer with the same name but not a server (sys_class_name != cmdb_ci_server).

If found, log the server name and the duplicate CI’s class; keep a running duplicate count; finally log the total.

*******Descriton****
1. var gr = new GlideRecord("cmdb_ci_server");
2. Creates a record set for Server CIs.


gr.addEncodedQuery("sys_class_name=cmdb_ci_server");
3. Redundant: you’re already targeting the cmdb_ci_server table which is a class table. This filter doesn’t harm, but it’s unnecessary.


while (gr.next()) { ... }
4. Loops through each server CI.


5.Inside loop:

Query cmdb_ci_computer for records with the same name but where sys_class_name != cmdb_ci_server.
6. If found, log the duplicate and increment dupCount.



7. Finally logs total dupCount.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/ACL enforcement using GlideRecord/README|ACL enforcement using GlideRecord]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Add n number of users to n number of groups using server scripts/README|Add n number of users to n number of groups using server scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Archiving Old Incident Records to Improve Performance/readme|Archiving Old Incident Records to Improve Performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Choose Window for better performance/README|Choose Window for better performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Compare_2_records/README|Compare_2_records]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Conditional Batch Update/README|Conditional Batch Update]]
