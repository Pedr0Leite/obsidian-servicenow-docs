---
title: "Security Incident - Error Message"
aliases:
  - KB0696562
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696562
kb_number: KB0696562
last_modified: 2024-04-07
---

## Security Incident - Error Message

  

### Issue

# Symptoms

* * *

When trying to create a new Security Incident, this message is seen "Illegal access to package\_private global script incident functions: caller not in scope rhino.global"

This error message is seen in the logs:   
  
Warning java.lang.SecurityException: Illegal access to package\_private global script incident functions: caller not in scope rhino.global   
Caused by error in <refname> at line 1   
\==> 1: global.incidentGetCaller(); 

# Release

* * *

Kingston Patch 6

# Cause

* * *

Business Rule Incident Functions is only Accessible from "This application scope only" 

# Resolution

* * *

Change the Business Rule Accessible from to "All Application Scopes." Clear the cache and try to create a new incident.
