---
title: "SSO users fail to get redirected to the IDP : \"SSO Provider not found or inactive at user record\""
aliases:
  - KB0787991
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787991
kb_number: KB0787991
last_modified: 2026-05-05
---

## SSO users fail to get redirected to the IDP : "SSO Provider not found or inactive at user record"

  

### Issue

-   SSO Users fail to get redirected to the SSO IDP Provider
-   In the Servicenow logon page the following error is observed: ""an error has occurred - please contact your system administrator"
-   The following error is observed in the System log "SSO Provider not found or inActive at user record:"

### Release

All releases

### Cause

The SSO IDP Provider was not found.

The instance checked for the IDP to redirect to from the "SSO Source" field in the User record.

If an incorrect value is placed in the SSO Source field for the user, the issue occurs 

### Resolution

In the SSO Source field, enter one of the following:

-   For SAML users, enter sso: followed by the sys\_id of the identity provider's record.
-   Validate that the sys\_id of the IDP record in Servicenow is the value in this field
