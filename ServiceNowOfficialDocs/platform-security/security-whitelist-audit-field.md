---
title: Include a table field in auditing \(inclusion listing\)
description: Track a subset of fields in an audited table by add those fields to an inclusion listing.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/security-whitelist-audit-field.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring auditing for a table, Auditing]
tags:
  - platform-security
  - type-task
---

# Include a table field in auditing \(inclusion listing\)

Track a subset of fields in an audited table by add those fields to an inclusion listing.

## Before you begin

Role required: admin

To add fields in a table to an inclusion list, you must have first [[t_EnableAuditingForATable|enabled auditing for that table]] and [[enable-whitelist-for-table|enabled inclusion list auditing for that table]].

## About this task

Add a set of fields to an inclusion list when you want to audit only a small number of an audited table's fields. If you need to audit most fields, and exclude only a few, follow the [[t_ExcludeAFieldFromBeingAudited|exclusion list procedure]] instead.

## Procedure

1.  Navigate to **All** &gt; **System Definition** &gt; **Dictionary**.

2.  If necessary, customize the list view to include showing the **Attributes** column.

3.  Navigate to the table and field \(column\) you want to the inclusion list.

4.  In the **Attributes** field, enter **audit=true**.

## Related

- [[t_EnableAuditingForATable|Configuring auditing for a table]]
- [[enable-whitelist-for-table|Enable inclusion list auditing for a table]]
- [[t_ExcludeAFieldFromBeingAudited|Exclude a field from being audited \(exclusion listing\)]]
