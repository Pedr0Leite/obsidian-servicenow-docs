---
title: "Updating 'read-only' policy in files"
aliases:
  - KB0787466
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787466
kb_number: KB0787466
last_modified: 2026-05-08
---

## Updating 'read-only' policy in files

  

### Summary

ServiceNow platform has files that are Out of Box, also known as Out of Box (OOB), with protection policy set as 'read-only'. The following Script Include **ChangeRequestStateHandlerSNC.** is an example of one of those files:

**![](sys_attachment.do?sys_id=22a1519647e23a90c4e1a325126d43b2)**

![](sys_attachment.do?sys_id=e6a1519647e23a90c4e1a325126d43b7)

The 'read-only' protection policy is set for a reason and should be respected. ServiceNow sets it when users (even admins) are not supposed to modify these files. The documentation about the 'read-only' protection policy states the following: **"Select this option to allow other application developers to see your script logic, but not to change it."**

The 'read-only' protection policy is also used to protect ownership of applications but one has to understand that Global scope is special compared to Private scopes:

-   A protection policy set in the Global scope will affect all users except ‘maint’.
-   A protection policy in a private scope will only be in effect on instances where the application is installed and will not be in effect for the admin of that application on instances where the app is in development.

If you have as a requirement to apply any customization to any script that has it's protection policy set as 'read-only', the recommendation is to create your own copy of this script and modify it to your own requirements:

-   **The 'Insert and Stay' UI Action must NOT be used** as it will create a copy of the file and including its protection policy preventing you from further customizing it or even deleting it. If that happens, this duplicate file will need to be removed by ServiceNow.  
      
    
-   To avoid creating a duplicated file, admin should create a brand new record from scratch (so NOT using the 'Insert and Stay' UI Action) and copy-paste the content of the out-of-the-box script to be customized.

If any issue is found during the process described above, please contact [ServiceNow Technical Support.](http://www.servicenow.com/support/contact-support.html "ServiceNow Technical Support")

Paid applications installed from the ServiceNow store are not owned by ServiceNow. It is required in this case to contact the Vendor of the application for informations relevant to protection policies at Vendor's files. Support Contacts can be found at **store.servicenow.com** at the page of the specific application.

### Related Links

More information about the Protection Policy can be found in the documentation: [Application file protection policy](https://docs.servicenow.com/csh?topicname=c_ProtectingApplicationFiles.html&version=latest "https://docs.servicenow.com/csh?topicname=c_ProtectingApplicationFiles.html&version=latest") and [Script protection policy](https://docs.servicenow.com/csh?topicname=c_ScriptProtectionPolicy.html&version=latest "https://docs.servicenow.com/csh?topicname=c_ScriptProtectionPolicy.html&version=latest").
