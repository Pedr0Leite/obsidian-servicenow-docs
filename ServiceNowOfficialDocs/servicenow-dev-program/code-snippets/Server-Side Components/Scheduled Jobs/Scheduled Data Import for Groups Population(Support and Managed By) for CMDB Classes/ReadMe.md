---
title: "Scheduled Data Import for Groups Population(Support and Managed By) for CMDB Classes"
aliases:
  - Scheduled Data Import for Groups Population(Support and Managed By) for CMDB Classes
tags:
  - servicenow-dev-program
  - code-snippet
  - scheduled-data-import-for-groups-populationsupport-and-managed-by-for-cmdb-classes
  - scheduled-jobs
---

This is a Post-Import Script designed for a Scheduled Import . Its purpose is to cleanly map and update the Support Group and Managed By Group fields on Configuration Items (CIs) after data has been loaded into the staging table.

Script Functionality
The script iterates through the records of an Import Set and performs the following core steps for each row:

 i)Extract Data: Reads the CI Class Display Name (u_class), Support Group Name (u_support_group), and Managed By Group Name (u_managed_by_group) from the staging table record.

 ii)Validate Class: Uses the u_class(name from staging table) value to look up and confirm the correct target CMDB table name (e.g., finding cmdb_ci_server from the display name "Server").

 iii)Resolve Groups: Finds the system-unique sys_ids for both the Support Group and Managed By Group names.

 iv)Update CIs: Queries the determined CMDB table, filters the CIs based on the Optional-Filters placeholder, and sets the support_group and managed_by_group fields using the resolved sys_ids.

**Points to note :
1) The schedule-import should be linked to a Data Source which has the spreadsheet attached(where groups and classes info is present)
2) This script populates the groups based on Group Name given in the spreadsheet(Make sure they are present in the instance and are following the appropriate naming convention)
3) The script provided is a post script ,which executes after the data is imported.**
   

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/API Token Expiry Warning/Readme|API Token Expiry Warning]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Approval Reminder/README|Approval Reminder]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto Disable account/Readme|Auto Disable account]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto close changes requests updated 30 days prior/README|Auto close changes requests updated 30 days prior]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto upgrade store applications/Readme|Auto upgrade store applications]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto-Assign Unassigned Incidents Older Than 30 Minutes/Readme|Auto-Assign Unassigned Incidents Older Than 30 Minutes]]
