---
title: "Create Knowledge Article Button Missing in HR Agent Workspace and Core UI"
aliases:
  - KB2633869
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2633869
kb_number: KB2633869
last_modified: 2025-11-24
---

## Create Knowledge Article Button Missing in HR Agent Workspace and Core UI

  

### Issue

The Create Knowledge Article button is not visible when viewing HR cases in HR Agent Workspace and Core UI, and the knowledge article creation process does not work as expected. Expected AI-assisted pop-ups (e.g., 'Use AI to draft this article') and relevant tasks are not appearing. The issue was observed in HR Agent Workspace, Core UI.  
  
  

### Symptoms

1\. Open HR Agent Workspace.  
2\. Navigate to any HR case (resolved or closed case).  
3\. Look for the Create Knowledge Article button.  
4\. Observe: The button is not present.  
5\. Repeat the same in Core UI for HR cases.  
6\. Observe: The button is also missing there.

### Release

Yokohama+

### Cause

The skill 'KB Generation' was not activated, and users lacked the required role 'sn\_hr\_core.basic' to view the 'Create Knowledge' UI action in HR Agent Workspace and Core UI.  
  

### Resolution

1\. Activate the 'KB Generation' skill if it is not already active.  
2\. Verify the skill configuration for 'KB Generation' to confirm it is properly set up.  
3\. If issues persist, review the skill configuration display settings in NAA.  
4\. Ensure the user has the role 'sn\_hr\_core.basic', as the skill 'KB Generation' requires this role to display the 'Create Knowledge' UI action on all HRSD products.  
5\. If the skill is active and required roles are provided, then the 'Create Knowledge' button appears in HR Agent Workspace and Core UI.
