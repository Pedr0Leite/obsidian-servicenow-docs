---
title: "HRSD Now Assist - Case Summarization "
aliases:
  - KB2775239
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2775239
kb_number: KB2775239
last_modified: 2026-04-13
---

## Issue

HRSD case summarization no longer displaying on a HR case on UI 16. where the option to summarize a case is missing at the top of the form after upgrade to Zurich. The problem was confirmed for HR Admin and User across case states (New, Work in Progress, Resolved).  
  

## Resolution

**Steps to Resolve**  
1\. Ensure the related plugins 'Platform AI Agents and Skills' \[sn\_uxc\_gen\_ai\] and 'Now Assist for HR Service Delivery (HRSD)' \[sn\_hr\_gen\_ai\] are compatible with the instance version, in this case Zurich Patch5  
2\. Repair or upgrade the plugins to the latest compatible versions using the Now Assist Suite application update mechanism to ensure compatibility of all Now Assist apps.   
3\. Verify the resolution by checking HR cases in the instance after.
