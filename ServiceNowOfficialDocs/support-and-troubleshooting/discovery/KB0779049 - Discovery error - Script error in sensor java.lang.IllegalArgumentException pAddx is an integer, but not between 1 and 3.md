---
title: "Discovery error - Script error in sensor: java.lang.IllegalArgumentException: pAddx is an integer, but not between 1 and 30!"
aliases:
  - KB0779049
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779049
kb_number: KB0779049
last_modified: 2024-04-08
---

## Discovery error - Script error in sensor: java.lang.IllegalArgumentException: pAddx is an integer, but not between 1 and 30!

  

### Issue

-   There is custom SNMP classifier developed for WAP device discovery. For some devices, the system is throwing below error.

Sensor error when processing SNMP - Identity: java.lang.IllegalArgumentException: pAddx is an integer, but not between 1 and 30!  
undefined (sys\_script\_include.778011130a0a0b2500c4595ad1d1d768.script; line 32)

-   This article will demonstrate on the investigations and probable use cases, hence in future, if a similar error occurs then this can be one of the cause and worth trying to fix.

### Cause

-   This is part of Problem - PRB1292098
-   The root cause is an entry 0.0.0.0/0 for the CI on dscy\_route\_interface table.

### Resolution

-   In order to resolve this issue, kindly make below changes to the code in 'DiscoveryReconciler' script include :

From:

var net = new SncIPNetworkV4(eigr.dest\_ip\_network);  
var routeInfo = {net: net, sysid: eigr.sys\_id + ''};  
exitRoutesByIface\[iface\].push(routeInfo);

To: (mainly wrapped the above code with an if condition to exclude 0.0.0.0/0 )

if(eigr.dest\_ip\_network != '0.0.0.0/0') {  
var net = new SncIPNetworkV4(eigr.dest\_ip\_network);  
var routeInfo = {net: net, sysid: eigr.sys\_id + ''};  
exitRoutesByIface\[iface\].push(routeInfo);}

-   NOTE - Kindly make the changes on sub production and test the use case multiple times before deploying it to production.
