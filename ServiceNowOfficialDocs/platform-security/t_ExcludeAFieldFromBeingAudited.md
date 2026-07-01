---
title: Exclude a field from being audited \(exclusion listing\)
description: Prevent the ServiceNow AI Platform from tracking a subset of fields in an audited table by excluding those fields from an audit.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/t\_ExcludeAFieldFromBeingAudited.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring auditing for a table, Auditing]
tags:
  - platform-security
  - type-task
---

# Exclude a field from being audited \(exclusion listing\)

Prevent the ServiceNow AI Platform from tracking a subset of fields in an audited table by excluding those fields from an audit.

## Before you begin

Role required: admin

To exclude a field in a table from being audited, you must have first [[t_EnableAuditingForATable|enable auditing for that table]].

## About this task

Add a set of fields to an exclusion list when you want to audit most of the fields in an auditable table. If you want to audit only a few fields, follow the [[security-whitelist-audit-field|inclusion listing procedure]] instead.

**Note:** Disabling [[c_AuditedTables|auditing]] on journal-based fields can impact the functionality of features, such as the Activity Formatter.

## Procedure

1.  Navigate to **All** &gt; **System Definition** &gt; **Dictionary**.

2.  If necessary, customize the list view to show the **Attributes** column.

3.  Navigate to the row corresponding to the table and field \(column\) you want to exclude from auditing.

4.  In the **Attributes** column for that row, enter `no_audit`.

## Related

- [[t_EnableAuditingForATable|Configuring auditing for a table]]
- [[security-whitelist-audit-field|Include a table field in auditing \(inclusion listing\)]]
- [[c_AuditedTables|Auditing]]
