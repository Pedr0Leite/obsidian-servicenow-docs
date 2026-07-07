---
title: "HTTP Logs Levels are not working"
aliases:
  - KB0749587
  - HTTP Logs Levels are not working
tags:
  - servicenow
  - support-kb
  - mid-server
  - ecc-queue
  - http-logging
  - outbound-integration
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749587
kb_number: KB0749587
last_modified: 2024-04-07
---

## HTTP Logs Levels are not working

  

### Issue

# Overview

HTTP Logging not working for any HTTP log levels.

# Subject

HTTP Logging not working for any HTTP log levels.

# Example

For outbound REST calls, HTTP logging is not happening for all the log levels. If the instance is sending the outbount REST messages thourgh MID Server. Logging will not be done in HTTP logs, rather it is handled by ECC queue and mid server.

So, we shall not be able to see the logs in Outbound HTTP logs.

# Additional Information

Initially, we also checked :

[https://docs.servicenow.com/csh?topicname=outbound-logging-properties.html&version=latest](https://docs.servicenow.com/csh?topicname=outbound-logging-properties.html&version=latest) 

Set 'glide.outbound\_http\_log.override' to 'true'   
Set 'glide.outbound\_http\_log.override.level' to 'ALL'

## Related

- [[KB0718589 - Why are my MID Server-related Jobs stuck and ECC Queue inputs still in Ready State]]
- [[KB0748136 - Outbound REST or SOAP messages timeout after upgrade]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0694711 - Outbound REST Web Services RESTMessageV2 and SOAPMessageV2 execute() vs executeAsync()|Outbound REST Web Services RESTMessageV2 and SOAPMessageV2 execute() vs executeAsync()]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0726269 - Outbound Rest Message that uses a MID Server with the endpoint behind a proxy fails with error java.net.SocketTimeoutExc|Outbound Rest Message that uses a MID Server with the endpoint behind a proxy fails with error java.net.SocketTimeoutException: connect timed out]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0745010 - How to send Outbound REST request with multipartform-data|How to send Outbound REST request with multipart/form-data]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0748136 - Outbound REST or SOAP messages timeout after upgrade|Outbound REST or SOAP messages timeout after upgrade]]
