---
title: "Duplicate entries in the table \"dscy_route_next_hop\" from Discovery"
aliases:
  - KB0721350
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721350
kb_number: KB0721350
last_modified: 2025-07-15
---

## Duplicate entries in the table "dscy\_route\_next\_hop" from Discovery

  

### Issue

The **dscy\_route\_next\_hop** table is updated by Discovery with duplicate records.

### Facts

Next hop is an IP address entry in a router's routing table, which specifies the next closest/most optimal router in its routing path. Every single router maintains its routing table with a next hop address, which is calculated based on the routing protocol used and its associated metric.

This image represents the table structure of "**dscy\_route\_next\_ho**p" in ServiceNow configuration management database (CMDB).

                   ![dscy\_route\_next\_hop table overview](sys_attachment.do?sys_id=a3382bb893fa6210c2513f986cba106a)

This table data is used for mapping L2/3 relationships in the CMDB.

### Release

All

### Cause

Probes & Patterns can both populate this table depending on your environment. 

### Resolution

## In the "Standard Network Router" classification probe you can disable the "SNMP - Routing":

1.  In order to stop creating duplicate records in this table, We can disable the line in the respective sensor.
2.  Go to script includes -> DiscoveryReconciler.

                   https://instance.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=4fa2ef960a0a0ba500d0ac5d968efa2d

           3. In the script go to line 189 and comment the line with "**//**".  This will restrict the writing of records on the table **dscy\_route\_next\_hop**.

                                  ![Editing the Script Include DiscoveryReconciler](sys_attachment.do?sys_id=e738afb893fa6210c2513f986cba1028)

## The following Patterns could also be altered by following these steps:

-   Disable the step : In "Network Switch" and "Network Router" patterns, disable "SNMP - Routing" library step and "Save with Libraries"
-   In "Windows OS - Servers and Linux Server" pattern, disable "Insert route gateways to dscy\_route\_next\_hop" step and "Save with Libraries"
    -   Insert route gateways IPv4 to dscy\_route\_next\_hop
    -   Insert route gateways IPv6 to dscy\_route\_next\_hop

  
note: Updating either of these will impact the relationships especially level 2 and level 3 relationships that depends on the dscy\_route\_next\_hop.
