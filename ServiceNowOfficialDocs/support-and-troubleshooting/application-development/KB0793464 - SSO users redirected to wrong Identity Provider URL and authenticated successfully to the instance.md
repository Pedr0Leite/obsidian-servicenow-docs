---
title: "SSO users redirected to wrong Identity Provider URL and authenticated successfully to the instance"
aliases:
  - KB0793464
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793464
kb_number: KB0793464
last_modified: 2025-01-22
---

## SSO users redirected to wrong Identity Provider URL and authenticated successfully to the instance

  

### Issue

Users redirected to the deactivated Identity Provider URL and able to login successfully with the deactivated Identity Provider instead of the newly configured Identity Provider URL.

Example : Multi Provider SSO configuration keeps sending users to ADFS Identity Provider record, instead of the newly created Microsoft Azure Identity Provider record.

### Release

All

### Cause

Script Include **SAML2\_update1** was customised on customer instance and was causing the issue.

### Resolution

Reverting the **SAML2\_Update1** script include to out of the box fixed the issue.
