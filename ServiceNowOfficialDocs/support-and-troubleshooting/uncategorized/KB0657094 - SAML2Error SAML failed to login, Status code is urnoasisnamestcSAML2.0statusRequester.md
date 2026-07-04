---
title: "SAML2Error: SAML failed to login, Status code is urn:oasis:names:tc:SAML:2.0:status:Requester"
aliases:
  - KB0657094
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657094
kb_number: KB0657094
last_modified: 2023-10-30
---

## Issue

When SSO is enabled, some SAML request will fail with **SAML2Error: SAML failed to login, Status code is urn:oasis:names:tc:SAML:2.0:status:Requester**

You notice this problem because reviewing the instance system logs (_syslog_ table), it shows:   

-   Source: SAML2
-   Error: **SAML2Error: SAML failed to login, Status code is urn:oasis:names:tc:SAML:2.0:status:Requester**. When it is supposed to be **urn:oasis:names:tc:SAML:2.0:status:Success**

## Resolution

Once you understand the error from the IdP event/system logs, you could either tune the instance SAML settings or update the IdP settings to avoid the problem.  
To understand the SAML request sent, you can use your browser development tools or contact your IdP for more details.  
  
For debugging, we recommend installing SAML debugging tools (e.g. [SAML tracer](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/ "SAML tracer") for Firefox, or [SAML Chrome panel](https://chrome.google.com/webstore/detail/saml-chrome-panel/paijfdbeoenhembfhkhllainmocckace?hl=en "SAML Chrome panel") for Chrome browsers) to access the SAML information sent and received in a more friendly manner.  

To troubleshoot:

1.  Install the debugging tools in the browser you will use to validate the problem.
2.  Reproduce the problem.
3.  Review the SAML request sent to the IdP (e.g. ADFS). Please provide this to your IDP administrator.
4.  Contact your IdP to understand the reason for the **urn:oasis:names:tc:SAML:2.0:status:Requester**.

 **Note:** **urn:oasis:names:tc:SAML:2.0:status:Requester** means the IdP did not like the SAML request that was sent, so it will respond with "**Requester**" instead of "**Success**".

## Additional Information

See this message on the Microsoft TechNet forums: [ADFS SSO and SAML](https://social.msdn.microsoft.com/Forums/en-US/100fcbef-79b1-406f-b7a7-5d9aa02c4711/adfs-sso-and-saml?forum=winserverDS "ADFS SSO and SAML")
