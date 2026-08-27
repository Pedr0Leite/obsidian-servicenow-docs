---
title: "custom Field shows in workspace view in backend but missing from agent workspace"
aliases:
  - KB0996728
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996728
kb_number: KB0996728
last_modified: 2024-08-27
---

## custom Field shows in workspace view in backend but missing from agent workspace

  

### Issue

custom Field shows in workspace view in backend but missing from agent workspace

### Cause

Custom UI policy on section  
Therefore, the problem here is not with the Agent Workspace, rather with UI 16, which is unable to hide it.  
  
  

### Resolution

UI16 is not able to hide it properly because the field is added twice on the form layout. If you just add the field only once on the form layout, the UI Policy will work fine also on UI16 and the field will be hidden.  
  
On the other hand, if the customer just wants this field to be visible, please ask them to disable the UI Policy.
