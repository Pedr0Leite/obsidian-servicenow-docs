---
title: "Instance is not reachable from Internet Explorer/Edge when using Single Sign-on authentication. "
aliases:
  - KB0656513
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656513
kb_number: KB0656513
last_modified: 2024-04-07
---

## Instance is not reachable from Internet Explorer/Edge when using Single Sign-on authentication.

  

### Issue

Instance is not reachable from Internet Explorer/Edge when using Single Sign-on authentication 

  
  

# Overview

* * *

 When using Single Sign-on to login, some users may not be able to access the instance using Internet Explorer/Edge but they can access it using Google Chrome. 

# Cause

* * *

Internet Explorer and Edge have a list of Trusted Sites and this issue occurs when one of the pages you're trying to access is not listed in the Trusted Sites of your browser settings. 

When using Single Sign-on on ServiceNow, if auto-redirection to the Identity Provider is set up, the instance redirects to the IdP URL. At this stage, if the IdP URL's domain is not listed in the IE/Edge's trusted sites list, the page does not load and it keeps spinning. 

# Solution

* * *

Follow the below procedure to fix the issue:

1.  On the instance, navigate to Identity Providers and open the IdP record.
2.  Check the Identity Provider URL field and copy the domain alone. For example, .windows.net.
3.  In Internet Explorer, click Tools, click Internet Options, and then click the Security tab.
4.  In the Select a Web content zone to specify its current security settings box, click Trusted Sites, and then click Sites.
5.  Add **\*.domain\_name** For example, **\*.windows.net**
6.  Click Close and then Apply.
7.  Access the instance and it is redirected to the Identity Provider successfully.
