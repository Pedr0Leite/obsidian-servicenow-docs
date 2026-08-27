---
title: "Resolving a failure to find a MID Server for an IP address"
aliases:
  - KB0622808
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622808
kb_number: KB0622808
last_modified: 2024-04-07
---

## Resolving a failure to find a MID Server for an IP address

  

### Issue

Service Mapping does not find a MID Server that matches the parameters used for selecting MID Servers for a discovery job.

Service Mapping applies the MID Server selection algorithm that finds the MID Server to carry out the discovery.

The configuration of the MID Server must answer the following necessary criteria:

-   IP range: this range must contain the IP address of the CI you are discovering
-   Capability:  
    -   SSH for Unix hosts
    -   WMI for Windows hosts
    -   SNMP for load balancers
-   Supported Application: Service Mapping or All

For more information, refer to [MID Server Configuration for Service Mapping](https://docs.servicenow.com/csh?version=latest&topicname=configure-mid-service-mapping.html "MID Server Configuration for Service Mapping"). 

### Symptoms

-   The business service map displays the warning icon instead of the load balancer CI.
-   The following error message is displayed: **No active MID Server found for IP X.X.X.X.**

### Resolution

1.  Navigate to **Service Mapping > MID Servers**.
2.  Click **MID Selection Test**.
3.  Enter the CI IP address in the **Target IP field**.
4.  Select **ServiceMapping** or **ALL** from the **Application** list.
5.  Select the relevant MID Server capability from the **Capability** list.
6.  Click **OK**.
7.  If you get the same error, configure one of the MID Servers used in your deployment to answer the necessary selection parameters.
