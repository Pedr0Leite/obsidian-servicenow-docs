---
title: "CSM Request Integration not supporting Case Type"
aliases:
  - KB0957522
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957522
kb_number: KB0957522
last_modified: 2025-09-03
---

## Issue

Installed “Case Types” and “CSM Integration with Request Management” plugins along with the common CSM plugins on our the customers instance

But unable to define the case type which should be used when a case is automatically created from a Request (as per the “CSM Integration with Request Management” functionality). Currently all cases created are being created at the Case table class level.

The requirement is to be able to configure this functionality to create the case instead at the table class level of one of the case type tables which are extended from the Case table class.  
  

## Resolution

  
Request creation from case was originally designed for creating base case records only. Hence there is reference to "RequestManagementIntegrationConstants" which is read only and contains a hard coded value that is used for setting the case table " RequestManagementIntegrationConstants.CASE\_TABLE = "sn\_customerservice\_case";   
  
Based on customer's se case, we can propose one of the below workarounds:  
  
1\. If customer is only creating Request where the underlying record is Case type, then you can update RequestManagementIntegrationConstants.CASE\_TABLE = "sn\_customerservice\_case"; using MAINT login, you might need assistance from ServiceNow to make this change if customer doesnt have MAINT access.

2\. Another workaround option is to create a new custom BR for e.g "Create Complaint Case from Request" and add the custom data mapping within this BR. The BR "Create Case from Request" (sys\_script\_a5b01d7d3bbb1300bfe04d72f3efc46b.xml) can be deactivated  
  
**Workaround :**  
  
Case creation from Request via portal happens through OOB business rule "Create Case For Request" (sys\_script\_a5b01d7d3bbb1300bfe04d72f3efc46b.xml)  
Above business rule, invokes the service management extension point, which create the baseline case record and maps the underlying fields.  
In order to create custom portal flow to create case type extension record from sc\_request from CSM portal, follow the below steps:  
  
_**Step 1:**_  
Created a NEW custom BR for e.g " Create Freight case for request" on sc\_request table  
Add all the custom data mapping between sc\_request and case type within this BR.  
  
_**Step 2:**_  
Set BR named "Create case for request" to not active. (sys\_script\_a5b01d7d3bbb1300bfe04d72f3efc46b.xml)  
  
_**Step 3:**_  
Portal Technical Details  
Clone widget named "sc\_catalog\_item" NEW custom widget  
Updated code on line 623 to read;  
$location.search('id=csm\_ticket&table=&sys\_id=' + a.parent\_id + '&view=);  
This line sets the redirect URL after a request is submitted through the CSM/custom portal. This line is what redirects to the case that was created by the request.
