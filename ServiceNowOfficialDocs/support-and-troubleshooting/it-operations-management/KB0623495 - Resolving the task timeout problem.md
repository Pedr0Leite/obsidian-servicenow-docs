---
title: "Resolving the task timeout problem"
aliases:
  - KB0623495
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623495
kb_number: KB0623495
last_modified: 2024-04-07
---

## Resolving the task timeout problem

  

### Issue

Resolving the task timeout problem

  
  

# Symptoms

* * *

There are task timeout error messages on the map and on the Discovery Messages tab.

# Possible Causes/Resolutions

* * *

There are several possible causes and resolutions.

## Possible Cause/Resolution 1

**Cause** – The MID Server does not pick up tasks because it does not pull messages from the ECC queue on time. 

**Resolution** – Perform the following steps:

1.  Navigate to the ECC\\Queue.
2.  Query for records with Topic ServiceDiscoveryProbe, Source matching the IP address on the message, and State is not Processed.
3.  Check that there are Queue records classified as Output, with the State attribute set to Ready. 
4.  Check the CPU consumption on the MID and if the MID CPU consumption is high, add MID Servers using the same range on another machine in order to reduce the load. 

## Possible Cause/Resolution 2

**Cause** – The MID Server does not pick up tasks because it stopped communicating with the ServiceNow instance.

**Resolution** – Restart the MID Server.

## Possible Cause/Resolution 3

**Cause** – The ServiceDiscoveryProbe probe working on the MID Server is slow or stopped functioning. The relevant MID Server is busy with a task that is taking a long time. 

**Resolution** – Perform the following steps:

1.  Navigate to the ECC\\Queue.
2.  Query for records with Topic ServiceDiscoveryProbe, Source matching the IP address on the message, and State is not Processed.
3.  Check that there are Queue records classified as Output with the State set to Processing.
4.  Change the mid.log.level MID configuration parameter to debug, and download the MID Sever logs.
5.  Look for exceptions that can help understand why pattern execution is hanging. Modify the task that takes a long time to run for efficiency.

## Possible Cause/Resolution 4

**Cause** – The instance is highly loaded and cannot process all input requests on the ECC queue in time. The Worker threads do not initiate Service Discovery Sensors that must pick up the input record from the ServiceDiscoveryProbe.

**Resolution** – Perform the following steps:

1.  Navigate to the ECC\\Queue.
2.  Query for records with Topic ServiceDiscoveryProbe, Source matching the IP address on the message, and State is not Processed.
3.  Check that there are Queue records classified as Input.
4.  Isolate the flows that mostly occupy the instance by navigating to Active Transactions or Slow Transactions.  
      
    For more information, see the product documentation topic [View and kill active transactions](https://docs.servicenow.com/csh?topicname=t_ViewAndKillAnActiveTransaction.html&version=latest).

## Possible Cause/Resolution 5

**Cause** – The processing of the ServiceDiscoveryProbe failed.

**Resolution** – Perform the following steps:

1.  Navigate to the ECC\\Queue.
2.  Query for records with Topic ServiceDiscoveryProbe, Source matching the IP address on the message, and State is not Processed.
3.  Check that there are Queue records classified as Input and the State is set to Error.
4.  In the instance logs, search for ServiceWatchInitialDiscoveryResultHandler.
5.  Find the log message that indicates the reason for this sensor failure and fix it.
