---
title: "Homepage dashboards with 'Interactive Filters' could fail loading if glide.rest.apis.disabled property is set"
aliases:
  - KB0657531
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657531
kb_number: KB0657531
last_modified: 2024-04-07
---

## Homepage dashboards with 'Interactive Filters' could fail loading if glide.rest.apis.disabled property is set

  

### Issue

Homepage dashboards with "Interactive Filters" could fail when loading if glide.rest.apis.disabled property is set

Problem

* * *

ServiceNow is very flexible and allows you to control the REST API access with a sys\_properties record named **glide.rest.apis.disabled**. It also allows you to disable ServiceNow-defined REST APIs by names. For example, if you set glide.rest.apis.disabled to "Table API,Scorecards API,Import Set API,Identification and Reconciliation API,Attachment API,Aggregate API," those REST API become unavailable.  
  

Symptoms

* * *

The following symptoms occur:

-   Dashboard 'Interactive Filters' fails to load the pages
    
    `![Loading failed](sys_attachment.do?sys_id=e5dbe0eadb42b450e515c22305961942 "Loading failed")`
    
-   Table API, Aggregate API, Import Set API, or Attachment API are not on the available list on the REST API Explorer  
      
    ![REST API explorer](sys_attachment.do?sys_id=e9dbe0eadb42b450e515c22305961947 "REST API explorer")  
      
    
-   Many drop-down menus show a 'Loading failed' message  
      
    
-   Javascript debug on the browser shows "400 (Bad request)" on some calls  
      
    
    `![Javascript error](sys_attachment.do?sys_id=2ddbe0eadb42b450e515c22305961965 "Javascript error")      `
    
-   REST API commands result on a message:  
    `   Requested URI does not represent any resource: /now/v2/<api>/<table>`

Cause

* * *

Several modules use REST API to retrieve information from the instance. When the REST API become unavailable, features that depend on those REST APIs start failing.  
  

Resolution

* * *

1.  Navigate to the sys\_properties form.
2.  Set the value of **glide.rest.apis.disabled** to **(empty)**.

 

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>: Setting glide.rest.apis.disabled could cause some features that depends on REST API to start failing.</td></tr></tbody></table>
