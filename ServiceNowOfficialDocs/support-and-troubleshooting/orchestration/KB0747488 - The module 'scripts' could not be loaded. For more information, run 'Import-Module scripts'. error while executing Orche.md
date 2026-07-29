---
title: " The module 'scripts' could not be loaded. For more information, run 'Import-Module scripts'. error while executing Orchestration  activity"
aliases:
  - KB0747488
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747488
kb_number: KB0747488
last_modified: 2024-04-07
---

## The module 'scripts' could not be loaded. For more information, run 'Import-Module scripts'. error while executing Orchestration activity

  

### Issue

# Symptoms

-   On executing a custom orchestration workflow, an activity throws an error about the missing module. This article will demonstrate on the investigations and probable use cases, hence in future, if a similar issue is observed, then this can be one of the cause and worth trying to fix.

# Steps to Reproduce

-   Note - The below steps are applicable to impacted instance only.  
    -   Connect to the Instance
    -   Navigate to Workflow Editor
    -   Open the impacted workflow and activity.
    -   Click on Start.
    -   Once completed, navigate to Workflow All Contexts and open the related record. In the record open Workflow Log tab where see below error message

  
  

& : The module 'scripts' could not be loaded. For more information, run 'Import-Module scripts'.At line:1 char:6+ & {& 'scripts\\PowerShell\\PSScript.ps1' -computer '10.43.148.33' -sc ...+  
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+CategoryInfo : ObjectNotFound: (scripts\\PowerShell\\PSScript.ps1:String) \[\], CommandNotFoundException+ FullyQualifiedErrorId : CouldNotAutoLoadModule

# Cause

-   Insufficient privilege to the user running the MID Server service.

# Resolution

-   The error displayed is misleading. The error is not related to the custom activity but is due to permission.
-   In order to fix this issue below steps can be followed.  
      
      
    -   Verify if the module which is shown as missing in the error exists or not. If it does not exists then try adding the missing module.
    -   Verify the User used for running has sufficient permission to perform the activity. Add local admin privileges to the user to perform the intended operation.
    -   Execute the MID Server Service using Local Admin user to make it work. Refer [How to Configure Windows MID Server service credentials](https://docs.servicenow.com/csh?topicname=r_ServiceNowPlatform.html&version=latest "How to Configure Windows MID Server service credentials") for more details.

# Additional Information

-   The above steps help to fix the issue reported.
-   If even after following above steps if you still see the error then kindly reach out to ServiceNow Technical Support for further assistance.
