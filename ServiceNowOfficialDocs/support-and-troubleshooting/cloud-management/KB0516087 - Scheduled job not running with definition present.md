---
title: "Scheduled job not running with definition present"
aliases:
  - KB0516087
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0516087
kb_number: KB0516087
last_modified: 2024-11-06
---

## Scheduled job not running with definition present

  

### Issue

When this happens you will typically see a scheduled job (report, script run, etc.) that is set up correctly; however, the job is not running.

### Cause

The scheduled job definition is not what the system uses to determine if there is a job that needs running and when to run it. When a Scheduled Job is created or updated, a record is inserted into the sys\_trigger table - found under System Scheduler -> Today's Scheduled Jobs. That record in the sys\_trigger table contains the last time the job was run, the next time it will be run, and what it is that needs to be run. Therefore, if you have a Scheduled Job that does not have an associated record in sys\_trigger, that job will not run. 

### Resolution

Set the Scheduled Job's active flag to false, save the record, then set it back to true and save the record again. This will force an insert of that job into the sys\_trigger table.
