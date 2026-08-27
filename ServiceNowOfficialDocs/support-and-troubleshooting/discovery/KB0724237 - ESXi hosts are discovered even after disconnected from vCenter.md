---
title: "ESXi hosts are discovered even after disconnected from vCenter"
aliases:
  - KB0724237
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724237
kb_number: KB0724237
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

-    Discovery keeps collecting data of the ESXi hosts from the vCenter database which are power off and disconnected. 

![](/sys_attachment.do?sys_id=4d6ae066db42b450e515c223059619bc)

# Release 

* * *

-   All versions

# Troubleshooting 

* * *

-   To determine whether the ESXi hosts are still attached to vCenter (ie. in power off & disconnected), in the Discovery logs for the payload which returned from **"VMware ESX Probe"**, observe below information from the input payload 

Input Payload info:   
  
"name":"esx\_host1.xxx.com","install\_status":false,   
"name":"esx\_host2.xxx.com","install\_status":false,   
"name":"esx\_host3.xxx.com","install\_status":false 

-   From above payload, the install status of ESXi hosts identified as false.
-   Discovery still collects data of these ESXi hosts from the vCenter database which means technically they are powered off but still attached to respective vCenter. 
-   The attached screenshot, represent that these ESXi hosts physically reflects in the respective vCenter. 

# Cause

* * *

-   Discovery identifies and classifies information about ESXi servers and ESXi resource pools through the discovery of vCenter.
-   This by means, these ESXi hosts information is pulled from the vCenter and not from the ESXi directly. 
-   Only when the ESXi hosts are completely detached from vCenter, data will not be pulled by Discovery.

# Resolution 

* * *

-   As a quick workaround, please communicate with vCenter admin team to detach ESXi hosts and remove the stale entries of these ESXi hosts from respective vCenter.
-   Communicate with VMware vendor and find the root cause of why the vCenter database holds the stale data of disconnected ESXi and resolve to avoid these situations in future.
