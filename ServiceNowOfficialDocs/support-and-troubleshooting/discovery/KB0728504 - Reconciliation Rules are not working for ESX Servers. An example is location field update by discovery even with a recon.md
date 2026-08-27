---
title: "Reconciliation Rules are not working for ESX Servers. An example is location field update by discovery even with a reconciliation rule"
aliases:
  - KB0728504
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0728504
kb_number: KB0728504
last_modified: 2024-04-07
---

## Reconciliation Rules are not working for ESX Servers. An example is location field update by discovery even with a reconciliation rule

  

### Issue

# Symptoms

* * *

Reconciliation Rules does not work for ESX Servers. An example reconciliation rule is on table "ESX Server" with data source to "Manual entry" and attribute to location. Still discovery would update the location based on the schedule location value.

# Release

* * *

All versions

# Cause

* * *

-   OOB, Identification and reconciliation rules are for CIs that go through identification engine, but ESX servers have their own custom logic for identification and don't go through IRE. 
-   Documentation on ESX Servers : 
    -   [https://docs.servicenow.com/csh?topicname=r\_DiscoverESXServers.html&version=latest](https://docs.servicenow.com/csh?topicname=r_DiscoverESXServers.html&version=latest) 
    -   "Discovery identifies ESX servers based on their serial numbers. If the serial number is not available, Discovery uses the combination of Correlation ID and MORID (Managed Object Reference ID) to identify the server. After running the vCenter classifier, Discovery launches the VMware - vCenter Datacenters probe, which launches the probes that explore the ESX server." 
-   As the ESX servers identification is purely based on the custom logic, reconciliation rules are not considered for ESX servers. If you apply the same reconciliation rule for any other CI like Windows, Linux servers, etc.. same would be considered and updated based on the reconciliation rules.

# Resolution

* * *

Below script include is used for ESX Servers insert/update.

  
"VCenterESXHostsSensor" :   
**https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=4c6fbb6f8f575200c2fe0b5437bdeeae** 

  
Two options to achieve this is

1.  Update above script include per the business needs. If you are considering to update this script include, please note that any future upgrades would skip this file and you need to review and merge them manually. 
2.  Write a business rule for updating the required fields by selective authorized data sources.
