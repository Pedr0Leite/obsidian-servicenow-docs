---
title: "Role delegation is not working as expected"
aliases:
  - KB0662219
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0662219
kb_number: KB0662219
last_modified: 2026-07-02
---

## Issue

On-Call Scheduling shows the role delegation not working.   
  

## Resolution

When a role is delegated, a change request is automatically created to handle the delegation. In an OOB instance there is a workflow called **Delegate roles to group member** which automates this process. The link below shows the workflow:   
  
/nav\_to.do?uri=wf\_workflow\_version.do?sys\_id=2add7c240a0a0b8200a2946d20749a92%26sysparm\_view=new\_workflow   
  
This workflow was not present in the affected instance. Due to this, the change process was not completing and the role was not delegated out as expected.
