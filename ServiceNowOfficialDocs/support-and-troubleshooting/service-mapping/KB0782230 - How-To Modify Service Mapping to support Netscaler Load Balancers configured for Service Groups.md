---
title: "How-To: Modify Service Mapping to support Netscaler Load Balancers configured for Service Groups"
aliases:
  - KB0782230
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782230
kb_number: KB0782230
last_modified: 2024-04-08
---

## How-To: Modify Service Mapping to support Netscaler Load Balancers configured for Service Groups

  

### Issue

This article details how to modify Patterns/Service Mapping in order to support Top-Down Discovery with Netscalers that utilize Service Groups (multiple IPs per Load Balancer service, instead of a single IP), which is currently unsupported.

NOTE: Dependent on Pattern fixes in PRB1360774

### Release

All, as of NYP1

### Cause

Currently the Netscaler SSH pattern doesn't properly gather multiple IP addresses for cmdb\_ci\_lb\_pool records to match the configured Service Group IP information on the Netscaler end. As a result, VIPs are not able to be properly correlated to cmdb\_ci\_lb\_service records which reference back to the Netscaler CI record in Service Mapping.

Additionally, Service Mapping does not search on any other tables (only cmdb\_ci\_lb\_service and LB CI records) to match VIPs to Load Balancers.

### Resolution

PRB1360774 contains the Pattern fixes to properly gather the IP information in cmdb\_ci\_lb\_pool and cmdb\_ci\_lb\_pool\_member records

We can utilize the DiscoveryHostUtils script include to workaround the Service Mapping component and search on these additional tables and return the proper Load Balancer CI record. Modify the "findHostByIp" function in "DiscoveryHostUtils" as follows:

findHostByIp : function(ip){  
  
// Check for IP matches manually on cmdb\_ci\_lb\_pool, and cmdb\_ci\_lb\_pool\_members to support Service Groups configuration  
var grLbP = new GlideRecord("cmdb\_ci\_lb\_pool");  
grLbP.addQuery("ip\_address","=",ip);  
grLbP.query();  
  
while (grLbP.next()) {  
if (grLbP.load\_balancer.operational\_status == "1")  
return grLbP.load\_balancer;  
}  
  
var grLbPM = new GlideRecord("cmdb\_ci\_lb\_pool\_member");  
grLbPM.addQuery("ip\_address","=",ip);  
grLbPM.query();  
  
while (grLbPM.next()) {  
if (grLbPM.load\_balancer.operational\_status == "1")  
return grLbPM.load\_balancer;  
}  
  
  
return null;  
},
