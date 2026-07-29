---
title: "Single Sign On Test connection is successful but  during actual login user is immediately redirected to logout"
aliases:
  - KB0785340
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785340
kb_number: KB0785340
last_modified: 2024-04-08
---

## Single Sign On Test connection is successful but during actual login user is immediately redirected to logout

  

### Issue

Single Sign On Test connection is successful but during actual login user is immediately redirected to logout

### Cause

Checking the system logs if you see the below error:

2019-11-14 11:35:33 (799) Default-thread-13 F48220FA1B498810D764759D1E4BCB71 txid=4492e4fa1b49 WARNING \*\*\* WARNING \*\*\* Evaluator: org.mozilla.javascript.EcmaError: "sessionIndex" is not defined.  
Caused by error in Installation Exit: 'MultiSSO' at line 1  
\==> 1: gs.include("PrototypeServer");  
2:  
3: gs.include("MultiSSO\_SAML2\_Update1");  
4: gs.include("MultiSSO\_DigestedToken");

This indicates that SAML response does not contain "sessionIndex"  
Sample attribute in SAML response that contains the SessionIndex  
<saml2:AuthnStatement AuthnInstant="2019-11-15T20:05:07.158Z" SessionIndex="SNCf58ab2979adc3a4d30fa487bafb0847b">

### Resolution

Check with the  IDP admin and make sure that sessionindex is returned in the SAML response.
