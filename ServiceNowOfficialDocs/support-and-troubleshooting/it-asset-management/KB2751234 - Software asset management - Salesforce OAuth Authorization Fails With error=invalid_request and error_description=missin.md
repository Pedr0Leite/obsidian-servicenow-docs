---
title: "Software asset management - Salesforce OAuth Authorization Fails With error=invalid_request and error_description=missing required code challenge"
aliases:
  - KB2751234
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2751234
kb_number: KB2751234
last_modified: 2026-02-12
---

## Issue

-   When generating an OAuth token from ServiceNow for a Salesforce integration, the Salesforce authorization window fails immediately with:
    -   **error=invalid\_request**
    -   **error\_description=missing required code challenge**
-   This prevents ServiceNow from completing the OAuth authorization and storing a valid token for the Salesforce connection.

## Resolution

1\. Salesforce Admin actions (required): 

1.  1.  Open Salesforce Setup
    2.  Go to App Manager
    3.  Locate the Connected App (or External Client App) used for ServiceNow
    4.  Open Manage (or Edit Policies / Edit depending on UI)
    5.  In API (Enable OAuth Settings):
        -   Disable the setting:
            -   Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows
        -   Confirm the required OAuth scopes for the integration are still selected (as applicable to your implementation), commonly:
            -   api
            -   refresh\_token / offline\_access
        -   Confirm the callback URL includes the ServiceNow redirect URL in the required format:
            -   [https://<your\_instance>.service-now.com/oauth\_redirect.do](https://%3cyour_instance%3e.service-now.com/oauth_redirect.do)

Save changes  
  
2\. ServiceNow Admin actions (validation)

-   -   -   In ServiceNow, open the relevant Connection & Credential record for the Salesforce integration
        -   Select Get OAuth Token (or Create and Get OAuth Token)
        -   Confirm the Salesforce login/consent screen opens successfully (instead of the PKCE error)
        -   Complete login and approve consent
        -   Confirm ServiceNow returns successfully and the token is created

3\. If PKCE cannot be disabled due to customer security policy: 

-   -   Create a separate dedicated Salesforce Connected App specifically for ServiceNow where PKCE is not enforced, if allowed by policy
    -   If PKCE is mandatory for all apps and no exception can be made, the standard OAuth setup flow for this integration will continue to fail unless the integration method is changed to one that supports PKCE (this typically requires a custom approach outside the standard setup path)
