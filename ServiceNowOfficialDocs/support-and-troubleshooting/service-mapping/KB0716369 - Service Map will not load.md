---
title: "Service Map will not load"
aliases:
  - KB0716369
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716369
kb_number: KB0716369
last_modified: 2024-04-07
---

## Service Map will not load

  

### Issue

# Symptoms

* * *

Service Map for Manual Service will not load.  Map will attempt to load (cycles) but will not complete.  If you open developer tools you may see RangeError:  Maximum call stack size exceeded.

![](/sys_attachment.do?sys_id=789e7c62db0ab450e515c2230596196e) 

# Release

* * *

All

# Cause

* * *

An large number of element within the map can cause a StackOverflow Exception.  We normally recommend around 200 element with in a Service Map for manageability and performance. 

# Resolution

* * *

Split big service into smaller Segments.
