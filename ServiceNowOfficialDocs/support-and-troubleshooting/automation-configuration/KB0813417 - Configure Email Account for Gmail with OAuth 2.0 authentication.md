---
title: "Configure Email Account for Gmail with OAuth 2.0 authentication"
aliases:
  - KB0813417
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813417
kb_number: KB0813417
last_modified: 2024-03-14
---

## Text

### Overview

ServiceNow email accounts can be configured to use [OAuth 2.0 authentication](https://docs.servicenow.com/bundle/utah-platform-security/page/administer/security/concept/c_OAuthApplications.html "OAuth authentication") for providers who support it.

This article focuses on setting up the OAuth Provider for use with a GMail account. Once configured, you will be able to retrieve access and refresh tokens from the Google OAuth Server using the OAuth2 Authorization Grant Type.

**Before beginning**

-   Install the **Email - OAUTH support for IMAP and SMTP** plugin
-   Get Google OAuth2 credentials (eg. client id, client secret etc.) from [Google API Console](https://console.developers.google.com/ "Google API Console") (more details about [Google OAuth2 protocol](https://developers.google.com/identity/protocols/OAuth2 "Google OAuth2 protocol")).

### Setting up OAuth for Gmail in ServiceNow

This KB configures an **oauth\_entity** record for the OAuth2 Authorization Grant Flow with Gmail.

1\. Configure Gmail OAuth endpoints as below

     Authorization URL: https://accounts.google.com/o/oauth2/auth  
     Token URL: https://accounts.google.com/o/oauth2/token  
     Token Revocation URL: https://accounts.google.com/o/oauth2/revoke  
     Redirect URL: <instance\_url>/oauth\_redirect.do

2\. OAuth API Script: **OAuthGoogleOfflineAccess**

3\. OAuth Entity Scopes:

Name: "Gmail Scope"  
OAuth scope: "https://mail.google.com"

4\. Update "OAuth Entity Profile Scopes" with "Gmail Scope" from previous step.

![](sys_attachment.do?sys_id=dd39e273937c82d0d9743f986cba1037)

5\. Create an email account with OAuth 2.0 Authentication and reference above OAuth Entity Profile in **OAuth Profile** field in Email accounts.

6\. Example of SMTP config looks like below (IMAP follows same rule with user names):

![](/sys_attachment.do?sys_id=66d96a37937c82d0d9743f986cba1029)

7\. Whatever is specified in the username is the email that should be entered when clicking "Authorize Email Account Access"
