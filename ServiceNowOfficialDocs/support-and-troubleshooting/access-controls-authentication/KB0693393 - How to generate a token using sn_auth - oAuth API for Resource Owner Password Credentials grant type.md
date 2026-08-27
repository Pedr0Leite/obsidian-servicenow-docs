---
title: "How to generate a token using sn_auth - oAuth API  for Resource Owner Password Credentials grant type?"
aliases:
  - KB0693393
tags:
  - servicenow
  - support-kb
  - oauth
  - sn_auth
  - GlideOAuthClient
  - rest-api
  - authentication
  - scripting
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693393
kb_number: KB0693393
last_modified: 2025-01-03
---

## Issue

  
  

# Description

* * *

This tutorial explains the steps to test oAuth - Resource Owner Password Credentials grant type using sn\_auth - oAuth API.

# Prerequisites

* * *

This tutorial assumes that client application 'empimranitsm\_rest\_integration is already registered in the third party oAuth Provider.Once the client application is registered, note down client id, client secret & grant type.

User id and password is required to access to generate token.This is provided by third party oAuth provider.

# Procedure

* * *

1)Configure oAuth Provider to access token from third party - oAuth Provider.

![](sys_attachment.do?sys_id=cc1de062db82b450e515c223059619f1) 

2)Run this script in the scripts background to test Resource Owner Password Credentials flow.

PasswordCredentialsFlow();

/\*\*\*\*

This scripts is useful to test client credential via glide scripting.

Prerequisites:Configure OAuth entity with type OAuth provider."empimranitsm\_rest\_integration" is the OAuth Provider. 

\*\*\*/

function PasswordCredentialsFlow(){

var tokenRequest = new  sn\_auth.GlideOAuthClientRequest();

tokenRequest.setGrantType("password");

tokenRequest.setRequestor("scripts background");

//If scope is required, pass scope name.

tokenRequest.setScope("useraccount");

tokenRequest.setUserName("admin");

tokenRequest.setPassword("admin");

var oAuthClient = new  sn\_auth.GlideOAuthClient();

//Retrieves the token for the client and the request set into a GlideOAuthClientResponse object.

var tokenResponse = oAuthClient.requestTokenByRequest("empimranitsm\_rest\_integration", tokenRequest);

//Prints GlideOAuthClientResponse object.

gs.info("Prints GlideOAuthClientResponse object members"); 

gs.info("Error:" + tokenResponse.getErrorMessage());

gs.info("Token Response Body:" + tokenResponse.getBody());

gs.info("Token Response Content Type:" + tokenResponse.getContentType());

gs.info("Token Response Code:" + tokenResponse.getResponseCode());

//gs.info("Token Response Parameters:" + tokenResponse.getResponseParameters());

var paramMap = tokenResponse.getResponseParameters()

gs.info("Iterating Token Response Parameters Starts");

for (param in paramMap){

gs.info("Key:"+param+" "+"value:"+paramMap\[param\].toString());

//paramMap.put(param, tokenResponse2\[param\].toString());

}

gs.info("Iterating Token Response Parameters Ends");

//This Returns GlideOAuthToken object 

var token = tokenResponse.getToken(); 

dumpToken(token);

}

function dumpToken(token) {

  if(token) {

       gs.info("Prints Glide oAuthToken Object Members");

       gs.info("AccessToken:" + token.getAccessToken());

       gs.info("AccessTokenExpiresIn:" + token.getExpiresIn());

       gs.info("Access Token SysID:" + token.getAccessTokenSysID());

       gs.info("Access Token Scope:" + token.getScope());

  }

}

**Sample Output:**

\*\*\* Script: Prints GlideOAuthClientResponse object members  
\*\*\* Script: Error:null  
\*\*\* Script: Token Response Body:{"access\_token":"lVTYldqvnm1Sxku9eCeareEtsD730ZrbMdVGBDzJZ-NdAEivTsGjN80jT-ToRq0RgW2UnRLRPEJTSDJOCFgb4Q","refresh\_token":"LkKYLypkbz4Axjbe4Ub8\_vmLPwGH7gTsmbbY5Xcm9pez7nv11yVb4Xj24O8Lt0Mcy2qdyyi3T9ufJF6sd-Ik8g","scope":"useraccount","token\_type":"Bearer","expires\_in":1799}  
\*\*\* Script: Token Response Content Type:application/json;charset=utf-8  
\*\*\* Script: Token Response Code:200  
\*\*\* Script: Iterating Token Response Parameters Starts  
\*\*\* Script: Key:access\_token value:lVTYldqvnm1Sxku9eCeareEtsD730ZrbMdVGBDzJZ-NdAEivTsGjN80jT-ToRq0RgW2UnRLRPEJTSDJOCFgb4Q  
\*\*\* Script: Key:refresh\_token value:LkKYLypkbz4Axjbe4Ub8\_vmLPwGH7gTsmbbY5Xcm9pez7nv11yVb4Xj24O8Lt0Mcy2qdyyi3T9ufJF6sd-Ik8g  
\*\*\* Script: Key:scope value:useraccount  
\*\*\* Script: Key:token\_type value:Bearer  
\*\*\* Script: Key:expires\_in value:1799  
\*\*\* Script: Iterating Token Response Parameters Ends  
\*\*\* Script: Prints Glide oAuthToken Object Members  
\*\*\* Script: AccessToken:lVTYldqvnm1Sxku9eCeareEtsD730ZrbMdVGBDzJZ-NdAEivTsGjN80jT-ToRq0RgW2UnRLRPEJTSDJOCFgb4Q  
\*\*\* Script: AccessTokenExpiresIn:1799  
\*\*\* Script: Access Token SysID:null  
\*\*\* Script: Access Token Scope:useraccount  
  

# Curl Command

* * *

A sample curl command to generate token

curl -X POST <token url> -H 'cache-control: no-cache' -H 'content-type: application/x-www-form-urlencoded' -d 'client\_id=ur\_client\_id&client\_secret=ur\_client\_secret  
&grant\_type=password&username=ur\_user\_name&password=ur\_password'

# Glide Scripting

* * *

A sample glide scripting to generate token

var oAuthClient = new sn\_auth.GlideOAuthClient();  
var requestor\_context = 'test';  
var requestor\_id = 'abc@xyz.com';  
var oauth\_profile\_id = 'oauth\_profile\_sysid';

var params = {grant\_type:'password', username:'ur\_user\_name', password:'ur\_password', resource:'ur\_resource\_id', oauth\_requestor\_context:requestor\_context, oauth\_requestor:requestor\_id, oauth\_provider\_profile:oauth\_profile\_id};

var json = new global.JSON();  
var text = json.encode(params);

var tokenResponse = oAuthClient.requestToken('oauth\_profile\_name', text);

var token = tokenResponse.getToken();  
var access\_token = token.getAccessToken() ;

# Applicable Versions

* * *

OAuth 2.0 Integration for Outbound Rest Message is supported from Helsinki release.This integration is tested in the Kingston release.

# Additional Information

* * *

1)GlideOAuthClientResponse - Scoped, Global

[https://docs.servicenow.com/csh?topicname=c\_GlideOAuthClientResponse.html&version=lateste.html](https://docs.servicenow.com/csh?topicname=c_GlideOAuthClientResponse.html&version=lateste.html)

2)GlideOAuthClientRequest - Scoped, Global

[https://docs.servicenow.com/csh?topicname=c\_GlideOAuthClientRequest.html&version=latesthtml](https://docs.servicenow.com/csh?topicname=c_GlideOAuthClientRequest.html&version=latesthtml)

3)GlideOAuthClient - Scoped, Global

[https://docs.servicenow.com/csh?topicname=c\_GlideOAuthClient.html&version=latest](https://docs.servicenow.com/csh?topicname=c_GlideOAuthClient.html&version=latest)

4)snc sn\_auth -oAuth API

[https://developer.servicenow.com/app.do#!/api\_doc?v=kingston&id=c\_OAuthGlideOAuthClient](https://developer.servicenow.com/app.do#!/api_doc?v=kingston&id=c_OAuthGlideOAuthClient)

## Related

- [[KB0693900 - How to generate a token using sn_auth - oAuth API  for Authorization grant type?]] - companion article for the Authorization Code grant type
- [[resource-owner-password-grant]] - official docs on the Resource Owner Password Credentials grant
- [[resource-owner-password-credential-workflow]] - official docs on the ROPC token workflow
- [[c_OAuthApplications]] - official docs on OAuth applications

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0693900 - How to generate a token using sn_auth - oAuth API for Authorization grant type|How to generate a token using sn_auth - oAuth API  for Authorization grant type?]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0725643 - How to generate bearer token for oAuth 2.0 - Authorization Grant type|How to generate bearer token for oAuth 2.0 - Authorization Grant type]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0743846 - Sending additional parameters to the OAuth Provider to retrive the access and refresh tokens using GlideOAuthClient()|Sending additional parameters to the OAuth Provider to retrive the access and refresh tokens using GlideOAuthClient()]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0745184 - OAuth Token of type 'Client Credentials' generates 'User Not Authenticated' in Inbound web service call|OAuth Token of type 'Client Credentials' generates 'User Not Authenticated' in Inbound web service call]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538763 - Determining if the SAML certificate is incorrect|Determining if the SAML certificate is incorrect]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538765 - Determining if ADFS is receiving a signed request| Determining if ADFS is receiving a signed request]]
