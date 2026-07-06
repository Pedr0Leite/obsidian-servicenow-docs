---
title: "Increasing Service Portal log (sp_log) to more than 90-day default"
aliases:
  - KB0686829
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0686829
kb_number: KB0686829
last_modified: 2025-01-10
---

## Increasing Service Portal log (sp\_log) to more than 90-day default

  

### Issue

For reporting purposes, you might want to have the Service Portal Log Entries table (sp\_log) store data for more than the 90-day default.

**Note** – Increasing the number of days stored in the log to more than the 90-day default could cause significant performance issues.

### Release

All versions using Service Portal

### Resolution

1.  Days are stored in seconds so determine the number of seconds in the number of days you want to use.
2.  The OOB value of 90 days is 7,776,000 secs.
3.  Navigate to System Maintenance > Table Cleanup.
4.  Search for a rule with the tablename sp\_log and open the record.
5.  Change **Age in seconds** to 31536000 (365 days in seconds).
6.  Save/submit the record.

### Related Links

[Apply Table Rotation](https://docs.servicenow.com/csh?topicname=t_ApplyTableRotation.html&version=latest "Apply Table Rotation")
