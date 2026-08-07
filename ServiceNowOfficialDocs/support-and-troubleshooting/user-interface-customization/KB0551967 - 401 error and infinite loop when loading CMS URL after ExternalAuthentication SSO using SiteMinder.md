---
title: "401 error and infinite loop when loading CMS URL after ExternalAuthentication SSO using SiteMinder"
aliases:
  - KB0551967
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551967
kb_number: KB0551967
last_modified: 2024-04-07
---

## 401 error and infinite loop when loading CMS URL after ExternalAuthentication SSO using SiteMinder

  

### Issue

401 error and infinite loop when loading CMS URL after ExternalAuthentication SSO using SiteMinder

Problem

* * *

There is a 401 error and infinite looping when loading a CMS site after ExternalAuthentication SSO using SiteMinder.    

Symptoms

* * *

Launching a CMS site URL (for example, https://<instance>.service-now.com/ess) when the instance is integrated with SSO using SiteMinder can cause an infinite loop and 401 unauthorized errors within the Chrome Developer Tool Console:  
  
  
![](sys_attachment.do?sys_id=a109e0aedb02b450e515c223059619d3)  
  
   
Cause

* * *

This issue only occurs when SAML (glide.authenticate.external) is enabled and the specific configuration below is in place:  
  

-   System property glide.authenticate.failed\_requirement\_redirect is set to the instance URL:  
    For example: https://<instance>.service-now.com  
    Product documentation reference: [https://docs.servicenow.com/csh?topicname=r\_ForcingLoginViaSSOOnly.html&version=latest](https://docs.servicenow.com/csh?topicname=r_ForcingLoginViaSSOOnly.html&version=latest)   
      
    
-   The view\_content Public Pages \[sys\_public\] record is set to **false**.  
    This makes CMS private and not available to "guest" requiring authentication and login.  
    Product documentation reference: [https://docs.servicenow.com/](https://docs.servicenow.com/) 

For the above scenario, the glide.authenticate.failed\_requirement\_redirect property needs to be set to a static page; otherwise, it goes into the authentication loop.  
  
  

<table class="noteTable" style="border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Warning" src="/Warning_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Warning</strong>:&nbsp;The <span style="font-family: 'courier new', courier;">glide.authenticate.failed_requirement_redirect</span> property should&nbsp;be set to the URL of the IdP login page or a company portal page outside of ServiceNow.</td></tr></tbody></table>

  
  

Resolution

* * *

This issue can be resolved using these steps:

1.  Set view\_content to **true**.
2.  Set glide.authenticate.failed\_requirement\_redirect to the URL of the IdP login page.

Another possible solution is to use this configuration:

1.  Set the glide.authenticate.failed\_requirement\_redirect system property to the URL of the IdP login page or a company portal page outside of ServiceNow.
2.  Add the glide.ui.rotate\_sessions system property.  
    Product documentation reference: [https://docs.servicenow.com/csh?topicname=c\_HighSecuritySettings.html&version=latest](https://docs.servicenow.com/csh?topicname=c_HighSecuritySettings.html&version=latest) 
3.  Rotate HTTP session identifiers to reduce security vulnerabilities.  
    See: https://www.owasp.org/index.php/Session\_Management#Rotate\_Session\_Identifiers
4.  Set Default: Yes

  

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note:</strong> If you are using the SAML 2.0 plugin for single sign-on authentication, set this feature to <strong>false</strong>. Otherwise, it interferes with the session information sharing that takes place between ServiceNow and the identity provider.</td></tr></tbody></table>
