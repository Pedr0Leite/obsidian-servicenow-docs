---
title: "How to enable Cloud Cost Management Workspace show spend data for last 12 months"
aliases:
  - KB2007248
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2007248
kb_number: KB2007248
last_modified: 2025-03-26
---

## How to enable Cloud Cost Management Workspace show spend data for last 12 months

  

### Issue

The customer needs help pulling in 12 months worth of cloud billing data into a customer instance. Dashboard graph currently have 6 months spend but need to expand to 12 months.

### Release

Washington DC and above

### Resolution

Out of Box Cloud Cost Management allow to download only past 6 months of billing data. There a  property below with it's type of integer, default value is 6 and cannot be more than 24.

To update data for more months follow step: 

1.   Update the system property 'sn\_cld\_intg\_core.number\_of\_months\_to\_lookback' with the value 12 to enable billing download for past 12 months  
    2\. Trigger billing download for the required months

![](/sys_attachment.do?sys_id=fbea6e6497a0aa14f03d739c1253af75)
