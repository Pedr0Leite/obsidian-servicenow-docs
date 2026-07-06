---
title: "Track Discovery Status"
aliases:
  - Track Discovery Status
tags:
  - servicenow-dev-program
  - code-snippet
  - track-discovery-status
  - itom
---

After a recent migration, the client wanted a quick and reliable way to verify whether specific IP addresses were being discovered by ServiceNow Discovery, and if so, determine which Discovery Status records they were associated with.

This requirement was critical to help the client:

Identify IPs that were discovered successfully.

Find those that were not rediscovered after migration.

Diagnose potential discovery or configuration issues efficiently.

The script provided below serves as a powerful troubleshooting utility. It allows administrators to instantly check which discovery job (status) a given IP address belongs to, enabling faster debugging and drastically reducing resolution time.

What the Script Does

The script performs the following steps:

Takes a list of IP addresses as input.

Looks up each IP in the cmdb_ci_computer table(It could be Linux, AIX,etc.) to find its corresponding Configuration Item (CI).

Queries the Discovery Device History (discovery_device_history) to determine whether the CI was created or updated by a discovery process.

Builds a JSON array mapping each IP address to its respective discovery status number (e.g., DIS123145).

Prints the result in the system logs for quick review and validation.

Example output:

[
  {"ip_address": "192.168.1.35", "discovery_status_number": "DIS123145"},
  {"ip_address": "192.168.1.27", "discovery_status_number": "DIS123189"},
  {"ip_address": "192.168.1.15", "discovery_status_number": "No discovery record found"}
]

Benefits

Saves significant debugging and analysis time.

Helps identify why certain CIs stopped being discovered after migration.

Provides clear mapping between IP addresses and their last discovery statuses.

Enables faster root cause analysis and improves operational efficiency.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/ITOM/Bulk Location Update/README|Bulk Location Update]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/ITOM/Discovery/Pre README|ServiceNow Discovery Pre Sensor Script: IP Router Association]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/ITOM/Discovery/README|Discovery]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/ITOM/Generate Discovery Schedule/README|Generate Discovery Schedule]]
