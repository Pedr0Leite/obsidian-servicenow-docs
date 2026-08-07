---
title: "SNMP probe timed out. Target is either unreachable or there are no valid credentials for it. "
aliases:
  - KB0783670
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783670
kb_number: KB0783670
last_modified: 2026-03-09
---

## SNMP probe timed out. Target is either unreachable or there are no valid credentials for it.

  

### Issue

-   SNMP credentials are configured
-   MID server is available and reachable to the network device.
-   When a discovery is executed, Shazzam is able to reach the device and identify the SNMP port is open:
    -   ![Log showing SNMP port is open ](/sys_attachment.do?sys_id=60afa21a93b8fa54d744b94c5cba100d)

The issue is that the SNMP classification fails with the error below:

![](/sys_attachment.do?sys_id=24afa21a93b8fa54d744b94c5cba1012)

### Facts

Expected Out of Box Behavior:

-   When executing a discovery on a network device, Shazzam is responsible to verify that the device is reachable.  
      
    -   If the device is not reachable, ECC should warn "The target is not reachable"
    -   If the device is reachable, the SNMP classification needs to be executed and verify for the credentials.  
          
        
-   If the credentials are validated successfully, the SNMP classification must need to move further with the available OIDs

![Log showing OIDs](/sys_attachment.do?sys_id=e8afa21a93b8fa54d744b94c5cba100f)

### Release

-   London Patch 10

### Cause

1.  Looking at the error message "SNMP probe timed out. Target is either unreachable or there are no valid credentials for it.", we see that it is indicating two failures:  
      
    -   SNMP probe timed out
    -   There are no valid credentials  
          
        
2.  If the SNMP is timed-out, it should not move further to check the credentials.
3.  If the Credentials are not available, it should complain about "No credential found for type \[SNMP V3\]"
4.  It is Observed that the discovery is executing the Validate methods for "Access" and "Credentials" as expected, but, the MID server could not pick up the right credentials even they are available.

### Resolution

1.  Log into the instance
2.  Verify the list of available MID servers  
           https://<instance-name>.service-now.com/ecc\_agent\_list.do
3.  Search for the MID server which is being used to discover the Network device 
4.  Open the MID server record and perform the below operations sequentially  
      
    -   Invalidate 
    -   Validate  
          
        
5.  Execute a Discovery on the Network device which was failing earlier, and it should complete successfully.

### Related Links

[Validate the MID Server](https://www.servicenow.com/docs/csh?topicname=t_ValidateAMIDServer.html&version=latest "Validate the MID Server")
