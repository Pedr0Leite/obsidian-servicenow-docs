---
title: Schedule or execute a job to delete records
description: Schedule a date and time to execute a delete job or execute the job immediately.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/schedule-execute-job-delete-records.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Deleting records safely in Core UI, Manage data growth in Core UI, Data Management, Tables and data, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-task
---

# Schedule or execute a job to delete records

Schedule a date and time to execute a delete job or execute the job immediately.

## Before you begin

Role required: admin

## About this task

Consider scheduling the delete job to run during non-business hours to minimize the potential performance impact on your users. Deleting all records in a table temporarily locks the table, which prevents inserts and updates. If you want to [[t_DeleteAllRecordsFromATable|delete all records from a table]], use the [[table-cleaner|table cleaner]] option instead. For more information, see [[deleting-older-records|Deleting older or unwanted records in Core UI]].

## Procedure

1.  Navigate to **All** &gt; **System [[c_DataManagement|Data Management]]** &gt; **Delete jobs**.

2.  Select a delete job record.

3.  Determine whether to schedule the delete job for a later time or run it right away.


## Result

The records are scheduled for deletion or deleted immediately. If you want to restore the deleted records, see [[rollback-delete-job|Rollback a delete job]].

**Parent Topic:**[[deleting-records-safely|Deleting records safely in Core UI]]

## Related

- [[deleting-older-records|Deleting older or unwanted records in Core UI]]
- [[rollback-delete-job|Rollback a delete job]]
- [[deleting-records-safely|Deleting records safely in Core UI]]
- [[t_DeleteAllRecordsFromATable|Delete all records from a table]]
- [[table-cleaner|Table cleaner]]
- [[c_DataManagement|Data Management]]
