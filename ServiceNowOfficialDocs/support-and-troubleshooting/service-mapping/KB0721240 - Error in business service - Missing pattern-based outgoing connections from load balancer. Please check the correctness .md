---
title: "Error in business service - Missing pattern-based outgoing connections from load balancer. Please check the correctness of the incoming connection"
aliases:
  - KB0721240
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721240
kb_number: KB0721240
last_modified: 2024-04-07
---

## Error in business service - Missing pattern-based outgoing connections from load balancer. Please check the correctness of the incoming connection

  

### Issue

# Symptoms

* * *

A business service created via HTTP(S) end point does not show a complete map and instead, the map stops post identifying the load balancer and throws the error

**Missing pattern-based outgoing connections from load balancer. Please check the correctness of the incoming connection**

# Cause

* * *

Starting Kingston, LB Service discovery by Service Mapping is exclusively based on the CMDB, meaning that data such as 'name', 'IP' and 'port' is taken from the CMDB prior to the pattern execution and basically based on what horizontal discovery previously discovered.  
  

So, when you see the error **Missing pattern-based outgoing connections from the load balancer. Please check the correctness of the incoming connection**

When we refer to the discovery log for the LB services, you see that step "Get connections" in "Connections to server farm" section shows the following error:  
No such resource \[name, INxxxxxxxxxxxxxxxxxxxxxxxxxxx\]  
No such resource \[name, INxxxxxxxxxxxxxxxxxxxxxxxxxxx\]  
  
When you debug and execute "show lb vserver <vserver\_name>" command on each of these names, you get that error.  
  
Also, when examining the incoming payloads from your quick discovery on the Load Balancer, we these lines:  
{"vsvrPort":"443","vsvrName":"INxxxxxxxxxxxxxxxxxxxxxxxxxxx","vsvrIpAddress":"xxx.xxx.xxx.xxx"}  
{"vsvrPort":"990","vsvrName":"INxxxxxxxxxxxxxxxxxxxxxxxxxxx","vsvrIpAddress":"xxx.xxx.xxx.xxx"}  
Meaning that horizontal discovery retrieves the wrong names for these Vservers.

# Resolution

* * *

The NetScaler device discovery, **vsvrName** returns hash instead of server name if entity name exceeds 32 bytes. Because of this, the CI names are displayed as the hash returned by snmp for vsvrName

1) Navigate to discovery definition -> Probes

2) Search for the probe 'SNMP - Netscalar - System'

3) Under the SNMP Fields related list, Look for 'services' under 'Name'

4) The 'Table Fields' contain ''vsrvrName" which has to be replaced by "vsvrFullName" and then save the probe.

Run Discovery on the business service or via quick discovery to know if the desired results are being seen.

# Additional Information

* * *

The issue has been fixed in London.
