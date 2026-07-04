---
title: "Per user license metric is not working as expected"
aliases:
  - KB0820586
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820586
kb_number: KB0820586
last_modified: 2024-04-08
---

## Per user license metric is not working as expected

  

### Issue

From the Software Entitlement License Metric "Per User" is not working correctly.   
The software model set to Per User and it is showing unlicensed installs with hundreds of unlicensed installs when they are actually recorded users in the results list.  
Identifying to be around 500 unlicensed installs but yet the Software Model Results shows compliant. Had to manually review the names and confirm they existed in both unlicensed installs as well as compliant list when using per user configuration.

### Cause

The Per User license metric seems to be working fine. When we use this License Metric, a single right covers all the installs for a user for the SAME software model. If you notice the results, the Software Model result has 0 unlicensed installs, however, there are unlicensed installs at the Product Result level which are for a DIFFERENT software model and that is expected. 

![](sys_attachment.do?sys_id=5e757445db80b4d0b55f0b55ca9619b7)

### Resolution

There are a couple of reasons because of which some installs are not getting covered in the SAME software model even though you might be expecting them to be included:

a. The software model has install condition to include only "Production" installs. Because of this, the non-production installs even if they belong to the same user will appear in unlicensed installs, since they can't be covered by this Software Model. 

![](sys_attachment.do?sys_id=d6757445db80b4d0b55f0b55ca9619b6)

b. Some of the discovery models are not normalized properly and do not have the Edition stamped on them. Because of this, they are not getting picked by the Software Model. To resolve this, add the Edition in the Discovery Models manually. 

![](sys_attachment.do?sys_id=9e757445db80b4d0b55f0b55ca961976)
