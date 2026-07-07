---
title: "Outbound REST or SOAP messages timeout after upgrade"
aliases:
  - KB0748136
  - Outbound REST or SOAP messages timeout after upgrade
tags:
  - servicenow
  - support-kb
  - rest
  - soap
  - outbound-integration
  - RESTMessageV2
  - SOAPMessageV2
  - timeout
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748136
kb_number: KB0748136
last_modified: 2023-12-21
---

## Outbound REST or SOAP messages timeout after upgrade

  

### Issue

Experiencing REST API timeouts after a recent upgrade? This article provides helpful troubleshooting information and steps to resolve the issue.

### Symptoms

After upgrading to Madrid, Kingston Patch 14 or higher, or London Patch or higher, outbound API messaging, RESTMessageV2 and SOAPMessageV2 API calls, may start to time out after 30 seconds for a response. But before the upgrade the timeouts did not occur.

You might see errors such as this in the logs:

Error: No response for ECC message request with sysid=nnnn... after waiting for 30 seconds in ECC Queue

### Release

-   Madrid
-   London Patch 7 (or higher)
-   Kingston Patch 14 (or higher)

### Cause

In Madrid, London Patch 7+, and Kingston Patch 14+, two system properties were added on the backend:  
glide.http.outbound.max\_timeout with a maximum value of 30 seconds  
glide.http.outbound.max\_timeout.enabled with a default value of true

The property glide.http.outbound.max\_timeout specifies the number of seconds that RESTMessageV2 and SOAPMessageV2 APIs wait for a response from a synchronous call, and the default and maximum value for this property is 30 seconds. As a result, outbound REST and SOAP API calls will start to time out after waiting 30 seconds for a response.

### Resolution

To resolve this issue, perform **both** of the following:

1.  **Add the following system property on the UI:**  
    Name: glide.http.outbound.max\_timeout.enabled  
    Type: boolean  
    Value: false
2.  **Use the waitForResponse() method to set the timeout in the REST or SOAP messages.**  
    Here are some examples:  
    [Asynchronous RESTMessageV2 example](https://docs.servicenow.com/csh?topicname=r_RESTMessageV2MIDServerExample.html&version=latest "Asynchronous RESTMessageV2 example")  
    [Asynchronous SOAPMessageV2 example](https://docs.servicenow.com/csh?topicname=r_AsyncronousSOAPMessageV2Example.html&version=latest "Asynchronous SOAPMessageV2 example")

### Related Links

The properties glide.http.outbound.max\_timeout and glide.http.outbound.max\_timeout.enabled may not be documented in the Kingston and London documentation since they were added to these releases in later patches.

## Related

- [[KB0694711 - Outbound REST Web Services RESTMessageV2 and SOAPMessageV2 execute() vs executeAsync()]]
- [[KB0749587 - HTTP Logs Levels are not working]]
- [[c_OutboundRESTWebService|Outbound REST Web Service]]
- [[c_OutboundSOAPWebService|Outbound SOAP Web Service]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691976 - The users with SOAP role not able to view the incident table data even though the ACLs return true.|The users with SOAP role not able to view the incident table data even though the ACLs return true.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0694711 - Outbound REST Web Services RESTMessageV2 and SOAPMessageV2 execute() vs executeAsync()|Outbound REST Web Services RESTMessageV2 and SOAPMessageV2 execute() vs executeAsync()]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0718496 - Outbound REST Webservice call with a large JSON Payload in the response body is not processed by the instance|Outbound REST Webservice call with a large JSON Payload in the response body is not processed by the instance]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0720035 - Error calling Scoped Outbound REST message|Error calling Scoped Outbound REST message]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0748481 - How to use custom WSDL for Inbound SOAP requests to ServiceNow.|How to use custom WSDL for Inbound SOAP requests to ServiceNow.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0749537 - Inbound SOAP API connection returns 302 error|Inbound SOAP API connection returns 302 error]]
