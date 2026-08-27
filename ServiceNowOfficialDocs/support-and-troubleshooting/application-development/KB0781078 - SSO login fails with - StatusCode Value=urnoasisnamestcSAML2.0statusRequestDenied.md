---
title: "SSO login fails with - StatusCode Value=\"urn:oasis:names:tc:SAML:2.0:status:RequestDenied"
aliases:
  - KB0781078
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781078
kb_number: KB0781078
last_modified: 2024-04-07
---

## SSO login fails with - StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:RequestDenied

  

### Issue

SSO login fails for some users but works for others .

Checking the logs on the instance, the below error is seen :

Error SAML2Error: SAML failed to login, Status code is urn:oasis:names:tc:SAML:2.0:status:Responder. When it is supposed to be urn:oasis:names:tc:SAML:2.0:status:Success SAML2

SAML Response contains the below status code :

<samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Responder"><samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:RequestDenied" /></samlp:StatusCode>

### Cause

This is a user specific issue on the ADFS/IDP end .

### Resolution

Please contact the IDP admin to check why the status code "RequestDenied" is sent for specific users (could be specific to user profile permissions . )
