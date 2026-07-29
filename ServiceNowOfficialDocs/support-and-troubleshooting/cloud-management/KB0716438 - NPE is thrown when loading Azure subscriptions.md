---
title: "NPE is thrown when loading Azure subscriptions"
aliases:
  - KB0716438
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716438
kb_number: KB0716438
last_modified: 2023-07-12
---

## Issue

###### Symptoms

* * *

In the mid logs, the below exception is found.

Failed to execute API - Caused by error in Ad hoc script 'azure-compute-1.0-ListSubscriptions' at line 1   
  
\==> 1: getResourceInfo();   
2:   
3: function getResourceInfo() {   
4: var res = new AzureSubscription(this.parameters, this.headers); 

  

#   

## Resolution

After correcting the proxy configuration, the issue was resolved.
