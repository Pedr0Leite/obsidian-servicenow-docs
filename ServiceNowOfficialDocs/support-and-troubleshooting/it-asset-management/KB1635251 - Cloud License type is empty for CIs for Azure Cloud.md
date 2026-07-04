---
title: "\"Cloud License type\" is empty for CIs for Azure Cloud"
aliases:
  - KB1635251
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1635251
kb_number: KB1635251
last_modified: 2025-11-07
---

## "Cloud License type" is empty for CIs for Azure Cloud

  

### Issue

Issue:“Cloud License type” is empty for few CIs on the Global Instance on cmdb\_sam\_sw\_install\_list table  
  

### Release

all

### Resolution

For the Cloud License type to be updated below are conditions, please verify:  
1\. VM should have a cmdb\_key\_value record with the values as below .  
For windows key = Windows\_OS\_License\_Type\_automatic  
value = BYOL or License Included

2\. "Virtualized by::Virtualizes" relationships should be present between the VM and the actual OS CI.

Please verify above conditions for the CIs with empty "Cloud License type"
