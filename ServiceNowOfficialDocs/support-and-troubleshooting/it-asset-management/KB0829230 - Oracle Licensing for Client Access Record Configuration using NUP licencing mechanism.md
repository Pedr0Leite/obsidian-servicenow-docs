---
title: "Oracle Licensing for Client Access Record Configuration using NUP licencing mechanism"
aliases:
  - KB0829230
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0829230
kb_number: KB0829230
last_modified: 2024-04-08
---

## Oracle Licensing for Client Access Record Configuration using NUP licencing mechanism

  

### Issue

-   Client Access Record for Oracle is configured on basis of Oracle instances.  
      
    
-   NUP licensing mechanism to calculate the licences.  
      
    
-   Multiple VMs hosted on single ESX.  
      
    
-   As the licensing is calculated on ESX server and not on Virtual, there is no option in client access to create record for the ESX.  
      
    
-   Understand how client access records be configured for Unique instances and if that instance is deleted then how the system will automatic create new client access record for another instance for same ESX having oracle DB running.

### Release

-   All

### Resolution

-   The client access records needs to be configured for the instance.  
      
    
-   We will license the CAL records for each instance based on the NUP minimums for the ESX host.  
      
    
-   If the instance is deleted, the CAL record will have an invalid instance.  
      
    
-   If the instance and its associated DB server install is moved to a different VM then the CAL record needs to be created for this new instance to correctly licence it.  
      
    
-   If the instance and the associated install "as is" is moved to a new VM on the same physical host then you may not need to recreate the CAL record as the instance and the install are the same.  
      
    
-   When licensing DB Server using NUP licences the users accessing each Oracle instance needs to be licensed.  
      
    
-   To support this the CAL records needs to be created for the Oracle instance that is running on the VM's.  
      
    
-   SAM will figure out the actual DB server installs that the Oracle instance is running on and the CI relationships (install->VM->ESX host)  
      
    
-   NUP minimum for the instances will be calculated based on the cores on the ESX host (25 NUP minimum per core) and will be compared with the CAL records for users accessing the instance to determine the NUP licences needed for each instance.  
      
    -   _NUP minimum : 25 x ESX cluster cores(#cpu’sxCores/cpu) x core factor  
          
        _
-   Determine and enter unique CAL records for each instance on the VM’s hosted by the ESX. Note here that if there are applications connected to the Oracle DB (called multiplexing), they need to license those users as well and add them to the CAL records.  
      
    
-   Compare the NUP minimum with the CAL records and take the greater for NUP licensing.  
      
    
-   If the VM’s move from one cluster to another, ensure that CAL records are correctly updated to reflect the unique NUP’s on each ESX cluster.  
      
    
-   Based on the number of CAL’s it has to be managed. It is proved to be more cost-efficient through multiplexing and have applications connect (with many users) to the Oracle DB.
