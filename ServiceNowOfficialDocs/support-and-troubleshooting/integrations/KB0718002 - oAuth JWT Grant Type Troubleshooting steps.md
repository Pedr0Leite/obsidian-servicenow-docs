---
title: "oAuth JWT Grant Type Troubleshooting steps"
aliases:
  - KB0718002
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718002
kb_number: KB0718002
last_modified: 2026-07-21
---

## oAuth JWT Grant Type Troubleshooting steps

  

### Issue

This article focuses on the possible troubleshooting steps involved for **oAuth 2.0 JWT bearer grant Type**.

### Procedure

1.  Enable debugger property related to oAuth  
    -   **com.snc.platform.security.oauth.debug** = true
    -   **glide.auth.debug.enabled** = true
2.  Ensure all the required parameters for oAuth Provider is configured.  
    1.  Client ID
    2.  Client Secret
    3.  Token URL
    4.  Profile
    5.  Scope
    6.  JWT Provider
3.  Validate if the **keystore** has a valid **password** in it. Ensure the same password is used within the NOW platform.
4.  Validate if the **signing key** within the **keystore** has a valid **password** in it. Ensure the same password is used within the NOW platform.
5.  **Get oAuth Token** from **Outbound Rest Message**.
6.  Logs are printed in the localhost logs if the debugger property is enabled. Check the log for any errors if the token is not generated.
7.  If there are no errors in the log verify if **JWT** is generated within the NOW Platform.  
    
    **Started to generate JWT  
    **AuthAdding payload claims to jwt with name = box\_sub\_type and value = enterprise  
    AuthAdding payload claims to jwt with name = aud and value = https://api.box.com/oauth2/token  
    AuthAdding payload claims to jwt with name = sub and value = 120961449  
    AuthAdding payload claims to jwt with name = iss and value = o9xqbay28g97deumamwz2s0tvtsfrusb  
    AuthAdding claims to jwt. Header Claims = \[\], keyId = , issuedAt = Thu Nov 15 15:15:52 PST 2018, expiresAt = Thu Nov 15 15:16:52 PST 2018, issuer = o9xqbay28g97deumamwz2s0tvtsfrusb, notBefore = null, signingAlgorithms=RS256, jwtId=e5a988d8-23da-465f-b34c-bbecff42257c  
    **Successfully generated JWT**
    
8.  Verify if the **request** is sent  
    
    OAUTH - OAuthHTTPRequest : Sending http request, url:https://api.box.com/oauth2/token  
    OAUTH - OAuthHTTPRequest : Sending http request, body:grant\_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczovL2FwaS5ib3guY29tL29hdXRoMi90b2tlbiIsInN1YiI6IjEyMDk2MTQ0OSIsImJveF9zdWJfdHlwZSI6ImVudGVycHJpc2UiLCJpc3MiOiJvOXhxYmF5MjhnOTdkZXVtYW13ejJzMHR2dHNmcnVzYiIsImV4cCI6MTU0MjMyMzgxMiwiaWF0IjoxNTQyMzIzNzUyLCJqdGkiOiJlNWE5ODhkOC0yM2RhLTQ2NWYtYjM0Yy1iYmVjZmY0MjI1N2MifQ.O1f7vpKPKgGJWfOn\_hXIu18d5AVv8wjqaxvEGlVQaNBWTQ3H4AKJ1XcE1VFrpeCXpxb0uZ2wb\_O4JctZeX-qP7aH9R9QovT9tMpxEQCpmDNX5XAs3iw\_X5yfT\_eYszMBcrS2ZpXbEj82lVLgGixV7tRWhq0tLgIoIUAPcnbAsu2L6ec5wsCyqAv4l4XwqicYjk8Pl94WbcfmFF3Cg2eWhELB2EFG5\_V48NOsvTHWBTkwp-aLS-YIH17w5uPAKht7BjtW0CBsbrCxjgVoc\_VGpLqHNyl0BXMHI9wBDSCffA2sWamGTDxqferagdYXt\_8jfkahqslKhmCAbCUonfnBSw&client\_secret=DRcW5sBRcuy4jDqryIoPB5BhCw7h1QzL&client\_id=o9xqbay28g97deumamwz2s0tvtsfrusb  
    SecurityUtils: Obfuscating Key : access\_token and all its children!
    
9.  Use the **jwt.io** site to decode assertion. Verify if **Header** and **Payload** are generated with all the required claims.  
      
    ![](sys_attachment.do?sys_id=50ad66c7db678510b5d6e6be139619ed)  
      
    
10.  If the request is processed by the oAuth Provider verify if a **response** was returned.  
     
     OAUTH - OAuthHTTPRequest : Received http response: {"access\_token":"\*\*\*\*\*\*\*\*","token\_type":"bearer","expires\_in":4245,"restricted\_to":\[\]}
     
11.  Verify if the **token** is returned in the response
12.  If the token is not returned review **error messages** and take appropriate action. Possible errors could be related to signing key, claims, client id, or client secret.
13.  The token is sent as an **Authorization header** for outbound REST messages, ensure the token matches the **request header**. Enable **Outbound HTTP Debugging** to log HTTP request and response  
       
     ![](sys_attachment.do?sys_id=20ad66c7db678510b5d6e6be139619f0)

### Release

Madrid

### Related Links

-   [Outbound Web Services Logging](https://docs.servicenow.com/csh?topicname=outbound-logging-properties.html&version=latest "Outbound Web Services Logging")
-   Encode/Decode JWT Token: [https://www.jsonwebtoken.io/](https://www.jsonwebtoken.io/)
-   JWT Builder [http://jwtbuilder.jamiekurtz.com/](http://jwtbuilder.jamiekurtz.com/)
-   Encode/Decode JWT Token: [https://jwt.io/](https://jwt.io/)
