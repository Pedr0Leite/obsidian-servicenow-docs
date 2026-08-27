---
title: "Update the logo and HTML content on the PDF Summary of the Work Order"
aliases:
  - KB0957795
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957795
kb_number: KB0957795
last_modified: 2024-02-23
---

## Update the logo and HTML content on the PDF Summary of the Work Order

  

### Issue

In Field Service Work Order. When we Sign and Confirm the work order then it generates a PDF Summary and attached it to the work order.

1.  Can we change the ServiceNow logo on the PDF Summary document? 
2.  Can we modify what content is displayed in the PDF Summary?

### Release

Paris

### Resolution

Yes, It Is Possible but you have to customize the OOB Script Includes "GeneralWOForm" in order to achieve this requirement.

-   1A. Line 45  
    this.headerImage = instance + "Print-logo-workorder.jpgx";  
    Coming from the "db\_image\_list" table.  
      
    
-   2A. parsedBody - Line 162  
    Go through with the code and Update the HTML parts.
