---
title: "Settings for MID Servers which is part of MID Server Cluster for REST Message"
aliases:
  - KB0716571
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716571
kb_number: KB0716571
last_modified: 2024-04-07
---

## Settings for MID Servers which is part of MID Server Cluster for REST Message

  

### Issue

# Overview

* * *

This KB discuss the settings for MID Servers which is part of MID Server Cluster for REST Message

# Settings for MID Servers which is part of MID Server Cluster for REST Message

* * *

The MID Server Cluster is supported for Rest Message call / functionality.

The MID Server criteria plays a major role in the setting of the MID Server Cluster.

-   Supported Applications
-   IP Ranges
-   Capabilities 

By default, the MID Server's criteria above are defined as "ALL" (during the setup if not Cancel).

However, there are some MID Servers that defined particular "Supported Applications, IP Ranges, Capabilities as per the requirements.

**To be able for the MID Server Cluster works for REST Message, ALL MID Servers should have the same criteria defined.**

# Example

* * *

MID Server Cluster: "MID Cluster" have the following MID Servers with the following criteria defined:

i. MID 1

Supported Applications: ALL

IP Ranges: ALL

Capabilities: WMI, ServiceMapping, SNMP, Resolve DNS, SSH, PowerShell, REST, VMware

ii. MID 2

Supported Applications: ALL

IP Ranges: ALL

Capabilities: ALL

iii. MID 3

Supported Applications: ALL

IP Ranges: ALL

Capabilities: ALL

With the settings defined above, if MID 1 goes down, the MID Server Cluster will not use the MID 2 and MID 3 (can be check in the ECC queue transaction, where there are no queues created for the MID 2 and MID 3 as part of the REST Message call).

To resolve:

MID 1 - Capabilities should be updated to use "ALL".

OR

MID 1, MID 2 and MID 3 - Capabilities should be updated to use only "REST".

OR 

MID 2 and MID 3 - Capabilities should be updated to use the same as Capabilities of MID 1.
