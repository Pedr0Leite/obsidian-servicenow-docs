---
title: Glide class overview
description: The ServiceNow Glide classes expose JavaScript APIs that enable you to conveniently work with tables using scripts.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/api-reference/scripts/r\_GlideClassOverview.html
release: australia
product: Scripts
classification: scripts
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Scripting, API implementation, API implementation and reference]
---

# Glide class overview

The ServiceNow Glide classes expose JavaScript APIs that enable you to conveniently work with tables using scripts.

Using the Glide APIs, you can perform database operations without writing SQL queries, display [[r_UIPages|UI pages]], and define UI actions. The following tables provide brief descriptions of the Glide classes and links to detailed information.

|Class|Description|
|-----|-----------|
|GlideRecord|Use this class for database operations instead of writing SQL queries. GlideRecord is a special Java class that can be used in JavaScript exactly as if it were a native JavaScript class. A GlideRecord is an object that contains records from a single table. See [GlideRecord](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/server-api-reference/c_GlideRecordScopedAPI.md).|
|GlideElement|Use this class to operate on the fields of the current GlideRecord. See [GlideElement](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/server-api-reference/c_GlideElementScopedAPI.md).|
|GlideSystem|Use this class to get information about the system. See [GlideSystem](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/server-api-reference/c_GlideSystemScopedAPI.md).|
|GlideAggregate|Use this class to perform database aggregation queries, such COUNT, SUM, MIN, MAX, and AVG, for creating customized reports or calculations in calculated fields. See [GlideAggregate](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/server-api-reference/c_GlideAggregateScopedAPI.md).|
|GlideDateTime|Use this class to perform date-time operations, such as date-time calculations, formatting a date-time, or converting between date-time formats. See [GlideDateTime](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/server-api-reference/c_GlideDateTimeScoped.md).|

|Class|Description|
|-----|-----------|
|GlideAjax|Use this class to execute server-side code from the client. See [[c_GlideAjaxAPI|GlideAjax]].|
|GlideDialogWindow|Use this class to display a dialog window. See [[c_GlideDialogWindowAPI|GlideDialogWindow]].|
|GlideForm|Use this class to customize forms. See [[c_GlideFormAPI|GlideForm]].|
|GlideList2|Use this class to customize \(v2\) lists, including normal lists and related lists. See [[c_GlideList2API|GlideList2]].|
|GlideMenu|Use this class to customize UI Context Menu items. See [[c_GlideMenuAPI|GlideMenu]].|
|GlideUser|Use this class to get session information about the current user and current user roles. See [[c_GlideUserAPI|GlideUser]].|

-   **[Glide stack](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/scripts/r_GlideStack.md)**  
Glide is an extensible Web 2.0 development platform written in Java that facilitates rapid development of forms-based workflow applications \(work orders, trouble ticketing, and project management, for example\).

**Parent Topic:**[Scripting](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/scripts/c_Script.md)

## Related

- [[c_GlideAjaxAPI|GlideAjax - Client]]
- [[c_GlideDialogWindowAPI|GlideDialogWindow - Client \(deprecated\)]]
- [[c_GlideFormAPI|GlideForm \(g\_form\) - Client]]
- [[c_GlideList2API|GlideList2 \(g\_list\) - Client]]
- [[c_GlideMenuAPI|GlideMenu \(g\_menu and g\_item\) - Client]]
- [[c_GlideUserAPI|GlideUser - Client]]
- [[r_UIPages|UI pages]]
