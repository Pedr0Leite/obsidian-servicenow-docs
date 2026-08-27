---
title: "Hardware Asset Licensing Counts Not Updating in HAM Pro"
aliases:
  - KB2436678
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2436678
kb_number: KB2436678
last_modified: 2025-08-19
---

## Hardware Asset Licensing Counts Not Updating in HAM Pro

  

### Issue

After registering hardware assets, the HAM Pro licensing usage count is not being updated on the ITAM Licensing Resource Counts (itam\_licensing\_resource\_counts\_list). 

### Symptoms

This issue occurs in production instance.

### Facts

Hardware assets belonging to a category that you don't opt in are excluded by default. 

### Release

All

### Resolution

1\. Opt-in the necessary resource categories for licensing count in the production instance. This can be done by navigating to the resource category list(sn\_hamp\_resource\_category\_list) and selecting the desired categories. 

2\. After opting-in the categories, manually run the HAM - Populate Licensing Data job to update the licensing counts.

3\. Verify that the licensing counts have been updated correctly on the ITAM Licensing Resource Counts (itam\_licensing\_resource\_counts\_list).   
  

### Related Links

[Opt-in or opt-out of HAM license resource categories](https://www.servicenow.com/docs/bundle/yokohama-it-asset-management/page/product/hardware-asset-management/task/optin-optout-ham-license-resource-categories.html "Opt-in or opt-out of HAM license resource categories")
