---
title: "Query - Software Model table and Software Discovery Model tables"
aliases:
  - KB0826535
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0826535
kb_number: KB0826535
last_modified: 2024-04-08
---

## Query - Software Model table and Software Discovery Model tables

  

### Issue

-   Understand if there is a connection between the **Software model table** and **Software Discovery model tables** ?  
      
    
-   Does the **Software model table** have any impact on the **Software Discovery model table** and by that to the discovered installed softwares ?
-   We use software model table for our request management and the Software discovery model & installed software tables are populated from external discovery sources as part of the CMDB and would like to understand if these tables have any rules or scripts that we need to consider.

### Release

-   All

### Resolution

-   Discovery models are auto-populated with **install table** during the Discovery process, which is a specific piece of software installed on the CI.  
      
    
-   Then Discovery Models will be normalized according to content library. This means each install record will auto-generate a Discovery Model if there’s not an existing one. And each Discovery Model can be associated with multiple install records.  
      
    
-   While Software Model is a model that is available to users which can be purchased, where various entitlements associated with the Software Models need to be created by the customer.  
      
    
-   If you open up a Software Model record, there is a “**show matching Discovery Model**” link, which will display all the associated Discovery Models, meaning multiple Discovery Models can be associated with one Software Model.  
      
    
-   For example, a generic software model Adobe Photoshop (version = anything) will find various versions of Adobe Photoshop Discovery Models. The parameters created for Software Model (version, edition, platform, language) will define the filters when finding its Discovery Models.  
      
    
-   During our reconciliation process, we look into one software model and its entitlements, then track through its Discovery Models to install records, then license those installs.  
      
    
-   The Software Model has a **Discover Map** (DMAP).  
      
    
-   The **DMAP** dictates which Discovery Models will be mapped to the Software model during the reconciliation process.  
      
    
-   It is recommended to use the DMAP provided in the content library, however customers can create their own.  
      
    
-   Software Install Conditions can also be used to specify conditions that need to be met for an install to be mapped to a Software Model.

### Related Links

-   For more details please refer the product documentation on Software Asset Management here below  
      
    -   [Discovery Model](https://docs.servicenow.com/csh?topicname=c_DiscoveryModels.html&version=latest "Discovery Model")  
          
        
    -   [Software Model](https://docs.servicenow.com/csh?topicname=c_SoftwareAssetMgmt.html&version=latest "Software Model")
