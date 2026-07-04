---
title: "Your OAuth redirect failed. Please check if the redirect URL setup in your OAuth configuration matches your ServiceNow instance URL when using Install App link on Zoom side"
aliases:
  - KB0961309
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961309
kb_number: KB0961309
last_modified: 2026-06-29
---

## Your OAuth redirect failed. Please check if the redirect URL setup in your OAuth configuration matches your ServiceNow instance URL when using Install App link on Zoom side

  

### Issue

When initiating  OAuth authentication from Zoom by clicking  Install App link  you can notice this message in the page: Your OAuth redirect failed. Please check if the redirect URL setup in your OAuth configuration matches your ServiceNow instance URL.

In the same time in the logs we notice:

2021-05-03 08:18:28 (185) Default-thread-4 CF3A77C7DB7BA050C27A11C8139619CE txid=10ebf7c7db7b #427401 /oauth\_redirect.do Parameters -------------------------  
2021-05-03 08:18:28 (186) Default-thread-4 CF3A77C7DB7BA050C27A11C8139619CE txid=10ebf7c7db7b \*\*\* Start #427401 /oauth\_redirect.do, user: sains  
2021-05-03 08:18:28 (186) Default-thread-4 CF3A77C7DB7BA050C27A11C8139619CE txid=10ebf7c7db7b WARNING \*\*\* WARNING \*\*\* OAuthRedirectProcessor caught a Exception with message Your OAuth redirect failed. Please check if the redirect URL setup in your OAuth configuration matches your ServiceNow instance URL.  
2021-05-03 08:18:28 (186) Default-thread-4 CF3A77C7DB7BA050C27A11C8139619CE txid=10ebf7c7db7b WARNING \*\*\* WARNING \*\*\* Your OAuth redirect failed. Please check if the redirect URL setup in your OAuth configuration matches your ServiceNow instance URL.

All the setup is done correctly as per [THIS DOC.](https://www.servicenow.com/docs/bundle/zurich-integrate-applications/page/administer/integrationhub-store-spokes/task/setup-zoom.html "THIS")

### Release

All

### Resolution

This is expected because the OAuth authentication should initiate from ServiceNow and not from Zoom.

However, the Install App link on Zoom is basically the Zoom authorization link. Once this is processed by Zoom, it redirects you to ServiceNow to the /oauth\_redirect.do endpoint.  
  
However on ServiceNow, the instance notices that it did not initiate an OAuth authorization request but it received a redirect.

Since the OAuth flow did not initiate from ServiceNow, it presents the message "Your OAuth redirect failed. Please check if the redirect URL setup in your OAuth configuration matches your ServiceNow instance URL" .  
  
The way the 'Install app' button is built on Zoom doesn't really help in this flow and this should be the same for other applications other than ServiceNow too.  
ServiceNow is the OAuth client connecting to the OAuth provider 'Zoom'. Therefore, it's required that the OAuth authentication is initiated from ServiceNow.  
  
The 'Install app' button on Zoom is not required when integrated ServiceNow with Zoom. It's probably best for Zoom to revisit the way the 'Install app' button is designed.
