---
title: "Router is not getting discovered when \"Network Device Exploration\" option disabled"
aliases:
  - KB0724906
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724906
kb_number: KB0724906
last_modified: 2024-04-07
---

## Router is not getting discovered when "Network Device Exploration" option disabled

  

### Issue

Router is not getting discovered when the "Network Device Exploration" option disabled.

Error in pattern logs:

 2019-01-13 23:03:53: Identification Engine: Discovery status is FAILURE, Identification sections in pattern failed: section: discovery, error: JAVASCRIPT\_CODE\_FAILURE: Caused by error in Ad hoc script 'EvalClosure-Insert physical\_interface\_count to cmdb\_ci\_ip\_router' at line 8   
5: var interfaceType;   
6: var physicalInterfaceTypesArray = physicalInterfaceTypes.split(",");   
7: var numOfPhysicalInterfaces = 0;   
\==> 8: for(var i = 0; i < routerExitInterfacesTable.size(); i++){   
9: routeMask = routerExitInterfacesTable.get(i).get("ipRouteMask");   
10: interfaceType = routerExitInterfacesTable.get(i).get("ifTypek");   
11: if(routeMask != "255.255.255.255" || physicalInterfaceTypesArray.indexOf(interfaceType) > -1){ 

### Release

All Versions.

### Cause

The "Network Device Exploration" tab is referencing a record in the table "discovery\_category\_device\_info".

https://<Instance\_Name>.service-now.com/nav\_to.do?uri=discovery\_category\_device\_info.do?sys\_id=91d41a39c3510200d8d4bea192d3aed5

Observe the list of Probes and Libraries.

![](sys_attachment.do?sys_id=83827fe0db8c70d0fec4fb24399619ed)

-   If probes are used for Network Discoveries, under SNMP Classifications for records like "Standard Network Switch" and "Standard Network Router", this would set  "Active = false" for the related probes in the "Triggers probes" related lists.
-   For Patterns, there is a Business Rule on this "discovery\_category\_device\_info" table called "Notify Mid about change". 
-   Patterns like "Network Router" and "Network Switch" do include calls to the libraries for probes like "SNMP - Routing" and "SNMP - Switching". 
-   Therefore, if this "Network Device Exploration" is set to false, this means that those steps will essentially not run when we run this Pattern. 

### Resolution

1.  Open below link:  https://<Instance\_name>/nav\_to.do?uri=%2Fdiscovery\_category\_device\_info\_list.do 
2.  Open "Network Device Exploration" 
3.  Under libraries -> Unlock and remove "SNMP - Routing". 
4.  Under probes -> Unlock and remove "SNMP - Routing". 
5.  Re-run the discovery with " "Network Device Exploration" option disabled.
