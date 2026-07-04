---
title: "Change Request is not closing even after closing the catalog task."
aliases:
  - KB0693291
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693291
kb_number: KB0693291
last_modified: 2024-04-07
---

## Change Request is not closing even after closing the catalog task.

  

### Issue

After Kingston upgrade, on closing CTASK, change is not closing and issue occurs only in prod instance

### Release

KP 6

### Cause

The issue happened due to extended database lock time. 

### Resolution

The active and close variables are related to a "Set Values" activity. 

Looking at the node logs, There is a lock time in the database.

Due to this lock-out time, the active and close variables were not updated and therefore the change request remained open.  
  
To resolve the issue, an index was created on the task table and it resolved the issue. 

#
