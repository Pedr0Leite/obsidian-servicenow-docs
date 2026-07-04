---
title: "Using ServiceNow mobile app with external authentication"
aliases:
  - KB0564232
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0564232
kb_number: KB0564232
last_modified: 2024-11-28
---

## Using ServiceNow mobile app with external authentication

  

### Issue

This article explains how to log in to the ServiceNow mobile app when using external authentication.

### Versions affected

-   Fuji
-   Geneva
-   ServiceNow Mobile App for iOS v.2.0.3 or earlier

### Procedure

The login behaviors between web environments and the native app are slightly different.

On the mobile app, you must enter your username regardless of whether you are an external user. After entering your username, you can either select **Use External Login** (if you require external login) or enter your password and click **Continue** (if you are a local credential user).

**Example:  
**user1@example.com = local user  
user2@external.com = external user

-   user1@example.com enters their username and password, then selects **Continue**  
    \- Local user is authenticated and logs in to the mobile app
-   user2@external.com enters _only_ their username, then selects **Use External Login**  
    \- At this point, user 2 is redirected to their IdP’s page.

### Problem

If using SSO with external authentication, you might receive the following error:

_Error: No external identity provider found for the username: <username>_

![](/sys_attachment.do?sys_id=76837b141b2b7450d01143f6fe4bcbb3) 

### Resolution

The error occurs because there is no valid Identity Provider (IdP) defined for the user who is trying to log in to the mobile app.

Since the resolution of [PRB656174](https://support.servicenow.com/nav_to.do?uri=problem.do?sys_id=dfcde6a66f2012401501f7307f3ee464 "PRB656174") (if no primary IDP is set for an instance iOS App login fails), the system property **glide.authenticate.sso.redirect.idp** with the sys\_id of the IdP need not be set anymore.

-   **Using single provider SSO**
    
    To set a default IdP, open the IdP record and select the **default** option.  
    When this default is set to **true** and a user with no SSO configuration selects **Use external login**, the user is redirected to the default IdP. For more information, see [Modify the primary and default IdP](https://docs.servicenow.com/csh?topicname=t_CreateUpdateIdentityProvider.html&version=latest). 
-   **Using multi-provider SSO**
    
    Configure the **sso\_source** field with the sys\_id for the IdP to which you want to connect, either in a company record that users are associated with or within the user record itself.
    
    For more information, see the topic [Configuring Users for Multi-Provider SSO](https://docs.servicenow.com/csh?topicname=t_ConfigureUsersMultiProviderSSO.html&version=latest "Configuring Users for Multi-Provider SSO") in the product documentation. 
    

### Recommendations

Many SSO issues are addressed in the latest releases so we recommend you use the following versions:

-   [Geneva Patch 5](https://docs.servicenow.com/csh?topicname=available-versions.html&version=latest "Geneva Patch 5") (or higher)
-   [ServiceNow Mobile App 2.0.3](https://itunes.apple.com/us/app/servicenow/id1044428492?mt=8 "ServiceNow Mobile App 2.0.3") (Apr, 21, 2016) or higher

### Related Links

See the following documentation topics:

-   Configuring Users for Multi-Provider SSO - [Geneva](https://docs.servicenow.com/csh?topicname=t_ConfigureUsersMultiProviderSSO.html&version=latest "Geneva")
-   Modify the primary and default IdP - [Geneva](https://docs.servicenow.com/csh?topicname=t_CreateUpdateIdentityProvider.html&version=latest "Geneva")
-   Add a property using sys\_properties.list - [Geneva](https://docs.servicenow.com/csh?topicname=t_AddAPropertyUsingSysPropsList.html&version=latest "Geneva")
-   [Geneva Multi-SSO enhancements](https://docs.servicenow.com/csh?topicname=c_MultipleProviderSingleSignOn.html&version=latest "Multi-SSO enhancements")
