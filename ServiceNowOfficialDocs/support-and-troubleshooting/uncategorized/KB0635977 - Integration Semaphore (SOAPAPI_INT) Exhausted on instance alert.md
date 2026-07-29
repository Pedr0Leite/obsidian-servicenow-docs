---
title: "Integration Semaphore (SOAP/API_INT) Exhausted on instance alert"
aliases:
  - KB0635977
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635977
kb_number: KB0635977
last_modified: 2025-01-03
---

## Integration Semaphore (SOAP/API\_INT) Exhausted on instance alert

  

### Issue

You receive this notification indicating our internal monitoring has detected an issue with your instance, which is being investigated. This is just a warning on your queue usage.

Some alerts could appear with subject **Integration Semaphore (SOAP/API\_INT) Exhausted on 'instance'  
**

### Cause

An instance has multiple application nodes. The default settings are for each application node to have a maximum of 50 semaphores, with 4 active threads at the time. If transactions come too fast or take too long, they can queue up. If the queue reaches the maximum setting, new transactions on the queue are refused.

For example, per node, with 4 threads and a queue of 50, if the transactions take 10 seconds, your application node can process 4 transactions in parallel every 10 seconds on the queue. It also means that the fifth transaction will wait up to 10 seconds to start. If 100 transactions come at one time,  46 (50-4) will queue up and the rest will be refused.

### Resolution

Ensure that your nodes are not being overloaded with long Web Service calls or too many calls in a short period of time.

Perform the following actions:

### Review your active nodes.

For each node, validate the API\_INT queue. For example, the following is the list of semaphores:

                AMB  API\_INT  Debug  Default  Presence  
\--------------  ---  -------  -----  -------  --------  
node\_\_\_\_\_\_\_\_01  0/4  1/4      0/4    2/16     0/8  
node\_\_\_\_\_\_\_\_02  0/4  0/4      0/4    3/16     0/8

In this example, the problem is no longer occurring.

If the problem were still occurring, **it would show 4/4.**

### Review the stats.do on each node.

On each node, review stats.do and search for the Semaphore set for API\_INT. The information available would appear as follows:

node\_\_\_\_\_\_\_\_01 - Available semaphores: 4 - Queue depth: 4 - Max queue depth: 50  
node\_\_\_\_\_\_\_\_02 - Available semaphores: 4 - Queue depth: 4 - Max queue depth: 50

In this example, the queues look normal. Note that some queries are queued up because it is not reaching the maximum set of 4. However, the presence of "Max queue depth: 50" shows the queue had reached its maximum.

If the problem is still occurring, you will see the Available semaphores equal 0. In that case, check the thread stack trace link on the semaphore queue to find more information.

### To find the source of the problem, review your transaction logs.

To find the root cause of the problem, check the transaction logs at the time the problem occurs.

Look for long transactions or for a large amount of them in a short period of time.

**You can check with the following link:** <instance>/syslog\_transaction\_list.do?sysparm\_filter\_only=true&sysparm\_query=sys\_created\_onONToday@javascript:gs.daysAgoStart(0)@javascript:gs.daysAgoEnd(0)%5EGROUPBYsys\_created\_by&sysparm\_first\_row=1&sysparm\_view=

Modify the example search to match the alert findings, for example, change the timings to the events that disrupted the queue.

Try grouping the results by 'Created by', then find the user that has more calls and validate the transaction that could be related to the problem.

### Finally, analyze the full picture of the information available.

The most common solutions are:

-   If the client Web Service application is making too many calls, try to reduce the throughput.
-   If the calls are taking too long, make the Web Service execute faster by making any long processing asynchronous.
-   If there are too many calls, try to group them together and process them in a data source or multiple update calls to Web Services.
-   If a user is abusing the system, make the user active = false and contact them.
-   Check whether the client Web Services is retrying the transactions too quite or too often (for example, because of refused responses)
-   Check whether the client application is making a full crawl on the instance (for example, mirroring or indexing Web Services applications), then time it at off-peak times with fewer parallel queries.
