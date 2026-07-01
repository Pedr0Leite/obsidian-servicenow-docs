---
title: Deleting records safely in Core UI
description: Safely delete records from a table without using scripts and without deleting the table by creating and executing delete jobs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/deleting-records-safely.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Manage data growth in Core UI, Data Management, Tables and data, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-concept
---

# Deleting records safely in Core UI

Safely delete records from a table without using scripts and without deleting the table by creating and executing delete jobs.

## Overview of deleting records safely

1.  [[mark-records-for-deletion|Mark records for deletion]]

    Determine which records to delete by creating a delete job.

2.  [[preview-affected-records-for-deletion|Preview affected records for deletion]]

    Preview the affected records before you schedule or execute the job. For example, you might want to preview a set of incident records that will be deleted before you delete them.

3.  [[schedule-execute-job-delete-records|Schedule or execute a job to delete records]]

    Schedule the job to run later or execute the job immediately.

4.  [[rollback-delete-job|Rollback a delete job]]

    Use the rollback option in the delete job If you need to restore deleted records after the job has run.


If you must delete a large number of records from a table rather than a selection of records, use the [[table-cleaner|table cleaner]] option. For details, see [[deleting-older-records|Deleting older or unwanted records in Core UI]].

-   **[Mark records for deletion](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/mark-records-for-deletion.md)**  
Mark records for deletion according to one or more criteria by creating a delete job.
-   **[Preview affected records for deletion](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/preview-affected-records-for-deletion.md)**  
Before you run a delete job, preview the count of affected records to see the impact of executing the delete job.
-   **[Schedule or execute a job to delete records](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/schedule-execute-job-delete-records.md)**  
Schedule a date and time to execute a delete job or execute the job immediately.
-   **[Rollback a delete job](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/rollback-delete-job.md)**  
Rollback a completed delete job to restore the deleted records.

**Parent Topic:**[[data-management-policies|Managing data growth in Core UI]]

## Related

- [[mark-records-for-deletion|Mark records for deletion]]
- [[preview-affected-records-for-deletion|Preview affected records for deletion]]
- [[schedule-execute-job-delete-records|Schedule or execute a job to delete records]]
- [[rollback-delete-job|Rollback a delete job]]
- [[deleting-older-records|Deleting older or unwanted records in Core UI]]
- [[data-management-policies|Managing data growth in Core UI]]
- [[table-cleaner|Table cleaner]]
