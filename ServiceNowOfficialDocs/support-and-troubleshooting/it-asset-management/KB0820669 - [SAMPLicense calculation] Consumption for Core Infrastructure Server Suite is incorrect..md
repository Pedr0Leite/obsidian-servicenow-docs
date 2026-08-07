---
title: "[SAMP\License calculation] Consumption for \"Core Infrastructure Server Suite\" is incorrect."
aliases:
  - KB0820669
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820669
kb_number: KB0820669
last_modified: 2024-04-08
---

## Issue

-   The license consumption calculation does not seem to be considering the virtualization rights for "Core Infrastructure Server Suite" model.
-   As per the Metric Attributes, each host when licensed completely can have 2 VM's but this condition is not being considered for eg. VMware vCenter Cluster: xxx under the License Workbench for "**Core Infrastructure Suite ----- Per Core (with CAL) ---- Rights Used**".

![](sys_attachment.do?sys_id=80852881db0cf0d016d2a345ca961913)

## Resolution

-   When DRS is enabled, each VM on the cluster needs to be licensed on each host in the cluster.
-   Since there are two hosts, the number of rights needed for each VM's is doubled (because of DRS enabled).

### How rights are calculated:

Below are the details about the rights calculation,

-   The cluster has 2 hosts, each having 2 processors and 6 cores per processor.
-   There is a total of 14 VMs having the CIS install combined on the two hosts. Since DRS is enabled, the VMs are free to move across hosts.

Rights needed for each host:-

-   Since VMs are free to move around, for each host we consider total 14 VMs present.
-   Since "min cores per processor" is 8, a host needs 2\*8 = 16 rights to be fully licensed, which allows it rights to host 2 VMs with CIS installs.
-   Since there are 14 VMs for each host, and each set of 16 rights allows access to 2 VMs, each host needs 16 \* (14/2) = 112 rights to fully license itself including all VMs.

Hence the Total rights needed to license the complete cluster = 2 (no. of hosts) \* 112 (rights to license each host) = 224.
