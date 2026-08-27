---
title: "While changing Assigned to field for Assets we get the error Asset 'Assigned to' is was cleared due to asset state changing."
aliases:
  - KB0830120
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830120
kb_number: KB0830120
last_modified: 2026-05-22
---

## While changing Assigned to field for Assets we get the error Asset 'Assigned to' is was cleared due to asset state changing.

  

### Summary

The assigned to field does not get updated because of the below out of the box business rule set on asset table:  
Clear Assigned To on update  
https://<instance-name>.service-now.com/sys\_script.do?sys\_id=594e2e93ef02200035c61ab995c0fb59  
  
The business rule will trigger whenever Assigned to value is present or is updated and State is 'On Order','In Stock' and 'In Transit'. In other words, if the State \[install-status\] of the asset is 'On Order','In Stock' and 'In Transit' it will not allow to update the 'Assigned to' field.  
  
A quick fix would be to set the State to anything other than 'On Order','In Stock' and 'In Transit', likewise, put the state of the asset to 'In maintenance' or 'In use' and change the 'Assigned to' field.
