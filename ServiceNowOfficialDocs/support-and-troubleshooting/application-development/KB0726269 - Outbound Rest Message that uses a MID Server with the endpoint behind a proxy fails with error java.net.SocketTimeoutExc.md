---
title: "Outbound Rest Message that uses a MID Server with the endpoint behind a proxy fails with error java.net.SocketTimeoutException: connect timed out"
aliases:
  - KB0726269
tags:
  - servicenow
  - support-kb
  - mid-server
  - outbound-rest
  - proxy
  - integration
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726269
kb_number: KB0726269
last_modified: 2023-11-27
---

## Issue

An Outbound Rest Message that uses a MID Server, with the endpoint behind a proxy, may fail with the error:  
java.net.SocketTimeoutException: connect timed out.

## Resolution

Navigate to the MID Server record on the instance and add these in the Properties tab.  
glide.http.proxy\_host - The proxy server hostname or IP address Example: proxy.company.com or 192.168.34.54.  
glide.http.proxy\_port - The port number for the proxy server Example: 8080.  
glide.http.proxy\_username - If the proxy server is authenticating using user name and password, enter a value for this property Example: proxyuser.  
glide.http.proxy\_password - If the proxy server is authenticating using user name and password, enter a value for this property Example: password.

## Related

- [[KB0745010 - How to send Outbound REST request with multipartform-data]] - other outbound REST/MID Server configuration
- [[KB0779975 - Outbound Web Service call via MID Server fails with Unable to decrypt parameter soap_password, using encrypted value]] - MID Server outbound call troubleshooting
- [[KB0755198 - Outbound REST Call through MID server fails with error javax.net.ssl.SSLHandshakeException Received fatal alert handshak]] - MID Server outbound REST failure

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0694711 - Outbound REST Web Services RESTMessageV2 and SOAPMessageV2 execute() vs executeAsync()|Outbound REST Web Services RESTMessageV2 and SOAPMessageV2 execute() vs executeAsync()]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0696002 - Configure Outbound Mutual Authentication (calling 3rd party Web Services) in ServiceNow Instance|Configure Outbound Mutual Authentication (calling 3rd party Web Services) in ServiceNow Instance]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0718496 - Outbound REST Webservice call with a large JSON Payload in the response body is not processed by the instance|Outbound REST Webservice call with a large JSON Payload in the response body is not processed by the instance]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0720035 - Error calling Scoped Outbound REST message|Error calling Scoped Outbound REST message]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0724429 - glide_list reference field created through a REST API call stores the actual value instead of reference of the field|glide_list  reference field created through a REST API call stores the actual value instead of reference of the field]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0743846 - Sending additional parameters to the OAuth Provider to retrive the access and refresh tokens using GlideOAuthClient()|Sending additional parameters to the OAuth Provider to retrive the access and refresh tokens using GlideOAuthClient()]]
