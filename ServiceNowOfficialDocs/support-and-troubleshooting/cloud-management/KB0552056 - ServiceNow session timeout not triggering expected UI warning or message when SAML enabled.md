---
title: "ServiceNow session timeout not triggering expected UI warning or message when SAML enabled"
aliases:
  - KB0552056
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0552056
kb_number: KB0552056
last_modified: 2024-03-01
---

## ServiceNow session timeout not triggering expected UI warning or message when SAML enabled

  

### Issue

The base system uses a default Apache session timeout of 30 minutes. After 30 minutes of inactivity in the application, the platform logs the user out automatically, unless the Remember Me option in the login screen is selected. When a session expires, the user receives the following warning: "**Your session has expired. Click OK to log in again.**"

# ![](/sys_attachment.do?sys_id=8db3d06b1bbafcd0acdc54e56b4bcb78)

### Cause

Following is the timeout scenario that occurs when ServiceNow is configured with SAML:

1.  Session timeout terminates the user session on instance - does not affect the IdP.
2.  Instance attempts to re-establish the session by making a SAMLRequest to the IdP.
3.  If the user session is not terminated at the IdP, it redirects back to the instance without showing a username/password prompt.
4.  If the user session is terminated at the IdP, it displays the IdPs login screen.

For the above timeout scenario, setting the IdP timeout property to a value that is slightly less than the ServiceNow timeout, allows users to see the IdP's login screen.

### Resolution

In order to see the login page of the IdP when the SN session expires, configure the IdP session to expire \*before\* the SN session does.

### Related Links

ServiceNow default Apache session timeout can be overwritten by doing either of the following:

-   Adding the **glide.ui.session\_timeout** system property (for more information, see [Modifying Session Timeout](https://docs.servicenow.com/ "Modifying Session Timeout"))
-   Installation Exit customizations for SAM instances (for more information, see Login Modifications in [Installations Exits](https://docs.servicenow.com/csh?topicname=r_InstallationExits.html&version=latest "Installations Exits"))

After customizing the ServiceNow session timeout on a SAML-enabled instance, users do not receive any type of warning. The screen does not respond and there is no change in the UI. In some cases, users receive a blank white page in the main content frame or a browser error about not being able to display the content for that frame.
