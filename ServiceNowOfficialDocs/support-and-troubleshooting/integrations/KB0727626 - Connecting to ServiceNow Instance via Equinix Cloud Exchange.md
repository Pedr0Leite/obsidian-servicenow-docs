---
title: "Connecting to ServiceNow Instance via Equinix Cloud Exchange"
aliases:
  - KB0727626
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727626
kb_number: KB0727626
last_modified: 2025-02-14
---

## Connecting to ServiceNow Instance via Equinix Cloud Exchange

  

### Issue

Connecting to ServiceNow Instance via Equinix Cloud Exchange

### Release

 N/A

### Resolution

# Procedure

* * *

ServiceNow has 2 redundant connections at each Equinix-enabled DC (see Additional Information section).

To provide better redundancy we recommend to request from Equinix 2 virtual connections per DC, which makes total 4 connection for DC pair where production and subproduction instances are hosted. 

To implement different load-balancing scenarios over those connections  customer can use BGP tools such as AS-PATH prepend and LocalPreference. 

**General procedure to request a connection:**

1.  Customer logs into Equinix portal and clicks the Create Connection button
2.  Customer fills out the connection request by selecting the ports on their side and entering in details such as BGP info.  
    1.  Customer selects local (to them) port and remote location.
    2.  Customer inputs Connection name, then selects a VLAN ID.  (The VLAN does not need to match ServiceNow's VLAN ID!) 
    3.  Customer inputs their BGP ASN and IP subnet that will be used for connection. 
    4.  Optional: "Available from remote locations" means that the customer doesn't have to be in the same facility as ServiceNow
3.  Customer creates CS case on ServiceNow support portal with request to turn-up Equinix connection created on Step 2. One CS case can be used for several Equinix connections if those are requested at the same time on Equinix portal.
4.  ServiceNow engineer will contact client via CS case for further details about circuit/BGP turn-up

**Notes:**

1\. Public AS and public IP addressing must be used (for connection itself and for advertised prefixes)

2\. BFD is not supported. For faster convergence customer can lower keepalive/holdtime timers on their side.

3\. In case one or more Equinix connection is down (physical circuit/BGP peer) traffic is forwarded using other Equinix connections following configured BGP policy. If all Equinix connections are down, ServiceNow Internet connections will be used as a last resort (in case same prefixes are advertised over public Internet). 

4\. Customer should run redundancy tests after turn-up of all needed virtual connections to make sure load-balancing works as expected in any scenario (like primary/secondary). Firewall/BGP policy configuration to implement those scenarios is solely on customer’s side. ServiceNow doesn’t do any custom configuration on those connections.

# Additional Information

* * *

-   [KB1704585  Network Connectivity Overview](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1704585)
-   [KB0547560 Internet circuit providers per datacenter](https://support.servicenow.com/kb_view.do?sysparm_article=KB0547560)
-   [KB0538621 Finding the IP address information for your instance](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538621)
