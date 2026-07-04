---
title: "How to isolate cases that have child cases"
aliases:
  - KB0853342
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0853342
kb_number: KB0853342
last_modified: 2023-07-12
---

## How to isolate cases that have child cases

  

### Issue

How to isolate cases that have child cases

### Resolution

Please follow bellow steps:

\--Type sn\_customerservice\_case.list in filter navigator as admin  
\--Configure list to bring "Parent case" column to the list:  
Click on "Update personalized list" (wheel icon on table)  
Bring "Parent case" from available to selected  
\--Filter the list \[Parent case\]\[is not empty\]  
\--On table list on Parent case Right click and navigate "Group by Parent case"
