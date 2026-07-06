---
title: "SAML Error: Ensure that the user you are trying to login is from the correct source, as mentioned in company's sso source field for user in servicenow instance."
aliases:
  - KB0814889
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814889
kb_number: KB0814889
last_modified: 2024-04-08
---

## SAML Error: Ensure that the user you are trying to login is from the correct source, as mentioned in company's sso source field for user in servicenow instance.

  

### Issue

After upgrading to Orlando, SSO logins are immediately redirected to the logout screen.

### Release

Orlando

### Cause

In the Orlando release, there is additional code in the SAML scripts that verify the 'sso\_source' field.  
If that field happens to contain the sys\_id of another Identity Provider record and not the one that had processed the SAMLResponse, the instance logs will have the following:  
  
SEVERE \*\*\* ERROR \*\*\* \*\*\* Script: Ensure that the user you are trying to login is from the correct source, as mentioned in company's sso source field for user in servicenow instance.

### Resolution

To address this error message, you can either update the 'sso\_source' value in the user/company record to the correct sys\_id of Identity Provider record or remove the current value.
