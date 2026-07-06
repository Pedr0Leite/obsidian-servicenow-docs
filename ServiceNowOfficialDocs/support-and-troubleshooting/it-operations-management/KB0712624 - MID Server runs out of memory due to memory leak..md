---
title: "MID Server runs out of memory due to memory leak."
aliases:
  - KB0712624
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712624
kb_number: KB0712624
last_modified: 2024-04-07
---

## MID Server runs out of memory due to memory leak.

  

### Issue

# Symptoms

* * *

MID Server memory usage trends up over time eventually exhausting the configured heap size and run into OutOfMemory errors. Once memory leak is severe enough it might not be able to respond to heartbeat probes from the Service Now instance and the instance will mark the MID Server as down. 

# Release

* * *

Jakarta and Newer.

# Cause

* * *

Heapdump analysis shows there are memory leak due to H2 Database connection leak. H2 is an in-memory Database used by Discover Patterns and Operational Intelligence. There is a bug where if an exception occur while executing a SQL query, the connection is not cleaned up and accumulates. Eventually this leads to memory exhaustion. Below is screenshot of the leaked H2 connection objects when performing Heap analysis:

![](sys_attachment.do?sys_id=f21ca82edb42b450e515c223059619cd)

# Resolution

* * *

This is fixed in PRB1293425 for Kingston Patch 8.

# Additional Information

* * *

In MID Server's agent0.log\[0-9\], look for the "LogStatusMonitor" log entries. These are MID Server health checks. If you look at 'used' memory, it trends up over time even when it's not processing any probes.

09/01/18 23:23:50 (616) LogStatusMonitor.60 stats threads: 83, memory max: 910.0mb, allocated: 496.0mb, used: 89.0mb, standard.queued: 0 probes, standard.processing: 0 probes, expedited.queued: 0 probes, expedited.processing: 0 probes, interactive.queued: 0 probes, interactive.processing: 0 probes

09/02/18 23:23:50 (616) LogStatusMonitor.60 stats threads: 83, memory max: 910.0mb, allocated: 712.0mb, used: 243.0mb, standard.queued: 0 probes, standard.processing: 0 probes, expedited.queued: 0 probes, expedited.processing: 0 probes, interactive.queued: 0 probes, interactive.processing: 0 probes  
  
09/03/18 22:24:50 (327) LogStatusMonitor.60 stats threads: 83, memory max: 910.0mb, allocated: 910.0mb, used: 498.0mb, standard.queued: 0 probes, standard.processing: 0 probes, expedited.queued: 0 probes, expedited.processing: 0 probes, interactive.queued: 0 probes, interactive.processing: 0 probes  
  
09/04/18 23:57:50 (567) LogStatusMonitor.60 stats threads: 87, memory max: 910.0mb, allocated: 910.0mb, used: 732.0mb, standard.queued: 0 probes, standard.processing: 0 probes, expedited.queued: 0 probes, expedited.processing: 0 probes, interactive.queued: 0 probes, interactive.processing: 0 probes  
  
09/05/18 10:28:18 (491) LogStatusMonitor.60 stats threads: 83, memory max: 910.0mb, allocated: 910.0mb, used: 877.0mb, standard.queued: 0 probes, standard.processing: 0 probes, expedited.queued: 0 probes, expedited.processing: 0 probes, interactive.queued: 0 probes, interactive.processing: 0 probes
