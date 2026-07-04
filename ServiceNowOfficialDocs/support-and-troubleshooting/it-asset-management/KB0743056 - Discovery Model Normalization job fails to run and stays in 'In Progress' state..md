---
title: "Discovery Model Normalization job fails to run and stays in 'In Progress' state."
aliases:
  - KB0743056
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743056
kb_number: KB0743056
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Discovery Model Normalization scheduled job fails to run and stays in 'In Progress' state.  
  
Some of the errors found in the logs are below:  
_Error: No Match found for in samp\_sw\_publisher_ 

# Environment

* * *

Software Asset Management plugins are installed.

# Cause

* * *

There are 11 scheduled jobs in cds\_client\_schedule with name starts with 'Download Software' that would pull the content every week. These jobs might have failed to pull the content and hence the normalization fails since it could not find the data.

![](sys_attachment.do?sys_id=ad5aac26db42b450e515c223059619ee)

# Resolution

* * *

a) Go to 'cds\_client\_schedule' table  
b) Search for the names starting with "Download Software", order by Last Update Date which would return 11 rows exactly in the same sequence  
   1) Download Software Content: Version  
   2) Download Software Content: Publisher  
   3) Download Software Content: Product  
   4) Download Software Content: Package  
   5) Download Software Content: Entitlement Definition  
   6) Download Software Content: Product Map  
   7) Download Software Content: Package Map  
   8) Download Software Content: Product Definition  
   9) Download Software Content: Product Process  
   10) Download Software Content: Suite Definitions  
   11) Download Software Content: Lifecyle Defnitions  
c) For each of the above , nullify the Last Update Date Value.  
d) Go to System Scheduler -> Scheduled Jobs  
e) Search for Name : Download Software, which would again give you 11 Rows  
f) Order by Next Action Date in Ascending order. After which the ordering of the Jobs should be in the above sequence that I had given in step(b).Run the jobs in the same order which would fill in the Last Update Date Value in 'cds\_client\_schedule' table.  
g) After these jobs are completed, run the SAM - Discovery Model Normalization which should be completed now.
