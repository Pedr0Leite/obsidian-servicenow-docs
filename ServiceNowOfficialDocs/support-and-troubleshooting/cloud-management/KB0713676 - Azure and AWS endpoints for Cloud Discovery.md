---
title: "Azure and AWS endpoints for Cloud Discovery"
aliases:
  - KB0713676
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713676
kb_number: KB0713676
last_modified: 2025-01-03
---

## Issue

  
  

# Description

* * *

1.  In CMPv2, cloud discovery probes go through mid server.
2.  If mid server traffic is going through proxy, azure and aws endpoints should be allowed from the mid server host.

# Procedure

* * *

1.  For AWS, if the endpoint contains the string 'amazonaws', it should be allowed. In our backend code, we leverage aws api to pull the data. For example, when we click on 'Discovery Datacenters' for a service account, in the backend we make a 'Describe Regions' call using aws api.   
    Ref: [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#using-regions-endpoints  
    ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#using-regions-endpoints)2. Below is an Azure endpoint url. You need to allow any endpoint that has 'management.azure.com'/'azure.com'   
    [https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines?api-version=2017-12-01](https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines?api-version=2017-12-01)   
     

# Applicable Versions

* * *

Post Istanbul (All versions)

# Additional Information

* * *

1.  Data collected by cloud discovery in the below doc.   
    Ref: [https://docs.servicenow.com/csh?topicname=r-discovery.html&version=latest](https://docs.servicenow.com/csh?topicname=r-discovery.html&version=latest)
