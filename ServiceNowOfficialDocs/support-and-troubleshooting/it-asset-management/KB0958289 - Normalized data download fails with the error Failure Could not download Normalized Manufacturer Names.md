---
title: "Normalized data download fails with the error \"Failure Could not download Normalized Manufacturer Names\""
aliases:
  - KB0958289
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0958289
kb_number: KB0958289
last_modified: 2026-05-18
---

## Issue

-   Navigate >> User Administration >> Normalization Data Services >> Guided setup.
-   In Step. Download Normalized Data, click Configure, and select "Start Download"  
    
    The download fails with error "Could not download Normalized Manufacturer Names"
    
    ![](/sys_attachment.do?sys_id=0733cc9897924ed8f03d739c1253af65)

## Resolution

If customer's instance is an on-prem instance, skip step 1 below.

1.  Find the customer's instance record in the following Instance table on HI: [https://support.servicenow.com/cmdb\_ci\_service\_list.do](https://support.servicenow.com/cmdb_ci_service_list.do). Copy down the following fields for that record:
    
    -   Instance name
    -   Instance ID
    -   Type/Purpose
2.  On the affected instance, run the following background script and copy the result:  
    `//////////////////////////////////////////////////   ``gs.print(GlideProperties.get("glide.cmdb.canonical.url"));`  
    `gs.print(GlideProperties.get("instance_name"));   ``gs.print(GlideProperties.get("instance_id"));   ``gs.print(GlideProperties.get("sn_apprepo.credential"));   ``//////////////////////////////////////////////////`
    
3.  Confirm whether the affected instance is:
    -   Prod or Subprod
    -   Regulated Market instance
4.  Create a task for "Dev-Platform Async" team and provide details/results from above steps.
