---
title: Table design and runtime settings
description: The Application access fields determine whether a table is accessible to other applications during design-time or run-time operations.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/r\_TableApplicationAccessFields.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Application access settings, Contextual development environment, Learning about developing on the ServiceNow AI Platform, Building applications]
tags:
  - application-development
  - type-reference
---

# Table design and runtime settings

The Application access fields determine whether a table is accessible to other applications during design-time or run-time operations.

<table id="table_wyn_pzb_br"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Can read

</td><td>

Select the check box to allow script objects from other application scopes to read records stored in this table. This option offers runtime protection. For example, a script in another application can query data on this table. You must first select read access to grant any other API record operation.

</td></tr><tr><td>

Can write

</td><td>

Select the check box to allow script objects from other application scopes to modify records stored in this table. This option offers runtime protection. For example, a script in another application can modify a field value on this table. This option is available only when the **Can read** check box is selected.

 Clear the check box to prevent script objects from other application scopes from modifying data stored in this table.

</td></tr><tr><td>

Can create

</td><td>

Select the check box to allow script objects from other application scopes to create records in this table. This option offers runtime protection. For example, a script in another application can insert a new record in this table. This option is available only when the **Can read** check box is selected.

 Clear the check box to prevent script objects from other application scopes from creating records in this table.

</td></tr><tr><td>

Can delete

</td><td>

Select the check box to allow script objects from other application scopes to delete records from this table. This option offers runtime protection. For example, a script in another application can remove a record from this table. This option is available only when the **Can read** check box is selected.

 Clear the check box to prevent script objects from other application scopes from deleting records from this table.

</td></tr><tr><td>

Allow access to this table via web services

</td><td>

Select the check box to allow users to make inbound web service queries to this table. This option offers both design-time and runtime protection. The user performing the query must have the correct permissions to access this table, even when this check box is selected.

 Clear the check box to prevent users from making web service queries to this table.

</td></tr></tbody>
</table>-   **[[c_RuntimeAccessToAppTables|Runtime access to applications tables]]**  
Runtime access determines if an API or web service call can run against an application table.
-   **[[c_DesignTimeAccessToAppTables|Design-time access to application tables]]**  
As the application developer, you can grant or deny other applications the permission to create configuration records, also known as [[c_ApplicationFiles|application files]], that extend the functionality of an application.

**Parent Topic:**[[c_ApplicationAccessSettings|Application access settings]]

## Related

- [[c_RuntimeAccessToAppTables|Runtime access to applications tables]]
- [[c_DesignTimeAccessToAppTables|Design-time access to application tables]]
- [[c_ApplicationAccessSettings|Application access settings]]
- [[c_ApplicationFiles|Application files]]
