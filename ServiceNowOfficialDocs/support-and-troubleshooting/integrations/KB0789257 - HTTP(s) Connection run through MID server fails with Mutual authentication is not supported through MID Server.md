---
title: "HTTP(s) Connection run through MID server fails with \"Mutual authentication is not supported through MID Server\""
aliases:
  - KB0789257
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789257
kb_number: KB0789257
last_modified: 2024-04-07
---

## HTTP(s) Connection run through MID server fails with "Mutual authentication is not supported through MID Server"

  

### Issue

HTTP(s) connection fails with "Mutual authentication is not supported through MID Server".

### Release

Pre New York releases. For newer releases search docs.servicenow.com for "Outbound web services mutual authentication" to confirm if mutual authentication via a MID server is supported.

### Cause

As documented on the following link, ServiceNow does not support mutual authentication for inbound requests or for outbound requests sent through a MID Server.

-   [Outbound web services mutual authentication](https://docs.servicenow.com/csh?topicname=c_OutboundWebServicesMutualAuth.html&version=latest "Outbound web services mutual authentication")

### Resolution

If the connection must use the MID server, set HTTP(s) connection field mutual\_auth = false via either form or list view and save. The mutual\_auth is hidden by default and will be displayed when field "URL Builder" is check marked.

### Related Links

-   [Outbound web services mutual authentication](https://docs.servicenow.com/csh?topicname=c_OutboundWebServicesMutualAuth.html&version=latest "Outbound web services mutual authentication")
