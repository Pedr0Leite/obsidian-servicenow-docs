---
title: "Safe Workplace QR code with no valid date"
aliases:
  - KB0869458
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869458
kb_number: KB0869458
last_modified: 2023-12-01
---

## Safe Workplace QR code with no valid date

  

### Issue

When a "health verification" record is submitted via producer" it does not show the valid to date.

### Release

Orlando Patch 7

### Resolution

OOB, it is already configured with script and flow. Below is the product document that gives us more information on how it works.  
  
Below is the Health and Saftey Requirement record that requires activation and there is also a flow 'Employee Health Verification Requirement' linked to it.  
https://OOBINSTANCE.service-now.com/sn\_imt\_core\_health\_and\_safety\_requirement.do?sys\_id=de3151dac1111010fa9b0669111834d0  
https://OOBINSTANCE.service-now.com/$flow-designer.do?sysparm\_nostack=true#/flow-designer/7e8115dac1111010fa9b0669111834f3  
  

By default, the flow is set to Inactive and need to be activated.

### Related Links

https://docs.servicenow.com/bundle/orlando-hr-service-delivery/page/product/employee-readiness-core/task/create-readiness-requirement.html
