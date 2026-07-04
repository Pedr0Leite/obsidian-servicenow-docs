---
title: " Determining if ADFS is receiving a signed request"
aliases:
  - KB0538765
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538765
kb_number: KB0538765
last_modified: 2025-10-21
---

## Issue

Determining if ADFS is receiving a signed request

This issue is related to an ADFS-signed SAML request. The user cannot log in or log out.

## Resolution

1.  Check with the ADFS administrator to see if ADFS enforces the signed request.
2.  If so, create a correct Java key store certificate record in SNC that includes the certificate from ADFS.
3.  Set glide.authenticate.sso.saml2.idp\_authnrequest\_url to **true** if the authentication request signing is required, and set to ADFS.Set glide.authenticate.sso.saml2.require\_signed\_logoutrequest to **true** if the log out request signing is required. Fill in the correct alias user/password and key store user/password.
4.  If necessary, re-import the SAML SP (SNC) metadata into ADFS (IDP)
