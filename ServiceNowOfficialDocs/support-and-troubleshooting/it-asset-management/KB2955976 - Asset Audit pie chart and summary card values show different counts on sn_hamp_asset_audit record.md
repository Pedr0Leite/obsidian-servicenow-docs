---
title: "Asset Audit pie chart and summary card values show different  counts on sn_hamp_asset_audit record"
aliases:
  - KB2955976
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2955976
kb_number: KB2955976
last_modified: 2026-04-14
---

## Asset Audit pie chart and summary card values show different counts on sn\_hamp\_asset\_audit record

  

### Summary

On a Hardware Asset Management (HAMP) Asset Audit record (sn\_hamp\_asset\_audit), the pie chart "Asset Audit Results by Asset Status" displays different totals than the summary card fields (Scanned and expected, Scanned and not expected, Expected and not found, New). The pie chart typically shows LOWER values than the summary cards. The discrepancy appears after the audit scan has completed and persists permanently.  
  
Example: Summary cards: Expected=111, Not Expected=29, Not Found=55, New=0 (Total=195) Pie chart: Expected=109, Not Expected=29, Not Found=54 (Total=192)  
  
  
Cause:   
The summary card values and the pie chart use different data retrieval strategies:   
  
\[-\] Summary cards:   
Read from precalculated integer fields on the sn\_hamp\_asset\_audit record. These values are calculated ONCE at the end of the audit scan by the  action item "Audit Scan" on sn\_hamp\_m2m\_audit\_asset. After the scan completes, these fields are never recalculated. 

`https://<instance-name>.service-now.com/sys_sg_write_back_action_item.do?sys_id=6741f2b501521110fa9b7e90b0a15329      at line 288`

  
\[-\] Pie chart:   
Runs a LIVE COUNT query against sn\_hamp\_m2m\_audit\_asset grouped by audit\_status on every form load 

`https://<instance-name>.service-now.com/`sys\_report.do?sys\_id=049544d651130010fa9bb8302cc1b43f  
  
The discrepancy occurs when sn\_hamp\_m2m\_audit\_asset records are modified AFTER the scan completes. The most common cause is like asset deletion: the asset field on sn\_hamp\_m2m\_audit\_asset has reference\_cascade\_rule="delete", so deleting an alm\_asset record (e.g., retiring or decommissioning an asset) automatically removes the corresponding m2m record. The pie chart reflects this removal immediately, but the summary card fields remain at their original populated values.
