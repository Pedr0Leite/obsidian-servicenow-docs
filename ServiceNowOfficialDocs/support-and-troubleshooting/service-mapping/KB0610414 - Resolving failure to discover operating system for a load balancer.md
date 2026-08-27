---
title: "Resolving failure to discover operating system for a load balancer"
aliases:
  - KB0610414
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0610414
kb_number: KB0610414
last_modified: 2024-10-04
---

## Issue

Problem

* * *

When running a top-down discovery with Service Mapping on a business service containing a load balancer, the discovery can fail. 

Symptom

* * *

The business service map displays the warning icon instead of the load balancer CI.

In releases prior to Jakarta, the following error is displayed: **Failed to detect operating system**.

In Jakarta, the following error is displayed: **Service Mapping triggered the horizontal discovery to find the host x.x.x.x, because this host was not in the CMDB. The horizontal discovery failed. See [discovery status](http://localhost:8080/nav_to.do?uri=/discovery_status.do%3Fsys_id%3D8d4dcb2c7f5532008f1c3b19befa91a7) for more info.** 

Possible Cause 1  

* * *

Load balancer configuration items (CI) also have related CIs for the services on those load balancers. In some cases, when a load balancer CI is deleted from the CMDB, its CI records for services are not removed from the CMDB. Then, a load balancer service CI does not have a parent and the **Load Balancer** field for the Load Balancer \[cmdb\_ci\_lb\_service\] record is empty. Service Mapping considers Virtual IP (VIP) addresses belonging to load balancer service CIs without a parent load balancer CI as invalid.  
Resolution 1  

* * *

1.  Look in the CMDB for the load balancer host machine.
2.  Remove records in the Load Balancer Service \[cmdb\_ci\_lb\_service\] table with empty **Load Balancer** fields.
3.  After these records are removed, run horizontal discovery (with the Discovery application) on the relevant load balancers that contain relevant VIPs.
4.  Run top-down discovery from Service Mapping.

  

Possible Cause 2

* * *

By default, a virtual IP with an install status of **Absent** or **NULL** is not considered viable. Starting with the Istanbul release, you can modify this behavior using the sa.inactive\_install\_status system property.

Resolution 2

* * *

1.  Determine why the VIP status was set to **Absent** or **NULL**.
2.  If necessary, change the default behavior by modifying the sa.inactive\_install\_status system property - remove the value to make Service Mapping consider any install status valid or modify the value to include statuses that Service Mapping ignores as invalid. For example, set the value of **Desired** and **Inactive** statuses to make them invalid and exclude them from the discovery process.

Possible Cause 3

* * *

An F5 BIG-IP load balancer’s operational status is not operational. Horizontal discovery sets the operational status of an F5 BIG-IP Load Balancer using an SNMP query.

Many deployments use F5 BIG-IP Load Balancers as redundant pairs (active/passive). In this scenario, load balancers are configured identically, where one is operational and the other is a failover. The failover load balancer becomes operational when its counterpart goes down.

In some cases, horizontal discovery does not retrieve the correct operational status value. Then, Service Mapping does not initiate discovery on the load balancer.

Another reason for this problem could be that the load balancer was not configured for redundancy and its operational mode was left as non-operational.

Resolution 3

* * *

1.  Verify that the information retrieved by horizontal discovery is accurate by navigating to **Discovery Definition > Probes**.
2.  Search the table for **SNMP - F5 BIG-IP – System**.
3.  Click the the **SNMP Fields** tab.
4.  Verify that there are two failover fields (failover1, failover2). If only one failover field exists, you should apply the attached update set (xml file) for this problem.
5.  If the F5 load balancer is configured as non-operational, change the status to operational:  
    **Key** = sa.active\_operational\_status  
    **Value** = 1,2

Possible Cause 4

* * *

The default discovery process identifies a CI as a Linux server if it finds an SSH port in use. It may lead to incorrect classification of load balancers running on Linux as Linux servers. This discrepancy prevents Service Mapping from running the necessary pattern that discovers the VIP, which causes discovery to fail.

Resolution 4

* * *

1.  Remove the incorrect Linux CI from the CMDB.
2.  Create a [discovery behavior](https://docs.servicenow.com/csh?topicname=t_CreateDiscoBehavior4LB.html&version=latest "discovery behavior") to first discover network devices using the SNMP protocol.  
    After Discovery has discovered Unix-based load balancers correctly.
3.  Rediscover the load balancer using the new Discovery schedule.
4.  After the load balancer CI is discovered, rerun Service Mapping discovery. 

Possible Cause 5

* * *

Your organization might run several discovery applications, referred to as discovery sources. If more than one discovery application discovers the same load balancer, sometimes they erroneously create separate CIs in the CMDB for the load balancer. The Identification engine identifies these CIs and marks one of them as duplicate.

Resolution 5

* * *

1.  Verify that the discovery source of the load balancer is valid:
    1.  Navigate to **System Definition > Choice Lists**.
    2.  Apply the following filter to the table:  
        element=discovery\_source  
        table=cmdb\_ci
    3.  Check that the discovery source of this load balancer exists in the table and that the **Inactive** attribute is set to **false**.
2.  Remove the duplicate CI from the CMDB.

Possible Cause 6

* * *

The discovery source of the load balancer is invalid. The following message is displayed: **Invalid data source exist in payload**.

Resolution 6

* * *

Perform the same procedure in the solution for probable cause 5, except discover the same load balancer CI using the horizontal discovery (using the Discovery application) instead of removing the duplicate CI.

Related troubleshooting articles  

* * *

See the following articles to troubleshoot issues with load balancer discovery:

-   [KB0610413](https://support.servicenow.com/kb_view.do?sysparm_article=KB0610413): Virtual IP names of load balancers are partially incorrect
-   [KB0610412](https://support.servicenow.com/kb_view.do?sysparm_article=KB0610412 "KB0610412"): Load balancers with the same serial number merge into one CI
-   [KB0610322](https://support.servicenow.com/kb_view.do?sysparm_article=KB0610322 "KB0610322"): Service Mapping troubleshooting: load balancer discovery
