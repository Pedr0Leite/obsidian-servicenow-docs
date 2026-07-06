---
title: "CMDB Health - Stale tasks are not created"
aliases:
  - KB0815198
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815198
kb_number: KB0815198
last_modified: 2025-04-07
---

## CMDB Health - Stale tasks are not created

  

### Issue

CMDB Health - Stale tasks are not created even when the Correctness jobs run and see the stale Metric on the CMDB-View Dashboard.

### Release

All Releases 

### Cause

User preference - Task Creation set to false.

### Resolution

If you would like to have the tasks generated then navigate to the below link and set the Create Task field to true.

/cmdb\_health\_metric\_pref\_list.do

Note: For the duplicate metric DUP tasks get created by IRE so you do not have to set the value to true.
