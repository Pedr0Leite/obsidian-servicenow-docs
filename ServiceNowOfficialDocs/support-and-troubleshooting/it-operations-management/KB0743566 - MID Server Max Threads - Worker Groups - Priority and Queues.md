---
title: "MID Server Max Threads - Worker Groups - Priority and Queues"
aliases:
  - KB0743566
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743566
kb_number: KB0743566
last_modified: 2025-10-31
---

## MID Server Max Threads - Worker Groups - Priority and Queues

  

### Issue

## Table of Contents

-   [The MID Server and the ECC Queue support Priority](#mcetoc_1i08s6q39r)
-   [Which features make use of Priorities](#mcetoc_1i08s6q39s)
-   [Making use of this information](#mcetoc_1i08s6q39t)

### The MID Server and the ECC Queue support Priority

Higher priority jobs can jump the queue, and execute quicker, in higher priority threads:

<table style="height: 65px;" border="1"><tbody><tr style="height: 13px;"><td style="height: 13px; width: 60px;"><em>Priority</em></td><td style="height: 13px; width: 77px;"><em>Thread Group</em></td><td style="height: 13px; width: 119px;"><em>No. Threads&nbsp;(default)</em></td><td style="height: 13px; width: 132px;"><em>Parameter</em></td><td style="height: 13px; width: 132px;"><em>Input Queue in Memory</em></td><td style="height: 13px; width: 68px;"><em>Java Priority</em></td><td style="height: 13px; width: 187px;"><em>work\monitors\ECCSender folder&nbsp;</em></td><td style="height: 13px; width: 265px;"><em>Examples of probes</em></td></tr><tr style="height: 13px;"><td style="height: 13px; width: 60px;">2 (default)</td><td style="height: 13px; width: 77px;">Standard&nbsp;</td><td style="height: 13px; width: 119px;">25&nbsp;</td><td style="height: 13px; width: 132px;">threads.max</td><td style="height: 13px; width: 132px;">500 (25*Threads)</td><td style="height: 13px; width: 68px;">5</td><td style="height: 13px; width: 187px;">output_2&nbsp;</td><td style="height: 13px; width: 265px;">JDBC, LDAP, Discovery...</td></tr><tr style="height: 13px;"><td style="height: 13px; width: 60px;">1&nbsp;</td><td style="height: 13px; width: 77px;">Expedited&nbsp;</td><td style="height: 13px; width: 119px;">20</td><td style="height: 13px; width: 132px;">threads.expedited.max</td><td style="height: 13px; width: 132px;">400 (20*Threads)</td><td style="height: 13px; width: 68px;">8</td><td style="height: 13px; width: 187px;">output_1</td><td style="height: 13px; width: 265px;">REST, SOAP</td></tr><tr style="height: 26px;"><td style="height: 26px; width: 60px;">0&nbsp;</td><td style="height: 26px; width: 77px;">Interactive&nbsp;</td><td style="height: 26px; width: 119px;">10&nbsp;</td><td style="height: 26px; width: 132px;">threads.interactive.max</td><td style="height: 26px; width: 132px;">40 (4*Threads)</td><td style="height: 26px; width: 68px;">10</td><td style="height: 26px; width: 187px;">output_0</td><td style="height: 26px; width: 265px;">HeartbeatProbe<br>SystemCommand: restartService, grabLog, etc.</td></tr></tbody></table>

When the MID Server retrieves a batch of output records from the ECC Queue, it will prioritise the higher priority jobs first (lower priority field value). The same applies to the ECCSender thread when passing results back to the instance. e.g. If a large Standard priority JDBC Import set is mid-way through, an Expedited result will not have to wait for all the import rows to be sent back to the instance first.

The MID Server will fetch more jobs than it has free threads if they are in the ecc\_queue. These remain queued in MID Server memory until a thread is free. The ECC Queue output record will be in Processing state, but it may be some time before it actually starts to be processed in a thread.  
Note: The Processed timestamp field in the ECC Queue cannot be relied on for this reason, as all it really means is the time the MID Server retrieved the record, not when the job started to run.

The higher priority jobs will be given more CPU time in the MID Server application once running. The thread pools map to different Java thread priorities, and Java will assign more resources to the job.

Java is a multi-threaded platform, and will use all the CPUs and Threads available to it. A dedicated host server/VM with many dedicated CPUs/Cores as you can get your hands on is recommended, or threads may execute considerably slower at busy times than they might when the MID Server is almost idle. That is important if you are expecting "Interactive" jobs to complete quick enough to avoid user transactions waiting too long for forms to update. e.g. A single LDAPListener thread may process user updates a lot slower while Discovery is also running in all other threads.

In the case of Discovery and Orchestration probes, the priority of the ecc\_queue input then dictates the priority of the sys\_trigger scheduled job that processes the sensor. Most scheduled jobs and async business rules in the platform are priority 100, so interactive inputs would take priority over those.

<table style="height: 52px; border-collapse: collapse;" border="1"><tbody><tr style="height: 13px;"><td style="width: 259px; height: 13px;">ECC Queue Priority</td><td style="width: 260px; height: 13px;">Scheduler Worker Priority (default)</td><td style="width: 260px; height: 13px;">System property</td></tr><tr style="height: 13px;"><td style="width: 259px; height: 13px;">2</td><td style="width: 260px; height: 13px;">110</td><td style="width: 260px; height: 13px;">glide.ecc.async.priority.standard</td></tr><tr style="height: 13px;"><td style="width: 259px; height: 13px;">1</td><td style="width: 260px; height: 13px;">105</td><td style="width: 260px; height: 13px;">glide.ecc.async.priority.expedited</td></tr><tr style="height: 13px;"><td style="width: 259px; height: 13px;">0</td><td style="width: 260px; height: 13px;">50</td><td style="width: 260px; height: 13px;">glide.ecc.async.priority.interactive</td></tr></tbody></table>

### Which features make use of Priorities

Generally everything should run at Standard priority, unless there is a very good reason why it needs to jump the queue. 

As of Vancouver, very few features deliberately set this to anything other than Standard, and those that do have often been as the solution (or cause) of a problem ticket.

-   Discovery/Service Mapping will use the priority of the Discovery Status record for all probes. This may vary depending on how the Discovery is launched:  
    -   Interactive: Pattern Designer debug mode, Cancel Discovery, XMLStats (PRB1564921)
    -   Expedited: Service Mapping, Discover Now, Quick Discovery (PRB1624010), Shazzam port scan probes of Standard priority schedules (PRB1408213)
    -   Standard: Scheduled Horizontal Discoveries, except Shazzam
-   MID Server:  
    -   Interactive: All SystemCommands, Test Credentials
-   Orchestration:  
    -   Expedited: Test Inputs in Activity Designer, Start workflow from the Workflow Editor, and now All normal workflow executions (PRB1301862)
-   IntegrationHub
    -   Expedited: All IPaasActionProbe
    -   Interactive: RESTProbe for Refresh OAuth Tokens
-   Cloud Management  
    -   Standard: APIProxyProbes CAPI orchestrator
-   Event Management  
    -   Interactive:  Pull Connectors, as new events need getting into the instance without delay
-   Change Management  
    -   Standard: Automatic and Manually triggered Discovery of Affected CIs
-   LDAP  
    -   Expedited: Test Connection and Browse (PRB1331240)
    -   Standard: Imports, Listener

### Release

Up to and including Zurich, and later

### Resolution

There is scope for certain real-time updated User-Interface triggered jobs, or quick integrations running as part of a user transaction, to be allowed to run as Expedited priority. Such as job running at higher priority would improve the user experience, and prevent blocking instance threads while waiting for the response which would increase overall instance performance. However often those integrations would be better running truly asynchronously, with a Sensor dealing with the eventual response from a low priority job in the background, without holding up a user's form or instance thread at all. A MID Server dedicated to those jobs may be a better solution.

A before insert business rule on the ecc\_queue table is a simple way to bump up the priority of specific outputs. It is very important to include the specific Queue, State, Topic, Name, Source and Agent Correlator fields in the conditions to make sure you don't effect more jobs that you intend.

If you intend to improve the throughput of your MID Server, then you do need to consider the number of threads, as well as the available CPUs. A lot of probes spend a lot of their time just waiting for responses from endpoints, blocking threads, without using CPU. If you choose to raise the Standard thread pool number - up to 200 is possible before hitting limits in Windows - you should also scale up the other thread pools in proportion as well. Don't only increase the number in threads.max, without also doing threads.expedited.max and threads.interactive.max.

With only 3 priorities, and really only 2 usable priorities, it is common for several sets of high priority jobs to be impacting each other, especially when there has been a flood of jobs due to a batch update. In this situation, consider dedicated MID Servers to each job, so they are fully protected from other jobs impacting them. 

**Important notes**: Once all Interactive threads are in use, critical MID Server system commands can be blocked, including HeartbeatProbe which is used by the instance to know if the MID Server is up, so it could be set as Down and become unusable. It's therefore a good idea to never use Interactive, and use Expedited for anything that must jump the Standard queue. Only if testing showed you had a need to jump the Expedited queue would you  consider Interactive.

Running higher priority Sensor scheduled jobs - either too many in a short time, or a few long running ones - have been known to cause performance issues for the instance. Discovery and Orchestration sensors at Interactive priority are priority 50 scheduled jobs, which is higher than most jobs and all async business rules, and equal to very important things like the text indexer and event management jobs. This can be dangerous, and any implementation above Standard priority needs to consider this.

And finally, "**When everything is a priority, nothing is a priority**", so don't be silly with this in custom implementations or you will defeat the purpose.

### Related Links

[MID Server System Requirements](https://docs.servicenow.com/bundle/utah-servicenow-platform/page/product/mid-server/reference/r_MIDServerSystemRequirements.html "MID Server System Requirements")

[Discovery MID Servers at 100% CPU - Good or Bad, Why and then what?](https://support.servicenow.com/kb_view.do?sysparm_article=KB0952290 "Discovery MID Servers at 100% CPU")

[MID Server Max Threads - Worker Groups - Priority and Queues](https://support.servicenow.com/kb_view.do?sysparm_article=KB0743566 "MID Server Max Threads - Worker Groups - Priority and Queues")
