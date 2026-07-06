---
title: "OAuth Token of type 'Client Credentials' generates 'User Not Authenticated' in Inbound web service call"
aliases:
  - KB0745184
tags:
  - servicenow
  - support-kb
  - oauth
  - authentication
  - integration
  - web-services
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745184
kb_number: KB0745184
last_modified: 2025-02-14
---

## OAuth Token of type 'Client Credentials' generates 'User Not Authenticated' in Inbound web service call

  

### Issue

Making a call to the instance to obtain OAuth token of Grant Type client\_credential and passing client id and client secret to the OAuth endpoint

_**https://<instance\_name>.service-now.com/oauth\_token.do**_ 

successfully generates an Access Token.

However, using this token in the Authorization header in the subsequent call to access a resource in the ServiceNow instance generates the error:

-   "Required to provide Auth information"
-   "User Not Authenticated"

**Note: This KB applies up to the Vancouver version. Starting from the Washington release, ServiceNow began supporting the "Client Credentials" grant type by linking it with a user in the OAuth Entity record. For more information refer to [KB1645212](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1645212 "KB1645212")**

### Release

**Up to Vancouver**

### Cause

The OAuth Access token that is generated when the grant type is client\_credential is associated with the 'guest' user.

This can be verified by checking the 'oauth\_credential' table for 'Token' and 'User'.

For the OAuth Authorization to work the token should be associated with a User on the instance and not to the guest user.

### Resolution

Client credential grant type is not applicable for Inbound OAuth Authentication to ServiceNow.

Please use one of the below default Grant Types:

1)Resource Owner Password Credentials

2)Authorization Code

## Related

- [[KB0743846 - Sending additional parameters to the OAuth Provider to retrive the access and refresh tokens using GlideOAuthClient()]] - related OAuth scripting
- [[KB0791131 - Script to retrieve Access and Refresh tokens using GlideOAuthClient libraries]] - GlideOAuthClient usage
- [[KB0693900 - How to generate a token using sn_auth - oAuth API for Authorization grant type]] - alternate supported OAuth grant type
- [[KB0693393 - How to generate a token using sn_auth - oAuth API for Resource Owner Password Credentials grant type]] - alternate supported OAuth grant type
- [[c_GlideOAuthClient]] - GlideOAuthClient API reference

