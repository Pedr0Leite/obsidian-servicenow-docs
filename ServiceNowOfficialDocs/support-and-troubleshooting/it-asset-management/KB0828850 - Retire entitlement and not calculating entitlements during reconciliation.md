---
title: "Retire entitlement and not calculating entitlements during reconciliation"
aliases:
  - KB0828850
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0828850
kb_number: KB0828850
last_modified: 2024-04-08
---

## Retire entitlement and not calculating entitlements during reconciliation

  

### Issue

-   How can we ensure that an entitlement record can be created but not counted or considered during reconciliation?  
      
    
-   If we retire entitlements, what happens to the allocated rights is this considered for reconciliation etc ?

### Release

-   All

### Resolution

1.  How can we ensure that an entitlement record can be created but not counted or considered during reconciliation?
2.  If you want to ignore the entitlements and installs for the related Software Model all together, then you will have to check the box for **License under management** under the software model.  
      
    ![](/sys_attachment.do?sys_id=f26770c9db88b890dc2beeb5ca96190e)  
    
3.  Is there any other way that we can avoid them being counted from reconciliation without unchecking that option on the software model 

The other option will be to retire the software entitlement.  
  

For those entitlement records which you do not want them to be included in the recon, set the end date to past date. This will retire the entitlement and set active rights to zero.   
  

Note that when the recon runs again, only those entitlements whose State = Retired, will be ignored. All other active/in use entitlements will continue to be used during recon.  
  

          4. If we retire entitlements, what happens to the allocated rights is this considered for reconciliation etc ?  
  

Only active entitlements are considered for reconciliation, retired entitlements are not counted  
  

### Related Links

1.  A new option, **License under management**, is added to the Software Models form. Use this option to indicate that you want to manage licenses for that software. If you clear the option, the software model won't be included in your reconciliation results. For upgraded software models, the license under management value is set to true by default. The value doesn't impact compliance results.  
      
    
2.  If you upgrade and have software models with this option selected, you can do a bulk update and clear the **License Under Management** option from any software models you don’t want to include in your reconciliation results. When you run reconciliation again, only the software models with the option still selected will display in your results.  
      
    
3.  To unlock the new SaaS License Management features, enable the following new plugins:  
      
    -   **SaaS License Management** (included with the Main plugin)  
          
        
    -   **SaaS License Management Integrations** (included with the Main plugin)  
          
        
    -   **Spend Detection** (you must first get the Software Spend Detection SKU at no additional cost, before you request this plugin in ServiceNow® HI)
