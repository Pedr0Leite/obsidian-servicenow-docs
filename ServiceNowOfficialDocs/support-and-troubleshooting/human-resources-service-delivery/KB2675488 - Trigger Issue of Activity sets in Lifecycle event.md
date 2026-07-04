---
title: "Trigger Issue of Activity sets in Lifecycle event "
aliases:
  - KB2675488
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2675488
kb_number: KB2675488
last_modified: 2026-03-30
---

## Trigger Issue of Activity sets in Lifecycle event

  

### Issue

  
Activity sets are running into errors.The error occurs due to dependency on tasks that have exceeded the workflow activity transaction limit of 5000, causing subsequent activity sets to fail.  
  

### Release

All

### Cause

  
1\. The workflow activity transaction limit of 5000 was exceeded for the activity sets within the HR Activity Launcher, causing the workflow to be cancelled and subsequent activity sets to fail due to dependency.

2\. The evaluation interval setting (default 4 hours) may contribute to the issue if set too low, leading to rapid exhaustion of the activity count.  
  

### Resolution

  
1\. Navigate to the HR case and click on the 'Resume Case' link to restart the workflow, resetting the activity count to zero.

2\. Resume any cases currently experiencing error issues to resolve the dependency-related errors.

3\. Avoid changing the default maximum activity count (5000) to prevent potential performance issues.

4\. Review the evaluation interval settings, as a low interval (e.g., 1 second) may cause errors faster than the default 4-hour interval.

5\. Refer to the KB article for details: https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB1117350.
