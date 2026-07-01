---
title: Design-time access to application tables
description: As the application developer, you can grant or deny other applications the permission to create configuration records, also known as application files, that extend the functionality of an application.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/c\_DesignTimeAccessToAppTables.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Table design and runtime settings, Application access settings, Contextual development environment, Learning about developing on the ServiceNow AI Platform, Building applications]
tags:
  - application-development
  - type-concept
---

# Design-time access to application tables

As the application developer, you can grant or deny other applications the permission to create configuration records, also known as [[c_ApplicationFiles|application files]], that extend the functionality of an application.

The permission applies to any platform feature that extends the functionality of an application data table such as:

-   Business rules
-   UI actions
-   Client scripts

These access permissions protect the application data table at design-time. The system prevents you from creating configuration records by hiding the application data table as an option in the **Table** field. For example, a protected application table does not appear as an option when you create configuration records such as UI actions and client scripts.

Even when permission is granted to create configuration records, some configuration records have additional restrictions to protect application data from unwanted changes from other application scopes.

-   **[[c_DefaultDesignAccessPermissions|Default design access permissions]]**  
By default, new [[c_ApplicationDataTables|application tables]] prevent other application scopes from creating configuration records on application data tables. This prevents any other applications from changing the functionality of a table.
-   **[[t_SetDesignTimeAccessToAppTables|Set design-time access to application tables]]**  
Set these access permissions to protect application tables at design-time.
-   **[[c_ExampleDenyingAllDesignAccess|Example denying all design access to a table]]**  
You can prevent other application scopes from creating configuration records on application data tables.
-   **[[c_ExampleGrantingAccessToConfigRecs|Example allowing configuration records for a table]]**  
You can permit other application scopes to create configuration records on application data tables.

**Parent Topic:**[[r_TableApplicationAccessFields|Table design and runtime settings]]

## Related

- [[c_DefaultDesignAccessPermissions|Default design access permissions]]
- [[t_SetDesignTimeAccessToAppTables|Set design-time access to application tables]]
- [[c_ExampleDenyingAllDesignAccess|Example denying all design access to a table]]
- [[c_ExampleGrantingAccessToConfigRecs|Example allowing configuration records for a table]]
- [[r_TableApplicationAccessFields|Table design and runtime settings]]
- [[c_ApplicationFiles|Application files]]
- [[c_ApplicationDataTables|Application tables]]
