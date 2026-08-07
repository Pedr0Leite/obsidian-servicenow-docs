---
title: "Checklist before cloning an instance with Digest / SSO / SAML / Multi SSO Integration to prevent denied authentication on clone target"
aliases:
  - KB0657100
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657100
kb_number: KB0657100
last_modified: 2025-08-13
---

## Checklist before cloning an instance with Digest / SSO / SAML / Multi SSO Integration to prevent denied authentication on clone target

  

### Issue

Cloning could cause your target instance to be inaccessible if it is done incorrectly and the source or target instance has SAML setup. We do not recommend to copy the SAML configuration from one system into another.

### Symptoms

After a clone, some users will not be able to login into their instance. They could experience either:

-   denied log in with "Username or password not valid"
-   receiving a logout redirection
-   being forwarded to an external system to authenticate incorrectly
-   their instance local password no longer working

### Release

Pre-Utah

### Cause

Due to security constraints, most transfers of SAML/SSO or Multi SSO settings will not work as they need to be configured on the Identity Provider (IdP) as well. They are not universal, so they can not be used on multiple systems. Instead, each instance needs to be registered on the final IdP independently.

If you create or overwrite a working setup, it could cause the target instance to fail to authenticate.

### Resolution

Before making a clone from one instance to another, ensure the followings:

1.  **Preserve SAML properties** on sys\_properties related to SAML/SSO/Multi SSO. Use the **System Clone > Preserve Data** on the source instance. If you need them, export them into XML, then manually import them on the target. As a guide, preserve properties starting with:
    -   glide.authenticate
    -   glide.security
    -   glide.entry
    -   glide.script
    -   glide.session
    -   glide.saml2
    -   com.glide.communications
    -   com.snc.integration.saml\_esig
2.  **Preserve SAML certificates** on sys\_certificate related to SAML/SSO/Multi SSO. Use the System Clone > Preserve Data on the source instance. If you need them, export them into XML, then manually import them on the target.
3.  **Preserve SAML users** on sys\_user related to SAML/SSO/Multi SSO. Use the System Clone > Preserve Data on the source instance.
4.  **Exclude the Multi SSO tables** sso\_properties, digest\_properties and saml2\_update1\_properties.
5.  **Ensure you have a LOCAL admin account** on sys\_user (not in LDAP or SAML) record on the **target clone** manually created and with a sys\_id that does not exist on the source instance of the clone.

 **Warning:** Out the box data preserver (clone\_data\_preserver) "Core Instance Properties" already preserves some SAML/SSO/Multi SSO data on sys\_properties

Finally,  
**DO**

-   Manually create the SAML/SSO/Multi SSO records on each instance independently as they need to be set up on their IdP as well independently.
-   If you need to copy some setup information (e.g. sys\_properties records), export the records into XML, then on the target import them as XML accordingly or as part of your Update sets.

**DO NOT**

-   Do not try to clone the SAML/SSO/Multi SSO setup from one system to another.
-   Do not change the sys\_id of your Multi SSO provider record as it will force your users to flush their cookies.

# Reset the MFA on a cloned instance

This [video](https://players.brightcove.net/6274575390001/nUx4EKfUz_default/index.html?videoId=6328971260112) shows how to reset the MFA on a cloned instance. 

### Related Links

[Data preservation on cloning target instances](https://docs.servicenow.com/bundle/utah-platform-administration/page/administer/managing-data/concept/data-preservation.html "Data preservation on cloning target instances")

[Clone an instance with a SAML integration](https://docs.servicenow.com/bundle/utah-platform-security/page/integrate/saml/task/t_CloneAnInstanceWASAMLIntegration.html "Clone an instance with a SAML integration")

[Users not able  to login in cloned target instance using Multi Factor Authentication (MFA)](https://support.servicenow.com/kb_view.do?sysparm_article=KB0860689 "Users not able  to login in cloned target instance using Multi Factor Authentication (MFA)")
