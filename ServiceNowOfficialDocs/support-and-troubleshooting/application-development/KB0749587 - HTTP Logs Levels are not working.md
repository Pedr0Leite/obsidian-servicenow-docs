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
