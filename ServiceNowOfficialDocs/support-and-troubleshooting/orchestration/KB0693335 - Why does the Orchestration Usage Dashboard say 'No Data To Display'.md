---
title: "Why does the Orchestration Usage Dashboard say 'No Data To Display"
aliases:
  - KB0693335
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693335
kb_number: KB0693335
last_modified: 2024-04-07
---

## Why does the Orchestration Usage Dashboard say 'No Data To Display'

  

### Issue

# Symptoms

* * *

When you open the Orchestration Usage dashboard, some gauges may say 'No Data To Display'.

From the navigation, open **Orchestration - Orchestration Usage**

# Release

* * *

Jakarta and later

# Cause

* * *

This is usually because there literally is no data to display.

If there is a workflow context that included orchestration activities, then each activity will be logged in the '**orch\_execution**' table. If that table is empty, then none have run yet.  
https://<instance>.service-now.com/**orch\_execution**\_list.do

That could be confirmed with this list, which queries the workflow context activity history directly:  
https://<instance>.service-now.com/**wf\_history**\_list.do?sysparm\_query=activity.**activity\_definition**.sys\_class\_name=**wf\_element\_definition**

You could further check the count records that provide the data for this dashboard, where Table contains 'orch':  
https://<instance>.service-now.com/**usageanalytics\_count**\_list.do?sysparm\_query=**table\_nameLIKEorch**

# Resolution

* * *

Once workflows that contain Orchestration activities have been run, you will start to see data displayed.
