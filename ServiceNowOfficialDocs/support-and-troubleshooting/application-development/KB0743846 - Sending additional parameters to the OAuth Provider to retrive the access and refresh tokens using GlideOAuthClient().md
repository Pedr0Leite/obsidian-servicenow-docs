---
title: "Sending additional parameters to the OAuth Provider to retrive the access and refresh tokens using GlideOAuthClient()"
aliases:
  - KB0743846
tags:
  - servicenow
  - support-kb
  - oauth
  - glideoauthclient
  - integration
  - scripting
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743846
kb_number: KB0743846
last_modified: 2024-04-07
---

## Sending additional parameters to the OAuth Provider to retrive the access and refresh tokens using GlideOAuthClient()

  

### Issue

# Description

 Some OAuth providers require additional parameters to be sent in addition to standard parameters (grant\_type,username, password , client\_id , client\_secret ) to issue access token and refresh token . This article explains how to send any additional parameters from the script .

# Procedure

0) Create the OAuth Provider record in ServiceNow instance with all the required values .

1) In the script , create a params string and include any additional parameters that the OAuth Provider expects .

2) For example if a parameter called "resource" needs to be sent , include it the the params variable .

3) Below is a sample code .

var oAuthClient = new sn\_auth.GlideOAuthClient();   
var requestor\_context = 'test';   
var requestor\_id = 'abc@xyz.com';   
var oauth\_profile\_id = '<sys\_od\_of\_oauth\_profile>';   
  
var params = {grant\_type:'password', username:'abc@abc.com', password:'pa$$word', resource:'123-123-123', oauth\_requestor\_context:requestor\_context, oauth\_requestor:requestor\_id, oauth\_provider\_profile:oauth\_profile\_id};   
  
var json = new global.JSON();   
var text = json.encode(params);   
var tokenResponse = oAuthClient.requestToken('<OAuth\_Profile\_Name>', text);   
var token = tokenResponse.getToken();   
var access\_token = token.getAccessToken() ;   
  
gs.log("AccessToken:" + access\_token);   
gs.log("AccessTokenExpiresIn:" + token.getExpiresIn());   
gs.log(" RefreshToken:" + token.getRefreshToken());

# Applicable Versions

All versions .

## Related

- [[KB0791131 - Script to retrieve Access and Refresh tokens using GlideOAuthClient libraries]] - companion GlideOAuthClient scripting article
- [[KB0745184 - OAuth Token of type 'Client Credentials' generates 'User Not Authenticated' in Inbound web service call]] - related OAuth token issue
- [[c_GlideOAuthClient]] - GlideOAuthClient API reference
- [[c_GlideOAuthClientRequest]] - GlideOAuthClientRequest API reference

