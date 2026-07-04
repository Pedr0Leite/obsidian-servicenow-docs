---
title: "Resolving failure to discover VIP for a load balancer"
aliases:
  - KB0621576
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621576
kb_number: KB0621576
last_modified: 2024-09-18
---

## Resolving failure to discover VIP for a load balancer

  

### Issue

Resolving failure to discover VIP for a load balancer 

Symptoms

* * *

The following symptoms indicate that the system failed to discover the load balancer VIP that is part of the business service:

-   The map displays either the load balancer configuration item (CI) with a warning icon or just the warning icon
-   The following error message appears for the CI that is expected to be the load balancer in the business service:   
      
    **Failed to recognize application. See the discovery log for more details**.

Cause

* * *

The system is trying to discover the VIP that has been removed from the load balancer configuration but was kept in the CMDB.

Resolution

* * *

1.  Run the horizontal discovery for the load balancer that now contains the VIP whose discovery failed.  
    This action discovers the load balancer and the VIP, and populates the CMDB with this data. For operational information, see [DiscoverNow](https://docs.servicenow.com/csh?topicname=c_DiscoveryConfiguration.html&version=latest?cshalt=yes "DiscoverNow").
2.  Run the horizontal discovery for the load balancer that previously contained the VIP whose discovery failed.  
    This action discovers the load balancer and removes the VIP from its record in the CMDB.
3.  Check that the CMDB record contains the correct information.
4.  Run the top-down discovery for the business service containing this load balancer VIP:
    1.  Navigate to **Service Mapping > Services > Business Services**.
    2.  Next to the relevant business service, click **View map**.
    3.  Click **Run discovery** (upper-right corner of the window).
