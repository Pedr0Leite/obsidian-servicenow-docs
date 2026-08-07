---
title: "Hardware Asset Refresh - how to determine if an asset is eligible for refresh"
aliases:
  - KB0962364
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0962364
kb_number: KB0962364
last_modified: 2025-01-02
---

## Hardware Asset Refresh - how to determine if an asset is eligible for refresh

  

### Summary

After activating the Hardware Asset Management plugin, we can see that in alm\_hardware, a new column eligible\_for\_refresh is added.  
This can be used to filter hardware assets you would like to refresh. For more information, see documentation: [Request a Hardware Asset Refresh](https://docs.servicenow.com/bundle/quebec-it-asset-management/page/product/hardware-asset-management/task/hardware-asset-refresh.html "Request a Hardware Asset Refresh")  

How does the logic fill in this value?

-   The logic to calculate eligibility for refresh is handled by the scheduled job "SAM - Calculate Asset Refresh Eligibility"
-   The job will call script include SAMRefreshEligibityCalculator
