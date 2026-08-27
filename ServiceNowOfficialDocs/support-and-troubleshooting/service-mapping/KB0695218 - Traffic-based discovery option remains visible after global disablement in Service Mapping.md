---
title: "Traffic-based discovery option remains visible after global disablement in Service Mapping"
aliases:
  - KB0695218
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695218
kb_number: KB0695218
last_modified: 2025-07-30
---

## Traffic-based discovery option remains visible after global disablement in Service Mapping

  

### Issue

By default, Service Mapping enables traffic-based discovery. You can disable this in Service Mapping at the product level by setting the global property sa.traffic\_based\_discovery.active to false. However, even after disabling this global setting, the traffic-based discovery checkbox still appears when creating new services.

#### Steps to reproduce: 

1.  Set the system property, sa.traffic\_based\_discovery.active, from true (default) to **false**. 
2.  Go to **Service Mapping** > **Home**
3.  Under the Map tile, select **Additional options.**
4.  Select **Define A Single Service Map.**  
    -   Add a name for your service
    -   Assign an owner
5.  Select **Save**. 
6.  Notice the Traffic Based Discovery checkbox remains selected.

### Release

Any supported release  

### Cause

Two different levels control traffic-based discovery:

-   Global level: The sa.traffic\_based\_discovery.active property controls whether the system generates traffic-based connections globally.

-   Service level: The Traffic Based Discovery option on the business service form operates at the business service level.

### Resolution

Simply disabling the global property does not remove traffic-based connections from the form display or map. This is expected, however they are prevented from being created in the Configuration Management Database (CMDB) and service maps. 

To remove existing traffic-based discovery connections:

1.  After disabling the system property, rerun discovery.
2.  Check that existing traffic-based connections are removed from your service map.
