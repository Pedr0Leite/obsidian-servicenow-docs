---
title: "Archiving Old Incident Records to Improve Performance"
aliases:
  - Archiving Old Incident Records to Improve Performance
tags:
  - servicenow-dev-program
  - code-snippet
  - archiving-old-incident-records-to-improve-performance
  - gliderecord
---

## Purpose
This document explains how to archive old incident records from the `incident` table to an archive table `ar_incident` to improve performance, while preserving historical data for reporting and audit purposes.
## Solution Overview
Use **ServiceNow Archive Rules** to automatically move incidents to an archive table based on specific conditions:
- Incidents that are **closed**.
- Incidents that are **inactive** (`active = false`).
- Incidents that were closed **150 days ago or earlier**.
The records are moved to the archive table `ar_incident`, which preserves all necessary fields for historical reference.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/ACL enforcement using GlideRecord/README|ACL enforcement using GlideRecord]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Add n number of users to n number of groups using server scripts/README|Add n number of users to n number of groups using server scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/CheckDuplicate-Server/readme|CheckDuplicate-Server]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Choose Window for better performance/README|Choose Window for better performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Compare_2_records/README|Compare_2_records]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Conditional Batch Update/README|Conditional Batch Update]]
