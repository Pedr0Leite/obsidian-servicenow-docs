---
title: "[Discovery - Shazzam] Shazzam not returning/running ports information intermittently (like WMI, ssh, snmp)"
aliases:
  - KB0745497
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745497
kb_number: KB0745497
last_modified: 2026-01-25
---

## \[Discovery - Shazzam\] Shazzam not returning/running ports information intermittently (like WMI, ssh, snmp)

  

### Issue

Shazzam not returning/running ports information intermittently (like WMI, ssh, snmp)

### Symptoms

During the discovery of large scale IP ranges, intermittently we might see that the Shazzam is not returning or missing some ports information like WMI (135), 22 etc.

### Facts

  

### Release

All

### Cause

Sometimes if these MID servers are on slower networks, sometimes the port probes that are being sent out don't get returned in a timely manner (based on our default settings), and therefore don't get reported back to the instance.

### Resolution

Method #1:

Use [Discovery Behaviors](https://docs.servicenow.com/csh?topicname=c_DiscoveryBehaviors.html&version=latest "Discovery Behaviors") to limit what port probes are used for certain scans. For example, if you are scanning Windows servers only in that IP range then set up Discovery Schedule to use behavior with "WMI only". So with this, it will send only WMI port probe to these target servers, which will help with the performance.

  
Method #2:

Use the [Shazzam probe parameters](https://docs.servicenow.com/csh?topicname=t_ConfigureTheShazzamProbe.html&version=latest "Shazzam probe parameters") (some specific) that you can add/modify that can help with the performance.   
  
One example to consider is to modify the parameter "shazzam\_chunk\_size" to use a smaller number such as "25 or 50 or some lesser based on your requirement" (default is "100"), this will help in slowing down sending and retrieving port probe results so that you get more results if some of these port probes take longer to return. Although this will slow down the Shazzam probe and take Discovery a little longer to run, you should get more consistent results.   
  
Another example, we can try increasing the value of the "[GenericTCP\_waitForConnectMS](https://docs.servicenow.com/csh?topicname=t_ConfigureTheShazzamProbe.html&version=latest "GenericTCP_waitForConnectMS")" parameter in the "Shazzam" probe.   
Currently, the default value is "1000" (1000ms = 1 second), however you can increase this value to a number like "5000" (5000 ms = 5 Secs) or "10000" (10000ms = 10 seconds) and see if this helps as well. 

### Related Links

-   [Discovery Behaviors](https://docs.servicenow.com/csh?topicname=c_DiscoveryBehaviors.html&version=latest "Discovery Behaviors")
-   [Shazzam probe parameters](https://docs.servicenow.com/csh?topicname=t_ConfigureTheShazzamProbe.html&version=latest "Shazzam probe parameters")
