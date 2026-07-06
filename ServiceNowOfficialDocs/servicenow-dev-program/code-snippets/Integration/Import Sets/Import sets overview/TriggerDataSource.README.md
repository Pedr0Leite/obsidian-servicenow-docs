---
title: "TriggerDataSource.README"
aliases:
  - TriggerDataSource.README
tags:
  - servicenow-dev-program
  - code-snippet
  - import-sets-overview
  - import-sets
---

The triggerDataSource() function eliminates the need for manually executing a Data Source from the UI. It programmatically triggers the import of a predefined Data Source record and loads the associated data into an Import Set table.
This function is typically used in:
* Scheduled Script Executions
* Flow Designer Actions.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Import Sets/Import sets overview/ModelManufacture.README|ModelManufacture.README]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Import Sets/Import sets overview/README|Import sets overview]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Import Sets/debug/README|debug]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0758037 - Azure AD Sync or an Import (e.g. LDAP Group Import) Being Interfered with by security_admin Role|Azure AD Sync or an Import (e.g. LDAP Group Import) Being Interfered with by \"security_admin\" Role]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0596441 - On JDBC data sources SQL with column aliases don't return any rows.|On JDBC data sources SQL with column aliases don't return any rows.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0747613 - When importing data, some staging table records are duplicating or an Import set row is duplicating|When importing data, some staging table records are duplicating or an Import set row is duplicating]]
