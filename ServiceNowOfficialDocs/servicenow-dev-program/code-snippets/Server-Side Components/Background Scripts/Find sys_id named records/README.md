---
title: "Find sys_id named records"
aliases:
  - Find sys_id named records
tags:
  - servicenow-dev-program
  - code-snippet
  - find-sys-id-named-records
  - background-scripts
---

## Find sys_id named records

Use this background script to find records that contain a sys_id value in a specified field (other than the actual sys_id field)

This might for example have happened by accident during migration of data between two ServiceNow instances where referenced records on the target instance were accidentally created due to a Choice action=create setting on a Field Map.

How to use:

Change the "table" and "field" variables to the table and field name you want to search for sys_ids in

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
