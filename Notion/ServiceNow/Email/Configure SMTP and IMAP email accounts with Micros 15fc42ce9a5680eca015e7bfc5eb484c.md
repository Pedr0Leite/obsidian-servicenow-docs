---
aliases:
  - "Configure SMTP and IMAP email accounts with Micros"
area: "Email"
source: notion-export
tags:
  - email
  - smtp
  - imap
  - oauth2
  - office365
  - troubleshooting
---

# Configure SMTP and IMAP email accounts with Microsoft Office365 using OAuth2

### Overview

An instance can be configured to connect to email accounts using [OAuth 2.0 authentication](https://docs.servicenow.com/bundle/newyork-servicenow-platform/page/administer/notification/task/t_SetUpOAuth2ForEmail.html) for providers who support it.

This article focuses on setting up the OAuth Provider for use with a 
Microsoft Office365 account. Once configured, you will be able to 
retrieve access and refresh tokens from the Microsoft Azure OAuth Server
 using the OAuth2 Authorization Grant Type.

Please note that while this article contains example screenshots of 
Microsoft product configuration screens, ServiceNow does not provide 
support for Microsoft products. Please direct any questions about the 
configuration and administration of Office365 or Exchange to your email 
administrators. **While we strive to help our customers, ServiceNow Support can only provide help with gathering the logs from your instance.** You will need to work with your email & Azure/Office365 administrators to configure Azure and Office 365.

Microsoft has announced and documented support for OAuth here:

1. Microsoft's [announcement](https://developer.microsoft.com/en-us/office/blogs/announcing-oauth-2-0-support-for-imap-smtp-client-protocols-in-exchange-online/) of support for OAuth 2.0 with their IMAP and SMTP services
2. Microsofts [official documentation](https://docs.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth) for configuring SMTP/IMAP with OAuth 2.0

**Exclusive Mailbox Access**ServiceNow instances 
assume exclusive use of the IMAP mailbox. The instance deletes mail from
 the server after reading. Therefore, using a mailbox that is shared 
among different services and/or users is not recommended. Each service 
or user will interfere with the instance's mail operations.

**Before beginning**

- Install the [**Email - OAUTH support for IMAP and SMTP**](https://docs.servicenow.com/bundle/xanadu-platform-administration/page/administer/notification/task/t_ActOAuthEmailAuthPlugin.html) plugin.

### 1. Register an application on Microsoft Azure Active Directory

Register an application on Azure Active Directory using this [article](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app). Make sure to configure following on Azure application.

- Configure ServiceNow OAuth redirect url

![image.png](Configure%20SMTP%20and%20IMAP%20email%20accounts%20with%20Micros/image.png)

• Create client secret for the application to prove its identity when requesting a token.

![image.png](Configure%20SMTP%20and%20IMAP%20email%20accounts%20with%20Micros/image%201.png)

Configure OAuth scopes on Azure applications for SMTP/IMAP and offline_access (for getting refresh token as per [docs](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#offline_access)).
 Azure recommends having the User.Read scope for proper functioning, so 
don't remove that. The final API permissions are shown below.

![apiPermissionNotRequiringAdminConsent.png](Configure%20SMTP%20and%20IMAP%20email%20accounts%20with%20Micros/apiPermissionNotRequiringAdminConsent.png)

### 2. Configure OAuth in ServiceNow for Microsoft

Configure an **oauth_entity** record with the OAuth2 
Authorization Grant Flow for Microsoft. Please note that all URLs in 
this article are specific to our Azure tenant, the URLs for your tenant 
may be different. Please get the correct URLs from your Azure 
administrator.

1. Configure Microsoft OAuth endpoints as below

Authorization URL: https://login.microsoftonline.com/[Azure Tenant ID]/oauth2/v2.0/authorize

Token URL: https://login.microsoftonline.com/[Azure Tenant ID]/oauth2/v2.0/token

Redirect URL: {Instance_URL}/oauth_redirect.do

2. OAuth Entity Scopes:

a. Name: "IMAP.AccessAsUser.All"

OAuth scope: "[https://outlook.office.com/IMAP.AccessAsUser.All](https://outlook.office.com/IMAP.AccessAsUser.All)"

b. Name: "SMTP.Send"

OAuth scope: "[https://outlook.office.com/SMTP.Send](https://outlook.office.com/SMTP.Send)"

c. Name: "offline_access"

OAuth scope: "offline_access"

3. Configure "OAuth Entity Profile Scopes" with all scopes created from step#2.

![updatedOAuthSettings.png](Configure%20SMTP%20and%20IMAP%20email%20accounts%20with%20Micros/updatedOAuthSettings.png)

4.Make sure the same scopes are in both the oauth_entity_profile record and the oauth_entity record

5. Create SMTP/IMAP email account with OAuth 2.0 Authentication and reference above OAuth Entity Profile in **OAuth Profile** field in Email accounts. See the Documentation: [Enable OAuth 2.0 for email.](https://docs.servicenow.com/bundle/paris-servicenow-platform/page/administer/notification/task/t_SetUpOAuth2ForEmail.html)

![Pasted image.png](Configure%20SMTP%20and%20IMAP%20email%20accounts%20with%20Micros/Pasted_image.png)

6. Use "**Authorize Email Account Access"** action to obtain the access and refresh token. You must use an **incognito/private window** and a local login (side_door.do if needed) to make sure your personal account is not picked up by Microsoft SSO login.
 The username/credentials of the email account should be provided, not 
your own credentials. If you try to authorize while you are already 
logged in to Azure, no pop-up window will appear and it might look like 
the authorization succeeded. However, the instance will receive an 
access token for your own credentials instead of the email account. 
Testing the connection will result in an error in this case since the 
instance will be using your account to access the mailbox and fail.

(Note: The instance needs to have a valid/active Oauth token to use 
to connect to the mailbox in question (it be IMAP or SMTP) so that once 
the connection is established, the email data can be pushed to the 
mailbox in question: if you don't have one, go into the Oauth profile 
being used in the email account record and there should be a link for 
"Get Oauth Token" which you can click on to obtain a new token.)

### Token refresh

Ensure the System Administrator user has the 'admin' role.  The OAuth
 2.0 implementation requires you to obtain an access and refresh token 
from your email provider for each third-party email account. The tokens 
are automatically saved to the instance database. A scheduled job at 
https://<instance>.service-now.com/nav_to.do?uri=sysauto_script.do?sys_id=35faf162eb233100469a20425206fedc
 regularly checks to see if email access tokens are valid. When the 
access token is not valid, but the refresh token is, the instance 
automatically regenerates a new access token.

The scheduled job is configured to run as *system administrator* and requires the the admin
 role. Without this role, the token refresh operation will fail when 
storing the token to the oauth_credential table. Access to the email 
account will fail when the access token expires.

Reference: [Authenticate an IMAP, POP or SMTP connection using OAuth](https://docs.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth)

### Additional logging

If the instance is not able to connect to the mailbox, please check 
the "Enable debug output" option in the sys_email_account record. This 
will output all the communication between the instance and the mail 
server in to the node logs. Please follow [How to download localhost logs from all or selected nodes](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0826291) to download the node logs. The relevant lines will contain DEBUG: SMTP or DEBUG: IMAP such as

```
2022-09-20 00:20:37 (002) worker.3 worker.3 txid=3359b621874e DEBUG: SMTP: enable SASL
2022-09-20 00:29:27 (018) worker.6 worker.6 txid=c96bfae9878e DEBUG: IMAP: AUTH: PLAIN
```

Please share this information with your email administrator and Azure
 administrator if needed as it may help them identify which stage the 
connection is failing. Do not forget to turn debugging off after 
troubleshooting, especially in production instances, as these options 
output all email traffic, including email content, to be output in to 
the node logs. This may cause node logs to be truncated after several 
gigabytes, and the node logs will become useless for troubleshooting 
other issues.

![Pasted image.png](Configure%20SMTP%20and%20IMAP%20email%20accounts%20with%20Micros/Pasted_image%201.png)

- **Error**: No OAuth refresh token for active email account. Manual reauthorization required. Account=""

At the step "Click **Authorize Email Account Access** to obtain the access and refresh token. "

Use an **incognito/private window**
 and a local login (side_door.do if needed). The username/credentials of
 the email account should be provided, not your own credentials.

- **Error**:invalid_request, AADSTS90002: Tenant 'xxxxxx-xxxxx-xxxxx' not found. Check to make sure
you have the correct tenant ID and are signing into the correct cloud.
Check with your subscription administrator, this may happen if there are no active subscriptions for the tenant.

Ensure the Azure Tenant ID in the Authorization URL and Token URL match the Tenant ID on the Azure Portal.

![Screen Shot 2022-07-28 at 3.54.12 pm.png](Configure%20SMTP%20and%20IMAP%20email%20accounts%20with%20Micros/Screen_Shot_2022-07-28_at_3.54.12_pm.png)

- **Error**: Connection Failed. Email sender connection invalid.: Cannot connect to
SMTP server: smtp.office365.com, as: <M365 Email as configured in
"User name" field>, message: failed to connect

API permission scopes assigned to registered Azure app are for 
Microsoft Graph resource. The mailbox might be assigned a license that 
doesn't have access to Graph API, e.g. Exchange Online (Plan 1). 
Switching to supported license, such as Office 365 E5 should fix the 
issue.

- **Error**: Email access token are not getting refreshed

Access tokens will not be refreshed automatically by the **"Refresh Email Access Token"**
 scheduled job if one of the oauth_entity records linked to a 
sys_email_account is set to Active = False. This is a known issue 
tracked via **PRB1588339** and a fix is available in **Utah Patch 1**.

- **Error**: IMAP emails not processed due to queued jobs in node caused by java.io.ExpiringCache.cleanup

This is a known issue tracked via **PRB1635023** and a fix is available in **Vancouver**.

### Email error received: OAuth token is not present or has expired after a password reset

- **Error**: Email is no longer flowing even though the account looks connected

If the Password has been changed on the IMAP account, you will need to re-pull the tokens. Refer to [**KB1295058**](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1295058)

![2024-02-10_16-20-12.png](Configure%20SMTP%20and%20IMAP%20email%20accounts%20with%20Micros/2024-02-10_16-20-12.png)

- **Error**: Connection Failed. Email sender connection invalid. :Cannot connect to
SMTP server: outlook.office365.com, as xxxxxxxxx message: Got bad
greeting from SMTP host:outlook.office365.com,port:993, response: *OK
The Microsoft Exchange IMAP4 service is ready.

Port 993 is for the Microsoft IMAP server. The correct port to use for the Microsoft SMTP server is 587.

## Related

- [[Email]]
- [[Outlook Actionable Messages]]
- [[SSO – SAML]]
- [[How to setup OAuth2 authentication for RESTMessage]]