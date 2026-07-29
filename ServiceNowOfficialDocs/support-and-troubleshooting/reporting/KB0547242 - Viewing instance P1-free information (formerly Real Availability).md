---
title: "Viewing instance P1-free information (formerly Real Availability)"
aliases:
  - KB0547242
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547242
kb_number: KB0547242
last_modified: 2025-08-04
---

## Viewing instance P1-free information (formerly Real Availability)

  

### Issue

ServiceNow customers and partners can use [Now Support's Instances Dashboard](https://support.servicenow.com/now?id=ns_manage_instances "Now Support's Instances Dashboard") to view the P1-free information for all their instances.

**P1-free** refers to the calculated percentage of production time when an instance is free of Priority 1 (Severe) issues—specifically, the percentage of time that an instance did not have a P1 case opened against it. Note that not all P1s are outages, so P1-Free does not represent instance availability.  

It is not possible for ServiceNow to provide standard availability reporting. Because our product is so customizable, there are too many variables as to why the service might be considered unavailable. Some of these might be within a customer's infrastructure or fall outside ServiceNow's responsibilities. The P1-Free dashboard provides information based on P1 history and is a great place to begin investigations into any outages that occurred over a given period of time. 

### Release

All releases

### Resolution

### Using the Instance Dashboard to view P1-free information

ServiceNow customers and partners can view data about their production and non-production instances from the Instances Dashboard on Now Support.

1.  Sign in to [https://support.servicenow.com/now](https://support.servicenow.com/now "https://support.servicenow.com/now")  
    -   \[**Partners only**\] To view a customer company, switch companies by clicking your name in the top-right.
2.  Click **Instances** in the top level navigation.
3.  Select **Instances Dashboard** in the drop-down menu.
4.  In the Instances Dashboard, click on the name of the instance you would like to see P1 information for in the "Instance name" column.
5.  Switch the **P1-Free** tab.  
      
    ![](/sys_attachment.do?sys_id=cd3079dd93953d107214b25d6cba1087 "Screenshot P1-Free 1.png")  
      
    

### Viewing P1-Free case history details

Scroll down on the P1-Free dashboard to see a calendar view of your P1-free case history. By default, the dashboard will show you information from the last 90 days. Different colors indicate the performance impact your instance sustains during a specific date on the calendar. Date ranges for P1-free case history include:

-   90 days
-   120 days
-   180 days
-   Custom range

Select a custom date range to view information from a specific time period.

![](/sys_attachment.do?sys_id=64507d1193d53d107214b25d6cba10e9 "Screenshot P1-Free 2.png")

**Note:** 12 months of data may be visualized and exported at any time. Additionally, data is only accurate to January 1, 2014 and is not recommended to view P1 case history prior to that time.
