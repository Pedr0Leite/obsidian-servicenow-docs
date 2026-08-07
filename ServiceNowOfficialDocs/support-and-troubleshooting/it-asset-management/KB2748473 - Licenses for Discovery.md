---
title: "Licenses for Discovery"
aliases:
  - KB2748473
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2748473
kb_number: KB2748473
last_modified: 2026-01-30
---

## Issue

In a situation where Discovery is used only as a supplementary source—primarily updating existing records rather than creating new ones—how is the licensing counted?

## Resolution

How the daily Discovery/Visibility CI count works   
In the daily count, ServiceNow evaluates CIs in the CMDB that are in the effective licensable classes and meet criteria such as:  
• Not marked as a duplicate (duplicate\_of is empty)  
• Most recent discovery is within the last 90 days (last\_discovered)  
• Discovery source is an allowed/licensable source (e.g., ServiceNow Discovery / Visibility and applicable Service Graph Connector sources)  
• Not in excluded statuses (for example, retired), plus other exclusion/deduplication rules depending on your version and CI type  
  
What this means for your "supplementary Discovery" scenario  
If Discovery scans a device and updates missing attributes on an existing CI, that CI can still be counted the same way as a newly created CI, as long as it falls into a licensable class and meets the criteria above (especially the "seen in last 90 days" and allowed source logic).  
Put simply: "update-only" usage is not automatically excluded — licensing is driven by which CIs are being discovered/managed by licensable sources and are in-scope at count time.  
  
Important nuance for EUC (laptops/monitors/etc.)  
Whether EUC devices are in-scope depends on the licensed categories / effective licensable CI classes in your subscription. The most reliable way to confirm is to review your instance's ITOM licensing metadata (license by CI types / ratios) and validate which CI classes are counted for Discovery/Visibility.  
  
How you can validate impact in your instance  
To see what's being counted:  
• Daily counts (raw daily numbers): ITOM License → License Daily Usage Count, use Aggregated = false (Aggregated = true is the rolling 90‑day average).  
• List of licensable CIs: ITOM License → Report ITOM Licensable CIs → select Discovery/Visibility → Populate licensable CIs → Show Licensable CIs.  
  
Compliance reporting note  
Official consumption is reported as a rolling 90‑day average of the daily counts. A short-term increase can influence the compliance value until it ages out of that 90‑day window.
