---
title: "Resolving disconnected cluster CIs on the business service map"
aliases:
  - KB0621531
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621531
kb_number: KB0621531
last_modified: 2024-04-07
---

## Resolving disconnected cluster CIs on the business service map

  

### Issue

Resolving disconnected cluster CIs on the business service map 

Symptoms

* * *

A cluster CI may appear detached from all CIs in map tiers above or below it.

![](sys_attachment.do?sys_id=2cbce0eedb42b450e515c2230596198b)

Cause

* * *

A CI that is part of this business service has been removed from the CMDB, leading to broken connections on the business service map.

Typically, this problem occurs after changing a load balancer configuration. The horizontal discovery performed by Discovery mistakenly creates a new load balancer in the CMDB, deleting the Virtual IP (VIP) of the existing load balancer.

Resolution

* * *

To resolve this issue:

1.  On the load balancer, verify that its virtual IP (VIP) is set to the same as it was in the CMDB before this issue occurred. 
2.  Perform the horizontal discovery of this load balancer with Discovery as described in [Run Quick Discovery](https://docs.servicenow.com/ "Run Quick Discovery").
3.  Perform the top-down discovery of the business service with Service Mapping.
    1.  Navigate to **Service Mapping > Services > Business Services**.
    2.  Click **View map** next the relevant business service.
    3.  Click **Run discovery** in the upper right corner of the window.

  

Please note there may be known problems in the platform that can cause floating CIs. Please open an incident with SN technical support to investigate your specific use case.
