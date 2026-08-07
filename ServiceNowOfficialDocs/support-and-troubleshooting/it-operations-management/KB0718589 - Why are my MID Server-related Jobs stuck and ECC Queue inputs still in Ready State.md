---
title: "Why are my MID Server-related Jobs stuck and ECC Queue inputs still in Ready State?"
aliases:
  - KB0718589
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718589
kb_number: KB0718589
last_modified: 2026-01-09
---

## Why are my MID Server-related Jobs stuck and ECC Queue inputs still in Ready State?

  

### Issue

This article is aimed at working out why **inputs** back from MID Servers are not getting processed in the instance. Symptoms would include:

-   Ecc Queue table \[ecc\_queue\] inputs, which are the results back from probes, remain in Ready state
-   Which in turn would cause  
    -   **Discovery schedules** get stuck and **time-out**
    -   **Service Maps** don't re-discover
    -   **Flows** don't progress past **IntegrtationHub** actions
    -   **Workflows get stuck** at an **Orchestration** Activity
    -   **Events** no longer come into **Event Management**
    -   **Import Sets** never receive the data from the **JDBC Data Source**
    -   MID Server related lists are not updated with Stats such as the Threads list.
    -   and there will be others...

Note: This KB is not dealing with Outputs, which is a completely different kettle of fish.

### Release

Any

### Resolution

## Table of Contents

-   [The Sensor is inactive](#mcetoc_1iiuk8s736b)
-   [There is no Sensor](#mcetoc_1iiuk8s736c)
    -   [ExportSetResult](#mcetoc_1jehequbd19)
    -   [SystemCommand](#mcetoc_1jehb1q5c3j) 
    -   [UpdateMetricsRegistrationCacheProbe](#mcetoc_1jehbqcbe1j)
-   [The Scheduler workers are backlogged...](#mcetoc_1iiuk8s736d)
    -   [...because the instance is not keeping up with the workload](#mcetoc_1iiukf98c2d)
    -   [...because the instance is Paused](#mcetoc_1iiukf98c2e)
-   [The Topic is LDAPConnectionTesterProbe, and it took more than 55 seconds](#mcetoc_1iiuk8s736e)
-   [The Sensor Crashed](#mcetoc_1iiuk8s736f)
-   [The input payload data was too large](#mcetoc_1iiuk8s736g)
-   [Domain Separation has hidden records the sensor depends on](#mcetoc_1iiuk8s736h)

## The Sensor is inactive

For an input to change state from Ready to Processing to Processed, it needs a Sensor, and that is always implemented as an Insert Business Rule on the ecc\_queue table. Most out-of-box features that use MID Servers will have a sensor, including:

| Feature | Business Rule |
| --- | --- |
| Discovery Probes | Discovery - Sensor  |
| Orchestration Activities | Automation - Sensors  |
| MID Server system | MID - Heartbeat, MID - Process XMLStats, etc. |
| Import Sets | JDBCProbeSensor |
| Event Management | Event Management - Connector |
| Integrations | ECC Queue Retry Policy  |

**Solutions**:  
**Check that the business rule is Active**.  
Check the Versions related list to see if the Business Rule has been customized, and **revert to the out-of-box version**. 

## There is no Sensor

If there is no sensor the input will remain in Ready state. That may be fine if it is the kind of fire-and-forget outbound integration where nothing needs to record or process the result. It's still best practice to have a sensor, even if all it does is mark the input processed.

For inputs from the **RESTMessageV2 or SOAPMEssageV2 API**, there is no out-of-box generic sensor. If no response is required and the API was executedAsync(), then these too can be ignored, but if the response does need processing then integrations using those APIs should have a sensor.

**Solution:** Implement a Sensor, so that the MID Server can be used asynchronously without causing performance issues.  
[**ServiceNow KB: Best practices for RESTMessageV2 and SOAPMessageV2 (KB0716391)**](https://support.servicenow.com/kb_view.do?sysparm_article=KB0716391 "ServiceNow KB: Best practices for RESTMessageV2 and SOAPMessageV2 (KB0716391)")

### ExportSetResult

System Export Sets don't have a sensor. These are run synchronously, blocking an instance thread while it waits for the MID Server to execute and return the ecc\_queue input. 

### **SystemCommand** 

There are many out-of-box SystemCommand probes which do not have sensors, and would therefore be expected to have inputs remaining in Ready state, including these common ones and others:

-   CitChanged
-   CustomOperationChanged
-   CustomParsingStrategyChanged
-   FileChange
-   LibsApplCategoryChanged
-   LibsDeviceInfoCategoryChanged
-   MetadataRulesChanged
-   PatternExtensionChanged
-   autoUpgrade
-   clear\_cookies
-   credentials\_reload - however a huge number of these might suggest an issue with OAuth2 credentials, and their token refresh.
-   deleteExpiredIHubPlans
-   file\_discovery\_whitelist - You can expect lots of these
-   invalidate\_cache
-   load\_properties
-   probe\_cache
-   range\_cache
-   resetQueryWindow
-   restart
-   signature\_validation\_certs\_reload
-   updateConfig

### UpdateMetricsRegistrationCacheProbe

This is related to Event Management and MetricBase metrics coming into the instance via MID Servers, and does not have a sensor.

## The Scheduler workers are backlogged...

The MID Servers insert the inputs into the ECC Queue via SOAP and using the instance's API-INT semaphores, and in order not to block those most sensor business rules run 'async', meaning they run in the Scheduler Worker threads.You can check for a backlog:

1.  Navigate to **System Diagnostics**.
2.  On the page, find **System Overview**.
3.  If the scheduler is backed up, **Events Pending** displays in red.

To know exactly what is queued, you will find the ready and running jobs in the Scheduler table \[sys\_trigger\], and the ecc\_queue related ones will have a similar name to the sensor business rule. e.g. The "Discovery - Sensors" business rule will create sys\_trigger records named "ASYNC: Discovery - Sensors". You can check that those are there:

1.  Navigate to **System Scheduler -> Scheduled Jobs**
2.  Add a filter for :  
    -   State is Ready, or State is Running
    -   Next action is Today
    -   Next action 'relative' on or before 1 minute ago
3.  You'll end up with a list URL something like this:   
    /sys\_trigger\_list.do?sysparm\_query=stateIN0,1^next\_action>javascript:gs.endOfYesterday()^next\_actionRELATIVELE@minute@ago@1

That will give the backlog of scheduler worker jobs for today. You could filter on 'Name Contains' if you know the sensor.

If your job is there, in Ready state, then it has not been run yet. Possible causes:-

### ...because the instance is not keeping up with the workload

Scheduler Worker threads are a shared resource, used by all async business rules and scheduled jobs in the platform, and so something completely unrelated to the MID Server jobs could be delaying or blocking processing.

The above list would give you an idea of the Names and age of the scheduler queue. If you filter this for only State = Running jobs, you can see what is currently running in the scheduler workers.

**Solution:** From the list you may be able to identify some long running jobs, or identify large number of similar quick running jobs, that have in effect been blocking the queue.

Seeing what's currently running should allow you to identify particular jobs to investigate to see if they are functioning normally. e.g. An unusually large batch update of incidents could have triggered a huge cascade of email notifications to CMDB owners. You could find anything.

If the backlog gets particularly bad, you might consider opening an support incident to help you identify the cause of the backlog.

But, if nothing is currently running, it may be...

### ...because the instance is Paused

Normally only an Upgrade would pause the schedulers, and automatically resume them afterwards.

You can check this by running a background script as an admin user:

1.  Navigate to **System Maintenance => Scripts - Background**
2.  In the '**Run script (JavaScript executed on server)**' box, paste this script

gs.log(gs.isPaused());

1.  Click **Run Script**

If that returns "true" then someone or something set the workers on pause meaning they won't process jobs.

**Solution**: Check that the instance is not currently in the middle of an upgrade, and wait for it to finish if it is: Navigate to **System Diagnostics -> Upgrade Monitor**

If the instance is not in the middle of an upgrade, then you probably need to open a support incident, as something has gone wrong.

## The Topic is LDAPConnectionTesterProbe, and it took more than 55 seconds

By default, the 'Test Connection' feature of LDAP Servers that use MID Servers will only wait 55 seconds for the result. This runs periodically, and when you click the link on the LDAP server form. 

If the Input for the probe takes longer than that to return to the instance, then that input will remain in Ready state, because the code that was waiting to process it already gave up waiting. 

See [KB0743756/PRB1331240 LDAP "Test Connection" and "Browse" features can timeout, and LDAP Monitor may show Connection Status as Not Connected, due to running at Standard(2) MID Server priority - Did not get a response from the MID server after waiting for 55 seconds](https://support.servicenow.com/kb_view.do?sysparm_article=KB0743756 "KB0743756/PRB1331240 LDAP \"Test Connection\" and \"Browse\" features can timeout, and LDAP Monitor may show Connection Status as Not Connected, due to running at Standard(2) MID Server priority - Did not get a response from the MID server after waiting for 55 seconds")

## The Sensor Crashed

In some cases a sensor may run, but crash before it has been able to update the state to Processing or Processed, and you are also very unlikely to see the Error String field populated with the reason.

**Solution**: Checking the system log or the app node localhost logs is often the only way to see what happened. Then search the knowledge base for known problems related to the errors you find.

## The input payload data was too large

If the input payload is particularly large, the SOAP Table API will move the value into an attachment instead of the actual record payload field. If that attachment is also too large for the platform limits, there will be no attachment saved. That could crash the sensor.

If the attachment is created, then the sensor may have trouble parsing and processing such a large amount of data, leading to long runtimes, or memory issues, that means the sensor fails.

**Solution**: Limits can be raised with various system properties, but it is better to implement the jobs so that multiple jobs run for sub-sets of data, to keep the input sizes smaller.

## Domain Separation has hidden records the sensor depends on

If everything involved is in Global domain, or all in the same domain, then there is usually not a problem. However, if the MID Server is is a different domain to the data then there may be problems when the sensors run as the MID Server user's domain. e.g. A workflow context running for a task in a parent domain uses a MID Server in a child domain for a job. The sensor runs in the child domain, and can't see the records in the parent domain, breaking the sensor.\\

**Solution**:  Have a MID Server installed specific to each domain, and ensure it is automatically selected by filling in the Applications, Capabilities and IP Ranges in each MID Server. In general, MID Servers in leaf domains work better than ones in in-between levels of the domains tree.
