---
title: "Canceling an HR case via Virtual Agent"
aliases:
  - KB1648393
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1648393
kb_number: KB1648393
last_modified: 2025-09-03
---

## Canceling an HR case via Virtual Agent

  

### Issue

Within HRSD Case management there are HR services which get associated to any given case. The HR service records have a field named "Case Options". One of the possible options is "User Cannot Cancel". In the Native and Workspace UI, applying this option will prevent the "Opened for" user from canceling the HR Case themselves. This KB will go over how this "prevent cancel" functionality works and how to respect the functionality when creating a Virtual Agent Topic that allows users to cancel an HR Case.

### Resolution

If we want to respect the same "Prevent Cancel" functionality when creating a VA Topic for HR Case management we should follow the same logic that is applied to the "Cancel" UI action that is attached to the HR Case table.  
  
The Cancel UI Actions visibility calls an API that will handle the logic for us. Here is the API: "sn\_hr\_core.hr\_Case().canCancelCase()"  
  
Within Virtual agent designer, upon adding any button or options for the user to cancel an HR case we want to make a call to the above mentioned API before populating an option to cancel an HR Case. This will allow the VA topic to match the behavior of the existing HR Case form UIs.

### Related Links

Here is an example of using the HR API to respect the "Prevent cancel" functionality in a VA topic. See lines 12-15 of the script for usage.

![](/sys_attachment.do?sys_id=d23945c647cbc210c4e1a325126d43ca "Screenshot 2024-06-28 at 11.02.43 AM.png")
