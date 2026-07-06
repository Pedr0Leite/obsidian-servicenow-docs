---
title: "How to get the client IP of the originating request"
aliases:
  - KB0743808
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743808
kb_number: KB0743808
last_modified: 2024-07-30
---

## How to get the client IP of the originating request

  

### Issue

# Procedure

You can get the originating request client IP through a script using the method:

```
gs.getSession().getClientIP()
```

  
For example:

```
var session = gs.getSession();
var addr = session.getClientIP();
gs.info(addr);
```

### Related Links

[getClientIP() developer documentation](https://developer.servicenow.com/app.do#!/api_doc?v=kingston&id=r_ScopedGlideSessionGetClientIP "getClientIP() developer documentation")
