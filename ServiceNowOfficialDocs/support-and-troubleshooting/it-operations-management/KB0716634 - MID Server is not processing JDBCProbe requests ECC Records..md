---
title: "MID Server is not processing JDBCProbe requests / ECC Records."
aliases:
  - KB0716634
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716634
kb_number: KB0716634
last_modified: 2024-04-07
---

## MID Server is not processing JDBCProbe requests / ECC Records.

  

### Issue

# Symptoms

* * *

MID Server is not processing JDBCProbe requests

# Release

* * *

Kingston Patch 10 and Lower

# Cause

* * *

When we have a MID Server which is making a JDBC connection, Under certain condition, when one multiple JDBC Probes are executing at the same time and they happen to load their respective drivers, deadlock at the native level can occur

We added MID Debug parameter   
[https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest](https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest)   
  
After that we can see the error -   
  
10/05/18 12:28:35 (556) ECCQueueMonitor.5 DEBUG: STANDARD threadpool queue is full! Skipping this message (will try again later).   
10/05/18 12:28:35 (556) ECCQueueMonitor.5 DEBUG: Event: GenericCounterMetricEvent   
10/05/18 12:28:35 (556) ECCQueueMonitor.5 DEBUG: Skipped message: Command /ms/dist/entmgt/PROJ/netcoolusers/prod/common/bin/nco\_alert -Manager ServiceNow -Agent '${agent}' -AlertGroup '${alert\_group}' -AlertKey '${alert\_key}' -Severity '   
${severity}' -Summary '${summary}' 4778e490db056784056d79578c9619eb   
10/05/18 12:28:35 (556) ECCQueueMonitor.5 DEBUG: Number of messages added to threadpool queue in current polling cycle: 0   
  
  
We are looking at the error as - STANDARD thread pool queue is full! Skipping this message (will try again later).   
  
We see the stack trace in the mid server thread is below   
  
| at com.service\_now.mid.connections.jdbc.JDBCConnection.establishConnection(JDBCConnection.java:97)   
| at com.service\_now.mid.connections.jdbc.JDBCConnection.connect(JDBCConnection.java:74)   
| at com.service\_now.mid.connections.jdbc.JDBCConnectionFactory.create(JDBCConnectionFactory.java:52)   
| at com.service\_now.mid.connections.ConnectionCachePool.getAvailableConnection(ConnectionCachePool.java:82)   
| - locked &lt;0x00000000c2626700&gt; (a com.service\_now.mid.connections.ConnectionCachePool)   
| at com.service\_now.mid.connections.ConnectionCache.get(ConnectionCache.java:94)   
| at com.service\_now.mid.probe.JDBCProbe.getJDBCConnection(JDBCProbe.java:710)   
| at com.service\_now.mid.probe.JDBCProbe.probe(JDBCProbe.java:107)   
| at com.service\_now.mid.probe.AProbe.process(AProbe.java:81)   
| at com.service\_now.mid.queue\_worker.AWorker.runWorker(AWorker.java:123)   
| at com.service\_now.mid.queue\_worker.AWorkerThread.run(AWorkerThread.java:20)   
| at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)   
| at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617) 

# Resolution

* * *

0\. Bring down MID Server

1\. Cleanup all old JDBC Probes record \[ set the ECC records state as 'error' \]  
  
2\. Import script include \[which is in the attachement\]  
  
3\. Run the script to load the drivers using Background scripts  
This will allow us to set the priority of the drivers load message to "interactive". The modified script include is attached to this Task. The script below sets the priority to 0:   
  
var midName = 'thanh-eclipse'; // Name of the MID Server  
var jspr = new JavascriptProbe(midName);   
jspr.setName('LoadJDBCDrivers');   
jspr.setPriority('0');   
jspr.addParameter('skip\_sensor', 'true');   
jspr.setJavascript('Packages.java.sql. DriverManager.getDrivers();');   
jspr.create();   
  
We should also create either a business rule or a script action to automatically run this script when a MID server is down. That way, when it comes back up, the message is there for it to load the drivers.   
  
4\. Restart MID Server  
  
5\. Run the JDBC Integration
