---
title: "Is it possible to map manager in sys_user table although no_auto_map=true ?"
aliases:
  - KB0783213
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783213
kb_number: KB0783213
last_modified: 2024-04-20
---

## Is it possible to map manager in sys\_user table although no\_auto\_map=true ?

  

### Issue

An attribute 'no\_auto\_map' exists out of the box that is meant to prevent automatic mapping of the field 'manager' in the sys\_user table when transforming data to import users into the platform

Is it possible to  disabling this attribute 'no\_auto\_map' shown in the dictionary entry of the field sys\_user.manager ?

### Resolution

Yes, this is possible to disable or remove attribute 'no\_auto\_map=true'  
  
It was set up that way out of the box because, additional coding is required to fetch the manager value from LDAP and then attempt a lookup against an existing user in Servicenow  
  
Out of the box, it is not possible to set the manger value from AD to the sys\_user.manager because this is a reference field, so the underlying real value is a sys\_id.  
  
If the field was automatically mapped, then it would fail and throw a mapping exception.  
  
It is possible to map but a little bit of additional coding is reequired to do the lookup from the name to return a Servicenow sys\_id  
  
The pre-requisite for the lookup to succeed is that the user manager name should already exist in Servicenow.
