---
title: "Disable SSO auto redirection for some Portals to local login while still keeping SSO authentication for others"
aliases:
  - KB0719767
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719767
kb_number: KB0719767
last_modified: 2025-04-22
---

## Disable SSO auto redirection for some Portals to local login while still keeping SSO authentication for others

  

### Issue

The **Login** widget for Service Portal or any other Portal will be redirected to Single Sign On (SSO) when the following conditions are satisfied:

1.  If the user is not logged in
2.  MultiSSO is enabled using the "**glide.authenticate.multisso.enabled**" system property
3.  Default IDP is set using the "**glide.authenticate.sso.redirect.idp**" system property

### Use Case

If you have SSO and want to implement a portal (like the Vendor Portal) where you don't want the Vendor Portal to do SSO login but directly land to it URL (eg, https://<instance-name>.service-now.com/vdp) and do Local Login BUT still want other portals to go through SSO authentication. 

### Resolution

1.  Make sure your instance is using the **Multiple Provider Single Sign-On Installer** plugin for SSO authentication and the **glide.authenticate.multisso.enabled** system property is enabled.
2.  Set the $sp sys\_public page to true. 

  
**NOTE:** This is a global configuration which will make all the Portal pages public and to make sure that the different Service Portal pages (which do SSO authentication) still go the SSO login and are not public, you will need to make sure that there is an OOTB "Login page" associated to them.

To make sure that the SSO authenticated Portal doesn't go to the SSO login we will still need to make sure that "Login page" associated to it (which is there OOTB) and will need to:

-   1 -Clone the OOB Login widget associated with the Portal.

-   2 - In the cloned Login widget comment this line containing the **glide.authenticate.sso.redirect.idp** property in the Server script and save the widget:
    -   _data.default\_idp = GlideProperties.get("glide.authenticate.sso.redirect.idp");_

-   3- Edit the Portal page that has a field "Login page" and open up the login page referenced
-   4 - In the login page, go to the section named "Page Content"

                - Click on the link: 'instance: Login (xxxxx), this opens up the widget instance

-   5  - In the widget instance page "Login", go to the bottom field named "Widget" in section Widget
-   6 - Edit the field 'Widget" and replace the OOTB Login widget reference with Login\_custom (the widget cloned is step 1)

             (Note: You can also use the **Widget Designer**.)
