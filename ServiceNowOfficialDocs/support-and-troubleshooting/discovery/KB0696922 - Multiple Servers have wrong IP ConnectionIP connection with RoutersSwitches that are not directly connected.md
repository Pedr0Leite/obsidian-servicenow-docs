---
title: "Multiple Servers have wrong  \"IP Connection::IP connection\" with Routers/Switches that are not directly connected"
aliases:
  - KB0696922
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696922
kb_number: KB0696922
last_modified: 2025-08-26
---

## Multiple Servers have wrong "IP Connection::IP connection" with Routers/Switches that are not directly connected

  

### Issue

Servers from one region are showing IP connection::IP connection with multiple different switches and routers that do not seem to be valid.

-   One server  has IP Connection :: IP connection relationship with more than 100 routers.
-   Most of these routers are located in a different region when compared to servers

### Release

All

### Cause

If you look at the SNMP-Routing input, You can see the following input from the switch. From this we create a router interface with dest\_ip\_network as 10.0.0.0/8

<ipRouteEntry instance=".10.0.0.0">   
<ipRouteIfIndex type="SnmpInt32">76</ipRouteIfIndex>   
<ipRouteDest type="SnmpIPAddress">10.0.0.0</ipRouteDest>   
<ipRouteMask type="SnmpIPAddress">255.0.0.0</ipRouteMask>   
<ipRouteNextHop type="SnmpIPAddress">0.0.0.0</ipRouteNextHop>   
<ipRouteType type="SnmpInt32">3</ipRouteType>   
</ipRouteEntry>

\-when discovery completes it will generate a discovery device complete event. Then, that event will trigger a script action, which will call the script include, which is the "L3 Mapping script". In that logic, it will search the dscy\_route\_interface table for hi\_ip and lo\_ip.

\-So, if you are scanning any computers or servers that fall within these ranges, you will get these "IP connection::IP connection" relationships created between those devices to this switch accordingly.

\-In some cases, this may be a valid route on the switch because of the configuration of the switch. You can ignore this by making some modifications to L3 Mapping script include.

### Resolution

If you would like to ignore this dest\_ip\_network, please add the following line in L3 Mapping script include to ignore the dest\_ip\_network 10.0.0.0/8 as it will have huge range(10.0.0.1-10.255.255.255). As said above, if you are scanning any server which is in range (10.0.0.1-10.255.255.255), it will create a IP connection::IP connection with the router. 

Please add the following to ignore this dest\_ip\_network

after below line (around 98): 

var gr = new GlideRecord("dscy\_route\_interface"); 

add:   
gr.addQuery("dest\_ip\_network","!=","10.0.0.0/8");

Please note, there may be other dscy\_route\_interface records that are causing the connection to be created. If adding the above query to exclude route "10.0.0.0/8" does not resolve the issue, check the dscy\_route\_interface table for other matching networks - or alternatively view the dscy\_route\_interface records for one of the routers that continues to have the relationships created. If you are able to confirm that another large network is defined in the dscy\_route\_interface table, add it as another query similar the above, making sure that the query exactly matches the "dest\_ip\_network" field of the dscy\_route\_interface table. 

To provide an example - if there were to be a dscy\_route\_interface for a router with dest\_ip\_network "169.0.0.0/8", you could add the following query at the same position as the above mentioned query:

gr.addQuery("dest\_ip\_network","!=","169.0.0.0/8");

Further troubleshooting information can be found in the following Knowledge Article:

[https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0598422](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0598422)
