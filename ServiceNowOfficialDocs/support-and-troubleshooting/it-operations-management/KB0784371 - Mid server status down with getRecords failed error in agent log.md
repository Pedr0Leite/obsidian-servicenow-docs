---
title: "Mid server status down with getRecords failed error in agent log"
aliases:
  - KB0784371
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784371
kb_number: KB0784371
last_modified: 2025-09-30
---

## Mid server status down with getRecords failed error in agent log

  

### Issue

Mid server goes down with below errors in agent log:

getRecords failed (Method failed: (https://<instance-name>.service-now.com/ecc\_queue.do?SOAP&displayvalue=all&redirectSupported=true)HTTP/1.1 401 Unauthorized with code: 401

### Release

Any

### Cause

All the above errors indicate 401 error code / invalid credentials and bad username /password combo

### Resolution

Common Security Configuration Issues :  
  
\*Verify that the user name and password combination that is being used by the MID Server is correct. This can be accomplished by logging into the target ServiceNow instance with the same set of credentials.

  
\*Verify that the user name used by the MID Server has the mid\_server role. From the ServiceNow instance, navigate to the sys\_user record of the MID Server user and verify that the Roles related list has the mid\_server and soap roles. Without these proper roles, the MID Server will have insufficient rights when accessing the instance.

  
\*Verify that the MID Server user has sufficient rights to the required tables. Log into the ServiceNow instance as the MID Server user. Check to see if you are able to navigate to the following tables and successfully read and create records: ecc\_queue, sys\_data\_source.

  
\*If granting the MID Server user the admin role resolves the issue, then this points to an issue with ACLs on the instance.  
NOTE: Changes on the roles of the MID Server user do not take effect for an active MID Server service until it is restarted.  
  
Verifying that the Instance allows MID Server Communication  
  
\*The MID Server uses SOAP Web Service with basic authorization to communicate with the instance. Verify that System Properties > Web Services > "Require basic authorization for incoming SOAP requests" is checked

  
\*The following Scripted Web Services must be active: GetMIDInfo, InstanceInfo, MIDAssignedPackages, MIDFieldForFileProvider, MIDFileSyncSnapshot, MIDServerCheck, MIDServerFileProvider. To view the list of available scripted web services, navigate to System Web Services > Scripted Web Services

  
\*The Public Page InstanceInfo is required to allow the MID Server to validate its version. Verify that this page is active by navigating to sys\_public.list
