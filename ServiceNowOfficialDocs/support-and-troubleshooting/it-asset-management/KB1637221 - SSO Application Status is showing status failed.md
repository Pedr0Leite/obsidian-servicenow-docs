---
title: "SSO Application Status is showing status failed"
aliases:
  - KB1637221
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1637221
kb_number: KB1637221
last_modified: 2024-04-03
---

## SSO Application Status is showing status failed

  

### Issue

SSO Application's Status is failing with status "failed"

-   The Outbound is failing with  
    {"error":{"code":"Authentication\_RequestFromUnsupportedUserRole","message":"User is not in the allowed roles","innerError"

### Cause

Global admin role is missing for the user who fetched the OAuth token

To check which fetched the OAuth token:

-   Navigate to System OAuth > Manage Tokens.
-   Find the token with the name of Azure and add the User column.

### Resolution

1.  Check the user roles of the user who fetched the OAuth token on Azure AD, iF GLOBAL Admin role is missing then add the role to that user.
2.  If Azure team denies for provide the Admin role to that user then use the already existing user who've admin role to fetch the OAUTH

-   -   Open an incognito browser window
    -   Login to Azure AD with the user who has Global admin access to Azure portal
    -   Login to ServiceNow, open the connection record and complete the auth steps (if already done, open Connection > Credential > Click on Generate OAuth Token).
