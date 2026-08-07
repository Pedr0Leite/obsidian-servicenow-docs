---
title: "How to configure  Outbound Rest Message with oAuth 2.0 JWT Bearer grant flow?"
aliases:
  - KB0718030
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718030
kb_number: KB0718030
last_modified: 2025-08-21
---

## Issue

This article focusses on configuring **oAuth 2.0 JWT bearer grant flow** for **outbound rest message**.

## Resolution

1.  [oAuth JWT Bearer Grant Type Integration Setup](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717946) has the steps to configure oAuth Profile for JWT Grant Type.  
      
    
2.  Once the profile is completed, Goto **System Webservices** >> **Outbound** >> **Rest Message**.  
      
    
3.  Open Rest Message.  
      
    
4.  Select **JWT oAuth Profile** from **Authentication >> oAuth Profile** field.  
    ![](sys_attachment.do?sys_id=da592ef8476f6a14d1a5ab29736d4368)  
      
    
5.  Save  
      
    
6.  Click **Get oAuth Token** to generate **JWT** token from **oAuth Provider**.Once the token is generated, token details are shown at the **info message** section.  
      
    
7.  Goto **System oAuth >> Manage Token** to see the JWT Token details.Filter the token by oAuth Profile.  
    ![](sys_attachment.do?sys_id=d2596af8476f6a14d1a5ab29736d43f8)
8.  Use the below scripting to test outbound rest message via Scripting.  
    
    ```
    jwtDemo();
    function jwtDemo(){
    
    try { 
    var r = new sn_ws.RESTMessageV2('Box JWT Demo', 'Default GET');
    
    //override authentication profile 
    //r.authentication type = 'oauth2';
    //r.setAuthenticationProfile(authentication type, "JWT_Demo default_profile");
    
    //set a MID server name if one wants to run the message on MID
    //r.setMIDServer('MY_MID_SERVER');
    
    //if the message is configured to communicate through ECC queue, either
    //by setting a MID server or calling executeAsync, one needs to set skip_sensor
    //to true. Otherwise, one may get an intermittent error that the response body is null
    //r.setEccParameter('skip_sensor', true);
    
    var response = r.execute();
    gs.info("response is"+response);
    var responseBody = response.getBody();
    gs.info("response body is"+responseBody);
    var httpStatus = response.getStatusCode();
    gs.info("httpStatus is"+httpStatus);
    }
    catch(ex) {
    var message = ex.message;
    gs.info("Message is"+message);
    }
    
    }
    ```
    

**Output:**

Ignore oauth entity from request. Use provider from oauth entity profile.  
Getting JWTProvider for jwtProviderSysId = e4967691dbf92300980c90b6db96190d  
Auth Cache hit, getting jwtProvider from cache.  
Getting JWTProviderConfig for jwtProviderId = e4967691dbf92300980c90b6db96190d  
Auth Cache hit. Getting JWTProviderConfiguration from cache  
Started to generate JWT  
AuthAdding payload claims to jwt with name = box\_sub\_type and value = enterprise  
AuthAdding payload claims to jwt with name = aud and value = [https://api.box.com/oauth2/token](https://api.box.com/oauth2/token)  
AuthAdding payload claims to jwt with name = sub and value = 120961449  
AuthAdding payload claims to jwt with name = iss and value = o9xqbay28g97deumamwz2s0tvtsfrusb  
AuthAdding claims to jwt. Header Claims = \[\], keyId = , issuedAt = Thu Nov 15 15:15:52 PST 2018, expiresAt = Thu Nov 15 15:16:52 PST 2018, issuer = o9xqbay28g97deumamwz2s0tvtsfrusb, notBefore = null, signingAlgorithms=RS256, jwtId=e5a988d8-23da-465f-b34c-bbecff42257c  
Successfully generated JWT  
OAUTH - OAuthHTTPRequest : Sending http request, url:[https://api.box.com/oauth2/token](https://api.box.com/oauth2/token)  
OAUTH - OAuthHTTPRequest : Sending http request, body:grant\_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczovL2FwaS5ib3guY29tL29hdXRoMi90b2tlbiIsInN1YiI6IjEyMDk2MTQ0OSIsImJveF9zdWJfdHlwZSI6ImVudGVycHJpc2UiLCJpc3MiOiJvOXhxYmF5MjhnOTdkZXVtYW13ejJzMHR2dHNmcnVzYiIsImV4cCI6MTU0MjMyMzgxMiwiaWF0IjoxNTQyMzIzNzUyLCJqdGkiOiJlNWE5ODhkOC0yM2RhLTQ2NWYtYjM0Yy1iYmVjZmY0MjI1N2MifQ.O1f7vpKPKgGJWfOn\_hXIu18d5AVv8wjqaxvEGlVQaNBWTQ3H4AKJ1XcE1VFrpeCXpxb0uZ2wb\_O4JctZeX-qP7aH9R9QovT9tMpxEQCpmDNX5XAs3iw\_X5yfT\_eYszMBcrS2ZpXbEj82lVLgGixV7tRWhq0tLgIoIUAPcnbAsu2L6ec5wsCyqAv4l4XwqicYjk8Pl94WbcfmFF3Cg2eWhELB2EFG5\_V48NOsvTHWBTkwp-aLS-YIH17w5uPAKht7BjtW0CBsbrCxjgVoc\_VGpLqHNyl0BXMHI9wBDSCffA2sWamGTDxqferagdYXt\_8jfkahqslKhmCAbCUonfnBSw&client\_secret=DRcW5sBRcuy4jDqryIoPB5BhCw7h1QzL&client\_id=o9xqbay28g97deumamwz2s0tvtsfrusb  
SecurityUtils: Obfuscating Key : access\_token and all its children!  
OAUTH - OAuthHTTPRequest : Received http response: {"access\_token":"\*\*\*\*\*\*\*\*","token\_type":"bearer","expires\_in":4245,"restricted\_to":\[\]}  
StorageEncrypter: ignoring already encrypted text starting with: aIm:S...  
\*\*\* Script: response is\[object RESTResponseV2\]  
\*\*\* Script: response body is{"type":"folder","id":"0","sequence\_id":null,"etag":null,"name":"All Files","created\_at":null,"modified\_at":null,"description":"","size":0,"path\_collection":{"total\_count":0,"entries":\[\]},"created\_by":{"type":"user","id":"","name":"","login":""},"modified\_by":{"type":"user","id":"6441126643","name":"empiali1(jwt\_demo)","login":"AutomationUser\_697501\_AXOowVN7fY@boxdevedition.com"},"trashed\_at":null,"purged\_at":null,"content\_created\_at":null,"content\_modified\_at":null,"owned\_by":{"type":"user","id":"6441126643","name":"empiali1(jwt\_demo)","login":"AutomationUser\_697501\_AXOowVN7fY@boxdevedition.com"},"shared\_link":null,"folder\_upload\_email":null,"parent":null,"item\_status":"active","item\_collection":{"total\_count":0,"entries":\[\],"offset":0,"limit":100,"order":\[{"by":"type","direction":"ASC"},{"by":"name","direction":"ASC"}\]}}  
\*\*\* Script: httpStatus is200
