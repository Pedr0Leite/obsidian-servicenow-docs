---
title: "CMDB Health Check"
aliases:
  - CMDB Health Check
tags:
  - servicenow-dev-program
  - code-snippet
  - cmdb-health-check
  - cmdb
---

# CMDB Health Check – Non-Operational Installed Applications

## Purpose
This script checks for Application Configuration Items (CIs) that are currently:
- Installed (`install_status = 1`)
- Non-operational (`operational_status = 2`)

## Why Run This Check?
Such records can signal potential CMDB data quality issues, as an application marked "Installed" should generally be in an active/operational state. Spotting these mismatches early helps:
- Prevent inaccurate reports and dashboards
- Improve incident/change assignment accuracy
- Maintain overall CMDB integrity

## Output
The script logs the count of Application CIs that fit the criteria:

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB CI Deduplication Task Generator/README|CMDB CI Deduplication Task Generator]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Dynamic Status Update Function/README|CMDB Dynamic Status Update Function]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Get CI Relationships/README|CMDB Get CI Relationships]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Utility Scripts/ReadME|CMDB Utility Scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Utility Scripts/softwareCreationREADME|softwareCreationREADME]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB record count/README|CMDB record count]]
