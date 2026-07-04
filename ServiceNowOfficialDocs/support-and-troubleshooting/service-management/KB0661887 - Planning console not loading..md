---
title: "Planning console not loading."
aliases:
  - KB0661887
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0661887
kb_number: KB0661887
last_modified: 2024-04-07
---

## Planning console not loading.

  

### Issue

Planning Console is not loading. 

### Resolution

After further investigation, it seems that few errors prompted in the console upon loading the Planning Console. 

**Uncaught Error: \[$injector:modulerr\] Failed to instantiate module sn.$sp due to:**   
**Error: \[$injector:modulerr\] Failed to instantiate module oc.lazyLoad due to:**   
**Error: \[$injector:nomod\] Module 'ngTable' is not available! You either misspelled the module name or forgot to load it. If registering a module ensure that you specify the dependencies as the second argument.** 

The widget dependencies record provided below was configured to **Include on Page Load**. This, in turn, was causing the Planning Console not to load.

https://XXX.service-now.com/nav\_to.do?uri=sp\_dependency.do?sys\_id=4a0e7dd24f6f9200c664c0818110c762
