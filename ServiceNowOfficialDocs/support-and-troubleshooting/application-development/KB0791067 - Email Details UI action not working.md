---
title: "Email Details UI action not working"
aliases:
  - KB0791067
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791067
kb_number: KB0791067
last_modified: 2024-04-07
---

## Email Details UI action not working

  

### Issue

User with HR role is not able to use Email UI action.

popupOpenEmailClient(URL) function is being used in Email UI action which is not working.

  

### Cause

Customization of OOTB ACL:

/nav\_to.do?uri=sys\_security\_acl.do?sys\_id=4c2b9ca497603000715a390ddd2975d2

The UI action is using function popupOpenEmailClient(url);

This is an internal script to display a standard email sending popup: popupOpenEmailClient().  
  
When using this feature, we need to allow these users of the application on an ACL named: EmailClientProcessor.

  

### Resolution

Activate OOTB for EmailClientProcessor

/nav\_to.do?uri=sys\_security\_acl.do?sys\_id=4c2b9ca497603000715a390ddd2975d2

This ACL will allow user with HR writer role to use Email UI action.
