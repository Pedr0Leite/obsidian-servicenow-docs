---
title: "The reconciliation job fails | Cannot set property \"unlicensedSubscriptionCnt\" of undefined to \"NaN\""
aliases:
  - KB0960757
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960757
kb_number: KB0960757
last_modified: 2024-03-28
---

## Issue

The reconciliation job is failing to run.

  

The error from the logs:  
\=========================================================================  
TypeError: Cannot set property "unlicensedSubscriptionCnt" of undefined to "NaN"  
  
at sys\_script\_include.40563b3cc1720010fa9b3e0c6a3c493a.script:347 (anonymous)  
at sys\_script\_include.40563b3cc1720010fa9b3e0c6a3c493a.script:95 (anonymous)  
at sys\_script\_include.602e129eb0276300fa9b028ca0d3b864.script:39 (anonymous)  
at sys\_script\_include.8a6dbe2887522300ede6f64936cb0b2c.script:64 (anonymous)  
at sys\_script\_include.8a6dbe2887522300ede6f64936cb0b2c.script:172 (anonymous)  
at sys\_script\_include.8a6dbe2887522300ede6f64936cb0b2c.script:65 (anonymous)  
at sys\_script\_include.8a6dbe2887522300ede6f64936cb0b2c.script:58 (anonymous)  
at sys\_script\_include.8a6dbe2887522300ede6f64936cb0b2c.script:46 (anonymous)  
at sys\_script\_include.30bbdf9587f52300923aa75fe5cb0b97.script:331 (anonymous)  
at sys\_script\_include.30bbdf9587f52300923aa75fe5cb0b97.script:328 (anonymous)  
at sys\_script\_include.30bbdf9587f52300923aa75fe5cb0b97.script:271 (anonymous)  
at sys\_script\_include.6761b0dd0b1232001a17650d37673a77.script:107 (anonymous)  
at sys\_script\_include.6761b0dd0b1232001a17650d37673a77.script:44 (anonymous)  
at sys\_trigger.70ebd2d01bef681089a4baeedc4bcb5c:1  
\=========================================================================

## Resolution

It is a known defect under PRB1482482 and is currently being investigated.  
  
The workaround would be to modify the following lines of code in the SamUserSubscriptionLicenseCalculator script include. Please test this on subprod instance first.  
https://instance-name.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=40563b3cc1720010fa9b3e0c6a3c493a  
  
Existing code - (lines 93 to 97)  
  
if (Object.keys(rightsNeeded).length !== 0) {  
this.markUnlicensedInstallsAfterAssignment(rightsNeeded);  
this.markUnlicensedSubscriptionsAfterAssignment(rightsNeeded);  
this.generateRightsNeededByForConsumer(rightsNeeded, userInfo);  
}  
  
Change this to -  
if (Object.keys(rightsNeeded).length !== 0) {  
this.generateRightsNeededByForConsumer(rightsNeeded, userInfo);  
this.markUnlicensedInstallsAfterAssignment(rightsNeeded);  
this.markUnlicensedSubscriptionsAfterAssignment(rightsNeeded);  
}  
  
Basically, the function "generateRightsNeededByForConsumer" should be invoked first.  
After making this correction, please run a reconciliation
