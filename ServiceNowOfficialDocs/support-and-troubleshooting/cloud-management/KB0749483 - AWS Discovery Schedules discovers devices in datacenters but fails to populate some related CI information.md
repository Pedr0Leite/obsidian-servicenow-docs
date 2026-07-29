---
title: "AWS Discovery Schedules discovers devices in datacenters but fails to populate some related CI information"
aliases:
  - KB0749483
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749483
kb_number: KB0749483
last_modified: 2024-04-07
---

## AWS Discovery Schedules discovers devices in datacenters but fails to populate some related CI information

  

### Issue

# Symptoms

AWS Datacenter.Discover.AWS Datacenter.Compute Interface.ListImages -- Error

AWS Discovery Schedules discovers devices in data centers but fails to populate some related CI information

CAPI Trail Log while processing cloud API response data shows - " **identification\_engine : MULTIPLE\_DEPENDENCIES Found multiple dependent relation items \[{"parent":97,"child":1,"type":"Hosted on::Hosts"}\] and \[{"parent":97,"child":0,"type":"Hosted on::Hosts"}\] in payload: no thrown error** "

# Release

Kingston, London

# Cause

\- Based on the error, check the input payload to the identification engine you can figure that there is a CMDB metadata hosting rule record relating cmdb\_ci\_cloud\_service\_account to the discovered cloud resource image type 'cmdb\_ci\_os\_template' which results in the existence of 2 hosting rules between 1 cloud resource - 'cmdb\_ci\_os\_template' with cmdb\_ci\_logical\_datacenter & cmdb\_ci\_cloud\_service\_account. Hence the error

\- The above example issue is pertaining to ListImages but similarly, you may find it useful in other cases

**![](/sys_attachment.do?sys_id=998c24aedb42b450e515c223059619ec)**

# Resolution

\- Delete the hosting rule record relating cmdb\_ci\_cloud\_service\_account to the discovered cloud resource image type 'cmdb\_ci\_os\_template' ( Image )
