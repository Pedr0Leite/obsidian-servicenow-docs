---
title: "Password Reset via Custom URL - Google reCAPTCHA error - ERROR for site owner:Invalid domain for site key"
aliases:
  - KB0788009
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788009
kb_number: KB0788009
last_modified: 2024-04-07
---

## Password Reset via Custom URL - Google reCAPTCHA error - ERROR for site owner:Invalid domain for site key

  

### Issue

Password Reset is available as a separate subscription from the rest of the ServiceNow platform and requires the Password Reset plugin.

To activate the plugin, navigate to System Definition -> Plugins, and activate the Password Reset Plugin with Demo Data.

After that, navigate to Password reset -> Properties > Processes and select your process. Go to the page defined by your Process through the Custom URL:

The captcha displays the following error: "ERROR for site owner: Invalid domain for site key"

### Cause

The secret key is different from the the system property "google.captcha.site\_key".

### Resolution

To use the Google reCAPTCHA service, instances that are running on a domain other than `service-now.com` require an API key pair from Google.

1.  1.  Request an API key pair (a site key and a secret) from Google at [https://www.google.com/recaptcha](https://www.google.com/recaptcha).
    2.  Set the following system properties  
        -   password\_reset.captcha.google.enabled:  
            -   set to true (true by default)
            -   Type is string
        -    google.captcha.site\_key: Set to the site key that Google provided.  
            -   Type: string
            -   Default: A site key that Google provided to ServiceNow
        -   google.captcha.secret : Set to the secret that Google provided.  
            -   Type: password2
            -   Default: An encrypted secret that Google provided to ServiceNow
                
                  
                

-   -   -     
            

### Related Links

Please note that google captcha is also used for various other purposes and they might need their own google captcha keys.

Configure Google reCAPTCHA for external user self-registration: [https://docs.servicenow.com/bundle/paris-platform-administration/page/integrate/authentication/task/configure-recaptcha-sp.html](https://docs.servicenow.com/bundle/paris-platform-administration/page/integrate/authentication/task/configure-recaptcha-sp.html)

Properties installed with Communities: [https://docs.servicenow.com/bundle/paris-customer-service-management/page/product/customer-communities/reference/communities-properties.html](https://docs.servicenow.com/bundle/paris-customer-service-management/page/product/customer-communities/reference/communities-properties.html)

sn\_ext\_usr\_reg.captchaEnabled Enables Google re-CAPTCHA on the self-registration page. Type: boolean Default value: true No Mention of seperate key/pw

  

System properties for configuring Walk-up Experience for guest users [https://docs.servicenow.com/bundle/paris-customer-service-management/page/product/customer-service-management/reference/csm-walkup-guest-configure.html](https://docs.servicenow.com/bundle/paris-customer-service-management/page/product/customer-service-management/reference/csm-walkup-guest-configure.html)

sn\_guest\_walkup\_cs.captcha.enabled    (true/false) No mention of a google key/pw needed.
