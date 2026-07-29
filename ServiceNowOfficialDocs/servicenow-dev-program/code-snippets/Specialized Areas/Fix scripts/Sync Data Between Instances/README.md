---
title: "Sync Data Between Instances"
aliases:
  - Sync Data Between Instances
tags:
  - servicenow-dev-program
  - code-snippet
  - sync-data-between-instances
  - fix-scripts
---

The script leverages the ServiceNow REST API to retrieve records from a specified table on the source instance, then transmits them to the target instance for insertion.

As an example, it is set up to sync active user records, but it can be easily modified for any other table and filter criteria.


Usage:

The script is configured with the following parameters:

table: Specifies the name of the table to sync (Example is sys_user).

query: A GlideRecord query string to filter the records to be synchronized

targetInstance: The ServiceNow instance to which data will be sent.

user and password: Credentials for authenticating with the target instance.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
