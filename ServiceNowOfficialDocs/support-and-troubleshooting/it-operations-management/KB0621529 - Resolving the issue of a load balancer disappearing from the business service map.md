---
title: "Resolving the issue of a load balancer disappearing from the business service map"
aliases:
  - KB0621529
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621529
kb_number: KB0621529
last_modified: 2024-04-07
---

## Resolving the issue of a load balancer disappearing from the business service map

  

### Issue

Resolving the issue of a load balancer disappearing from the business service map  

Symptoms

* * *

A load balancer disappears from the business service map. There are connections going directly from the entry point of the business service to the next tier CIs. The rest of the CIs also disappear from the map.

![A load balancer before and after removing it from CMDB](sys_attachment.do?sys_id=599ae0a6db42b450e515c22305961955 "A load balancer before and after removing it from CMDB") 

  
Cause

* * *

The load balancer, which is part of this business service, has been removed from the CMDB, leading to broken connections on the business service map.

Typically, this problem occurs after changing a load balancer configuration. The horizontal discovery performed by Discovery mistakenly creates a new load balancer in the CMDB, deleting the Virtual IP (VIP) of the existing load balancer. 

  
Resolution

* * *

  

 Perform the following steps to resolve this issue:

1.  On the load balancer, verify that its virtual IP (VIP) is set to the same as it was in the CMDB, before this issue occurred. 
2.  Perform the horizontal discovery of this load balancer with Discovery as described in [Run Quick Discovery](https://docs.servicenow.com/ "Run Quick Discovery").
3.  Perform the top-down discovery of the business service with Service Mapping:
    1.  Navigate to **Service Mapping > Services > Business Services**.
    2.  Next to the relevant business service, click **View map**.
    3.  In the upper right corner of the window, click **Run discovery**.
