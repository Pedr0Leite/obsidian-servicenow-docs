---
title: "How to generate a token using sn_auth - oAuth API  for Authorization grant type?"
aliases:
  - KB0693900
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
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693900
kb_number: KB0693900
last_modified: 2024-12-12
---

## Issue

This article explains the steps to test **Auth** grant type using the **sn\_auth - oAuth API** for outbound rest message.

## Resolution

In order to achieve the above, Run this script in the scripts background.

/\*\*\*\*   
This scripts is useful to test client credential via glide scripting.   
Prerequisites:Configure OAuth entity with type OAuth provider."Azure AD" is the OAuth Provider.   
  
curl -d "grant\_type=authorization\_code&code=uDFbKLcxsgdwPL4afMqAZIWPUNQAIHFxEtMw0U7rPBCAGDTK9\_3vBUHIRCrdKOdivvHFQrr42bzJ743ufNpPQw&client\_id=e7670e22fdeb1300091ee995affe2247&client\_secret=K2::;\]A|~3&redirect\_uri=https%3A%2F%2F**instancename**.service-now.com%2Foauth\_redirect.do" [https://instancename.service-now.com/oauth\_token.do](https://empimranitom.service-now.com/oauth_token.do)   
  
\*\*\*/   
  
AuthFlow();  
function AuthFlow(){   
  
var tokenRequest = new sn\_auth.GlideOAuthClientRequest();   
tokenRequest.setGrantType("authorization\_code");   
tokenRequest.setParameter("grant\_type","authorization\_code");   
tokenRequest.setParameter("code","uDFbKLcxsgdwPL4afMqAZIWPUNQAIHFxEtMw0U7rPBCAGDTK9\_3vBUHIRCrdKOdivvHFQrr42bzJ743ufNpPQw");   
tokenRequest.setParameter("client\_id","e7670e22fdeb1300091ee995affe2247");   
tokenRequest.setParameter("client\_secret","K2::;\]A|~3");   
tokenRequest.setParameter("redirect\_uri","[https://empimranitsm.service-now.com/oauth\_redirect.do](https://empimranitsm.service-now.com/oauth_redirect.do)");   
  
  
  
  
var oAuthClient = new sn\_auth.GlideOAuthClient();   
  
//Retrieves the token for the client and the request set into a GlideOAuthClientResponse object.   
var tokenResponse = oAuthClient.requestTokenByRequest("Google Contacts API Integration", tokenRequest);   
  
//Prints GlideOAuthClientResponse object.   
gs.info("Prints GlideOAuthClientResponse object members");   
gs.info("Error:" + tokenResponse.getErrorMessage());   
gs.info("Token Response Body:" + tokenResponse.getBody());   
gs.info("Token Response Content Type:" + tokenResponse.getContentType());   
gs.info("Token Response Code:" + tokenResponse.getResponseCode());   
gs.info("Token Response Parameters:" + tokenResponse.getResponseParameters());   
  
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
  

## Additional Information

Doc site

[https://www.servicenow.com/docs/csh?topicname=c\_OAuthApplications.html&version=latest](https://www.servicenow.com/docs/csh?topicname=c_OAuthApplications.html&version=latest)

## Related

- [[KB0693393 - How to generate a token using sn_auth - oAuth API  for Resource Owner Password Credentials grant type?]] - companion article for the ROPC grant type
- [[authorization-code-grant]] - official docs on the OAuth Authorization Code grant
- [[c_OAuthApplications]] - official docs on OAuth applications

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0693393 - How to generate a token using sn_auth - oAuth API for Resource Owner Password Credentials grant type|How to generate a token using sn_auth - oAuth API  for Resource Owner Password Credentials grant type?]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0725643 - How to generate bearer token for oAuth 2.0 - Authorization Grant type|How to generate bearer token for oAuth 2.0 - Authorization Grant type]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0743846 - Sending additional parameters to the OAuth Provider to retrive the access and refresh tokens using GlideOAuthClient()|Sending additional parameters to the OAuth Provider to retrive the access and refresh tokens using GlideOAuthClient()]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0745184 - OAuth Token of type 'Client Credentials' generates 'User Not Authenticated' in Inbound web service call|OAuth Token of type 'Client Credentials' generates 'User Not Authenticated' in Inbound web service call]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538763 - Determining if the SAML certificate is incorrect|Determining if the SAML certificate is incorrect]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538765 - Determining if ADFS is receiving a signed request| Determining if ADFS is receiving a signed request]]
