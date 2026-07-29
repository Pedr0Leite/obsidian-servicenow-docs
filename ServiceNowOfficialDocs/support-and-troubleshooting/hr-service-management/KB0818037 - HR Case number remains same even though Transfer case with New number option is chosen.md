---
title: "HR Case number remains same even though \"Transfer case with New number\" option is chosen"
aliases:
  - KB0818037
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818037
kb_number: KB0818037
last_modified: 2025-09-03
---

## HR Case number remains same even though "Transfer case with New number" option is chosen

  

### Issue

When we use option transfer case in HR cases, the record is actually getting transferred but the number field remains same. Steps are as in below,

 Steps to Reproduce:

-   Impersonate as any HR user.
-   Go to All HR Cases and try to create one.
-   Upon the case creation click on "Transfer case".
-   We can see a dialog box that renders the type of transfer.
-   Choose the "transfer case with new number", we can see the new case number is created with the same old case number but with a different sys\_id.

### Release

Any Instance where HR application is installed

### Cause

Custom Business rule has set the Number again to the transferred case number which has the following code,

**current.number = current.transferred\_from.number;**

### Resolution

Consider checking all the artifacts available related to the Transfer case Functionality to be OOTB,

1.  StandardCaseTransfer - Script Include.  
    https://<instance>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=428f23fa3b4c33003585802b13efc484
2.  hr\_TransferCase - Script Include,  
    https://<instance>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=32678a3453b72300ff25ddeeff7b1213
3.  HR Transfer case configurations, check whether they are OOTB   
    https://<instance>.service-now.com/sn\_hr\_core\_transfer\_case\_config\_list.do?sysparm\_query=&sysparm\_view=
4.  hr\_TemplateUtils - Script Include.  
    https://<instance>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=d9f16db02f321200b3c9a310c18c959e
5.  Transfer Case, UI action  
    https://<instance>.service-now.com/nav\_to.do?uri=sys\_ui\_action.do?sys\_id=c83e5ca42f131200b3c9a310c18c959d
6.  Check the "Task" field dictionary setting and found to be similar to OOTB,  
    https://<instance>.service-now.com/nav\_to.do?uri=sys\_dictionary.do?sys\_id=4aa902710f11310001024ebce1050e30%26sysparm\_view=advanced
7.  Check all the before Insert Business rules running on sn\_hr\_core\_case table and check if there are any custom code which is setting the number back to the same number.
8.  Deactivate the custom code that sets the HR case number.
