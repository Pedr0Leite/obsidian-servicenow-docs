---
title: "Change Request UI actions are not available when expected"
aliases:
  - KB0695934
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695934
kb_number: KB0695934
last_modified: 2024-04-07
---

## Change Request UI actions are not available when expected

  

### Issue

# Symptoms

* * *

After activating the Change Management - Core plugin, several issues were noticed with Change Request:   
  
\- Unable to progress changes, UI actions are missing.   
\- Approving a change CHG0030770 to closed automatically.   
\- The CHG0030770 workflow shows that the task is still waiting on Assess; however, the Request Approval UI action isn't visible. 

# Release

* * *

Kingston Patch 7

# Cause

* * *

The issue is caused by the change request state value being set to 1 rather than the expected value of -5 (New). During our call, we found that the dictionary override for the state field on change\_request table was not correct. 

# Resolution

* * *

Use the out of box dictionary override on the state field for change request.

#
