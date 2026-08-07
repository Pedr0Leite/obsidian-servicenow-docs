---
title: "Multi-Provider SSO: How to Configure a Service Portal Page to Display a Local Login Page and No Longer Redirect to the \"Auto Redirect IdP's\" Login Page"
aliases:
  - KB0747338
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747338
kb_number: KB0747338
last_modified: 2024-04-07
---

## Multi-Provider SSO: How to Configure a Service Portal Page to Display a Local Login Page and No Longer Redirect to the "Auto Redirect IdP's" Login Page

  

### Issue

# Description

You are using Multi-Provider SAML SSO with a defined "Auto Redirect IdP"

When going to your Service Portal page, e.g.:

https://<instance\_name>.service-now.com/<service\_portal>

You get redirected to the IdP login page as is defined in the "Auto Redirect IdP"

Instead of the redirection to the "Auto Redirect IdP", you want a local login page where you have an option to "Use external login"

How can this be configured?

# Procedure

(1) In the navigator go to Service Portal -> Portals -> select the affected Service Portal

(2) To the right of the "Login page" select the "Preview this record" icon and open that record

(3) Under "Page Content" select the login widget link

(4) Select "Clone Widget" and set the Name field to whatever you want to use

(5) Edit the "Client controller" script, in this case comment out the redirection to the IdP as follows:

// if (!c.data.is\_logged\_in && c.data.multisso\_enabled && c.data.default\_idp) {  
// c.server.get({  
// action: "set\_sso\_destination",  
// pageURI: c.data.pageURI  
// }).then(function() {  
// $window.location = "/login\_with\_sso.do?glide\_sso\_id=" + c.data.default\_idp;  
// });  
// }  
  
Save it

(6) Go back to your service portal record (from step (1)), to the right of the "Login page" select the "Preview this record" icon and open that record

(7) From there select the "Open in Page Editor" Related Link

(8) Select the block to the left of "Login", e.g. "Instance 2"

(9) At the bottom under "Widget" select the new cloned widget (as named in step (4)) from the drop down, save it

(10) Now when going to the service portal page here:

https://<instance\_name>.service-now.com/<service\_portal>

You are no longer being redirected to the "Auto Redirect IdP" login page, instead you get a local login page with an option to use "Use external login"

# Applicable Versions

Any Version
