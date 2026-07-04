---
title: "While moving lifecycle case to rescind, State value gets stuck into \"rescind in progress\" state. It's not moving further to the \"rescinded\" state"
aliases:
  - KB0998934
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998934
kb_number: KB0998934
last_modified: 2025-09-03
---

## While moving lifecycle case to rescind, State value gets stuck into "rescind in progress" state. It's not moving further to the "rescinded" state

  

### Issue

While moving lifecycle case to rescind, State value gets stuck into “rescind in progress” state. It's not moving further to the “rescinded” state

### Resolution

Upon investigation, I found that this issue was happening because the "task closer" Business Rule has been customized.  
Once reverted, everything works as expected.  
  
To do so, follow the steps below.  
  
NEXT STEPS:  
  
1\. Navigate to System Definition > Business Rules  
2\. In the "Name" column search for "task closer" and go to the record  
3\. In the Versions related list, Right-Click the most recent record with the Source of "System Upgrades: glide-version..."  
4\. Select "Revert to this version"  
5\. Select OK when prompted
