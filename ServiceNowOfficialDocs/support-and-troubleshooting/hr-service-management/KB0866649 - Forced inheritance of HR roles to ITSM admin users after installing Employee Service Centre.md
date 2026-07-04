---
title: "Forced inheritance of HR roles to ITSM admin users after installing Employee Service Centre "
aliases:
  - KB0866649
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0866649
kb_number: KB0866649
last_modified: 2024-04-08
---

## Issue

After installing mployee Service Centre roles forced inheritance of HR roles to ITSM admin users.  
Employee Service Centre roles ("sn\_hr\_sp.admin" and "sn\_hr\_sp.esc\_admin") are forced inheritance to admin and those admin users are unable to remove them (they get the message "delete is protected"). 

Same thing for happens for Lifecycle Event roles (« sn\_hr\_le… ») as well.

How to fix this.

## Resolution

Below are 2 different solutions to remove sn\_hr\_sp.esc\_admin role from admin role.  
  
**Note: _Before following below steps ensure that someone else in the organisation has the Employee Service Center administrator \[sn\_hr\_sp.esc\_admin\] role._**  
  
Proposed Solution 1:  
1\. Log in as admin.  
2\. Go to below sys\_user\_role\_contains record:

nav\_to.do?uri=%2Fsys\_user\_role\_contains.do%3Fsys\_id%3D7f9ee708e0242300964ff00a1bf36735%26sysparm\_view%3D%26sysparm\_record\_target%3Dsys\_user\_role\_contains%26sysparm\_record\_row%3D3%26sysparm\_record\_list%3Drole%3D2831a114c611228501d4ea6c309d626d%26sysparm\_record\_rows%3D7  
  
3.1 Go to Settings from top right Corner.  
3.2 Click Developer  
3.3 In Application choose "Human Resources: Service Portal"  
4\. Delete the above record.  
  
Proposed Solution 2:  
1\. Log in as admin.  
2\. From User Administration, go to Roles (left navigation menu).  
3\. Click admin.  
4\. From the Contains Roles tab, click Edit.  
5\. Change the scope of instance to "Human Resources: Service Portal"  
5.1 Go to Settings from top right Corner.  
5.2 Click Developer  
5.3 In Application choose "Human Resources: Service Portal"  
6\. From the Contains Roles List column, highlight and move sn\_hr\_core.admin to the Collection column.  
7\. Click Save.  
  
 **NOTE : _Please apply these steps in a non-prod instance & test before applying them on prod instance._**
