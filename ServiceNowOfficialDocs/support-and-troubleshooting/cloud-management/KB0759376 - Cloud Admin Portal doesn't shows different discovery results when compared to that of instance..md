---
title: "Cloud Admin Portal doesn't shows different discovery results when compared to that of instance."
aliases:
  - KB0759376
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759376
kb_number: KB0759376
last_modified: 2024-04-07
---

## Cloud Admin Portal doesn't shows different discovery results when compared to that of instance.

  

### Issue

Load balancer count shows different in Cloud Admin Portal when compared to that of Instance.

In instance, it shows as below:

![](sys_attachment.do?sys_id=006dc434db48b0d0fec4fb243996195a)

  

Whereas in Cloud Admin Portal, for the same Logical Datacenter and same Service Account, it shows different results:

![](sys_attachment.do?sys_id=446dc434db48b0d0fec4fb243996195c)

### Cause

The cause of this issue is because of the way Admin Portal queries for the resources for cloud service account.

It only queries and shows Load Balancers which are active\[Admin Portal -->Manage-->Cloud Account\].

If load balancer operational status is Retired/non-operational and Status is Retired, they will be ignored.

Navigate to the table cmdb\_ci\_cloud\_load\_balancer and check if load balancers with the following condition are visible.

Operational Status : Operational and Status : Installed

### Resolution

-   Check, why the Load Balancer's Operational Status is not "Operational" and /or Status is not "Installed". Business rules are the first place to start with.
-   Both of these conditions should be met for the Load Balancers to show up in Admin Portal.
-   This expected behavior and can't be changed. 
-   Please check why the Load Balancers' Operation Status and/or Status are getting changed.
