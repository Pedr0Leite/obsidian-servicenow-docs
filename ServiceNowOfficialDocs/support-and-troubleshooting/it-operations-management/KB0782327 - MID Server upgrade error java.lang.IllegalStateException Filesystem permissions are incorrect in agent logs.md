---
title: "MID Server upgrade error \"java.lang.IllegalStateException: Filesystem permissions are incorrect\" in agent logs"
aliases:
  - KB0782327
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782327
kb_number: KB0782327
last_modified: 2024-04-08
---

## MID Server upgrade error "java.lang.IllegalStateException: Filesystem permissions are incorrect" in agent logs

  

### Issue

-   During MID Server Upgrade, the below error is displayed in agent logs.  
    
    10/19/19 01:21:12 (244) StartupSequencer User \_mid\_server\_user\_i has all necessary roles  
    10/19/19 01:21:12 (307) StartupSequencer SEVERE \*\*\* ERROR \*\*\* Cannot read file: E:\\Program Files\\MID Server Prod\\agent\\export\\asset  
    10/19/19 01:21:12 (307) StartupSequencer SEVERE \*\*\* ERROR \*\*\* test failure  
    java.lang.IllegalStateException: Filesystem permissions are incorrect  
    at com.service\_now.mid.services.StartupSequencer.runTests(StartupSequencer.java:400)  
    at com.service\_now.mid.services.StartupSequencer$Starter.run(StartupSequencer.java:349)
    
-   This article will demonstrate the investigations and probable use cases, hence in the future, if a similar error occurs then this can be one of the causes and worth trying to fix.

### Cause

-   This error is mainly caused due to insufficient permissions/roles assigned to the MID Server Service User. 
-   During Upgrade when MID Server tries to access the folder but as it has insufficient privileges, it throws the permission error.

By default, the MID Server service runs as a **Local System** account. This account only grants access to the machine on which the MID Server is running, not to other systems on the network. Therefore, you must change the service credentials to one of the following types:

-   A Domain User account. This account should have local admin rights to allow automatic MID Server upgrade.
-   A specific user account that has local admin access to the MID Server machine as well as access to other systems on the network.

### Resolution

-   In this case, the error is thrown while accessing the content of folder C:/ServiceNow/.../export/asset.
-   This is a custom folder and not part of the OOTB installation. Thus to fix this error, below 2 approaches can be considered.  
      
    1.  Providing MID Server user sufficient permissions to access the content of the "export" folder so that the upgrade will continue.
    2.  Deleting the folder >> content inside it and restarting the MID Server Service to initiate the upgrade process.

Note: As this is a custom folder, the contents of the folder are used by various integrations. Thus if the folder is deleted or content is removed then the associated integrations may fail. Thus it is always good to restore the content once the upgrade is complete.

### Related Links

[Configure Windows MID Server service credentials](https://docs.servicenow.com/csh?topicname=r_ServiceNowPlatform.html&version=latest "Configure Windows MID Server service credentials")
