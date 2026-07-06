---
title: "Executing a script  in Scripts - Background module never completes"
aliases:
  - KB0789122
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789122
kb_number: KB0789122
last_modified: 2023-10-21
---

## Executing a script in Scripts - Background module never completes

  

### Issue

When running a script from Scripts - Background module, the script never returns.

The timer keeps counting; or get a "...  Took too long to respond"

### Cause

The script, of course, is taking a long time to execute.  
  

This occurs even if the "Cancel after 4 hours" is disabled (unchecked).

### Resolution

Can view the script and it's processing information in the Script Execution History module.

Go to sys\_script\_execution\_history.list  
  
Sort by Start time.  
Can check for your script, also.  
  
If Finished time is updated; then your script has completed; otherwise, continue to monitor logs to verify the script is still executing.

If Finished, first verify the results are correct from the script; or if running a change request, validate the change plan.  
Can cancel the Scripts background, if all is verified and script is showing completed in the script execution history table.
