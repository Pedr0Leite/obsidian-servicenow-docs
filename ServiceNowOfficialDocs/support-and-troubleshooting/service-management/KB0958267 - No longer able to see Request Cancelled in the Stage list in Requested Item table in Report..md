---
title: "No longer able to see \"Request Cancelled\" in  the Stage list in Requested Item table in Report."
aliases:
  - KB0958267
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0958267
kb_number: KB0958267
last_modified: 2025-01-02
---

## No longer able to see "Request Cancelled" in the Stage list in Requested Item table in Report.

  

### Summary

No longer able to see “Request Cancelled” in the Stage list in Requested Item table in Report.

### Release

Paris Patch 4

### Instructions

  
1.This is a defect and a PRB has been created for this.  
  
Most Probable Cause:  
The plug in "Cloud Provisioning and Governance" after getting installed removes the "Request Cancelled" option from the drop down list in the sc\_req\_item.list.  
  
2.This is an intermittent issue and we have created a PRB for this PRB1484399. The product team will work on this and get this fixed in the future releases.  
  
  
  

### Related Links

Workaround:

  
Please follow the steps below to access the "Request Cancelled "stage.  
1.Type context in the filter then click on show related fields in the drop down.  
2.Then click on "Context==> Workflow context fields" from the drop down.  
3.Then click "stage" in the drop down and you can now search "Request Cancelled " as an option. for example stage is "Request Cancelled"  
4\. You will now be able to filter your records based on the stage "Request Cancelled"
