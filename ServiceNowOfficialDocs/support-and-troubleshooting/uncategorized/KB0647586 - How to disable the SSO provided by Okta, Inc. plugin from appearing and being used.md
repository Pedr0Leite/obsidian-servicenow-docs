---
title: "How to disable the \"SSO provided by Okta, Inc.\" plugin from appearing and being used"
aliases:
  - KB0647586
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647586
kb_number: KB0647586
last_modified: 2024-04-07
---

## How to disable the "SSO provided by Okta, Inc." plugin from appearing and being used

  

### Issue

How to disable the "SSO provided by Okta, Inc." plugin from appearing and being used

Problem

* * *

SSO provided by Okta, Inc. plugin is not longer supported by OKTA. We recommend to migrate your OKTA authentication to use our Integration - Multiple Provider Single Sign-On Installer plugin instead. However, once you moved your SSO integration to Multi Provider SSO, the old OKTA menus still show.  
  

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: Disabling <strong>SSO provided by OKTA</strong> module does not affects the Multi Provider Single Sign-On plugin.</td></tr></tbody></table>

  
  

Cause

* * *

Plugins do not have an un-install option. Manually modify the instance to disable the plugins.  

Resolution

* * *

To disable your SSO provided by Okta, Inc. plugin, login into instance using local **admin** account.  
  
Navigate to the instance application module and make it disabled: Uncheck **Active** checkbox.  
  

<table style="background-color: #ebebeb;"><tbody><tr><td>&nbsp;&lt;instance&gt;/nav_to.do?uri=sys_app_application.do?sys_id=555a3314c0a801660132e91044d5081a</td></tr></tbody></table>

  
![Go to the instance application module and make it disabled: Uncheck 'Active' checkbox](sys_attachment.do?sys_id=b76c2c6edb42b450e515c2230596194c "Go to the instance application module and make it disabled: Uncheck 'Active' checkbox")  
  
  
Navigate to the instance installation exit for Okta, and Uncheck **Active** checkbox  

<table style="background-color: #ebebeb;"><tbody><tr><td>&nbsp;&lt;instance&gt;/nav_to.do?uri=sys_installation_exit.do?sys_id=ddbb0444bf121100e628555b3f073951</td></tr></tbody></table>

  
![Go to the instance installation exit for OKta, and Uncheck 'Active' checkbox](sys_attachment.do?sys_id=b36c2c6edb42b450e515c22305961952 "Go to the instance installation exit for OKta, and Uncheck 'Active' checkbox")  
  
Finally, refresh left navigation pane if **SSO provided by OKTA** module still appears.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: Refresh left navigation pane if <strong>SSO provided by OKTA</strong> module still appears.</td></tr></tbody></table>
