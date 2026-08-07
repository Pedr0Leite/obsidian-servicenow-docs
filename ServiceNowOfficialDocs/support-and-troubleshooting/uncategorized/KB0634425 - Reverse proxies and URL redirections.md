---
title: "Reverse proxies and URL redirections"
aliases:
  - KB0634425
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0634425
kb_number: KB0634425
last_modified: 2025-09-25
---

## Reverse proxies and URL redirections

  

### Issue

ServiceNow is a cloud based application. Some customers would like to "rename" their instances with a more user-friendly URL. While reverse proxies and redirection URLs are a good idea, they fail to cover all the use cases. Here are some details on this matter.

###   
Symptoms

When ServiceNow is redirected by proxy or URLs, the proxies or redirection tools may face problems with a high level of calls or behave differently than if directly connecting to the instance.

### Cause

Reverse proxies and redirection URL require rules to process the calls. These rules need to be correctly configured to achieve the desired behavior. However, there are connection functions essential for ServiceNow and they need to be excluded from interception. In addition, some ServiceNow functions could cause a bottle neck on the proxies and redirection URL appliances as they are used to keep applications up-to-date with the cloud information.

### Resolution

ServiceNow support is not able to support setup on the proxies or redirection services outside ServiceNow offerings.

While we do not have information on how setup the redirection rules, here are a few recommendations:

-   Avoid intercepting the following URLs or it could cause performance problems:  
    /amb/connect  
    /amb/handshake   
    /api/now/ui/presence
-   Blocking /amb URLs could cause application features to fail and lead to unpredictable behavior in the instance. As more and more product features rely on /amb, the impact of disabling the URLs will get more and more significant.
-   Pay special attention to our xmlhttp.do page. This page is used to handle XHR requests that perform transactions after the initial form has loaded. They perform all sorts of different functions.
-   Try setting the redirection URL on the root directory. For example, **<server>**/ instead of **<server>/dir/**

Finally, ServiceNow support is not able to provide rule settings on the proxies or redirection services as they are outside our ServiceNow cloud. If you are setting up a reverse proxy or redirection URL, to understand what is in each of the different pages on the instance, you need to use network profiling tools to see what data is contained and to map the ServiceNow pages correctly to the rules required. As our product is constantly changing, we do not have specific documentation on the content for specific UI pages.  
  
Please note security issues or concerns are addressed immediately. Please contact support.

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>: To understand ServiceNow pages on the instance, you need to use network profiling tools to see what data is contained and to map the ServiceNow pages correctly to the rules required.</td></tr></tbody></table>
