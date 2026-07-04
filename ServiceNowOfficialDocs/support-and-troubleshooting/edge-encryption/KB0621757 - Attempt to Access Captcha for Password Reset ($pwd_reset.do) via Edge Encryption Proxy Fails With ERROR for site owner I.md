---
title: "Attempt to Access Captcha for Password Reset ($pwd_reset.do) via Edge Encryption Proxy Fails With: \"ERROR for site owner: Invalid domain for site key\""
aliases:
  - KB0621757
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621757
kb_number: KB0621757
last_modified: 2024-04-07
---

## Attempt to Access Captcha for Password Reset ($pwd\_reset.do) via Edge Encryption Proxy Fails With: "ERROR for site owner: Invalid domain for site key"

  

### Issue

Attempt to Access Captcha for Password Reset ($pwd\_reset.do) via Edge Encryption Proxy Fails With: "ERROR for site owner: Invalid domain for site key" 

Problem

* * *

This issue can be reproduced as follows:

1.  Activate the Password Reset Plugin with Demo Data.
    
2.  Navigate to **Password Reset** > **Properties** > **Processes** > and select Demo Self-Service Process 1.
    
3.  Set the following values:
    
    Active  
    Apply to all users  
    Public access  
    Display captcha
    
4.  Click **Save**.
    
5.  Go to the page defined by the Demo Self-Service Process 1 through the Edge Proxy URL:
    
    https://<edge\_proxy\_host:<port>/$pwd\_reset.do?sysparm\_url=demo1
    
    The captcha displays the following error:
    
    ERROR for site owner:  
    Invalid domain for site key
    
    If you do not go through the Edge Proxy, for example, by going to https://<instance\_name>.service-now.com/$pwd\_reset.do?sysparm\_url=demo1, the captcha "I'm not a robot" is displayed.
    

Cause

* * *

The issue is caused by the use of the Google Captcha which is configured by default in the Password Reset plugin. For more information, refer to the documentation topic [Configure Google reCAPTCHA](https://docs.servicenow.com/csh?topicname=t_ConfigureGoogleRecaptcha.html&version=latest).

The following system properties on the instance are configured to work only with the service-now.com domain:

google.captcha.secret  
google.captcha.site\_key

Therefore, the captcha works correctly when going through the instance URL, which uses the service-now.com domain. Going through the proxy is not being presented as the service-now.com domain but rather as the proxy IP/host, which causes the following failing response to be returned from Google:

<!DOCTYPE HTML><html dir="ltr"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">  
<meta http-equiv="X-UA-Compatible" content="IE=edge">  
<style type="text/css">  
@font-face {  
    font-family: 'Roboto';  
    font-style: normal;  
    font-weight: 400;  
    src: local('Roboto Regular'), local('Roboto-Regular'), url(//fonts.gstatic.com/s/roboto/v15/2UX7WLTfW3W8TclTUvlFyQ.woff) format('woff');  
    }  
@font-face {  
    font-family: 'Roboto';  
    font-style: normal;  
    font-weight: 500;  
    src: local('Roboto Medium'), local('Roboto-Medium'), url(//fonts.gstatic.com/s/roboto/v15/RxZJdnzeo3R5zSexge8UUT8E0i7KZn-EPnyo3HZu7kw.woff) format('woff');  
    }  
@font-face {  
    font-family: 'Roboto';  
    font-style: normal;  
    font-weight: 900;  
    src: local('Roboto Black'), local('Roboto-Black'), url(//fonts.gstatic.com/s/roboto/v15/mnpfi9pxYH-Go5UiibESIj8E0i7KZn-EPnyo3HZu7kw.woff) format('woff');  
    }

</style>  
<link rel="stylesheet" type="text/css" href="https://www.gstatic.com/recaptcha/api2/r20161102163809/styles\_\_ltr.css">  
<script>  
  
</script></head>  
<body><script>  
recaptcha.anchor.ErrorMain.init("\[\\x22ainput\\x22,,,,,,\[1,1,1\]\\n,\\x22Invalid domain for site key\\x22,6\]\\n");  
</script></body></html>  

Resolution

* * *

There are two options to resolve this issue.

-   To make this work from the Edge Proxy address but no longer work from the instance hostname address:
    
    1.  Go to the Google recaptcha site (https://www.google.com/recaptcha/admin), log in with a Google account, and select Get reCAPTCHA:
        
    2.  Enter a Label and a Domain (the IP Address or host name of the Edge Proxy) and select Register.
        
        The next screen will provide a Site key and a Secret key.
        
    3.  Select Export > XML (this record) for the existing system properties.
        
        Keep these files, which are the values for the service-now.com domain:
        
        google.captcha.secret
        
        google.captcha.site\_key
        
    4.  For the google.captcha.secret property, replace the current value after the second } (keep the rest before the second }) with the provided Secret key and save it.
        
    5.  For the google.captcha.site\_key property, replace the current value with the provided Site key and save it.
        
        Accessing through the Edge Proxy will now work correctly but accessing through the instance hostname will display the error message originally seen with Edge Proxy access. The Google recaptcha and the instance can be configured only to work from one domain, so either it will work with the Edge Proxy or the instance hostname but not both.
        
-   To have the captcha render from both the Edge Proxy and the instance hostname URL, use the CAPTCHA service that is provided with the base ServiceNow system rather than Google reCAPTCHA. To switch to the base system CAPTCHA service, change the system property password\_reset.captcha.google.enabled from true to false and save it.
