---
title: "Hardware Asset Workspace – \"Page not found\"
aliases:
  - KB2676048
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2676048
kb_number: KB2676048
last_modified: 2026-03-27
---

## Hardware Asset Workspace – "Page not found"

  

### Issue

Clicking Hardware Asset Workspace returns Page not found

### Symptoms

Navigate to Hardware Asset Workspace.

The page does not load (Page not found).

### Release

Any release

### Cause

The UX Page Registry entry for Hardware Asset Workspace was customised. That customisation broke the route registration, so the workspace URL and menu mapping no longer resolved.  
  
https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_ux\_page\_registry.do?sys\_id=e8e2fc35530130106b86ddeeff7b126f

### Resolution

Revert the record to Out-of-Box (OOB), which will resolve the issue.  
  
If the below record is missing, then add it from OOB or any other working instance

https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_ux\_page\_registry.do?sys\_id=e8e2fc35530130106b86ddeeff7b126
