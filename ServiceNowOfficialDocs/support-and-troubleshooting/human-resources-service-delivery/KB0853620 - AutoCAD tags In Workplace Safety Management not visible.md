---
title: "AutoCAD tags In Workplace Safety Management not visible"
aliases:
  - KB0853620
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0853620
kb_number: KB0853620
last_modified: 2024-04-08
---

## Issue

The issue is that when a floor plan file ( .Dxf format) is uploaded to the “Upload Floor Plan” module in the Workplace Safety Management application, different layers in it can be seen but it is not possible to match the Tags to the spaces created, there is no data available in it.

## Resolution

This issue would occur if the room / space labels are defined as TEXT or MTEXT objects in the AutoCAD rather than as **block references**.  
  
\================================================  
Related documentation  
\================================================  
[https://docs.servicenow.com/csh?topicname=providing-your-workplace-data.html&version=latest](https://docs.servicenow.com/csh?topicname=providing-your-workplace-data.html&version=latest)  
  
From the documentation...  
  
Prior to uploading a .dxf file, work with your AutoCAD designers to ensure the following:  
The file uses block references and not single-line or multi-line text for space labels.  
The blocks attributes have human-understandable tags.  
The block references have attribute values appropriately set.  
Note: Using blocks is highly recommended. Do not use text objects.  
  
Please forward the information to the AutoCAD designer so that they can change the TEXT or MTEXT objects to block references.
