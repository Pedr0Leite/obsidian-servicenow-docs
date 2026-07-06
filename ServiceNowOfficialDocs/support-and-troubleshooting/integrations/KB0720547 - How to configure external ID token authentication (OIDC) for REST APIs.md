---
title: "How to configure external ID token authentication (OIDC) for REST APIs"
aliases:
  - KB0720547
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720547
kb_number: KB0720547
last_modified: 2026-05-04
---

## How to configure external ID token authentication (OIDC) for REST APIs

  

### Issue

Learn how to configure external ID token authentication using OpenID Connect (OIDC) to access the Table API or a Scripted Web Service with JSON Web Tokens (JWTs).

OIDC is an authentication layer built on OAuth 2.0. It allows clients, including ServiceNow, to verify end-user identity by validating JWT tokens that contain user information. ServiceNow supports only JWT tokens for API authentication.

A JWT, defined in RFC 7519, consists of three parts separated by dots: Header, Payload, and Signature. The payload contains claims that the system validates during token verification.

### How OIDC authentication works

1.  The instance admin registers an app with a third-party OIDC provider.​
2.  The instance admin configures the OIDC provider in the instance, specifying the OIDC metadata URL, user claim, and user field.
3.  The instance admin sets up the OAuth OIDC Entity using the client ID \[client\_id\] and client secret \[secret\_id\] from the provider.​
4.  API users obtain a JWT and include it in the Authorization bearer header when calling ServiceNow REST APIs.
5.  The instance checks whether the bearer token is an OAuth access token. If not, it validates the token as a JWT.
6.  The instance validates the JWT by verifying the signature, expiry, and user claim.​
7.  The instance authenticates the request by matching the user from the JWT to a record in the User \[sys\_user\] table.​

#### **Authentication outcomes**

-   **User found**: The request is authenticated.
-   **User not found, auto user-import enabled**: The system creates the user using a predefined transform map, and then authenticates the request.
-   **User not found, auto user-import disabled**: Authentication fails and the API call returns a 401 error.

#### **JTI claim verification**

If **Enable JTI claim verification** is selected, each JWT can be used for only one API call. Subsequent calls using the same token fail. If this option is not selected, the instance does not check whether the JWT has been used previously. 

![Flow chart describing how OIDC authentication works](sys_attachment.do?sys_id=8fe38677931a3690101833527cba105f)

### Integration setup

#### Register the app with your OIDC provider

Register your application with your OpenID Connect provider. Check your identity and access management solution documentation for provider-specific instructions. For a list of certified providers, see [OpenID Certification](https://openid.net/certification/).

#### **Set up the OAuth OIDC Entity configuration** 

1.  Go to **System OAuth** > **Application Registry**.
2.  Select an existing record (**Demo data**) or select **New** to create a new record.
3.  Select **Configure an OIDC provider to verify ID tokens**.
4.  Complete all required fields, including **Client ID** and **Client Secret**. Your OIDC provider supplies these values.
5.  Configure the OAuth Entity **Scopes**. Your OIDC provider supplies the scope details.

  
![Example of OAuth OIDC Entity configuration screen](sys_attachment.do?sys_id=43e38677931a3690101833527cba103f)

#### Optimized version OIDC provider configuration fields 

<table style="border-collapse: collapse; width: 100%; border: 1px solid rgb(149, 165, 166);" border="1"><tbody><tr><td style="padding: 10px; border-color: rgb(149, 165, 166);"><p><strong>OIDC provider configurations&nbsp;</strong></p></td><td style="padding: 10px; border-color: rgb(149, 165, 166);"><p><strong>Description</strong>&nbsp;&nbsp;</p></td></tr><tr><td style="padding: 10px; border-color: rgb(149, 165, 166);"><p>&nbsp;OIDC provider</p></td><td style="padding: 10px; border-color: rgb(149, 165, 166);"><p>The name of the OIDC provider&nbsp;</p></td></tr><tr><td style="padding: 10px; border-color: rgb(149, 165, 166);"><p>&nbsp;OIDC metadata URL</p></td><td style="padding: 10px; border-color: rgb(149, 165, 166);"><p>The metadata URL for your OIDC provider. Check your provider documentation for this value.&nbsp;</p></td></tr><tr><td style="padding: 10px; border-color: rgb(149, 165, 166);"><p>&nbsp;User claim</p></td><td style="padding: 10px; border-color: rgb(149, 165, 166);"><p>The claim which is validated against user table</p></td></tr><tr><td style="padding: 10px; border-color: rgb(149, 165, 166);"><p>&nbsp;User field</p></td><td style="padding: 10px; border-color: rgb(149, 165, 166);"><p>The claim validated against the User [sys_user] table.&nbsp;</p></td></tr><tr><td style="padding: 10px; border-color: rgb(149, 165, 166);"><p>Enable JTI claim verification</p></td><td style="padding: 10px; border-color: rgb(149, 165, 166);"><p>When enabled, JWT validation includes verification of the JTI (JWT ID) sent by the provider. When disabled, the JTI is not validated even if present in the token.&nbsp;&nbsp;</p></td></tr></tbody></table>

![Example of OIDC provider configuration screen ](sys_attachment.do?sys_id=87e38677931a3690101833527cba1043)

#### **Get a JWT** 

Use your OIDC provider to generate an ID token for the client program.

#### **Invoke a REST API call** 

Include the ID token in the Authorization header to access the Table API or a Scripted Web Service.

**Example cURL request**

curl -X GET --header "Accept:application/json" https://<instance\_name>.service-now.com/api/now/table/incident/897b04f2dbd4a300a135364e9d961952 -k --header "Authorization: Bearer eyJraWQiOiJjNTZtZTlXU0xPVnY3UFMwcTg4Qzl1b0lzNjFQYTdmUG4yZFVFOW9RNUg4IiwiYWxnIjoiUlMyNTYifQ..." 

If authentication succeeds, the API returns a valid application/json response. If authentication fails, the API returns an error message.

**User not authenticated error** 

{"error":{"message":"**User Not Authenticated**","detail":"Required to provide Auth information"},"status":"failure"}

### JWT claim validations

The Now Platform parses the payload in the JWT and compares it against the JWT claim validation configurations. If the configured values do not match the claims in the JWT, a validation error is logged in the localhost log. 

![Example of JWT claim validations screen](sys_attachment.do?sys_id=8fe38677931a3690101833527cba1021)

### User provisioning

To automatically provision users from OIDC claims, configure a data source and transform map.

1.  Create a data source with type **OIDC.**
2.  Associate a transform map with the data source.
3.  Select the data source in the OIDC provider configuration.
4.  Select **Automatically provision users**.
5.  Assign the appropriate roles. 

  
![Example of user provisioning screen](sys_attachment.do?sys_id=c3e38677931a3690101833527cba105c)

The Now Platform parses the claim values and populates the staging table. The transform map runs and loads data into the target table. 

**Example of Import Sets screen**

![Example of Import Sets screen](sys_attachment.do?sys_id=4be38677931a3690101833527cba101d)

### Localhost log examples

The following examples show key log entries for different authentication scenarios. Use these patterns to troubleshoot OIDC authentication issues. Note that transaction IDs, timestamps, session IDs, and user names will differ per instance.

**Successful authentication**

2018-12-11 15:50:32 (275) API\_INT-thread-2 SYSTEM txid=db83700edb1a **DEBUG: Auth JWT token sucessfully verified for algorithm=RS256**   
2018-12-11 15:50:32 (299) API\_INT-thread-2 SYSTEM txid=db83700edb1a **DEBUG: Auth All claims are sucessfully validated.**   
2018-12-11 15:50:32 (319) API\_INT-thread-2 SYSTEM txid=db83700edb1a **HTTP authorization validated user 'oauth.admin'**   
2018-12-11 15:50:32 (319) API\_INT-thread-2 SYSTEM txid=db83700edb1a **Session user set to oauth.admin** 

**Failed authentication (JTI claim verification failure)** 

2018-12-11 13:16:59 (966) API\_INT-thread-2 SYSTEM txid=a260184adbd6 **SEVERE \*\*\* ERROR \*\*\* Failed in jti(JWT token\_id) claim verification. Token is already used.**   
2018-12-11 13:16:59 (966) API\_INT-thread-2 SYSTEM txid=a260184adbd6 **WARNING \*\*\* WARNING \*\*\* Oauth authentication failed for access token** ... **No user found**.   
2018-12-11 13:16:59 (966) API\_INT-thread-2 SYSTEM txid=a260184adbd6 **WARNING \*\*\* WARNING \*\*\* Failed authorization by script include 'BearerAuth'**   
2018-12-11 13:16:59 (967) API\_INT-thread-2 SYSTEM txid=a260184adbd6 #30849 **\[REST API\] RESTAPIProcessor : User Not Authenticated**   
2018-12-11 13:16:59 (967) API\_INT-thread-2 SYSTEM txid=a260184adbd6 DEBUG: Session inactivity timeout changed for unauthorized session. Inactive\_interval=60 seconds 

**Successful claims validation** 

2018-12-11 17:44:24 (316) API\_INT-thread-3 SYSTEM txid=2f9dcd4edb9e **DEBUG: Auth Going to verify claims:\[name\]**   
2018-12-11 17:44:24 (317) API\_INT-thread-3 SYSTEM txid=2f9dcd4edb9e **DEBUG: Auth JWT token sucessfully verified for algorithm=RS256**   
2018-12-11 17:44:24 (320) API\_INT-thread-3 SYSTEM txid=2f9dcd4edb9e **DEBUG: Auth All claims are sucessfully validated.**

**Failed claims validation**

2018-12-11 18:06:15 (276) API\_INT-thread-1 SYSTEM txid=67925142dbde **DEBUG: Auth Going to verify claims:\[name\]**   
2018-12-11 18:06:15 (278) API\_INT-thread-1 SYSTEM txid=67925142dbde **SEVERE \*\*\* ERROR \*\*\* JWT verification failed. exception:com.auth0.jwt.exceptions.InvalidClaimException: The Claim 'name' value doesn't match the required one.**

### Troubleshooting

#### **Enable OAuth debugging**

Set the following system properties to **true** to enable detailed logging:

-   com.snc.platform.security.oauth.debug
-   glide.auth.debug.enabled

#### **Review logs and validate tokens**

-   Check the localhost log for error messages.
-   Use an [external JWT decoder](https://jwt.io/) to inspect token contents and verify claims.

  
  
![Example of an external JWT decoder to inspect token contents and verify claims](sys_attachment.do?sys_id=07e38677931a3690101833527cba1019)

### Release

Beginning with the London release

### Resolution

This article provides configuration guidance. No resolution is required.

### Related Links

**Standards and specifications** 

-   [RFC 7519: JSON Web Token (JWT)](https://tools.ietf.org/html/rfc7519)
-   [OpenID Connect protocol documentation](https://auth0.com/docs/protocols/oidc)
-   [OpenID Certification (list of certified providers)](https://openid.net/certification/)

**Okta resources (example OIDC provider)**

-   [Okta OIDC API documentation](https://developer.okta.com/docs/api/resources/oidc)
-   [Okta Overview: OAuth 2.0 and OpenID Connect](https://developer.okta.com/docs/concepts/oauth-openid/)
-   [Okta JWT validation guide](https://developer.okta.com/code/dotnet/jwt-validation)
-   [Sign up for an Okta developer account](https://developer.okta.com/signup/)

**ServiceNow product documentation**

-   [OAuth 2.0](https://www.servicenow.com/docs/bundle/zurich-platform-security/page/administer/security/concept/c_OAuthApplications.html)
-   [Inbound REST API authentication](https://www.servicenow.com/docs/bundle/zurich-conversational-interfaces/page/administer/virtual-agent/task/configure-send-request.html)
