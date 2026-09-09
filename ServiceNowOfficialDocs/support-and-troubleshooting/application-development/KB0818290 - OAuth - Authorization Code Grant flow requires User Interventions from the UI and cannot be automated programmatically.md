---
title: "OAuth - Authorization Code Grant flow requires User Interventions from the UI and cannot be automated programmatically"
aliases:
  - KB0818290
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818290
kb_number: KB0818290
last_modified: 2026-06-16
---

## OAuth - Authorization Code Grant flow requires User Interventions from the UI and cannot be automated programmatically

  

### Issue

-   Considering the scenario where:
    1.  An external application is the **3rd Party OAuth Provider**
    2.  The instance has defined a third party OAuth Provider record
    3.  The OAuth Provider record has the **Default Grant type set to Authorization Code**
    4.  A **REST Message** is defined with Authentication type to OAuth 2.0 and the OAuth profile defined at b.
-   Clicking the **Get OAuth Token** UI Action in the REST Message at point d. will request an authorization token from the 3rd Party OAuth Provider. This will open a _Request for Permission_ window to the user UI (Browser).
-   This **_Request for Permission step cannot be automated programmatically_**.

### Release

-   Any release

### Cause

-   This is **expected behavior**. The **User Permission must be** provided with an **interactive** User Intervention, this is on purpose.
-   However, once the access and refresh tokens are retrieved in the above step, the refresh token will be used automatically by ServiceNow until its expiration to get new access tokens as and when required.

Note: Once the refresh token is expired, user needs to fetch the tokens manually.

Reference: [https://www.oauth.com/oauth2-servers/making-authenticated-requests/refreshing-an-access-token/](https://www.oauth.com/oauth2-servers/making-authenticated-requests/refreshing-an-access-token/)

### Resolution

-   If the requirement is to have a **non-interactive** integration with OAuth provided authorization the possible approaches (if supported by the 3rd Party Application Endpoint) are:
    -   **Client Credentials Grant Type**
    -   **JWT grant type**

### Related Links

-   Please review the following documentation for your further information:
-   [OAuth 2.0 Authorization Code Grant flow](https://docs.servicenow.com/csh?topicname=c_OAuthAuthorizationCodeFlow.html&version=latest "OAuth 2.0 Authorization Code Grant flow")
-   [OAuth 3rd Party Provider - Authorization Code Grant Flow - Example](https://docs.servicenow.com/csh?topicname=c_OAuth2ProfileTutorialGoogle.html&version=latest "OAuth 3rd Party Provider - Authorization Code Grant Flow - Example")
-   [What is the Authorization Code Grant Flow](https://developer.okta.com/blog/2018/04/10/oauth-authorization-code-grant-type "What is the Authorization Code Grant Flow")
-   [OAuth 2.0 Client Credentials](https://docs.servicenow.com/csh?topicname=c_OAuthApplications.html&version=latest "OAuth 2.0 Client Credentials")
-   [OAuth 2.0 JWT Bearer grant type](https://docs.servicenow.com/csh?topicname=JWT-Bearer-token-support.html&version=latest "OAuth 2.0 JWT Bearer grant type")
