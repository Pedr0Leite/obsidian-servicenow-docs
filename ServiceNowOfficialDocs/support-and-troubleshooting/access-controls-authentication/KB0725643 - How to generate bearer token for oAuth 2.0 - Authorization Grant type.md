---
title: "How to generate bearer token for oAuth 2.0 - Authorization Grant type"
aliases:
  - KB0725643
tags:
  - servicenow
  - support-kb
  - oauth
  - oauth2
  - authorization-code-grant
  - bearer-token
  - rest-api
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725643
kb_number: KB0725643
last_modified: 2025-09-17
---

## Issue

The **Now Platform** supports **OAuth 2.0 - Authorization Grant type** for public clients to generate an **access token**. This requires 3 steps.

1.  Register the app
2.  Generate Authorization Code
3.  Generate Bearer Token using Authorization Code.

### Use Case

Use **Access Token** to access **Table API** or **Scripted Web Service**.

### Register the app

Navigate to **System oAuth** > **Application Registry** > **Create an OAuth API endpoint for external clients**

![](sys_attachment.do?sys_id=602efa704727aa14d1a5ab29736d4366)

<table style="width: 90%; border-style: solid; border-color: #000;" border="1" cellpadding="4"><tbody><tr style="height: 13px;"><td style="height: 13px; width: 165px;"><strong>Name</strong></td><td style="height: 13px; width: 779px;"><strong>Definition</strong></td></tr><tr style="height: 13px;"><td style="height: 13px; width: 165px;">Name</td><td style="height: 13px; width: 779px;">Name of the registered app</td></tr><tr style="height: 13px;"><td style="height: 13px; width: 165px;">Client ID</td><td style="height: 13px; width: 779px;">client id of the registered app</td></tr><tr style="height: 13px;"><td style="height: 13px; width: 165px;">Client Secret</td><td style="height: 13px; width: 779px;">client secret of the registered app</td></tr><tr style="height: 14px;"><td style="height: 14px; width: 165px;">Redirect URI</td><td style="height: 14px; width: 779px;">Authorization code is returned to this URI. This is usually the endpoint of the registered app. The screenshot has <em>login.do</em> for demo purposes</td></tr><tr style="height: 13px;"><td style="height: 13px; width: 165px;">Authorization Code Life Span</td><td style="height: 13px; width: 779px;">The lifespan of the authorization code. Extend the lifespan if required. It expires in 60 seconds by default.<br><em>(To edit either add auth_code_lifespan field to the <a href="https://docs.servicenow.com/csh?topicname=configure-form-layout.html&amp;version=latest" target="_blank" rel="noopener noreferrer">form&nbsp;</a>or the <a href="https://docs.servicenow.com/csh?topicname=c_PersonalLists.html&amp;version=latest" target="_blank" rel="noopener noreferrer">columns&nbsp;</a>on the list view then increase to integer more than 60)</em></td></tr><tr style="height: 13px;"><td style="height: 13px; width: 165px;">Access Token Life Span</td><td style="height: 13px; width: 779px;">The lifespan of the access token</td></tr><tr style="height: 13px;"><td style="height: 13px; width: 165px;">Refresh Token Life Span</td><td style="height: 13px; width: 779px;">The lifespan of the refresh token</td></tr></tbody></table>

### Generate Authorization Code

**Authorization code** requires a **user login**. Use these steps to generate an authorization code.

1.  Access the **authorization endpoint**. This requires **response type**, **redirect uri**, and **client id:  
    **  
    Sample edit this URL to match the above and put it in your browser:  
      
    
    ```
    https://<Instance_Name>.service-now.com/oauth_auth.do?grant_type=authorization_code&redirect_uri=https://<Instance_Name>.service-now.com/login.do&client_id=<CLIENT_ID>&response_type=code&state=123
    ```
    
    See the following for more info:  
    [Authorization code flow state parameter requirement](https://docs.servicenow.com/csh?topicname=oauth-auth-code-flow-state-parm.html&version=latest)  
      
      
    
2.  The user is redirected to **oauth login** page: /oauth\_login.do  
      
    ![](sys_attachment.do?sys_id=282efa704727aa14d1a5ab29736d4368)  
      
    
3.  Enter valid credentials. \[Ensure the user has permissions to read/write on the oauth\_credential table or use "admin" account to override ACL issues\]  
      
    
4.  User needs to either **Allow/Deny** the request.  
      
    ![](sys_attachment.do?sys_id=602efa704727aa14d1a5ab29736d4386)  
      
    
5.  Authorization code is returned to **redirect uri** after clicking **Allow** will show up in the browser URL and look like the following:  
    
    ```
    https://<INSTANCE_NAME>.service-now.com/login.do?code=iz8efjPNK-4Q_ZOS3DcEqcJa9oXo1uLhpItv30PhaeknEfGWMF2haVCpYwGLg7cXzVpYqkMnkHF242VuFe8ZCQ&state=123
    ```
    
    ![](/sys_attachment.do?sys_id=58614b704767aa14d1a5ab29736d4356 "Capture4.PNG")
    
6.  Authorization code is valid for **60 seconds** by default so if you take to long to do the next steps just redo steps 2-5 to get new code. You can increase this value from the list view or form --><auth\_code\_lifespan>  
      
    
7.  Copy the code as this will be used in the next steps  
      
      
    

### Generate Bearer Token

**oauth\_token.do** supports **post** ( **form url encoded** ) to generate an **access** token. This requires **code**, **redirect uri**, **client id**, **client secret**, and **grant type** to generate an access token.  
  
You can either use Postman or cURL to post the request.   
  
**Postman  
  
POST** 

```
https://<Instance_Name>.service-now.com/oauth_token.do
```

**Body \[x-www-form-urlencoded\]  
  
**Update **"redirect\_uri", "grant\_type", "code", "client\_secret" & "client\_id"** here:  
![](/sys_attachment.do?sys_id=8ae0cbbc4727aa14d1a5ab29736d437a "Capture4.PNG")  
**  
Curl:**

```
curl -d "grant_type=authorization_code&code=<AUTH_CODE>&client_id=<CLIENT_ID>&client_secret=<CLIENT_SECRET>&redirect_uri=https://<INSTANCE_NAME>.service-now.com/login.do" https://<INSTANCE_NAME>.service-now.com/oauth_token.do
```

**Sample Output:  
**

```
{
    "access_token": "SFgoFLvSiNVIwtU9O1U0hNsk2PaogKYkyg2KtnoilUmmeliibScwAG8A1vQlXODllLvHhcD1",
    "refresh_token": "GyLc-OX2Jd-NHpMpQUJbIcOhgqkQu-WoWhqNX68xouWV47Mn2TKqGU12EDsUoShND",
    "scope": "",
    "token_type": "Bearer",
    "expires_in": 1799
}
```

## Resolution

Ensure all the required parameters are passed to resolve the error. Afterwards you can use the access token to do other API calls until it expires.

If you get an error during the call such as "access\_denied" please do the following:

1.  Test the same username/password for logging into the UI, ensure it does not require MFA
    -   If user used for Oauth call can login without issues using local login move to next step. Otherwise correct this behavior.  
          
        
2.  Test the Oauth call with a user that can do the above which has the admin role, if it works for an admin user but not another user it lacks sufficient roles to pull and oAuth token.
    -   Try adding addition roles such as: snc\_internal, web\_service\_admin, oauth\_admin, etc...
    -   If issue is not with roles check the Auth Scope set on the application registry

## Additional Information

-   RFC: [https://tools.ietf.org/html/rfc6749#section-1.3.1](https://tools.ietf.org/html/rfc6749#section-1.3.1 "https://tools.ietf.org/html/rfc6749#section-1.3.1")
-   [OAuth authorization code grant flow](#mce_temp_url#5494)

## Related

- [[KB0693900 - How to generate a token using sn_auth - oAuth API for Authorization grant type]]
- [[KB0693393 - How to generate a token using sn_auth - oAuth API for Resource Owner Password Credentials grant type]]
- [[KB0783404 - User unable to get an OAuth 2.0 access token]]
- [[configure-an-oauth-authorization-code-grant]] - official docs on configuring the OAuth authorization code grant
- [[c_OAuthAuthorizationCodeFlow]] - official docs on the OAuth authorization code flow

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0693393 - How to generate a token using sn_auth - oAuth API for Resource Owner Password Credentials grant type|How to generate a token using sn_auth - oAuth API  for Resource Owner Password Credentials grant type?]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0693900 - How to generate a token using sn_auth - oAuth API for Authorization grant type|How to generate a token using sn_auth - oAuth API  for Authorization grant type?]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0753132 - Users getting Unauthorized access error in Service Portal when REST API level ACLs are in place|Users getting \"Unauthorized access\" error in Service Portal when REST API level ACLs are in place ]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0724965 - User Criteria is not working via REST API or Web Service call|User Criteria is not working via REST API or Web Service call]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0727636 - How to export bulk data from ServiceNow using REST API pagination|How to export bulk data from ServiceNow using REST API pagination]]
