---
title: "Execute operation on script include 'SysRelatedList' from scope 'Discovery and Service Mapping Patterns' was denied"
aliases:
  - KB0724138
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724138
kb_number: KB0724138
last_modified: 2025-06-02
---

## Execute operation on script include 'SysRelatedList' from scope 'Discovery and Service Mapping Patterns' was denied

  

### Issue

Post upgrade to London some of the Links on App scope throws error as below

"Execute operation on script include 'SysRelatedList' from scope 'Discovery and Service Mapping Patterns' was denied.  
The application 'Discovery and Service Mapping Patterns' must declare a cross scope access privilege. Please contact the application author to update their privilege requests."

Example: While a click on review Kubernetes Application which was downloaded and installed from ServiceNow Appstore, it errors as below   
  

                     ![](/sys_attachment.do?sys_id=1f715304dbe92990770be6be1396197e) 

### Release

London, Quebec

### Cause

The issue here is that they did not have the cross-scope privilege records configured correctly. 

### Resolution

-   Create  cross-scope privilege record for the Application

 Procedure : 

1.  Navigate to System Application > Application Cross-Scope Access
2.  Click on New to create a new record
3.  In the form, fill in the following data:

-   Target Scope:      Select the module "Discovery and Service Mapping Patterns"
-   Target name:       SysRelatedList
-   Target type:         Script Include
-   Status:                Allowed
