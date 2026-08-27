---
title: "Discovery failed with exceptions: java.lang.IllegalArgumentException: Missing required parameter ip_address"
aliases:
  - KB0690885
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0690885
kb_number: KB0690885
last_modified: 2024-04-07
---

## Discovery failed with exceptions: java.lang.IllegalArgumentException: Missing required parameter ip\_address

  

### Issue

# Symptoms

* * *

There are Java exceptions in discovery logs for Network devices(Routers and switches).  
  

```
java.lang.IllegalArgumentException: Missing required parameterip_addressat com.service_now.mid.probe.shazzam.scanners.APortScanner.getParamAsIP(APortScanner.java:208)at com.service_now.mid.probe.shazzam.scanners.APortScanner.init(APortScanner.java:56)at com.service_now.mid.probe.shazzam.scanners.AUDPPortScanner.init(AUDPPortScanner.java:35)at com.service_now.mid.probe.shazzam.scanners.DNS.init(DNS.java:63)at com.service_now.mid.probe.DNS.addScanners(DNS.java:140)at com.service_now.mid.probe.DNS.processChunk(DNS.java:114)at com.service_now.mid.probe.ShazzamBase.syncProcessChunk(ShazzamBase.java:71)at com.service_now.mid.probe.DNS.probe(DNS.java:90)at com.service_now.mid.probe.AProbe.process(AProbe.java:84)at com.service_now.mid.queue_worker.AWorker.runWorker(AWorker.java:125)at com.service_now.mid.queue_worker.AWorkerThread.run(AWorkerThread.java:20)at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)at java.lang.Thread.run(Thread.java:748)
```

# Release

* * *

Jakarta and Kingston.

# Cause

* * *

The cause of this problem is both sensors and patterns enabled at the same time. Either of the one should be used, but not both.

-   There is a DNS probe in discovery which is causing Java exceptions.
-   This probe is for resolving DNS names of IPs.
-   This would get triggered twice, one for SMMP Identity - Multiprobe and once again for Horizontal Pattern probe.
-   When it gets triggered with SMMP Identity - Multiprobe, proper IP Addresses are being sent to DNS probe and it is processing good. No error here.
-   When it gets triggered with Horizontal Pattern probe, "null" parameter is being sent instead of IP Address. And this activity seems to be redundant. 
-   This is because, there are both Probes and Sensors, Patterns enabled for discovery.

# Resolution

* * *

-   Identify which classification is triggered for the discovery. It should be either "Standard Network Router" or "Standard Network Switch".
-   Open the classifier. (Navigate to Discovery Definition -> CI Classification -> All and search for respective classifier).
-   Under "Triggers Probes" section, you can remove "Horizontal Pattern".
-   Re-run the discovery and it should go good now without errors.

# Additional Information

* * *

You can contact Customer Support if you have any questions performing the above steps.
