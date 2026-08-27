---
title: "debug"
aliases:
  - debug
tags:
  - servicenow-dev-program
  - code-snippet
  - debug
  - import-sets
---

# Debugging Import Sets & Transform Maps

When you load data and execute the transform maps via the platform UI, it runs in the background which means it is not accessible to the Script Debugger.

Using this snippet you can pass the Import Set sys_id (in a state of Pending) and it will execute all the transform maps on that import set in the foreground, and be available to step through any code in the Script Debugger.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Import Sets/Import sets overview/ModelManufacture.README|ModelManufacture.README]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Import Sets/Import sets overview/README|Import sets overview]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Import Sets/Import sets overview/TriggerDataSource.README|TriggerDataSource.README]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0758037 - Azure AD Sync or an Import (e.g. LDAP Group Import) Being Interfered with by security_admin Role|Azure AD Sync or an Import (e.g. LDAP Group Import) Being Interfered with by \"security_admin\" Role]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0596441 - On JDBC data sources SQL with column aliases don't return any rows.|On JDBC data sources SQL with column aliases don't return any rows.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0747613 - When importing data, some staging table records are duplicating or an Import set row is duplicating|When importing data, some staging table records are duplicating or an Import set row is duplicating]]
