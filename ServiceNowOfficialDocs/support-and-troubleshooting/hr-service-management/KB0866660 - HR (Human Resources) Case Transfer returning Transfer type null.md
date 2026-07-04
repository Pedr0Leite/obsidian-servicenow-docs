---
title: "HR (Human Resources) Case Transfer returning Transfer type null"
aliases:
  - KB0866660
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0866660
kb_number: KB0866660
last_modified: 2025-12-23
---

## HR (Human Resources) Case Transfer returning Transfer type null

  

### Summary

When transferring an HR case to another HR service, we are redirected to the 'Transfer Case' ui\_page which has a Transfer type drop-down list with no values or null in it

![](sys_attachment.do?sys_id=b42c31bb47a3315077b5ab29736d4315)

### Instructions

1\. We can check if any of the Script includes mentioned below are customized and test by reverting them to OOB (out of box):

-   hr\_TransferCase
-   ReclassifyCaseTransfer
-   StandardCaseTransfer
-   HRSecurityUtils

[https://docs.servicenow.com/bundle/paris-hr-service-delivery/page/product/human-resources/concept/reclassify-hr-case.html](https://docs.servicenow.com/bundle/paris-hr-service-delivery/page/product/human-resources/concept/reclassify-hr-case.html)  
  
2\. Check if UI (user interface) Page 'Transfer Case' is customized  
  
3\. If everything is OOB, Navigate to HR Administration > Transfer Case Configuration

Check if Standard Transfer Case Configuration is de-activated. If yes, the issue is related to [KB0856404](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0856404) (must be logged into NowSupport to view)  
4\. Check for script include: HRSecurityUtils has the below script updated

getNextObjNumberPadded: function(tableName){  
        return new global.NumberManager(tableName).getNextObjNumberPadded();  
    },

5\. Please refer to the below KB for more information

[https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB1123984](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1123984)
