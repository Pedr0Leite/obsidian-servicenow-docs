---
title: "Dynamic Record Archiving"
aliases:
  - Dynamic Record Archiving
tags:
  - servicenow-dev-program
  - code-snippet
  - dynamic-record-archiving
  - script-includes
---

#  Dynamic Record Archiving Logic

##  Overview
This snippet provides a reusable logic to archive or flag records in ServiceNow that are older than a specified threshold. It helps maintain data hygiene, improve performance, and support compliance with data retention policies.

You can choose between two modes:
- **Flag Mode**: Marks records as archived using a custom field (`u_archived`).
- **Move Mode**: Moves records to a corresponding archive table (e.g., `incident_archive`) and deletes the original.

---

##  Use Case
- Archive incidents older than 1 year.
- Clean up old tasks, requests, or custom records.
- Automate data lifecycle management via Scheduled Jobs.

---

##  Parameters
| Parameter           | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `tableName`         | Name of the table to archive (e.g., `incident`)                             |
| `dateField`         | Date field to filter by (e.g., `opened_at`, `created_on`)                   |
| `archiveThresholdDays` | Number of days before today to consider for archiving (e.g., `365`)         |
| `archiveMode`       | `'flag'` to mark records, `'move'` to transfer to archive table             |

---

##  Example Usage
```javascript
var archiver = new RecordArchiver('incident', 'opened_at', 365, 'flag');
archiver.archiveRecords();

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
