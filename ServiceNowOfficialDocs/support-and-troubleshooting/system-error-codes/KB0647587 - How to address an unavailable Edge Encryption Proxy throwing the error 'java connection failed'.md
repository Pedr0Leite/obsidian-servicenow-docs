---
title: "How to address an unavailable Edge Encryption Proxy throwing the error 'java connection failed'"
aliases:
  - KB0647587
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647587
kb_number: KB0647587
last_modified: 2024-12-05
---

## How to address an unavailable Edge Encryption Proxy throwing the error 'java connection failed'

  

### Issue

How to address an unavailable Edge Encryption Proxy throwing the error 'java connection failed'

  

Problem

* * *

EEP are connecting via an Enterprise Proxy, this may cause an issue if the Enterprise Proxy is intermittently unreachable.

  

Symptoms

* * *

Applications show time out errors, but the EEP does not show any errors until restarted.  

-   Instance logs will show the **Java connection timeout**
-   Users will experience the **Edge Encryption Proxy as unavailable**

  

Cause

* * *

The error occurs when the further **connection to an intermediate proxy can not be established**. Without connectivity the encryption proxy cannot reach the instance.  

  

  
Resolution

* * *

Diagnose the **intermediate proxy** and restart it if necessary. This has to be 100% reachable and running.  
Following that, the **Edge Encryption Proxy Service will need to be restarted**. Error messages, if present, will not appear before a few minutes that the service has been running.
