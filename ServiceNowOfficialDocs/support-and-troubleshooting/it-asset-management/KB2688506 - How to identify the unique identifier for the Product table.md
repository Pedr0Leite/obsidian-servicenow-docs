---
title: "How to identify the unique identifier for the Product table"
aliases:
  - KB2688506
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2688506
kb_number: KB2688506
last_modified: 2026-05-15
---

## How to identify the unique identifier for the Product table

  

### Issue

What is the unique identifier for the Product table in ServiceNow?

### Release

N/A

### Resolution

The `sys_id` field is the only unique identifier on the Product table. This value does not change unless a major structural update is applied to the record.

If a two-field combination is needed to identify a product, you can use both the Product and Publisher fields together as a composite identifier.

Note that some default scripts in the base system reference the `sys_id` of a product as a hard-coded value. If you modify or recreate a product record, verify that any scripts referencing the original `sys_id` are updated accordingly.

Steps to locate sys\_id

1.  Log in to your ServiceNow instance.
2.  Navigate to the Product table (for example, using the application navigator or a direct table URL).
3.  Open the relevant product record.
4.  Right-select the field label of any field, then select Show — sys\_id to display the unique identifier for that record.
