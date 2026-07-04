---
title: "Login fails when cookies are disabled on browser"
aliases:
  - KB0547925
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547925
kb_number: KB0547925
last_modified: 2024-05-19
---

## Login fails when cookies are disabled on browser

  

### Issue

Login fails when cookies are disabled on the browser   
  

Problem

* * *

When attempting to log in to ServiceNow, the page appears to just refresh and does not seem to log you in, but there are no error messages to indicate if or why the login failed.

Symptoms

* * *

If you are experiencing the following symptoms, investigate the cause below to identify the issue.

-   There are no error messages to indicate that the login failed.
-   When using a valid username and password, the screen reloads the login page instead logging you in to ServiceNow.  
      
      
    

Cause

* * *

When a user is not logged in to ServiceNow and a request to a non-public page is made, users are redirected to the login page. Once a user successfully logs in to ServiceNow, a session cookie is stored by the browser that is sent with every request to prove to ServiceNow that the user has been authenticated. When browser security settings prevent the creation of these session cookies, requests to non-public pages are redirected to the login page. This occurs because a session cookie does not exist in the request, and therefore ServiceNow does not know that the user has already been authenticated.  
  
  
  
Resolution

* * *

Ensure that cookies are enabled for your browser and use one of the supported browser versions listed in [product documentation](https://docs.servicenow.com/ "product documentation").
