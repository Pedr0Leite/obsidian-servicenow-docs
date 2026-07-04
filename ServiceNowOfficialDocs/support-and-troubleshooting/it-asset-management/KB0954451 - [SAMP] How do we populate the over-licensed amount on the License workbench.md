---
title: "[SAMP] How do we populate the over-licensed amount on the License workbench"
aliases:
  - KB0954451
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0954451
kb_number: KB0954451
last_modified: 2025-01-03
---

## \[SAMP\] How do we populate the over-licensed amount on the License workbench

  

### Summary

This KB will explain how do we populate the [Over-licensed amount](https://docs.servicenow.com/bundle/paris-it-asset-management/page/product/software-asset-management2/concept/c_SAMDashboard.html "Over-licensed amount") in SAMP reconciliation.

### Release

Jakarta ++

### Instructions

-   The Over-licensed amount on the License Workbench is populated from the values from the License Metric Result.
-   The column (over\_licensed\_amount) is calculated as below:

**Over Licensed Amount = Number of Unused Rights (Rights Available) \* Average Price**

Both these column are available on the License Metric result table (samp\_license\_metric\_result). You can navigate to the related ones as below:

Recon Result >> Product Result >> Software Model Result >> License Metric Result.

  

  

### Related Links

[Software Asset Management dashboard](https://docs.servicenow.com/bundle/paris-it-asset-management/page/product/software-asset-management2/concept/c_SAMDashboard.html "Software Asset Management dashboard")
