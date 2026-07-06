---
title: "Errors: \"AudienceRestriction validation failed. No matching audience found sending users\" to external_logout_complete.do"
aliases:
  - KB0787186
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787186
kb_number: KB0787186
last_modified: 2025-07-11
---

## Errors: "AudienceRestriction validation failed. No matching audience found sending users" to external\_logout\_complete.do

  

### Issue

Customer reports they are not using SSO / Multi-Provider SSO yet when a user try to access ServiceNow instance in browser, user is redirected to external\_logout\_complete.do page stating below message on screen:

\=============

Logout Succeeded

**Logout Successful**

You have successfully logged out.

\=============

### Release

Applicable to all releases

### Cause

SSO / Multi-Provider SSO is one of the external authentication methods available and not the only one. Therefore, in this case when Multi-Provider SSO is not active, it confirms some other external authentication is active which is broken or misconfigured. System property **glide.authenticate.external** controls enabling / disabling external authentication.

### Resolution

For a quick relief, set system property **glide.authenticate.external** value as false and check what other external authentication is customer using and you can fix it according.
