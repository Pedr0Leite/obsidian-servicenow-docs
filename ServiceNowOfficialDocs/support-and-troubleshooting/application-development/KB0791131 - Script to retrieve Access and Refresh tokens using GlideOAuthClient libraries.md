---
title: "Script to retrieve Access and Refresh tokens using GlideOAuthClient libraries"
aliases:
  - KB0791131
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791131
kb_number: KB0791131
last_modified: 2026-01-06
---

## Script to retrieve Access and Refresh tokens using GlideOAuthClient libraries

  

### Summary

Below is sample script Script to retrieve Access and Refresh tokens using GlideOAuthClient libraries

This could be run from background scripts for testing purpose

### Release

All releases

### Instructions

  
**Code to retrieve Access token and Refresh Token:**  
  
var oAuthClient = new sn\_auth.GlideOAuthClient();  
var requestor\_context = 'test';  
var requestor\_id = 'abc@xyz.com';  
var oauth\_profile\_id = '43d6bab3db849f009a6ff9b61d961957'; // profile ID \[sys\_id of  'OAuth Entity Profiles' (oauth\_entity\_profile) record in OAUTH registry  record\]  
  
var params = {grant\_type:"password", username:'admin', password:'pwd', oauth\_requestor\_context:requestor\_context, oauth\_requestor:requestor\_id, oauth\_provider\_profile:oauth\_profile\_id}; //  
var json = new global.JSON();  
var text = json.encode(params);  
var tokenResponse = oAuthClient.requestToken('oAuth Test', text); //'oAuth Test' is the name of the OAuth application registry record (oauth\_entity)  
var token = tokenResponse.getToken();  
var access\_token = token.getAccessToken() ;  
  
gs.log("AccessToken:" + access\_token);  
gs.log("AccessTokenExpiresIn:" + token.getExpiresIn());  
gs.log(" RefreshToken:" + token.getRefreshToken());  
  
  
**Code to retrieve a new Access Token using Refresh token**  
  
var oAuthClient = new sn\_auth.GlideOAuthClient();  
var requestor\_context = 'test';  
var requestor\_id = 'abc@xyz.com';  
var oauth\_profile\_id = '43d6bab3db849f009a6ff9b61d961957'; // profile ID \[sys\_id of  'OAuth Entity Profiles' (oauth\_entity\_profile) record in OAUTH registry  record\]  
  
var params = {grant\_type:"refresh\_token", refresh\_token:"<value\_of\_refresh\_token>", oauth\_requestor\_context:requestor\_context, oauth\_requestor:requestor\_id, oauth\_provider\_profile:oauth\_profile\_id};  
var json = new global.JSON();  
var text = json.encode(params);  
var tokenResponse = oAuthClient.requestToken('oAuth Test', text); //'oAuth Test' is the name of the OAuth application registry record (oauth\_entity)  
var token = tokenResponse.getToken();  
var access\_token = token.getAccessToken() ;  
  
gs.log("AccessToken:" + access\_token);  
gs.log("AccessTokenExpiresIn:" + token.getExpiresIn());gs.log(" RefreshToken:" + token.getRefreshToken());

**Making an outbound REST call with the retrieved token**

// make the outbound REST call with the retrieved token

var r = new sn\_ws.RESTMessageV2('empukemburu03\_outbound', 'Default GET'); 

//setting oauth profile and oauth requester profile

r.setAuthenticationProfile('oauth2', oauth\_profile\_id); 

r.setRequestorProfile(requestor\_context, requestor\_id);

var response = r.execute(); 

var responseBody = response.getBody(); 

var httpStatus = response.getStatusCode(); 

gs.log(responseBody);

## Related

- [[KB0743846 - Sending additional parameters to the OAuth Provider to retrive the access and refresh tokens using GlideOAuthClient()]] - extends this script to send extra OAuth parameters
- [[KB0745184 - OAuth Token of type 'Client Credentials' generates 'User Not Authenticated' in Inbound web service call]] - related OAuth token/grant type issue
