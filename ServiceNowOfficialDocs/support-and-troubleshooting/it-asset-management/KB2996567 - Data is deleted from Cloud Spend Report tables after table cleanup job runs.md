---
title: "Data is deleted from Cloud Spend Report tables after table cleanup job runs"
aliases:
  - KB2996567
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2996567
kb_number: KB2996567
last_modified: 2026-05-04
---

## Data is deleted from Cloud Spend Report tables after table cleanup job runs

  

### Issue

Records are deleted from Cloud Spend Report tables unexpectedly.

### Release

Not Release Specific

### Cause

Cloud Cost Management (CCM) includes default table cleanup rules that remove inactive and outdated records from spend report tables.

Specifically, the scheduled job **CCM CleanUp Inactive And Old Monthly Spend Records** deletes inactive records from the `sn_cld_spend_core_monthly_aggregated_cost` table each time the job runs.

To review the configured table cleanup rules for the CCM scope, navigate to **System Maintenance** > **Table Cleanup** and filter by Application: **Cloud Spend Reports Core**

To review the scheduled job, navigate to **System Definition** \> **Scheduled Jobs** and search for **CCM CleanUp Inactive Aggregated Spend Records**.

### Resolution

This behavior is by design. The table cleanup job removes inactive and outdated records from Cloud Spend Report tables according to the configured cleanup rules.

If you need to retain records for a longer period, you can modify the table cleanup rule threshold by following these steps:

1.  Navigate to **System Definition** > **Table Cleanup**.
2.  Filter by Application: **Cloud Spend Reports Core**.
3.  Open the relevant cleanup rule.
4.  Update the Age field to the desired retention period.
5.  Select Update to save the changes.

### Related Links

[Create a table cleanup rule](https://docs.servicenow.com/csh?topicname=activate-table-cleanup.html&version=latest)
