---
title: "SLA Workflow is not progressing properly - why?"
aliases:
  - KB0759053
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759053
kb_number: KB0759053
last_modified: 2024-04-07
---

## SLA Workflow is not progressing properly - why?

  

### Issue

The user had recently implemented a new SLA Workflow. Within the workflow, the user had a SLA Percentage Timer which should wait for 100% of the SLA's duration and then progress the workflow.

This is not happening. When the SLA breaches, the Workflow is not progressing as the user would expect. They wanted to know why.

### Resolution

The issue, in this case, is that the user had two SLA Percentage Timers where the first was configured correctly, but the second was not.

Within the first SLA Percentage Timer, the Percentage field value was set to "50". This is fine.  
  
In the second SLA Percentage Timer, however, the Percentage field value was set to "100". This is not correct when considering the first SLA Percentage Timer as the total field values for Percentage are greater than 100.  
  
The way the SLA Percentage Timer activity works is that, when multiple of them are used, they add the percentages together. So, in essence, the user's current configuration was saying, "Wait until the SLA is at 150% of Business Elapsed Time, then move forward" (50% + 100% = 150%).  
  
To remedy the behavior, please ensure that the total Percentage value of _all_ SLA Percentage Timers present in the workflow equal to 100%.
