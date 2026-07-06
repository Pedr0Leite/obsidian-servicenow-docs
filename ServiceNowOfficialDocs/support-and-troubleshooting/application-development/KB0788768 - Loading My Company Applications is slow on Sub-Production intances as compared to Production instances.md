---
title: "Loading My Company Applications is slow on Sub-Production intances as compared to Production instances"
aliases:
  - KB0788768
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788768
kb_number: KB0788768
last_modified: 2024-04-08
---

## Loading My Company Applications is slow on Sub-Production intances as compared to Production instances

  

### Issue

Loading My Company Applications (navigation: System Applications > My Company Applications) is slower on Sub-Production instances as compared to Production instances.

### Cause

The page load time is dependent on the number of candidate updates received from the [ServiceNow Store](https://store.servicenow.com/sn_appstore_store.do#!/store/home "ServiceNow Store"). Candidate updates are the Application updates that the instances receive from the ServiceNow Store.

By default, Sub-Production instances will have access to all Applications that are marked as "Show in sub production" on the Store, irrespective of the entitlements. However, Production instances have only access to Applications they are entitled for. Since there are fewer updates to load on Production instances, the page will load quicker than on Sub-Production instances.

![](sys_attachment.do?sys_id=20041009db00b8d066e0a345ca961918)

### Resolution

The load times are expected to get better with subsequent family releases.

The loading time can be checked as follows - 

1.  When the page is loaded, in Chrome for example, do an Inspect -  
    From the URL - https://<instance>.service-now.com/sn\_appclient\_api\_v1.do? - Network Tab > Timing, check the "Waiting (TTFB) in seconds", which is equivalent to the time taken by the page to load.  
      
    
2.  On inspecting the JSON object in the response from the URL - https://<instance>.service-now.com/sn\_appclient\_api\_v1.do, the Repo Processing time can be identified with below syntax -  
        "repoProcessingTime":<time in milliseconds>.

### Related Links

**Note**: To compare a Sub-Production instance with a Production one, make sure that the following System Properties have the same value:

sn\_appclient.dev\_repository\_base\_url  
sn\_appclient.repository\_base\_url
