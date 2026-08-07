---
title: "The field \"Allow automated content updates\" is not working, new content is being updated for the software models"
aliases:
  - KB1545433
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1545433
kb_number: KB1545433
last_modified: 2023-10-08
---

## The field "Allow automated content updates" is not working, new content is being updated for the software models

  

### Issue

Disabled the field "Allow automated content updates" so new content will not get updated on specific software models, post that also we can see DMAP value is getting changed by the content update.

### Cause

This field functionality is only limited to suite components and lifecycle changes to the software models, if we don't want these content changes applied to specific software models, we can clear the "Allow automated content updates" flag on the Software Model form.

### Resolution

It is working as expected the restriction on the content update is only for "suite component and lifecycle changes to the software models" not for DMAP.

The field "Allow automated content updates" is part of the Schedule job "SAM - Create lifecycles and suites for a software model"  
https://<instance-name>.service-now.com/nav\_to.do?uri=sysauto\_script.do?sys\_id=fe829c66e77013003dd10558d2f6a9e7

The scheduled job responsible for the DMAP update is "SAM - Apply latest content changes"   
https://<instance-name>.service-now.com/nav\_to.do?uri=sysauto\_script.do?sys\_id=26f6310bdb8773004fbf75868c961988

### Related Links

[SAM content Updates](https://docs.servicenow.com/bundle/vancouver-it-asset-management/page/product/software-asset-management2/concept/sam-content-updates.html)
