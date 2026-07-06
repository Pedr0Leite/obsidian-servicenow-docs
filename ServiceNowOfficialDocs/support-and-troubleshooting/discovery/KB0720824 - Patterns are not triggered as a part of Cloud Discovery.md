---
title: "Patterns are not triggered as a part of Cloud Discovery"
aliases:
  - KB0720824
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720824
kb_number: KB0720824
last_modified: 2024-04-07
---

## Patterns are not triggered as a part of Cloud Discovery

  

### Issue

# Symptoms

* * *

During cloud discovery on a service account, patterns to identify other cloud services are not triggered.

# Release

* * *

All

# Cause

* * *

1\. CloudApplicationDiscovery script include is responsible for triggering patterns.   
2\. In the script include, we are hitting an exception line 66 (JP-9c) -> No mid found per required capabilities.   
3\. In the code and we look at applications configured for the mid server. In this case, no applications were configured for the mid server. This was causing the issue.

#   

### Resolution

Goto the respective mid server and add the application 'Discovery' or 'All'.
