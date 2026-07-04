---
title: "Script include that calls JDBCProbe fails with java.lang.NullPointerException"
aliases:
  - KB0565304
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0565304
kb_number: KB0565304
last_modified: 2024-04-07
---

## Script include that calls JDBCProbe fails with java.lang.NullPointerException

  

### Issue

Script include that calls JDBCProbe fails with java.lang.NullPointerException

Problem

* * *

When executing a script include that calls the JDBCProbe, through the ECC queue, it fails with the following error:

03/23/16 14:39:31 (664) Worker-Standard:JDBCProbe Detect JDBCConnection interrupted. Retry: 1 of 3&#13;  
03/23/16 14:39:31 (664) Worker-Standard:JDBCProbe SEVERE \*\*\* ERROR \*\*\*  
java.lang.NullPointerException  
java.util.concurrent.ConcurrentHashMap.replaceNode(ConcurrentHashMap.java:1106)  
java.util.concurrent.ConcurrentHashMap.remove(ConcurrentHashMap.java:1097)  
com.service\_now.mid.message\_executors.CancelProbeExecutor.deregisterProbe(CancelProbeExecutor.java:25)  
com.service\_now.mid.probe.JDBCProbe.probe(JDBCProbe.java:123)  
com.service\_now.mid.probe.AProbe.process(AProbe.java:80)  
com.service\_now.mid.queue\_worker.AWorker.runWorker(AWorker.java:107)  
com.service\_now.mid.queue\_worker.AWorkerThread.run(AWorkerThread.java:20)  
java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)  
java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)  
java.lang.Thread.run(Thread.java:745)  
  

The MID Server log shows the following error:

03/23/16 14:39:16 (952) ECCQueueMonitor.5 SEVERE \*\*\* ERROR \*\*\* Error while registering probe: Thread-1007 to cancel, no agent\_correlator value&#13;  

Symptoms

* * *

  

-   This issue occurs in Geneva or later releases but works correctly in prior releases.
-   The JDBCProbe script include does not add agent\_correlator to the output ecc\_queue record

Cause

* * *

The agent\_correlator is a new requirement for ecc\_queue records in Geneva. This field associates outbound requests with the resulting response record in the ECC queue. This issue occurs because the JDBC Probe that is created via the script include is not providing a value for the agent\_correlator field. Therefore, when the MID server processes the response to the JDBCProbe, it fails to find a value and throws a null pointer exception.

  
Resolution

* * *

In the create section of the script include, set the agent\_correlator field as follows:

u.agent\_correlator=u.addParameter('agent\_correlator',gs.generateGUID());

The following example shows a complete script include that calls the JDBCProbe:

// Obtain MID Server  
var mid = new GlideRecord('ecc\_agent');  
mid.addQuery('name','MIDSERVERTEST');  
mid.query();  
mid.next();

// Get a specific Data Source (predefined to connect to a specific database instance)  
var ds = new GlideRecord('sys\_data\_source');  
ds.addQuery('name','TestDBA');  
ds.query();  
ds.next();  
gs.log("DataSource:" + ds.sys\_id);

//Create a JDBC Probe to Select/Query  
var u = new JDBCProbe(mid.name);  
**u.agent\_correlator=u.addParameter('agent\_correlator',gs.generateGUID());**  
u.setDataSource(ds.sys\_id);  
u.setFunction('SELECT');  
u.setTable("dba.companies");  
u.addParameter('skip\_sensor','true');  
u.create();
