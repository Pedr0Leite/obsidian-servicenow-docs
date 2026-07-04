---
title: "Resolving high memory usage error during Performance Analytics data collection"
aliases:
  - KB0597793
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597793
kb_number: KB0597793
last_modified: 2025-09-18
---

## Resolving high memory usage error during Performance Analytics data collection

  

### Issue

When running a Performance Analytics data collection job, the job is canceled due to high memory usage.

One or more Performance Analytics data collection jobs are canceled automatically and no scores are collected. The job **State** is **Collected with errors**.  
  
The following error appears in the job log:  
"High memory usage during data collection. Reduce the number of records included in the indicator source <Indicator source> to prevent this issue. Create multiple, filtered indicator sources instead of using a single large indicator source."

### Cause

During the collection process, the instance performs a check on the available memory for the application node. If the total memory consumption is above a threshold, the collection job will stop in order to avoid causing the node to run out of memory. Memory can be allocated to multiple jobs at the same time. If multiple jobs run concurrently, the total memory usage may exceed the threshold causing the instance to cancel the Performance Analytics data collection job.

### Resolution

-   Run other scheduled jobs that consume large amounts of memory at a different time than any Performance Analytics data collection job. Running these jobs at different times ensures that the instance has sufficient memory available for the data collection job.
-   Reduce the number of records included in the indicator source(s) that are evaluated by the data collection job.
