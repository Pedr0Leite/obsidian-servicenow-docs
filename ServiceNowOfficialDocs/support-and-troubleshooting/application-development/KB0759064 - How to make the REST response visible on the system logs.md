---
title: "How to make the REST response visible on the system logs"
aliases:
  - KB0759064
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759064
kb_number: KB0759064
last_modified: 2025-01-22
---

## Issue

When debugging an inbound rest call, the main property  used is 'glide.rest.debug'.  This gives you great information on the inbound request process.  However, it will not return the response.  

## Resolution

1\. Add the following code to the scripted webservice.

gs.log("DEBUG: " + JSON.stringify(result), "REST DEBUG");  
  

It should be the vary last line before the result return.

2\. Replace data with your return variable you used in your script.

Note:  be careful with returning large responses as this does right to the system logs.  It's meant for troubleshooting the integration in sub-production environments.
