---
title: "Unable to match value '' with field 'norm_product' in table 'samp_sw_usage'. Expecting type 'reference"
aliases:
  - KB1700885
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1700885
kb_number: KB1700885
last_modified: 2026-02-02
---

## Issue

The SAM - Collect Microsoft 365 Usage scheduled job run failed  
  
We see below error in system logs:   
Unable to match value '' with field 'norm\_product' in table 'samp\_sw\_usage'. Expecting type 'reference'

## Resolution

To resolve this issue, please remove and re-add the discovery map (same values) in the below software model for Microsoft 365 in below list where child is empty  
https://<instance>.service-now.com/cmdb\_m2m\_suite\_model\_list.do?sysparm\_query=suite\_child.productISEMPTY
