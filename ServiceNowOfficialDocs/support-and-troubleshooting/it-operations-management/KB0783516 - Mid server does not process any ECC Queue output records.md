---
title: "Mid server does not process any ECC Queue output records"
aliases:
  - KB0783516
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783516
kb_number: KB0783516
last_modified: 2026-06-19
---

## Mid server does not process any ECC Queue output records

  

### Issue

-   The MID Server is up and validated, still it does not process any ECC queue Output records with State 'ready'. Also, no traces related to this issue are reported under agent or wrapper logs.  
      
    ![](sys_attachment.do?sys_id=ee5d6b38db807890dc2beeb5ca9619c4)

### Release

ALL

### Cause

-   OOB Scripted Web Service \[sys\_web\_service\] records related to the mid servers were customized and these files have not been upgraded and skipped during the instance upgrade.  
      
    -   InstanceInfo
    -   GetMIDInfo
    -   MIDAssignedPackages
    -   MIDFieldForFileProvider
    -   MIDFileSyncSnapshot
    -   MIDServerCheck
    -   MIDServerFileProvider

### Resolution

-   It is recommended, not to modify or delete the scripted web services records. In order to fix this issue, the below steps can be followed.  
      
    -   Revert the mid server related customized Scripted Web Service records to the OOB version.
    -   Restart the mid server.  
          
        
-   The ECC queue output records will be picked up by the mid server and processed successfully.

### Related Links

-   [MID Server configuration](https://docs.servicenow.com/csh?topicname=c_MIDServerConfiguration.html&version=latest "MID Server configuration")
-   [Scripted Web Services](https://instance_name.service-now.com/sys_web_service_list.do?sysparm_query=nameINInstanceInfo%2C%20GetMIDInfo%2C%20MIDAssignedPackages%2C%20MIDFieldForFileProvider%2C%20MIDFileSyncSnapshot%2C%20MIDServerCheck%2C%20MIDServerFileProvider&sysparm_first_row=1&sysparm_view= "Scripted Web Services")
