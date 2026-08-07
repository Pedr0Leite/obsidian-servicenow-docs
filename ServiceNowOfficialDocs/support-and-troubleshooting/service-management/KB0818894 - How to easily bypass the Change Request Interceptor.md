---
title: "How to easily bypass the Change Request Interceptor"
aliases:
  - KB0818894
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818894
kb_number: KB0818894
last_modified: 2025-07-28
---

## How to easily bypass the Change Request Interceptor

  

### Issue

The user wanted to know if it was possible to bypass the Change Request Interceptor - and if so, how.

### Resolution

Within the instance of concern, go to the "Create New" Change module:

-   nav\_to.do?uri=sys\_app\_module.do?sys\_id=323bb07bc611227a018aea9eb8f3b35e

Once there, under the "Link type", change the value from "New Record" to "URL (from Arguments)". Set the value of "Arguments" to "change\_request.do" and save the record.  
  
Now, each time a user clicks on the "Create New" module under the "Change" Application, it will not be intercepted as before.
