---
title: "SAM Pro Entitlement Import workspace missing \"New\" button due to modified Action Assignment (sys_declarative_action_assignment)"
aliases:
  - KB2711629
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2711629
kb_number: KB2711629
last_modified: 2026-01-11
---

## Issue

→ In Software Asset Workspace → License Operations → Licensing → Entitlement import, the New button is missing, preventing manual entitlement import creation in the workspace UI

## Resolution

→ Navigate to the affected area and confirm the behavior  
→ Software Asset Workspace → License Operations → Licensing → Entitlement import

→ Validate the action assignment record  
→ Open the record below and verify it matches OOB configuration (not pointing to an incorrect/custom version)  
→ `https://<instance_name>.service-now.com/nav_to.do?uri=sys_declarative_action_assignment.do?sys_id=17c13e7273131010a0a79329faf6a794`

→ Restore OOB behavior  
→ Revert the impacted `sys_declarative_action_assignment` record back to OOB/default (or correct it to reference the proper OOB action) using your standard change process  
→ Refresh the workspace and validate the New button is restored
