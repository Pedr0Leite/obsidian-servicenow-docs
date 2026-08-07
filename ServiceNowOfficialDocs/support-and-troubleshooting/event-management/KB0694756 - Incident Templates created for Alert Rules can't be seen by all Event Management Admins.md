---
title: "Incident Templates created for Alert Rules can't be seen by all Event Management Admins"
aliases:
  - KB0694756
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694756
kb_number: KB0694756
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

There are a large number of Incident Templates which were created to be used in Alert Rules which are not visible globally by all EM Admins. Previously, Incident Templates that were created by an evt\_mgmt\_admin could be viewed by ALL users with the evt\_mgmt\_admin role. Now when viewing an Alert Rule that was uses an Incident template created by somebody besides yourself, you can not see the criteria in the INC template, but instead see "Record not found", and you can't locate the template in the list in Event Management -> Rules -> Incident Templates. 

# Release

* * *

Jakarta and above

# Cause

* * *

The cause here is the business rule "SNC Template Query" on the sys\_template table. The business rule specifically checks for three conditions based on the below line in the script :   
  
if(gs.hasRole('template\_editor\_group') || gs.hasRole('template\_editor')){   
//User can read templates for themselves, their groups, or global   
           answer =  'global=true^ORuser=javascript:gs.getUserID()^ORgroup=javascript:getMyGroups()';   
  
If the global is true or if the user himself created the template or if the user is part of the same group of the user who created the task template.   
  
The business rule is OOTB. 

# Resolution

* * *

1.This is OOTB behavior and is working as designed

2.modify the business rule or make sure the conditions in the BR are satisfied or deactivate the business rule based on your requirement as fix. 

#
