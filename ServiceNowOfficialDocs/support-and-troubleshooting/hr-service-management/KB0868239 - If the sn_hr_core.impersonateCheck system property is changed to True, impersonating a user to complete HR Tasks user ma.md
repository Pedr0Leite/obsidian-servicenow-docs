---
title: "If the sn_hr_core.impersonateCheck system property is changed to True, impersonating a user to complete HR Tasks user may find themselves unable to access some data"
aliases:
  - KB0868239
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0868239
kb_number: KB0868239
last_modified: 2025-09-03
---

## If the sn\_hr\_core.impersonateCheck system property is changed to True, impersonating a user to complete HR Tasks user may find themselves unable to access some data

  

### Issue

A client script was not populating the fields as expected for a HR Task on HR Portal.

Customer was impersonating the user that the task is assigned to  
Opening the HR Service Portal (in nav) or /hrportal  
Go to My HR To-dos  
Click on the task in the list

In a reference field they had the option to select a user, you can pick any user.  
  
Expected:

The client script populates the other fields automatically based on this user.

Actual:

Nothing populated.

It seems the issue was happening only when impersonating due to the above system property. When the user actually logs into instance (as opposed to impersonating), this issue should not happen even if the property is set to true.

### Release

ALL

### Cause

The HR impersonate check system property was set to true in the customers instance. This property makes sure that users can access HR information only when they actually log into the instance and prevents the access if impersonating.  
  
https://<instancename>.service-now.com/nav\_to.do?uri=sys\_properties.do?sys\_id=7a5330019f22120047a2d126c42e70f0  
  
  

### Resolution

Please follow PRB1733328 for more information.

The issue was fixed in the Xanadu release. 

Workaround:

After setting this property to false, can no longer reproduce the issue.
