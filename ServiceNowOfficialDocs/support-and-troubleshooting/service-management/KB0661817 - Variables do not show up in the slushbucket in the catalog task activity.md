---
title: "Variables do not show up in the slushbucket in the catalog task activity "
aliases:
  - KB0661817
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0661817
kb_number: KB0661817
last_modified: 2024-04-07
---

## Variables do not show up in the slushbucket in the catalog task activity

  

### Issue

Variables do not show up in the slushbucket in the catalog task activity.  

  

### Cause

The Task variables column is calling a Script Include getWorkflowVariables instead of the out of the box wf\_variables().  

  

  

### Resolution

Change the attribute from custom Script Include getWorkflowVariables() to wf\_variables() in sys\_dictionary for task\_variables.
