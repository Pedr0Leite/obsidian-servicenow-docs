---
title: "VMware Metric Group getting replaced by 'Common"
aliases:
  - KB2631559
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2631559
kb_number: KB2631559
last_modified: 2026-05-21
---

## VMware Metric Group getting replaced by 'Common'

  

### Issue

While importing entitlements using excel template using OOTB metric group 'Vmware'. Once the template was uploaded, the entitlements were processed but the Metric Group value is getting  replaced by 'Common'. 

### Symptoms

Although the "PPN" exists with the Metricgroup "VMware", it is getting updated as "Common" after upload and no errors were seen

### Release

Yokohama 

### Cause

In general the metric group gets mapped to "common" when there is no entry for the provided metric group in " Metric group cache "

### Resolution

Seems the Metric group is case sensitive.  
  
In the metric group cache i see the name as "VMware",but in the import  if we  specify it as "Vmware"(m is small). So it is not finding that in the "samp\_sw\_metric\_group" cache and reverting back to common.

  
[https://<instance>.service-now.com/samp\_sw\_metric\_group\_list.do?sysparm\_clear\_stack=true](https://instance.service-now.com/samp_sw_metric_group_list.do?sysparm_clear_stack=true)  
  
Please give the metric group same as the one present in the "samp\_sw\_metric\_group"

  
  

### Related Links

Software license metrics   
https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/concept/c\_SAMLicenseMetrics.html
