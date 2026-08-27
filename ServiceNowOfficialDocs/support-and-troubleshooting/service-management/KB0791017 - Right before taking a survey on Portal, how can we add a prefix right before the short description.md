---
title: "Right before taking a survey on Portal, how can we add a prefix right before the short description?"
aliases:
  - KB0791017
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791017
kb_number: KB0791017
last_modified: 2025-01-02
---

## Right before taking a survey on Portal, how can we add a prefix right before the short description?

  

### Summary

Right before taking a survey on Portal, how can we add a prefix right before the short description? (see screenshot)

  
  
![screenshot of survey on portal](sys_attachment.do?sys_id=723974791b554550faf255fa234bcb46)

### Release

All

### Instructions

clone the following widget and rename  
Take Survey  
/sp\_widget.do?sys\_id=d65e4495c3331200e44574e1c1d3aeb2  
In the body HTML template, modifed the following line & save:  
  
From:

<div ng-if="data.trigger\_desc" style="font-size:15px;">  
{{::data.trigger\_desc}}  
</div>

to:

<div ng-if="data.trigger\_desc" style="font-size:15px;">  
Short Description: {{::data.trigger\_desc}}  
</div>

to use the new widget in the portal, modified the following portal page:  
/sp\_instance.do?sys\_id=127e4495c3331200e44574e1c1d3ae9c  
click on the widget tab, and select the cloned widget you created from above & save
