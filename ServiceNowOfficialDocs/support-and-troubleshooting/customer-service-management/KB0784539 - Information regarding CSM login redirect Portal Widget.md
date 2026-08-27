---
title: "Information regarding \"CSM login redirect\" Portal Widget"
aliases:
  - KB0784539
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784539
kb_number: KB0784539
last_modified: 2025-04-04
---

## Issue

Why "CSM login redirect" widget is introduced in NewYork and what impact it might have if we left it deactivated?

## Resolution

The widget 'CSM login redirect' is being used in csmlogin page.  
If a user tries to access any page which required login they will be redirected to the portal default login page (i.e) csmlogin  
when a user logs into the portal through csmlogin page after the successful authentication through the 'login' widget we can redirect the user to any page that we desire by setting the session storage cache values. If no value is present then it will be automatically redirected to portal default home page (i.e) csmindex  
This widget's purpose is only to redirect the user to desired page after login authentication
