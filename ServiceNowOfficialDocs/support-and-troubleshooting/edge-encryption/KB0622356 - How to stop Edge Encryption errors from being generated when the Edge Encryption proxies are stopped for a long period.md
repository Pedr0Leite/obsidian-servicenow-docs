---
title: "How to stop Edge Encryption errors from being generated when the Edge Encryption proxies are stopped for a long period"
aliases:
  - KB0622356
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622356
kb_number: KB0622356
last_modified: 2024-04-07
---

## How to stop Edge Encryption errors from being generated when the Edge Encryption proxies are stopped for a long period

  

### Issue

How to stop Edge Encryption errors from being generated when the Edge Encryption proxies are stopped for a long period

# Problem

* * *

Localhost logs will have several entries if an Edge Encryption proxy is being unresponsive. However, if the proxies have been intentionally stopped (for example, for a planned maintenance), the logs will continue to show those errors at intervals.

For example:

\--localhost------ PDT TIME  
2016-08-15 04:07:11 (068) worker.1 worker.1 SEVERE \*\*\* ERROR \*\*\* sn\_edge\_encryption: The proxy XXX is unresponsive. Last response 2016-08-15 11:06:38  
2016-08-15 04:07:11 (069) worker.1 worker.1 SEVERE \*\*\* ERROR \*\*\* sn\_edge\_encryption: There is no encryption proxy online  
\--localhost------

# Symptoms

* * *

If you run an Edge Encryption proxy on an instance and then stop it, after a few minutes alerts will start to appear. The logs will show several errors such as the following:

SEVERE \*\*\* ERROR \*\*\* sn\_edge\_encryption: The proxy XXX is unresponsive. Last response xxxx

# Cause

* * *

The instance uses the sys\_encryption\_proxy entries to detect Edge Encryption proxy outages. These entries are not removed when the proxies are down, as they are part of the monitoring system for your instance.

# Resolution

* * *

If you need to stop the Edge Encryption proxy for a long time and do not want the logs to show the proxies as unresponsive, remove the relevant records from the sys\_encryption\_proxy table. This will clear out entries made by any Edge proxy that might have connected previously. These entries are regenerated next time the proxies are executed. This action also stop the monitoring systems from generating a false alarm.
