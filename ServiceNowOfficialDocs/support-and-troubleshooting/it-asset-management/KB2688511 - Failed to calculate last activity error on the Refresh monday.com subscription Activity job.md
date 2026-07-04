---
title: "\"Failed to calculate last activity\" error on the \"Refresh monday.com subscription Activity\"  job "
aliases:
  - KB2688511
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2688511
kb_number: KB2688511
last_modified: 2025-12-18
---

## "Failed to calculate last activity" error on the "Refresh monday.com subscription Activity" job

  

### Issue

1.  Scheduled job "SAM - Refresh monday.com subscription Activity" fails immediately with "Failed to calculate last activity".
2.  Testing the subflow "monday.com Update User Activity" returns an InvalidPathException error: "Could not find path in stream: $.data.boards".

### Release

N/A

### Resolution

1.  Identified that the problematic subflow has been deprecated due to multiple issues; activity data is now updated through the subscriptions job itself.
2.  Recommended running the fix script 'SAM - Remove Monday activity subflow' to remove the deprecated subflow and related jobs, as activity population is now handled by the Download subflow.  
      
    \=> Running the fix script would remove the job.
