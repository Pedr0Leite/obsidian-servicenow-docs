---
title: "How to discover F5 Load Balancer using SSH"
aliases:
  - KB0781036
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781036
kb_number: KB0781036
last_modified: 2025-08-07
---

## How to discover F5 Load Balancer using SSH

  

### Issue

F5 Load Balancer is classified using SNMP classification: "F5 BIG-IP Load Balancer".   Some Customers would like to discover F5 using SSH.

### Release

All

### Resolution

To use the "F5 Load Balancer SSH" pattern:

1.  Open Discovery Definition > CI Classification > SNMP > F5 BIG-IP Load Balancer > Triggers probes tab >
2.  change Pattern from  
    **F5 Load Balancer**  
    to  
    **F5 Load Balancer SSH**
3.  Make sure TMSH is enabled on the F5 device, and create a SSH credential on ServiceNow instance.

The SSH credential should have an user that has permission to run "list" and "show" command in TMSH on the F5 device.

In out of the box configuration, "Unix Classify" is launched before SNMP classification, and pops warning messages. The warning message can be ignored. In case you would like to remove these warning messages, we recommend creating a discovery schedule, and use discovery behavior so that the Unix Classify probe won't be launched.

  
To do this, you may refer to doc below:  
[Create a Discovery behavior](https://www.servicenow.com/docs/csh?topicname=create-disco-behavior.html&version=latest "Create a Discovery behavior")

### Related Links

[F5 BIG-IP load balancer discovery](https://www.servicenow.com/docs/csh?topicname=c_LoadBalancerF5BIGIP.html&version=latest "F5 BIG-IP load balancer discovery")
