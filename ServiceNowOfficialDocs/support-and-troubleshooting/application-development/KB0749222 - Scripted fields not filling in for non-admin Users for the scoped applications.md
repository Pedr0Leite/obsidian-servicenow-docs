---
title: "Scripted fields not filling in for non-admin Users for the scoped applications"
aliases:
  - KB0749222
  - Scripted fields not filling in for non-admin Users for the scoped applications
tags:
  - servicenow
  - support-kb
  - script-includes
  - acl
  - client-callable-script-include
  - glideajax
  - scoped-apps
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749222
kb_number: KB0749222
last_modified: 2024-01-28
---

## Scripted fields not filling in for non-admin Users for the scoped applications

  

### Issue

# Symptoms

There is onload- client scripts which call the script-include and pre-populated the fields on the form. The fields are pre-populated for the admin user, but not working for non-admin users.

The back-end logs show the error message as "Security restrictions on script include: <Name of the Script Include>"

# Cause

The non-admin user is not having access for the script include.

# Resolution

Need to create  "Client-callable script include ACL" for the script Include with the same name of script include. Follow the below steps to create ACL

1- Type ACL on the navigator filter

2- Go To System Security -> Access Control(ACL)

3- Click New

4- Chose Type as "client\_callable\_script\_include", Operation as "execute", Name as "<Name of the Script Include>" used and save

# Additional Information

[Client-callable script include ACL rules](https://docs.servicenow.com/csh?topicname=acl-rule-types.html&version=latest#d924140e405 "Client-callable script include ACL rules")

## Related

- [[KB0687687 - GlideAjax is working inconstantly]]
- [[acl-rule-types|ACL rule types]]
- [[sc-privacy-on-client-callable-script-includes|Security controls for client-callable script includes]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0750886 - ACL script is failing at script include function call|ACL script is failing at script include function call]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0687687 - GlideAjax is working inconstantly|GlideAjax is working inconstantly]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/AjaxAsyncOnSubmit/README|AjaxAsyncOnSubmit]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Check Weekend - Client Side/README|Check Weekend - Client Side]]
