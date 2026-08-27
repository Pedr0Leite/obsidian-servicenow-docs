---
title: "\"Collect Employee Input\" HR Task Type is missing"
aliases:
  - KB0853056
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0853056
kb_number: KB0853056
last_modified: 2025-09-03
---

## "Collect Employee Input" HR Task Type is missing

  

### Issue

The user was missing the "Collect Employee Input" HR Task Type. They wanted to know why.

### Cause

This functionality comes from the "Human Resources Scoped App: Lifecycle Events" plugin (ID: com.sn\_hr\_lifecycle\_events).

### Resolution

After running some tests, it was found that even in an Out of Box (OOB) instance with the HR Scoped Application installed, the sys\_choice record for "Collect Employee Input" (collect\_Information) was not present.  
  
After installing the "Human Resources Scoped App: Lifecycle Events" plugin, however, it was noted that the sys\_choice record appeared.   
  
Therefore, it can be deduced that it is necessary for Lifecycle Events to be activated to have the ability to utilize this functionality.
