---
title: "Multiple Node Events caused by discovery jobs \"Sensor error: Transaction cancelled: maximum execution time exceeded\""
aliases:
  - KB0782955
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782955
kb_number: KB0782955
last_modified: 2026-03-06
---

## Issue

Large amounts of data being collected in serial causing Multiple Node Events to be reported. 

## Resolution

Enable parallel processing.  
1) Navigate to sys\_properties.list  
2) Search for the property : glide.discovery.multi\_page\_serial\_mode  
3) Set the value to false  
  

## Additional Information

Discovery - Multipage Sensors
