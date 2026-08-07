---
title: "Not able to generate metadata  for a  particular IDP record  - Multi provider SSO"
aliases:
  - KB0792678
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792678
kb_number: KB0792678
last_modified: 2025-02-14
---

## Not able to generate metadata for a particular IDP record - Multi provider SSO

  

### Issue

Customer was not able to generate metadata from Single Sign-on properties for a particular IDP record.

By clicking on 'Generate Metadata', no metadata is seen as below :

![](sys_attachment.do?sys_id=d11f9bf0dbc434d0b55f0b55ca961927)

### Release

NA

### Cause

This appears when 'Sign AuthnRequest '/'Sign LogoutRequest' checkbox  on customer's identity provider record is true and Signing/Encryption Key Alias and Password fields are empty incorrect.

![](sys_attachment.do?sys_id=691f9bf0dbc434d0b55f0b55ca961928)

### Resolution

Uncheck the 'Sign AuthnRequest '/'Sign LogoutRequest' checkbox and hit generate metadata on the required IDP record ,we can see that the Metadata is generated .  
  

Customer must make sure that Signing/Encryption Key Alias and Password fields are updated correctly.The default OOB value for Signing/Encryption Key Alias and Signing/Encryption Key Password is saml2sp.

### Related Links

[https://community.servicenow.com/community?id=community\_question&sys\_id=7877cb69db1cdbc01dcaf3231f96197c](https://community.servicenow.com/community?id=community_question&sys_id=7877cb69db1cdbc01dcaf3231f96197c)
