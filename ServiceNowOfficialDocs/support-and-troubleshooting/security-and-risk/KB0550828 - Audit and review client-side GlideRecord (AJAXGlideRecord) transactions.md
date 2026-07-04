---
title: "Audit and review client-side GlideRecord (AJAXGlideRecord) transactions"
aliases:
  - KB0550828
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550828
kb_number: KB0550828
last_modified: 2025-11-14
---

## Issue

The intended audience for this document are System Administrators, Consultants, and Partners of the ServiceNow solution with experience in system security.  
  
ServiceNow has created this article as a proactive effort to ensure customer environments are correctly configured for auditing and reviewing user access permissions for GlideRecord API calls to the ServiceNow platform.

 **Note:** This article pertains to the [client-side GlideRecord API](https://docs.servicenow.com/csh?topicname=c_GlideRecordClientSideAPI.html&version=latest "client-side GlideRecord API") utilized in components such as UI pages and client scripts. It is not to be confused with the [server-side GlideRecord API.](https://docs.servicenow.com/csh?topicname=c_GlideRecordAPI.html&version=latest "server-side GlideRecord API.")

### What is the client-side GlideRecord API?

The client-side [GlideRecord](https://docs.servicenow.com/csh?topicname=c_GlideRecordClientSideAPI.html&version=latest "GlideRecord") (formerly AJAXGlideRecord) API allows the execution of user-submitted queries in the server-side Rhino sandbox. GlideRecord can be called from components such as UI pages and client scripts to perform various record operations.  

### Why are we locking down client-side GlideRecord API?

Through client scripts, it is possible to query arbitrary data from the server through the GlideRecord API. This is similar to a server-side glide record request. Executing queries server-side is an extremely powerful and useful tool in many deployments. As we expose this functionality to the client-side requests through GlideRecord API, appropriate access permission validation is necessary on the server side before the data or command is processed.

The system property **glide.script.secure.ajaxgliderecord** on the instance is used to validate for access control lists (ACLs) to GlideRecord API calls, which enables you to query data under the logged-in user's access control rights and permission scope. For example, if the user is logged in as an ESS user who does not have permission to read the \[cmn\_location\] table, then any GlideRecord API call on his behalf would fail.  The value of the property should be set to "true".

The GlideRecord calls can originate from various places within an instance. The next section provides instructions describing how to find the GlideRecord calls in client scripts.

 **Note:** To understand the comprehensive nature and entry points of all the GlideRecord API calls and their associated transactions, perform appropriate testing on the non-production instance with the system property **glide.script.secure.ajaxgliderecord** set to **true** before making any changes to production instance.

 **Note:** ServiceNow recommends [cloning](https://docs.servicenow.com/csh?topicname=c_SystemClone.html&version=latest "cloning") over the data sets and configurations from the production instance to a non-production instance before testing.

### Identifying the GlideRecord API calls in Scripts

 **Note:** The following steps are applicable if the ACL rules for the instance users/roles have been modified from their original configuration, or if any customization was made to the instance that would enable a user who would otherwise be restricted though User Interface to retrieve instance information through GlideRecord API queries. Note that any integration scripts that are being utilized to retrieve information will fall in scope.

Potential applications that might contain scripts with GlideRecord calls include but are not limited to [client scripts](https://docs.servicenow.com/csh?topicname=client-scripts.html&version=latest "client scripts"), [UI pages](https://docs.servicenow.com/csh?topicname=r_UIPages.html&version=latest "UI pages"), [UI macros](https://docs.servicenow.com/csh?topicname=c_UIMacros.html&version=latest "UI macros"), and [Dynamic blocks](https://docs.servicenow.com/csh?topicname=t_CreateADynamicBlock.html&version=latest "Dynamic blocks") under CMS.

1.  Log in to the instance using an Administrator role.
2.  In the navigation filter, enter the desired application (for example, **Client Scripts**)**.**
3.  Click into the application. On the right-hand pane, click **Show/Hide filter** to find the appropriate records.
4.  In the condition filter, click \[**AND\]** and then \[**Script\] \[contains\] \[GlideRecord\].**
5.  Click **Run.**
6.  The result set shows all records containing **GlideRecord** calls. The script will contain the associated target table name (for example: sys\_db\_object).

 **Note:** The result set can contain entries that are default to the instance and might not require any ACL changes, if no customization was involved as mentioned in the previous note.

Next steps: Note all of the **table** names in the result set. Users running these client scripts should have the necessary access permissions on the respective tables. 

### How to validate table ACLs on an instance

ServiceNow provides administrators with interactive access-control functionality in the application through the Contextual Security Auditor plugin. This plugin helps administrators understand and evaluate the access control settings configured on the ServiceNow system tables. As described in [List of Plugins](https://docs.servicenow.com/ "List of Plugins"), this plugin is **NOT** available by default and must be requested by the customer and installed by ServiceNow Customer Support.

Instructions on how to request the Contextual Security Auditor plugin can be found on the [Activate a Plugin](https://docs.servicenow.com/csh?topicname=t_ActivateAPlugin.html&version=latest "Activating ServiceNow").

### Procedure

 **Note:** The following procedure is only an **example** on how to audit the tables (in our example, we are using sys\_db\_object) using Auditor tool, and how to read the result set. The Access controls rules should be Customer driven based on the business context. This section **ONLY** shows how to read the existing ACL rules on a particular table(s), to get insight into any potential impact that might occur after the system property(as mentioned in this article) has been set.

This procedure describes how to configure, customize, and run the **Contextual Security Auditor** application once the plugin is installed on the instance:

1.  Log in to the instance using an **Administrator** role.
2.  In the navigation filter, enter **Audit**.  
    ![](/Application_menu.JPGx)  
    
3.  Click **Audit Sets**.
4.  In the right-hand pane, click **New** to create a new audit set.  
    ![](/Audit_set.JPGx)  
     
5.  The record you create acts as a framework that contains the **Roles** versus **Targets/Assets** that are being audited.
6.  Ensure that **check** **field level security** checkbox is selected so the audit can run against a particular system table (**this example uses the table identified in the previous section**) or else the audit will be performed against all the application tables.  
    ![](/Screen%20Shot%202015-07-27%20at%203.53.49%20PM.JPGx)  
    
     **Note:** ServiceNow recommends not to run the audit against all the tables at once due to memory exhaustion that might occur as a result.
    
7.  Pick the target table that needs to be audited against. Add the users/roles in the slushbucket on the right-hand side of the pane that needs to be audited.  
    Add the users/roles under which the existing GlideRecord calls should run so you would know if that is the expected behavior.  
       
      ![](/Screen%20Shot%202015-06-18%20at%2011.49.03%20AM.JPGx)
8.  Click the **Check ESS** checkbox for non-users that have to be audited.  
    ![](/Screen%20Shot%202015-06-18%20at%2011.24.38%20AM.JPGx)
9.  Submit the record.
10.  Click **Execute now** in the desired record.
11.  Once the operation is complete, the sections **Security Audit Lines** populate themselves to show the results of the audit operation.  
     ![](/Screen%20Shot%202015-07-27%20at%204.00.26%20PM.JPGx)  
     
12.  As shown in this example result set, the **itil** role has access to the **read** operation against the **sys\_db\_object** table.
13.  Based on the results, modify the existing ACL records accordingly, if needed.  
     

## Additional Information

-   [Add a system property](https://docs.servicenow.com/csh?version=latest&topicname=t_AddAPropertyUsingSysPropsList.html "Add a system property")
-   [Apply ACLs to AJAXGlideRecord (client-side Glide record)](https://docs.servicenow.com/csh?topicname=r_ApplyACLsToAJAXGlideRecord.html&version=latest "Apply ACLs to AJAXGlideRecord (client-side Glide record)")
-   [UI\_Pages](https://docs.servicenow.com/csh?topicname=r_UIPages.html&version=latest)
-   [UI\_Macros](https://docs.servicenow.com/csh?topicname=c_UIMacros.html&version=latest)
-   [Dynamic Blocks](https://docs.servicenow.com/csh?topicname=t_CreateADynamicBlock.html&version=latest "Dynamic Blocks")
-   [Client scripts](https://docs.servicenow.com/csh?version=latest&topicname=client-scripts.html "Client scripts")
-   [Client-side GlideRecord](https://docs.servicenow.com/csh?version=latest&topicname=c_GlideRecordClientSideAPI.html?cshalt=yes "Client-side GlideRecord")
-   [Platform security](https://docs.servicenow.com/csh?version=latest&topicname=features-platform-security.html "Platform security")
