---
title: "MID Server upgrade error \"An active MID Server with a duplicate name detected\" in agent logs"
aliases:
  - KB0782337
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782337
kb_number: KB0782337
last_modified: 2024-04-08
---

## MID Server upgrade error "An active MID Server with a duplicate name detected" in agent logs

  

### Issue

-   During MID Server Upgrade, we see below error getting added to the agent logs file.  
    
    10/19/19 01:46:08 (827) StartupSequencer User \_mid\_server\_user\_i has all necessary roles  
    10/19/19 01:46:08 (921) StartupSequencer Getting instance ACLs for table: ecc\_agent  
    10/19/19 01:46:09 (358) StartupSequencer WARNING \*\*\* WARNING \*\*\* Encountered error: \[An active MID Server with a duplicate name detected.\]  
    in ensuring agent record on the instance. Retry...  
    10/19/19 01:46:09 (358) StartupSequencer Waiting to retry in 5 minutes. Attempt 1 of 3.   
    10/19/19 01:51:09 (450) StartupSequencer WARNING \*\*\* WARNING \*\*\* Encountered error: \[An active MID Server with a duplicate name detected.\]   
    in ensuring agent record on the instance. Retry...   
    10/19/19 01:51:09 (450) StartupSequencer Waiting to retry in 5 minutes. Attempt 2 of 3.
    
-   This article will demonstrate the investigations and probable use cases, hence in the future, if a similar error occurs then this can be one of the causes and worth trying to fix.

### Resolution

-   In General, there exist no mid servers which share the same name thus the error we see is for the same mid server which is upgrading. In order to fix this issue, below steps considered.  
    -   Resolve all the issues present under "MID Server Issues" tab
    -   Set the status of MID to down (if it is already not present.)
    -   Restart the Mid Server Service.  
          
        
-   Please review the below screenshot for the changes to be made.  
      
    

![](sys_attachment.do?sys_id=8440acc11b007414f34d33bc1d4bcb9e)

-   Once the suggested changes are made and MID Server Service is restarted then MID Server will initiate the upgrade and gets completed successfully.
