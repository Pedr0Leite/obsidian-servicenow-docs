---
title: "Dashboard missing from the \"Publisher Overview\" page"
aliases:
  - KB0856273
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0856273
kb_number: KB0856273
last_modified: 2024-04-08
---

## Dashboard missing from the "Publisher Overview" page

  

### Issue

-   Dashboard missing from the "Publisher Overview" page

### Release

-   All

### Cause

-   Customization done on the instance, there by not showing the correct navigation URL for "Publisher Overview" as compared to OOB.  
    

### Resolution

**Steps to reproduce**:

-   Log in to the instance  
      
    
-   From the navigator type "Publisher Overview" and open it.  
      
    
-   Observe that a specific tab/s missing.  
    

  

**Resolution**:

-   Check for the "Publisher Overview" URL on your instance. It will be something like the below.  
      
    $pa\_dashboard.do?sysparm\_dashboard=75e790fce73003004c6f07d8d2f6a99e&sysparm\_cancelable=true&sysparm\_editable=false&sysparm\_active\_panel=false&sysparm\_ignore\_default\_filter=false  
      
    ![](sys_attachment.do?sys_id=16e8b0c5dbccb8d022e0fb2439961980)  
      
    
-   The "Publisher Overview" URL OOB is as below.  
      
    $pa\_dashboard.do?sysparm\_dashboard=da54a91967c1130061b452e457415a18&sysparm\_editable=false&sysparm\_active\_panel=false&sysparm\_ignore\_default\_filter=false  
      
    ![](/sys_attachment.do?sys_id=16e8b0c5dbccb8d022e0fb243996194c)  
      
    
-   Copy the OOB URL from the above and paste it on your instance, and it will load the data correctly.  
      
    
-   Update the OOB URL from above against "Arguments" in the below link to revert it back to OOB to be able to see all the dashboards.  
      
    [https://.service-now.com/sys\_app\_module.do?sys\_id=340eecf0e77003004c6f07d8d2f6a9f7&sysparm\_record\_rows=1&sysparm\_record\_scope=de723a2b93703200662714f1b47ffb69&sysparm\_record\_target=sys\_app\_module&sysparm\_record\_list=titleCONTAINSpublisher%5EORDERBYorder&sysparm\_nostack=true&sysparm\_record\_row=1](https://instance_name.service-now.com/sys_app_module.do?sys_id=340eecf0e77003004c6f07d8d2f6a9f7&sysparm_record_rows=1&sysparm_record_scope=de723a2b93703200662714f1b47ffb69&sysparm_record_target=sys_app_module&sysparm_record_list=titleCONTAINSpublisher%5EORDERBYorder&sysparm_nostack=true&sysparm_record_row=1 "https://<instance_name>.service-now.com/sys_app_module.do?sys_id=340eecf0e77003004c6f07d8d2f6a9f7&sysparm_record_rows=1&sysparm_record_scope=de723a2b93703200662714f1b47ffb69&sysparm_record_target=sys_app_module&sysparm_record_list=titleCONTAINSpublisher%5EORDERBYorder&sysparm_nostack=true&sysparm_record_row=1")  
      
    ![](sys_attachment.do?sys_id=9ae8b0c5dbccb8d022e0fb2439961981)

### Related Links

-   Check for the below plugins if installed on the instance  
      
    -   "com.snc.pa.samp" plugin for "Performance Analytics - Content Pack - Software Asset Management Professional"  
          
        
    -   "com.snc.samp.core" plugin for "Software Asset Management Professional Core"  
          
        
    -   "com.snc.sams" plugin for "Software Asset Management Foundation"  
          
        
    -   "com.snc.sam" plugin for "Software Asset Management Extensions"  
          
        
    -   "plugin com.snc.samp.microsoft" plugin for "Software Asset Management Professional for Microsoft"  
          
        
    -   "com.sn\_samp\_vmware" plugin for "Software Asset Management Professional for VMware"  
          
        
    -   "com.snc.samp.oracle" plugin for "Software Asset Management Professional for Oracle"  
          
        
    -   "com.sn\_samp\_ibm" plugin for "Software Asset Management Professional for IBM"  
          
        
    -   "com.sn\_samp\_citrix" plugin for "Software Asset Management Professional for Citrix"  
          
        
-   In certain scenarios, though everything is correct due to some missing files during the plugin installation, data or dashboards will be missing. In such cases, re-installing the plugins will fix the issue.  
      
    
-    If the case is that when the "**Publisher Overview**" is loaded and it gives a blank page without any dashboard information, there is a possibility that the property "**glide.cms.enable.responsive\_grid\_layout**" under "**sys\_properties**" table is "**false**". Update it to "**true**" and the data should be updated.
