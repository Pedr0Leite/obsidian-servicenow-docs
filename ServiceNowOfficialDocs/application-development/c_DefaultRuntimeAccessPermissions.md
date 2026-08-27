---
title: Default runtime access permissions
description: The default runtime access permissions apply to new application data tables.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/c\_DefaultRuntimeAccessPermissions.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Runtime access to applications tables, Table design and runtime settings, Application access settings, Contextual development environment, Learning about developing on the ServiceNow AI Platform, Building applications]
tags:
  - application-development
  - type-concept
---

# Default runtime access permissions

The default runtime access permissions apply to new application data tables.

By default, new [[c_ApplicationDataTables|application tables]] only allow read access from other application scopes.

|Field|Value|
|-----|-----|
|**Accessible from**|All application scopes|
|**Can read**|Enabled|
|**Can create**|Disabled|
|**Can update**|Disabled|
|**Can delete**|Disabled|
|**Allow access to this table via web services**|Enabled|

\[Omitted image "DefaultRuntimeAccessPermissions.png"\] Alt text: Default runtime access permissions

**Parent Topic:**[[c_RuntimeAccessToAppTables|Runtime access to applications tables]]

## Related

- [[c_RuntimeAccessToAppTables|Runtime access to applications tables]]
- [[c_ApplicationDataTables|Application tables]]
