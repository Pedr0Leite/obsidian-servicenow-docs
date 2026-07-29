---
title: "Activated \"Change Management - Standard Change Catalog\" plugin and custom Change workflows broke"
aliases:
  - KB0715930
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715930
kb_number: KB0715930
last_modified: 2024-04-07
---

## Activated "Change Management - Standard Change Catalog" plugin and custom Change workflows broke

  

### Issue

# Symptoms

* * *

-   After activating the "Change Management - Standard Change Catalog" plugin (com.snc.change\_management.standard\_change\_catalog), custom Change workflows are no longer working as expected

# Release

* * *

Jakarta Patch 9c

# Cause

* * *

When the above plugin was activated, the "Change Management - Core" plugin was also activated, which added three new Change types to the user's system (other than their previously utilized custom types).  
  
Now, there are identically named entries for two of the three Change types (two "Standard" and two "Normal" sys\_choice records, all of which are active = true).

# Resolution

* * *

After a thorough investigation, no issue was found with the design or functionality of the user's custom "Standard Change" workflow.  
  
In fact, a workflow successfully attaches to a Change Request when either the non-current/non-OOB "Standard" Change type or the current OOB "Standard" Change type is used.  
  
The only time an issue arises is when _both_ "Standard" sys\_choice Change types are active = true. This is the when the unexpected behavior is experienced.  
  
When one or the other is deactivated, there is no issue. The user just needs to be sure that the desired active = true sys\_choice Change type is the same as selected in the relevant Workflow's conditions.
