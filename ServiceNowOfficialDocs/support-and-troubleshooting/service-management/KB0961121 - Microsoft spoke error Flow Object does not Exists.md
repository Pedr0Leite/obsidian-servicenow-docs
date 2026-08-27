---
title: "Microsoft spoke error: Flow Object does not Exists"
aliases:
  - KB0961121
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961121
kb_number: KB0961121
last_modified: 2024-03-30
---

## Microsoft spoke error: Flow Object does not Exists

  

### Issue

When trying to use the code snippet option from the Post a Message (Microsoft Teams Spoke) , the error 'Flow Object does not Exists' is observed. 

### Cause

When clicked on the code snippet option on the action and execute this code in background script with respective inputs, we get the exception "Flow Object does not Exists"

When reviewed this code, we could see the action is called with internal name and NOT the actual name. When checked the "post a message" action from the Flow designer , we could see the internal name is empty.  In general, this should have the value "post\_a\_message"

As we are calling the action with internal name which doesn't exist on the action , we get this exception "Flow Object does not Exists"

### Resolution

We need to manually update the internal name on the table sys\_hub\_action\_type\_definition table to the correct value. Go to the sys\_hub\_action\_type\_definition table --> filter for the action --> make sure the internal name column is added to list of fields --> change the name to "post\_a\_message"

Incase you were prompted with any security exceptions while doing this field update, please check for any ACL's which are restricting this update. Suggest to perform this update with admin role
