---
title: "How to force Service Mapping and Discovery Patterns to use Netstat for process detection on Solaris Servers"
aliases:
  - KB0725084
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725084
kb_number: KB0725084
last_modified: 2024-04-07
---

## How to force Service Mapping and Discovery Patterns to use Netstat for process detection on Solaris Servers

  

### Issue

Service Mapping and Horizontal Discovery Patterns do not use Netstat for process detection for Solaris Servers with version below 11.2. In order to enable Service Mapping to use Netstat (instead of lsof), follow the procedure below.

### Resolution

1.  Navigate to MidServer -> Properties
2.  Add the mid server property **mid.servicewatch.process\_detection\_solaris.use\_netstat** with a value of true and provide the mid server name in the Mid Server field.  
    
3.  In the case where you want all the mid servers to use netstat, leave the Mid Server field to blank so that it is applicable to all mid servers
