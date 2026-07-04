---
title: "Unable to view the 'Expected end ' field on work order form"
aliases:
  - KB0856162
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0856162
kb_number: KB0856162
last_modified: 2024-04-08
---

## Unable to view the 'Expected end ' field on work order form

  

### Issue

-   On the work order form ( wm\_order ) unable to view the field ' Expected End ' or ' Estimated End ' fields together 
-   Either one of them is hidden when the other is visible on the form

### Resolution

-   On the work order form , among the two fields ' Estimated End ' and ' Expected End ' only one of them is visible.
-   There is a client script ' Hide End Date Fields ' which sets the field's Display to false based on the Process cycle the application is running on
    
    https://<instance\_name>.service-now.com/sys\_script\_client.do?sys\_id=3f524b67c333210081d7dccdf3d3aeb3&sysparm\_record\_target=sys\_script\_client&sysparm\_record\_row=1&sysparm\_record\_rows=1&sysparm\_record\_list=scriptCONTAINSexpected\_end%5EORDERBYorder
    
      
    
-   The Expected end is visible when the 'request-driven ' is set , and the estimated end field is visible when ' task driven '.  
    
-   https://<instance\_name>.service-now.com/$sm\_config.do?sysparm\_application=Field%20Service&sysparm\_app\_name=field\_service&sysparm\_title=Field%20Service
-   Based on customer's requirement the process cycle can be set or customize the client script to have both the fields visible , but this will be considered as customization.

### Related Links

STEPS TO REPRODUCE :

-   Hop into the instance 
-   Navigate to ' wm\_order ' table
-   Users will be able to view only one of the field , either Estimated end or Expected end
