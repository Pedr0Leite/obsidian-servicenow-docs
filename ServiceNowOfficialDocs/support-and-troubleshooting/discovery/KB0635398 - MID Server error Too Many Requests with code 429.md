---
title: "MID Server error \"Too Many Requests with code: 429\"
aliases:
  - KB0635398
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635398
kb_number: KB0635398
last_modified: 2025-11-04
---

## MID Server error "Too Many Requests with code: 429"

  

### Issue

MID Server error "Too Many Requests with code: 429"

### Cause

The API\_INT is one of the semaphores used by the MID servers when communicating to the instance. If the API\_INT semaphores are exhausted, and the queue depth has reached the max queue depth, then the instance will return the error "Too Many Requests with code: 429" to any MID server clients attempting communication. Because there are no available semaphores, the instance will not be able to receive any inputs or heartbeats from the MID server.

When this happens, the errors like the following can be seen in the MID server logs:

ECCQueueMonitor.5 WARNING \*\*\* WARNING \*\*\* Method failed: (https://YOUR\_INSTANCE.service-now.com/ecc\_queue.do?SOAP&amp;displayvalue=all&amp;redirectSupported=true)HTTP/1.1 429 Too Many Requests with code: 429&#13;
ECCQueueMonitor.5 SEVERE \*\*\* ERROR \*\*\* getRecords failed (Method failed: (https://YOUR\_INSTANCE.service-now.com/ecc\_queue.do?SOAP&amp;displayvalue=all&amp;redirectSupported=true)HTTP/1.1 429 Too Many Requests with code: 429)&#13; 

### Resolution

To check whether the API\_INT semaphores are exhausted:

1.  In a browser window, navigate to <your\_instance>.service-now.com/stats.do.
    
2.  Search for API\_INT.
    
3.  Check that there are no available semaphores and the queue depth equals the max queue depth.
    
    An exhausted API\_INT resembles the following example.
    
    API\_INT
    Available semaphores: 
    Queue depth: 50
    Max queue depth: 50
    0:F48CE383DB6A760098E53CAF9D961901 #583094 /api/now/table/sys\_audit (API\_INT-thread-2) (2:05:30.388)
    1:C25E23C3DB6A760098E53CAF9D961962 #583187 /api/now/table/sys\_audit (API\_INT-thread-4) (1:57:30.087)
    2:6BCE63C3DB6A760098E53CAF9D9619F4 #583264 /api/now/table/sys\_audit (API\_INT-thread-1) (1:55:29.678)
    3:95157F47DB6A760098E53CAF9D9619D9 #584585 /api/now/table/sys\_audit (API\_INT-thread-3) (1:28:03.004)
    
    In this example, note that long queries on the sys\_audit table are using up all available API\_INT semaphores. However, the long-running queries could be on a different table.
    

The solution depends on what is keeping the semaphores busy.

**For immediate relief:**

1.  Navigate to User Administration > All Active Transactions.
    
2.  Find the long-running transactions keeping the semaphores busy.
    
    Confirm with the team responsible for the transactions that killing the transactions will not cause any issues.
    
3.  Kill the transactions to free up the semaphores.
    

**For long-term relief:**

Contact the team responsible for the long-running transactions and work with the team on improving the transactions.

### Related Links

-   [KB0661756, "MID Server "Down" troubleshooting"](https://support.servicenow.com/kb_view.do?sysparm_article=KB0661756 "MID Server \"Down\" troubleshooting")
    
-   [KB0623708, "Binding MID Servers to nodes using "cookies" can cause load balancing issues, resulting in 429 errors"](https://support.servicenow.com/kb_view.do?sysparm_article=KB0623708 "Binding MID Servers to nodes using \"cookies\" can cause load balancing issues, resulting in 429 errors")
