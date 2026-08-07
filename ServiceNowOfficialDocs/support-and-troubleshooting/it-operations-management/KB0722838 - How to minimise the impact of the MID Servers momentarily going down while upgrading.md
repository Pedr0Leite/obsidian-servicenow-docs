---
title: "How to minimise the impact of the MID Servers momentarily going down while upgrading"
aliases:
  - KB0722838
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722838
kb_number: KB0722838
last_modified: 2025-11-14
---

## How to minimise the impact of the MID Servers momentarily going down while upgrading

  

### Issue

Immediately after an Instance upgrade (including patches and hotfixes), all MID Servers will also Auto-Upgrade themselves to match the new version, otherwise, there may be code and data mismatches which can break things.

**During that auto-upgrade, the MID Servers will momentarily go DOWN** in order to replace application files before restarting. That can take approx 10 seconds to 2 minutes depending on the performance of the host server, and the time spend waiting for file locks to clear.

**Note** that, due to known PRB1322060, Madrid MID servers will take longer than 2 minutes ([https://support.servicenow.com/kb\_view.do?sysparm\_article=KB0754285](https://support.servicenow.com/kb_view.do?sysparm_article=KB0754285)). This issue is resolved in New York.

**This is almost always not noticed and doesn't cause any issues, because by its nature MID Server is a fundamentally Async feature that works via an ECC Queue**, however...

This could in theory cause jobs to fail, if:

-   A job is sent to a **specific MID Server**, and has a **timeout set in the instance**. e.g. Synchronous RESTMessageV2 is set to 15s timeout, and the MID Server hasn't a chance to run it in that time.
-   A job uses **MID Selection** algorithms, and this is **the only MID Server that matches** the Capability/Application/IP range. e.g. Orchestration
-   and there may be others.

MID Server Down and Up events will be caused, which may lead to Notifications being sent.

**Long-running jobs may get interrupted, and so will run again** from the beginning after the upgrade. For a data push, that may theoretically cause duplicate inserts/updates at the endpoint.

A **job that has already finished may run again** if the MID Server is restarted after finishing a job, but the input has not yet been passed back to the instance. See [KB0743121/PRB1330405](https://support.servicenow.com/kb_view.do?sysparm_article=KB0743121 "KB0743121/PRB1330405") for more details.

## Features always affected by a restart:

These features need a single dedicated MID Server, so will be affected when that MID Server restarts:

-   LDAP
-   Export sets
-   JDBC data sources
-   SOAPMessageV2/RESTMessageV2 API called synchronously from scripts, without a sensor business rule.
-   and probably others.

## Features not affected by the restart:

-   Discovery / Service Mapping - Probes/Sensors will continue to run after the upgrade. Any interrupted will re-run.
-   Orchestration - Assuming more than 1 MID Server is set up for each combination of Capability/Application/IP Range, and at least one remains UP. If no MID Server is available then the workflow Activity will error, and transition to the error, and assuming the workflow is designed to loop back and retry after a short timer, then this is not an issue. 
-   and probably others.

### Release

Anywhere MID Servers are in use.

### Cause

This is the expected behavior and unavoidable due to the current design of the MID Server and its upgrade code: Files cannot be replaced with new versions while they are in use.

### Resolution

There are several things that can be done to minimize the risk, depending on how the MID Server is used.

## Avoid running more than you have to around the time of an Instance Upgrade

During the instance upgrade, the system scheduler is paused, so that most scheduled jobs will not run. At the end of the instance upgrade, this is enabled again, and that is before the MID Servers start to upgrade, so it is possible a lot of queued jobs are likely to be trying to run at exactly the same time as the MID Servers are starting their auto-upgrades.

Avoid that my manually disabling, or deactivating any MID Server-related jobs before the upgrade, and only turn them back on again after the MID Servers have also upgraded.

Long-running jobs may get interrupted, and so will run again from the beginning after the upgrade. For a data push, that may theoretically cause duplicate inserts/updates at the endpoint.

## Configure Fail-over Clusters or MID Selection

Where possible, select MID Server automatically, via MID Selection, Discovery Behaviours or Clusters. If one MID Server is DOWN then another can be used. Not all features are yet updated to leverage these MID Server features.

Add your MID Server and additional MID Servers to a Cluster configured for Fail-over protection, and configure the fail-over MID Servers with at least the same capabilities as the MID Server it is intended to relieve.

**Note: More than one MID Server can be installed on the same Host server**. A typical fail-over cluster might be 2 MID Servers each on 2 Host servers, totaling 4 MID Servers.

## Make use of the "Fail over MID server" script action, for jobs already queued in Ready state

When a mid\_server.down event is fired, which is a record in the sysevent table create when any MID Server status is set as Down, a Script Action called 'Fail over MID server' runs. When a MID Server momentarily goes down during a restart, that script action will run.

This will **re-assign any ECC Queue output records still in Ready or Processing state to another MID Server**, using either of these methods:

1.  If the job was assigned to a MID Server using MID Selector in the first place:
    -   Re-run the MID Selection algorithms using the same criteria as the original MID Selection was done.
    -   This depends on another MID Server still being up, with the same Capabilities/IP Ranges/Applications defined as the down MID Server
2.  If the job was assigned to a MID Server directly, or via a Cluster:
    -   Assign the job to another member of the same Failover Cluster that the MID Server is a member of.
    -   This depends on the MID Server being a member of a Failover Cluster, and there being other members that are up.

This will also re-assign outputs that are **already in processing state**, which guarantees all jobs get run, but can mean the job ends up getting run twice:

'Processing' means the mid server already took the jobs from the queue. It may be at any of these stages of the process:

-   The MID Server has the job in its internal queue on RAM. (MID Servers deliberately fetch more jobs at a time than they have available threads to run them in)
-   The job may be executing in a worker thread
-   The job may have completed, and the result saved in a temporary XML file in the ECC Sender Folder, but not yet returned to the instance as an ECC Input record.
-   The ECC input record was inserted, but the Business Rules that set the Output record to Processed in response to that have not done that yet.

If the MID Server is only temporarily down, due to a network/communication issue between the MID Server and Instance, but is actually still running, this can lead to jobs that were reassigned in Processing state to be run by the original and failover MID Server. It is rare but does happen. Some integrations can have a problem with this, such as records being pushed to another system twice causing duplicates.

## Control when the Upgrade runs, by temporarily Pinning the MID Server version

If a MID Server is Pinned, then it will stay on that version. This can be used to delay the upgrade until you are sure no jobs will be affected while it happens.

**Warning: The auto-upgrade should not be delayed more than a few minutes due to the risk of code and data mismatches breaking things while the MID Server version is wrong for the instance.**

For each MID Server:-

1.  add the Parameter **mid.pinned.version** and set the value as the **MID buildstamp:** value shown in your Stats page (/stats.do) before the upgrade.  
    e.g. for an upgrade from London Patch 4 to Madrid:   
    Name: mid.pinned.version  
    Value: london-06-27-2018\_\_patch4-11-21-2018\_12-04-2018\_1527
2.  Allow the instance upgrade to finish.
3.  Ensure no jobs will need to use the MID Server in the next few minutes.
4.  Delete the mid.pinned.version parameter. (Delete the parameter record. Don't just clear it, or it will not be un-pinned)
5.  Click Upgrade on the MID Server form to cause the Upgrade to happen now.

## Pin a single member of each MID Server cluster until the other members are upgraded

You can temporarily pin just one of the MID Servers in each fail-over cluster, to ensure one will remain up for whatever jobs are en-queued during the upgrades of the other cluster members.

## Minimize the number of MID Servers that can Upgrade at the same time to One

Since the London release, it is possible to restrict the number of concurrent MID Server upgrades. This is designed to avoid SOAP semaphore exhaustion but has the side-effect of allowing you to control the maximum number of MID Servers that can be downloading the upgrade files at the same time. This should allow the upgrades of MID Servers to be spread out more.

Add these two properties to the instance System Property \[sys\_properties\] table:

-   mid.download.through.instance=true
-   concurrent.dist.download=1

### Related Links

Main Docs page for:

-   [MID Server Upgrade](https://docs.servicenow.com/search?q=MID+Server+upgrade "MID Server Upgrade")
-   [MID Server Cluster Configuration](https://docs.servicenow.com/search?q=MID+Server+cluster+configuration "MID Server Cluster Configuration")
-   [MID Server selection](https://docs.servicenow.com/search?q=MID+Server+selection "MID Server selection")
