---
title: "How to redirect users to /login_locate_sso.do page from instance URL"
aliases:
  - KB0758382
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758382
kb_number: KB0758382
last_modified: 2025-01-03
---

## How to redirect users to /login\_locate\_sso.do page from instance URL

  

### Summary

Some customers might want that when they open the URL - [http://instance.service-now.com,](http://instance.service-now.com,) they are redirected automatically to [http://instance.service-now.com/login\_locate\_sso.do](http://instance.service-now.com,) , when they have multiple IDPs.

### Release

Applicable for all instances

### Instructions

This is a custom code, and should be tried in sub-prod instance first. This is related to eliminating the external login page.

-   Create a script include - Example it is named as PreLoginScript as below with a function named 'redirectToLoginLocateSSO'
    
    var PreLoginScript = Class.create();  
    PreLoginScript.prototype = {  
    initialize: function() {  
    },  
      
    redirectToLoginLocateSSO: function() {   
    return "/login\_locate\_sso.do";   
    },  
      
    type: 'PreLoginScript'  
    };
    
-   Update the Update the system property - `glide.entry.page.script` value as below  
    
    new PreLoginScript().redirectToLoginLocateSSO();
    

Now, when the instance URL is opened, the user will be redirected to [http://instance.service-now.com/login\_locate\_sso.do](http://instance.service-now.com,)

Note: In `glide.entry.page.script` system property, if value has been set for `SPEntryPage()`, then that will be replaced by the value above. Both cannot be there.
