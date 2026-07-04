---
title: "Service Portal requires requires 'Multi SSO' to provide external authentication access on the Login widget"
aliases:
  - KB0657354
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657354
kb_number: KB0657354
last_modified: 2024-04-07
---

## Service Portal requires requires 'Multi SSO' to provide external authentication access on the Login widget

  

### Issue

Service Portal requires requires 'Multi SSO' to provide external authentication access on the Login widget

Problem

* * *

Service Portal is an alternative to the Content Management System (CMS) and a simple way to create portals for end users. However, if external authentication by SSO is required, the additional dialog will not be displayed without the Muti SSO plugin installed.

![External authentication](sys_attachment.do?sys_id=df8be0aadb42b450e515c223059619c5 "External authentication")

Symptoms

* * *

You will recognize this problem because:

-   You do not have Multi SSO plugin installed
-   You do have SAML plugin installed
-   You are using Service Portal login widget
-   The Service Portal login page does not show the option to **Use external login**

Cause

* * *

To use single sign-on with Service Portal, enable the Integration - Multiple Provider Single Sign-On Installer plugin (com.snc.integration.sso.multi.installer). This is documented [here.](https://docs.servicenow.com/csh?topicname=c_SPSSOLoginAndRedirects.html&version=latest#c_URLRedirects "here")

Resolution

* * *

To allow external authentication with Service Portal, ensure you have our Multiple Provider Single Sign-On Installer plugin installed and configured.  
On most setups, you will need to contact your Identity Provider (IdP) administrator to re-validate your new IdP record metadata.  
  
Please perform the followings:

1.  Backup your SAML properties and configuration and install the Multiple Provider Single Sign-On Installer plugin.
2.  The installation could create a migrated IdP record. If it doesn't, please create it. Finally, validate the IdP is correct with Test Connection and [activate the required options](https://docs.servicenow.com/csh?topicname=t_SettingUpMultiProviderSSO.html&version=latest "active the required options").
3.  Validate the external authentication login will show on Service Portal.

Alternatively, you could workaround this limitation by asking your users to go to your instance root page / first, on which they would authenticate, then navigate to the Service Portal page after they were successful authenticated.  

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>: Fully test these changes on development before making changes on production</td></tr></tbody></table>
