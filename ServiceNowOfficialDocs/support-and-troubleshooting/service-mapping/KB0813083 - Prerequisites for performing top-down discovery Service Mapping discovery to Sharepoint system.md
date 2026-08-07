---
title: "Prerequisites for performing top-down discovery / Service Mapping discovery to Sharepoint system"
aliases:
  - KB0813083
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813083
kb_number: KB0813083
last_modified: 2025-05-28
---

## Prerequisites for performing top-down discovery / Service Mapping discovery to Sharepoint system

  

### Issue

  
Following are the prerequisites for performing top-down discovery / Service Mapping discovery to Sharepoint system:

  
On your ServiceNow instance, create a Windows Credential.

This Windows credential must have:

-   WMI Query access to remote Sharepoint server
-   Permission to run http get request to the SharePoint Central Administration URL

  
Also on the ServiceNow instance, create / assign credential alias cmdb\_ci\_appl\_sharepoint to the Windows credential.

**Notes:**  
Out of the box, we don't need applicative credential, and we don't support using two separate credentials with different permissions to discover Sharepoint.  
  

However, if you want to use two separate credentials for Sharepoint top-down discovery, for example: one credential has WMI query permission, the other has permission to the Sharepoint farm, the following workaround can be used:

1.  Create a Windows credential that has WMI query access to remote Sharepoint server.
2.  Create an applicative credential with type cmdb\_ci\_appl\_sharepoint. The user used in the applicative credential should have permission to run http get request to the SharePoint Central Administration URL.
3.  In pattern Microsoft Sharepoint, section Connection to Sharepoint services, modify the EVAL script in step 10 from:  
    return com.snc.sw.util.HttpInvokerUtil.get(ctx,${CentralAdministrationURL},'');  
    to  
    return com.snc.sw.util.HttpInvokerUtil.get(ctx,${CentralAdministrationURL},'cmdb\_ci\_appl\_sharepoint');
4.  Save and publish the pattern.
