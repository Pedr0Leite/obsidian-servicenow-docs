---
title: "Metric Group missing for some IBM related License Metric"
aliases:
  - KB2789274
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2789274
kb_number: KB2789274
last_modified: 2026-02-25
---

## Issue

**Reason behind OOTB behavior**  
There are some License metric records which has the "Metric group" is empty for IBM  
\- Checked in OOTB:  
1\. Per Core (Physical Core)  
[https://instance\_name.service-now.com/nav\_to.do?uri=samp\_sw\_license\_metric.do?sys\_id=54e17c55932222…](https://instance_name.service-now.com/nav_to.do?uri=samp_sw_license_metric.do?sys_id=54e17c5593222200caef14f1b47ffb63 "https://instance_name.service-now.com/nav_to.do?uri=samp_sw_license_metric.do?sys_id=54e17c5593222200caef14f1b47ffb63")2\. Virtual server  
[https://instance\_name.service-now.com/nav\_to.do?uri=samp\_sw\_license\_metric.do?sys\_id=bbcf5e64686a19…](https://instance_name.service-now.com/nav_to.do?uri=samp_sw_license_metric.do?sys_id=bbcf5e64686a1910f877984ee67627c0 "https://instance_name.service-now.com/nav_to.do?uri=samp_sw_license_metric.do?sys_id=bbcf5e64686a1910f877984ee67627c0")

## Resolution

It is confirmed with the development team that this is **expected behaviour** and some records in license metrics that are **not supported yet**, added into the table for some IBM IASP use cases.

For now, the **IBM publisher pack** supports the following license metrics:

-   Authorized User
-   Authorized User Value Unit
-   Employee User Value Unit
-   External User Value Unit
-   Per Device
-   Per Named User
-   Per Processor
-   Per User
-   Processor Value Unit (PVU)
-   Resource Value Unit (RVU)
-   Virtual Processor Core (VPC)

The license metric which are supported OOTB will have metric group added to it. As of now, Per Core (Physical Core) and Virtual server are not supported OOTB for IBM.

## Additional Information

Below document gives you the supported license metrics for IBM:  
  
[https://www.servicenow.com/docs/r/it-asset-management/now-assist-for-software-asset-management-sam/ibm-publisher-pack.html](https://www.servicenow.com/docs/r/it-asset-management/now-assist-for-software-asset-management-sam/ibm-publisher-pack.html)
