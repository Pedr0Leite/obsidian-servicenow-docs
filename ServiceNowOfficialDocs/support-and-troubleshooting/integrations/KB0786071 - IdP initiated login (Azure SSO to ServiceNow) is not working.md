---
title: "IdP initiated login (Azure SSO to ServiceNow) is not working"
aliases:
  - KB0786071
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786071
kb_number: KB0786071
last_modified: 2024-04-08
---

## IdP initiated login (Azure SSO to ServiceNow) is not working

  

### Issue

SSO Integration is setup between a ServiceNow instance (Service Provider - SP) and Microsoft Azure (Identity Provider - IdP). Now when a user performs an SP initiated login, it works good i.e. user is authenticated successfully.

However, when a user performs an IdP initiated login attempt i.e. first login to Azure portal and from there clicks on ServiceNow link, the login attempt fails and user eventually end-up with instance login page i.e. **https://instance.service-now.com/navpage.do**.

If you enable **Auto-redirect**  for that specific IdP (in question) in ServiceNow instance, everything works fine and issue is not reproducible anymore. 

### Release

Applies to all releases

### Cause

Generally in this situation (IdP initiated login), an IdP generates a SAML Response and push it towards integrated ServiceNow instance and then ServiceNow platform validate that response and allows the user to get authenticated. (No SAML Request will be generated in this case, only SAML Response.)

But Microsoft Azure works differently, it makes use of Log In/ Sign In URL of Service Provider (configured on Azure side) and redirect the user to that link which in turn will generate a **SAML Request** and Azure answers with a **SAML Response** and eventually the user gets authenticated after a successful SAML validation. (SAML Request and SAML Response both are generated in this case).

In this case, the Service Provider Sign In URL in Azure configuration is currently configured as **https://instance.service-now.com/navpate.do** which is why no SSO redirection triggers when a user click on ServiceNow link from Azure portal.

**NOTE:** This is not an issue with ServiceNow platform rather a configuration issue on Microsoft Azure portal.

### Resolution

Please change Service Provider (ServiceNow Instance) Sign On URL on Azure configurations in below format:

**OLD:** https://instance.service-now.com/navpage.do

**New:** [https://instance.service-now.com/login\_with\_sso.do?glide\_sso\_id=<sys\_id](https://instance.service-now.com/login_with_sso.do?glide_sso_id=\<sys_id) of the sso configuration>

**NOTE:**

The given solution is not limited to MS Azure instead applicable for all those IdPs which does not generate/send the **SAML Response** on IdP initiated login attempt.
