---
title: "ACL on Database Views"
aliases:
  - KB0535471
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535471
kb_number: KB0535471
last_modified: 2026-04-30
---

## Issue

 

ACL on Database Views

* * *

Unlike ordinary _base tables_ in a relational database, a view does not form part of the physical schema. As a result set, it is a virtual table dynamically computed or collated from data in the database when access to that view is requested.

It is important to understand that table level ACL is not applicable on database views. Assuming that the underlying table ACL will be applicable to Views is not correct. To safeguard the underlying table information as exposed through a View, you can create an ACL on views. 

The Field level ACLs(example: table.field, table.\*) will still be applicable in viewing the result of join since the fields in Database view are actually a dynamic link to the physical fields. 

Summary of the ACL behavior:

-   Table-level ACL for database view (example: Incident SLA.None) is checked when a database view is viewed 
-   Table-level ACL for physical table (example: Incident.None) is NOT checked when a database view is viewed 
-   Field-level ACL for physical table (example: Incident.Number) is checked when a database view is viewed 
-   Field-level ACL for database view (example: Incident SLA.Number) is NOT checked when a database view is viewed 

To configure ACLs on database views, follow these steps:

1.  Elevate your role to security\_admin.
2.  Go to **System Definition > Database Views**.
3.  Open any database view from the list.
4.  Right-click and select **Configure > Security Rules**.

ACL on views are displayed.

![](sys_attachment.do?sys_id=76f9cc8293e4cb90f2167de86cba10e7 "Configuring Database View Security")

## Resolution

n/a
