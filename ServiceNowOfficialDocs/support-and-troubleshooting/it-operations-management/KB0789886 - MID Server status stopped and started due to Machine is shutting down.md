---
title: "MID Server status stopped and started due to \"Machine is shutting down\"
aliases:
  - KB0789886
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789886
kb_number: KB0789886
last_modified: 2026-06-19
---

## MID Server status stopped and started due to "Machine is shutting down"

  

### Issue

We often see issues were MID server is restarted and customer suspect this is happening because of upgrade to new release. Hence, the good practice is to grab MID server logs from the affected MID server and find root cause.

### Release

All Releases

### Resolution

1.  Open affected MID Server record from the instance.
2.  Under **Related Links**, Click  **Grab MID Logs.**
3.  Navigated to ECC queue and add following filter:

-   -   Topic \[is\] \[SystemCommand\]
    -   Source \[is\] \[grabLog\]
    -   Agent \[is\] \[your MID Server name\]

Search for the **Agent0.log.0** and **wrapper.log** entries in the list view. These logs are also accessible in the \\agent\\logs\\ file path.

**Wrapper Log**:  
  
2019/12/15 00:33:17 | **Machine is shutting down**.&#13;  
2019/12/15 00:35:29 | --&gt; Wrapper Started as Service&#13;  
2019/12/15 00:35:34 | Java Service Wrapper Standard Edition 64-bit 3.5.36&#13;  
2019/12/15 00:35:34 | Copyright (C) 1999-2018 Tanuki Software, Ltd. All Rights Reserved.&#13;  
2019/12/15 00:35:34 | [http://wrapper.tanukisoftware.com&#13;](http://wrapper.tanukisoftware.com&#13;)  
2019/12/15 00:35:34 | Licensed to ServiceNow, Inc. for MID&#13;  
2019/12/15 00:35:34 | &#13;  
2019/12/15 00:35:47 | Child process: Java version: timed out&#13;  
2019/12/15 00:35:47 | Failed to retrieve the version of Java. Resolving to the lowest supported version (1.4).&#13;  
2019/12/15 00:35:58 | Wrapper Process has not received any CPU time for 21 seconds. Extending timeouts.&#13;  
2019/12/15 00:35:58 | Launching a JVM...&#13;  
2019/12/15 00:35:58 | Wrapper Process has not received any CPU time for 21 seconds. Extending timeouts.&#13;  
2019/12/15 00:35:58 | Launching a JVM...&#13;  
2019/12/15 00:37:24 | WrapperManager: Initializing...&#13;  
2019/12/15 00:37:24 | Wrapper Process has not received any CPU time for 57 seconds. Extending timeouts.&#13;  
2019/12/15 00:37:34 | Startup failed: Timed out waiting for a signal from the JVM.&#13;

  
**Agent Log**:  
  
12/15/19 00:33:18 (649) WrapperListener\_stop\_runner Running under Java version: 1.8.0\_181-sncmid1, java PID: 7616, args: stop&#13;  
12/15/19 00:33:18 (650) WrapperListener\_stop\_runner Stopping MID server&#13;  
12/15/19 00:33:18 (650) WrapperListener\_stop\_runner Main.handleStop() before shutdown, OperationalState=UP&#13;  
12/15/19 00:33:18 (919) WrapperListener\_**stop\_runner Setting mid status to Down**&#13;  
12/15/19 00:33:18 (919) WrapperListener\_stop\_runner Instance.updateAgentRecordStopped(), OperationalState=UP&#13;  
12/15/19 00:33:19 (138) WrapperListener\_stop\_runner interrupting thread IdleConnectionMonitor.5&#13;  
12/15/19 00:33:19 (310) WrapperListener\_stop\_runner interrupting thread AutoUpgrade.3600&#13;  
12/15/19 00:33:19 (466) WrapperListener\_stop\_runner interrupting thread PatternAttributeFileMonitor.3600&#13;  
12/15/19 00:33:19 (622) WrapperListener\_stop\_runner interrupting thread StatusMonitor.600&#13;  
12/15/19 00:33:19 (778) WrapperListener\_stop\_runner interrupting thread RefreshMonitor.65&#13;  
12/15/19 00:33:19 (935) WrapperListener\_stop\_runner interrupting thread LogStatusMonitor.60&#13;  
12/15/19 00:33:20 (091) WrapperListener\_stop\_runner interrupting thread ECCQueueMonitor.40&#13;  
12/15/19 00:33:20 (247) WrapperListener\_stop\_runner interrupting thread FileSyncer.1&#13;  
12/15/19 00:33:20 (403) WrapperListener\_stop\_runner interrupting thread ECCSender.1&#13;  
12/15/19 00:33:20 (997) WrapperListener\_stop\_runner Destroying injector...&#13;  
12/15/19 00:33:21 (341) WrapperListener\_stop\_runner Closing com.service\_now.mid.amb.AMBClientProvider&#13;  
12/15/19 00:33:22 (325) WrapperListener\_stop\_runner Closing com.service\_now.monitor.PriorityThreadPoolProvider&#13;  
12/15/19 00:33:22 (325) WrapperListener\_stop\_runner Shutting down ThreadPool-Standard&#13;  
12/15/19 00:33:22 (325) WrapperListener\_stop\_runner Shutting down ThreadPool-Expedited&#13;  
12/15/19 00:33:22 (325) WrapperListener\_stop\_runner Shutting down ThreadPool-Interactive&#13;  
12/15/19 00:33:22 (356) WrapperListener\_stop\_runner ThreadPool-Standard terminated&#13;  
12/15/19 00:33:22 (356) WrapperListener\_stop\_runner ThreadPool-Expedited terminated&#13;  
12/15/19 00:33:22 (356) WrapperListener\_stop\_runner ThreadPool-Interactive terminated&#13;  
12/15/19 00:33:22 (372) WrapperListener\_stop\_runner Closing com.service\_now.mid.extension.container.ExtensionContainer&#13;  
12/15/19 00:33:22 (372) WrapperListener\_stop\_runner ExtensionContainer is shutting down...&#13;  
12/15/19 00:33:22 (372) WrapperListener\_stop\_runner ...waiting a maximum shutdown time of 1000ms&#13;  
12/15/19 00:33:22 (372) WrapperListener\_stop\_runner ExtensionContainer is cleanly shut down&#13;  
12/15/19 00:33:22 (372) WrapperListener\_stop\_runner Closing com.service\_now.mid.probe.event.SNEventBulkSender&#13;  
12/15/19 00:33:22 (513) EventBulkSenderThread-1 the event sender was stopped after sending 0 events in 0 bulks.&#13;  
12/15/19 00:33:22 (513) WrapperListener\_stop\_runner Closing com.service\_now.mid.cluster.ignite.IgniteClusterManager&#13;  
12/15/19 00:33:22 (513) WrapperListener\_stop\_runner Main.handleStop() after shutdown, OperationalState=UP&#13;  
12/15/19 00:33:22 (606) MIDServer MID Server stopping&#13;  
12/15/19 00:33:23 (013) MIDServer Stoping LDAP Listener for: LDAP SBMOffshore&#13;  
12/15/19 00:33:23 (903) MIDServer MID Server stopped&#13;  
  
  
**Observation**:  
Found in logs the MID server service stopped because the "Machine is shutting down" triggered. Hence, due to host machine shut down the MID server service stopped.  
  
Further customer to check internally to find out the reason for Machine shut down with the time stamp available in the agent logs.  
  

### Related Links

This is one cause which we identified for MID server restarted in Agent logs. There might be more reasons for the MID server getting restarted. Hence, review MID Server agent logs for more details.  
  
"Machine is shutting down" explanation  
[https://wrapper.tanukisoftware.com/doc/english/qna-shutdown.html](https://wrapper.tanukisoftware.com/doc/english/qna-shutdown.html)
