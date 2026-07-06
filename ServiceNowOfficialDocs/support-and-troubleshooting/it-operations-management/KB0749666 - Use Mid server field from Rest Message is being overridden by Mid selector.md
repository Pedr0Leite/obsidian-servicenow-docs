---
title: "Use Mid server  field from Rest Message is being overridden by Mid selector"
aliases:
  - KB0749666
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749666
kb_number: KB0749666
last_modified: 2025-01-17
---

## Use Mid server field from Rest Message is being overridden by Mid selector

  

### Issue

You define a mid server from the rest message and it will fall back to Mid server selector algorithm.

Use Mid server" field from Rest Message is being overridden by Mid selector when running the REST message.

### Release

 London, Madrid

### Cause

-   Mid server from the REST message will be over written by the Mid selector based on the Supported Application and Capabilities. 
-   This is by design, we will override the mid from our mid selector algorithm based on specific criteria and will pick one of the mid servers from the matching lis

### Resolution

1.  If you would like to use only the mid server that has been configured in the REST message, create a new Capability and assign it to mid server and also the Orchestration activity of the mid server.
2.  This will result in only mid server with the custom capability being picked up when using the REST activity.
