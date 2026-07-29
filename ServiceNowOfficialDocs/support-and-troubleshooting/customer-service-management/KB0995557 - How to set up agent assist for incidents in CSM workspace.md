---
title: "How to set up agent assist for incidents in CSM workspace ?"
aliases:
  - KB0995557
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0995557
kb_number: KB0995557
last_modified: 2025-03-31
---

## How to set up agent assist for incidents in CSM workspace ?

  

### Issue

When making an incident form layout in the workspace\_uib (CWF Workspace Integrations scope), how can we make the Contextual search results available for incidents in the CSM Workspace (only CSM workspace visible is the CSM Configurable workspace)?

### Resolution

This can be achieved in the agent assitant screen by adding the incident table to the screen condition.

sys\_ux\_screen record: /nav\_to.do?uri=sys\_ux\_screen.do?sys\_id=7b93d16453c3101043d7ddeeff7b1211

Modify the Screen Conditon

from :

parent.table=sn\_customerservice\_case  
  
to :

parent.table=sn\_customerservice\_case^ORparent.table=incident
