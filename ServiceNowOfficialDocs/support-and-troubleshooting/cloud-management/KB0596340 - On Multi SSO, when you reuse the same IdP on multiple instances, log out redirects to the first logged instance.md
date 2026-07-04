---
title: "On Multi SSO, when you reuse the same IdP on multiple instances, log out  redirects to the first logged instance"
aliases:
  - KB0596340
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596340
kb_number: KB0596340
last_modified: 2024-04-07
---

## Issue

On Multi SSO, when you reuse the same IdP on multiple instances, logout redirects to the first logged instance 

  

Problem

* * *

If you configure Multiple Provider Single Sign-On with the same IdP on multiple instances and then open two or more of those instances on the same browser, it uses the **SAME IdP session and IdP cookie with the SAME IdP domain.** Single Sign-on log in works as expected. The problem occurs when you try to log out. When the second instance is logged out, it simply reuses the first instance's created IdP session and redirects to the first instance log out page. This leaves the session open.  
 

  

Symptoms

* * *

This problem occurs if you:  

-   have configured Multiple Provider Single Sign-On
-   are sharing the same IdP provider on your instances
-   are logging in on all of them with the same browser

Cause

* * *

This is an intended behavior when you open multiple instances in the same browser session where the IdP is shared. The first IdP session parameters are always used. The rest reuse the initial cookie session, which validates against the IdP token if it applicable. That includes log out request, which is identified as the instance stored on the first cookie.  

  

Resolution

* * *

Use any of the following workarounds to manage the problem:

-   If using SSO to log in to your instances, tell your users to log out before logging in to another instance that shares the same IdP
-   Educate your users to flush the cookies and close the browser if they face this problem
-   Alternatively, modify your installation exits to meet your business requirements
