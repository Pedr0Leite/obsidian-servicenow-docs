---
title: "Get Reference Record"
aliases:
  - Get Reference Record
tags:
  - servicenow-dev-program
  - code-snippet
  - get-reference-record
  - gliderecord
---

# Get Reference Record with GlideRecord

This folder contains examples demonstrating how to retrieve and work with reference records using `getRefRecord()` in ServiceNow server-side scripting.

## Overview

`getRefRecord()` is used to retrieve the full GlideRecord object of a reference field. This allows access to additional fields from the referenced record, such as `name`, `email`, or other attributes beyond the display value.

Because `getRefRecord()` does not throw an error when the reference field is empty or invalid, it is important to use `isValidRecord()` to verify that the reference was successfully retrieved before accessing its fields.

## Script Descriptions

- get_assignment_group_from_incident.js retrieves the assignment group from an incident record and prints its name if the group exists.
- get_requested_by_user.js retrieves a change request by `sys_id`, then accesses the `requested_by` user record. If valid, it prints the user's username and email.

## Best Practices

- Always use `isValidRecord()` after calling `getRefRecord()` to ensure the reference is valid.
- Use `getRefRecord()` when you need to access fields from a referenced record, not just its display value.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/ACL enforcement using GlideRecord/README|ACL enforcement using GlideRecord]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Add n number of users to n number of groups using server scripts/README|Add n number of users to n number of groups using server scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Archiving Old Incident Records to Improve Performance/readme|Archiving Old Incident Records to Improve Performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/CheckDuplicate-Server/readme|CheckDuplicate-Server]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Choose Window for better performance/README|Choose Window for better performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Compare_2_records/README|Compare_2_records]]
