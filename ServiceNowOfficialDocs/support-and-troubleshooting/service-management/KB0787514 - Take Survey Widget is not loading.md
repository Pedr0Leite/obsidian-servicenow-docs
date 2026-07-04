---
title: "\"Take Survey\" Widget is not loading"
aliases:
  - KB0787514
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787514
kb_number: KB0787514
last_modified: 2024-04-08
---

## "Take Survey" Widget is not loading

  

### Issue

"Take Survey" Widget is not loading

### Resolution

This issue is caused when customizations are made to (SPSurveyAPI) script include below:  
https://XXInstanceNameXX.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=5c2bd381c3331200e44574e1c1d3aee4  
  
Reverting this Script Include to the latest OOB version available resolves this issue.
