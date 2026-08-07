---
title: "How to stop automatic redirect to latest case if a HR case has been transferred"
aliases:
  - KB0953711
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0953711
kb_number: KB0953711
last_modified: 2025-09-03
---

## How to stop automatic redirect to latest case if a HR case has been transferred

  

### Summary

This article will cover how, when reclassifying a HR case, to stop the automatic redirect which happens to bring the user to the latest HR case in the list of transfers that have occurred against said case. 

**Note****:** the method which will be discussed here requires customization against the _hr\_TransferCase_ Script Include, and is not supported by ServiceNow's technical support team.

### Instructions

It is a natural process Out of Box (OOB) via the _hr\_TransferCase_ Script Include that the instance should follow the chain of transfers of a HR case to the latest case (if it has been transferred at least once).

This process is controlled by the **_getLatestTransfer_** function within the aforementioned Script Include.  

Therefore, to halt this process from happening automatically, the **_getLatestTransfer_** function can be commented out. At the time of the creation of this article (Paris release, Patch 5), the function spans lines 277-284. If following this guide at a later patch number or family release, check within the _hr\_TransferCase_ Script Include to be sure the correct code is commented out.

On doing this, the automatic redirect will be stopped, but the user will still have the ability to click the banner message like the below, which has a link to the transferred\_to case:

![](sys_attachment.do?sys_id=a7718f07db16a0d0f77799ead3961995)
