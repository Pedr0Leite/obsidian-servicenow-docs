---
title: "Configure SMTP and IMAP email accounts with Microsoft Office365 using OAuth2"
aliases:
  - KB0816072
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0816072
kb_number: KB0816072
last_modified: 2026-06-11
---

## Configure SMTP and IMAP email accounts with Microsoft Office365 using OAuth2

  

### Overview

An instance can be configured to connect to email accounts using [OAuth 2.0 authentication](https://docs.servicenow.com/bundle/newyork-servicenow-platform/page/administer/notification/task/t_SetUpOAuth2ForEmail.html "OAuth authentication") for providers who support it.

This article focuses on setting up the OAuth Provider for use with a Microsoft Office365 account. Once configured, you will be able to retrieve access and refresh tokens from the Microsoft Azure OAuth Server using the OAuth2 Authorization Grant Type.

Please note that while this article contains example screenshots of Microsoft product configuration screens, ServiceNow does not provide support for Microsoft products. Please direct any questions about the configuration and administration of Office365 or Exchange to your email administrators. The screenshots belong to our test Azure systems and show a set of configuration that worked for ServiceNow during testing. Your configuration may be different or the screens may be different. **While we strive to help our customers, ServiceNow Support can only provide help with gathering the logs from your instance.** You will need to work with your email & Azure/Office365 administrators to configure your Azure and Office 365 tenants.

Microsoft has announced and documented support for OAuth here:

1.  Microsoft's [announcement](https://developer.microsoft.com/en-us/office/blogs/announcing-oauth-2-0-support-for-imap-smtp-client-protocols-in-exchange-online/ "announcment") of support for OAuth 2.0 with their IMAP and SMTP services
2.  Microsofts [official documentation](https://docs.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth "official documentation") for configuring SMTP/IMAP with OAuth 2.0

**Exclusive Mailbox Access  
**ServiceNow instances assume exclusive use of the IMAP mailbox. The instance deletes mail from the server after reading. Therefore, using a mailbox that is shared among different services and/or users is not recommended. Each service or user will interfere with the instance's mail operations.

**Before beginning**

-   Install the [**Email - OAUTH support for IMAP and SMTP**](https://docs.servicenow.com/bundle/xanadu-platform-administration/page/administer/notification/task/t_ActOAuthEmailAuthPlugin.html "Email - OAUTH support for IMAP and SMTP") plugin.

### 1\. Register an application on Microsoft Azure Active Directory

Register an application on Azure Active Directory using this [article](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app "article"). Make sure to configure following on Azure application.

-   Configure ServiceNow OAuth redirect url

![Configure ServiceNow OAuth redirect url](/sys_attachment.do?sys_id=6f0f146397950bd0539e35d11153af77 "Configure ServiceNow OAuth redirect url")

-   Create client secret for the application to prove its identity when requesting a token.

![Create client secret ](/sys_attachment.do?sys_id=630f146397950bd0539e35d11153afac "Create client secret ")

-   Configure OAuth scopes on Azure applications for SMTP/IMAP and offline\_access (for getting refresh token as per [docs](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#offline_access "docs")). Azure recommends having the User.Read scope for proper functioning, so don't remove that. The final API permissions are shown below.![Configure OAuth scopes - API Permissions](/sys_attachment.do?sys_id=db0f146397950bd0539e35d11153af11 "Configure OAuth scopes ")

### 2\. Configure OAuth in ServiceNow for Microsoft

Configure an **oauth\_entity** record with the OAuth2 Authorization Grant Flow for Microsoft. Please note that all URLs in this article are specific to our Azure tenant, the URLs for your tenant may be different. Please get the correct URLs from your Azure administrator.

1\. Configure Microsoft OAuth endpoints as below

     Authorization URL: https://login.microsoftonline.com/\[Azure Tenant ID\]/oauth2/v2.0/authorize  
     Token URL: https://login.microsoftonline.com/\[Azure Tenant ID\]/oauth2/v2.0/token  
     Redirect URL: {Instance\_URL}/oauth\_redirect.do

2\. OAuth Entity Scopes:

a. Name: "IMAP.AccessAsUser.All"  
    OAuth scope: "[https://outlook.office.com/IMAP.AccessAsUser.All](https://outlook.office.com/IMAP.AccessAsUser.All)"

b. Name: "SMTP.Send"  
    OAuth scope: "[https://outlook.office.com/SMTP.Send](https://outlook.office.com/SMTP.Send)"

c. Name: "offline\_access"  
    OAuth scope: "offline\_access"

3\. Configure "OAuth Entity Profile Scopes" with all scopes created from step#2.

![Configure "OAuth Entity Profile Scopes"](/sys_attachment.do?sys_id=a30f546397950bd0539e35d11153af33 "Configure \"OAuth Entity Profile Scopes\"")

4\. Make sure the same scopes are in both the oauth\_entity\_profile record and the oauth\_entity record

5\. Create SMTP/IMAP email account with OAuth 2.0 Authentication and reference above OAuth Entity Profile in **OAuth Profile** field in Email accounts. See the Documentation: [Enable OAuth 2.0 for email.](https://docs.servicenow.com/bundle/paris-servicenow-platform/page/administer/notification/task/t_SetUpOAuth2ForEmail.html "Enable OAuth 2.0 for email")

#### ![ Create SMTP/IMAP email account with OAuth 2.0 ](/sys_attachment.do?sys_id=ef0f146397950bd0539e35d11153afe6 " Create SMTP/IMAP email account with OAuth 2.0 ")

VERY IMPORTANT: If  in the following step you do not get asked for username and password the account will not be able to send emails. ENSURE you are logged in as a local admin account in an incognito window for the next step.

Explanation: the SMTP or IMAP account will otherwise be authorized with your personal AD account, this will not allow the instance receive or send emails. 

6\. Use "**Authorize Email Account Access"** action to obtain the access and refresh token. You must use an **incognito/private window** and a local login (side\_door.do if needed) to make sure your personal account is not picked up by Microsoft SSO login. The username/credentials of the email account should be provided, not your own credentials. If you try to authorize while you are already logged in to Azure, no pop-up window will appear and it might look like the authorization succeeded. However, the instance will receive an access token for your own credentials instead of the email account. Testing the connection will result in an error in this case since the instance will be using your account to access the mailbox and fail.

Note: You can use the **Scripts - Background** provided in [KB2071947](/kb?id=kb_article_view&sysparm_article=KB2071947 "Access Token validation for OAuth configured with Microsoft Identity Platform") to validate the JWT (Access Token) and confirm if the Email Account Access was properly Authorized.

(Note: The instance needs to have a valid/active Oauth token to use to connect to the mailbox in question (it be IMAP or SMTP) so that once the connection is established, the email data can be pushed to the mailbox in question: if you don't have one, go into the Oauth profile being used in the email account record and there should be a link for "Get Oauth Token" which you can click on to obtain a new token.)

### Token refresh

Ensure the System Administrator user has the 'admin' role.  The OAuth 2.0 implementation requires you to obtain an access and refresh token from your email provider for each third-party email account. The tokens are automatically saved to the instance database. A scheduled job at https://<instance>.service-now.com/nav\_to.do?uri=sysauto\_script.do?sys\_id=35faf162eb233100469a20425206fedc regularly checks to see if email access tokens are valid. When the access token is not valid, but the refresh token is, the instance automatically regenerates a new access token.

The scheduled job is configured to run as _system administrator_ and requires the the admin role. Without this role, the token refresh operation will fail when storing the token to the oauth\_credential table. Access to the email account will fail when the access token expires.

Reference: [Authenticate an IMAP, POP or SMTP connection using OAuth](https://docs.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth "https://docs.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth")

### Additional logging

If the instance is not able to connect to the mailbox, please check the "Enable debug output" option in the sys\_email\_account record. This will output all the communication between the instance and the mail server in to the node logs. Please follow [How to download localhost logs from all or selected nodes](/kb?id=kb_article_view&sysparm_article=KB0826291) to download the node logs. The relevant lines will contain DEBUG: SMTP or DEBUG: IMAP such as

2022-09-20 00:20:37 (002) worker.3 worker.3 txid=3359b621874e DEBUG: SMTP: enable SASL  
2022-09-20 00:29:27 (018) worker.6 worker.6 txid=c96bfae9878e DEBUG: IMAP: AUTH: PLAIN

Please share this information with your email administrator and Azure administrator if needed as it may help them identify which stage the connection is failing. Do not forget to turn debugging off after troubleshooting, especially in production instances, as these options output all email traffic, including email content, to be output in to the node logs. This may cause node logs to be truncated after several gigabytes, and the node logs will become useless for troubleshooting other issues.

### Known Errors  
![Connection Failed error](/sys_attachment.do?sys_id=ab0f146397950bd0539e35d11153afa4 "Connection Failed error")

-   **Error**: No OAuth refresh token for active email account. Manual reauthorization required. Account=""

At the step "Click **Authorize Email Account Access** to obtain the access and refresh token. "  
Use an **incognito/private window** and a local login (side\_door.do if needed). The username/credentials of the email account should be provided, not your own credentials.

-   **Error**:invalid\_request, AADSTS90002: Tenant 'xxxxxx-xxxxx-xxxxx' not found. Check to make sure you have the correct tenant ID and are signing into the correct cloud. Check with your subscription administrator, this may happen if there are no active subscriptions for the tenant.

Ensure the Azure Tenant ID in the Authorization URL and Token URL match the Tenant ID on the Azure Portal.  
  

### ![Cannot connect to SMTP error](sys_attachment.do?sys_id=ef0f146397950bd0539e35d11153afed "Cannot connect to SMTP error")

-   **Error**: Connection Failed. Email sender connection invalid.: Cannot connect to SMTP server: smtp.office365.com, as:  <M365 Email as configured in "User name" field>, message: failed to connect

API permission scopes assigned to registered Azure app are for Microsoft Graph resource. The mailbox might be assigned a license that doesn't have access to Graph API, e.g. Exchange Online (Plan 1). Switching to supported license, such as Office 365 E5 should fix the issue.

-   **Error**: Email access token are not getting refreshed

Access tokens will not be refreshed automatically by the **"Refresh Email Access Token"** scheduled job if one of the oauth\_entity records linked to a sys\_email\_account is set to Active = False. This is a known issue tracked via **PRB1588339** and a fix is available in **Utah Patch 1**.

-   **Error**: IMAP emails not processed due to queued jobs in node caused by java.io.ExpiringCache.cleanup

This is a known issue tracked via **PRB1635023** and a fix is available in **Vancouver**.

### Email error received: OAuth token is not present or has expired after a password reset

-   **Error**: Email is no longer flowing even though the account looks connected

If the Password has been changed on the IMAP account, you will need to re-pull the tokens. Refer to [**KB1295058**](/kb?id=kb_article_view&sysparm_article=KB1295058 "KB1295058")

![Got bad greeting from SMTP - error](/sys_attachment.do?sys_id=d70fd06397950bd0539e35d11153af1a "Got bad greeting from SMTP - error")

-   **Error**: Connection Failed. Email sender connection invalid. :Cannot connect to SMTP server: outlook.office365.com, as xxxxxxxxx message: Got bad greeting from SMTP host:outlook.office365.com,port:993, response: \*OK The Microsoft Exchange IMAP4 service is ready.

Port 993 is for the Microsoft IMAP server. The correct port to use for the Microsoft SMTP server is 587.

#### Common Issues:

1.  [SMTP and IMAP Email Account Test Connections Fail with OAuth Authentication](/kb?id=kb_article_view&sysparm_article=KB1642290)  
      
    
2.  [When creating a new Email Account which uses OAuth 2.0, it is not possible to configure it with an OAuth profile of type "Resource Owner Password Credentials"](/kb?id=kb_article_view&sysparm_article=KB2400156)  
      
    
3.  [Office 365 SMTP email account test connection fails after OAuth authorization](/kb?id=kb_article_view&sysparm_article=KB1648902)  
      
    
4.  Looking at the above setup Step 6 in this articles setup steps is often missed or done improperly please re-review.  
      
    
5.  May encounter 401 or 400 errors if the endpoint URLs are incorrect, grant type is incorrect, or user lacks permissions to needed resources.

#### Further considerations:

It might be wise to discuss with your mail administrators if the instance IP (for making connections into the customers network on the My Ip information catalog item) can be whitelisted as a trusted IP for sending emails through office365.com

**Other supporting documentation includes:**

Microsoft Graph application-permission-based access:  
"[https://docs.wpo365.com/article/166-send-email-using-microsoft-graph-with-application-level-permissions](https://docs.wpo365.com/article/166-send-email-using-microsoft-graph-with-application-level-permissions)"

ServiceNow developer blog on Graph API setup:  
"[https://www.servicenow.com/community/developer-blog/reading-email-using-microsoft-graph-api/ba-p/3084506](https://www.servicenow.com/community/developer-blog/reading-email-using-microsoft-graph-api/ba-p/3084506)"

Microsoft's guidance on restricting Graph API access to specific shared mailboxes via Application Access Policies:  
"[https://learn.microsoft.com/en-us/answers/questions/2149155/permissions-to-access-shared-mailbox-to-read-and-s](https://learn.microsoft.com/en-us/answers/questions/2149155/permissions-to-access-shared-mailbox-to-read-and-s)"

ServiceNow's documentation  for Graph-based email reading using OAuth and Graph API:  
"[https://www.servicenow.com/docs/bundle/yokohama-platform-administration/page/administer/notification/concept/read-email-using-ms-graph.html?state=seamless](https://www.servicenow.com/docs/bundle/yokohama-platform-administration/page/administer/notification/concept/read-email-using-ms-graph.html?state=seamless)"
