---
title: "Update Sets were applied to instance however the previous flow version is executed"
aliases:
  - KB0954685
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0954685
kb_number: KB0954685
last_modified: 2025-11-17
---

## Issue

-   Update set(s) were applied on the instance however previous flow or flow action are being executed
-   from the "Test" button in the designer, the latest version is executed, the reason being is that force recompilation happens
-   Republishing flow or action does not resolve this issue

## Resolution

var gr = new GlideRecord("sys\_hub\_action\_type\_definition");  
gr.get("<sys\_id>");  
gr.setValue("latest\_snapshot", gr.getValue("master\_snapshot"));  
gr.setWorkflow(false);  
gr.update();  
  
gr = new GlideRecord("sys\_hub\_flow");  
gr.get("<sys\_id>");  
gr.setValue("latest\_snapshot", gr.getValue("master\_snapshot"));  
gr.setWorkflow(false);  
gr.update();
