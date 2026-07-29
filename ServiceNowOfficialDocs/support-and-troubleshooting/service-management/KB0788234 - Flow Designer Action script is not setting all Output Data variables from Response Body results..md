---
title: "Flow Designer Action script is not setting all Output Data variables from Response Body results."
aliases:
  - KB0788234
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788234
kb_number: KB0788234
last_modified: 2025-09-03
---

## Flow Designer Action script is not setting all Output Data variables from Response Body results.

  

### Issue

The user had a Flow Action which was failing to set all output data variables from their response body (two of five variables did not have data in them). Yet, if they ran the same script in the background, it worked fine. The user wanted to know why this was.

### Resolution

The issue the user was facing was that when a response body came back, only three of five output data variables had values (meaning two did not).   
  
The root cause of the missing variable data is that the Flow Action needed to be recompiled. It was found that there was a stale output mapping that was not getting cleared out until the action was recompiled.  
  
This staleness happens for various reasons (flows being copied, moved between instances, etc). In those scenarios, there are times when flows / sub-flows / actions are not updated properly with their internal mappings (inputs ➛ outputs).  
  
A usual good practice is to find the base component that is breaking down (in this case the action) and modify it in such away where the system has to recompile the action (generate a new snapshot/version and have all references to that action use that latest version).  
  
Please note that this behavior was originally encountered with a user in Madrid Patch 7. Much work has been done since Madrid Patch 7 to prohibit users from encountering such behaviors in later releases.
