---
title: "Determining if the main and failover LDAP servers are running"
aliases:
  - KB0538724
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538724
kb_number: KB0538724
last_modified: 2024-05-01
---

## Determining if the main and failover LDAP servers are running

  

### Issue

Determining if the main and failover LDAP servers are running 

Problem

* * *

Users are able to access the instance, but it takes longer than expected.  

Symptoms

* * *

-   User authentication is delayed.
-   There is an unexpected behavior when attempting to log in.  
      
    

Cause

* * *

If the instance is configured with multiple IPs during LDAP server configuration, there may be an issue when one of the servers is not accessible.  
  
See [Specify Redundant LDAP Servers](https://docs.servicenow.com/ "Specify Redundant LDAP Servers") for information on redundant LDAP servers.  
  
  
Resolution

* * *

-   Verify with the LDAP administrator that the configured LDAP servers are available.
-   Update the LDAP server configuration to list only one IP in the **Server URL** field, noting how long it takes for the user(s) to be authenticated.
-   If IPs are listed in the **Server URL**, try using the **FQDN** instead.
-   Contact the network administrator to verify that the VPN and/or firewalls are configured correctly.

If the suggestions above did not resolve the issue, create an incident (INT) ticket, and include this information:

-   The network administrator contact information
-   The result of nslookup /  host of the affected instance from the LDAP server(s)
-   The result of ping / traceroute from LDAP servers to the instance URL, noting the start and endpoint IPs.
-   The result of packet captures that can be opened in Wireshark, noting the start and endpoint IPs, and the time frames when the user authentication was requested.
