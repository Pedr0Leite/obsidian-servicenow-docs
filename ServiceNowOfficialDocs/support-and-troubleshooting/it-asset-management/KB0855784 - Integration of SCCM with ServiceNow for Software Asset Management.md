---
title: "Integration of SCCM with ServiceNow for Software Asset Management"
aliases:
  - KB0855784
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0855784
kb_number: KB0855784
last_modified: 2024-04-08
---

## Integration of SCCM with ServiceNow for Software Asset Management

  

### Issue

-   Integration of SCCM with Servicenow for Software Asset Management.  
      
    
-   How does the integration done for "License Reclamation" differ in terms of Discovery data and Client software distribution? 

### Release

-   All

### Resolution

-   **Microsoft SCCM 2016** plugin is required for integration.  
      
    
-   If the query is to understand a case, if there are 10 licenses that was not used for the last 6 months and if you wish to uninstall that software from the client machine, will it work directly by creating a request with Servicenow as SCCM is already integrated with it ?  
      
    
-   The response to the above is, we don't believe there is such feature as of now with **SCCM Integration**. With this **SCCM Integration**, customer can put all the relevant CI data and update or create them in the respective **CMDB\_CI** tables. On top of it, if the customer wishes to integrate the target CI and then install or uninstall a software, then it is not a part of this integration.  
      
    
-   With SCCM integration, only discovery data is populated in the Servicenow tables.  
      
    
-   During the **SCCM Integration**, customer will be providing the information like **SQL database URL** along with a **Password**. This will query the target SQL database with the SQL source provided in the import sets. Using **JDBC connectivity**, calls will be made via the **Mid Server** and all the information from the SQL database will be pulled and then placed in the respective **CMDB\_CI** tables.  
      
    
-   License comes as part of the "**Software Asset Management Professional**" plugin which cannot be mixed with the **SCCM Integration**.  
      
    
-   With **SCCM Integration**, we can only pull the data from the SQL database and can push them into the respective CMDB tables.  
      
    
-   Using **SCCM Integration** to install or uninstall a software which is not in use for a long time, can be achieved integrating SCCM with "**Orchestration"** plugin, where in one can create their own "**Workflows"** to based on their requirement (either install or uninstall a software). When the "**Orchestration"** plugin is activated, "**Client Software Distribution"** plugin gets added using which "**Reclamation"** can be performed.
