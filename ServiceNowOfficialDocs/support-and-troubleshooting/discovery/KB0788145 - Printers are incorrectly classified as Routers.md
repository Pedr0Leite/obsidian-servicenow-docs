---
title: "Printers are incorrectly classified as Routers"
aliases:
  - KB0788145
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788145
kb_number: KB0788145
last_modified: 2025-01-16
---

## Issue

You will see devices that show they are Printers based on their SNMP - Classify Input Payload but are incorrectly classified as Routers, causing discovery to fail.  
  

## Resolution

You will want to set the "**Standard Network Router"** Classifier to not Classify devices if they meet a certain condition that applies to ONLY your Printers. 

In this example, all printers that contain **SL-M2870FW** (the Model Number) in the sysDescr section of the SNMP - Classify Input payload will not be classified as routers.

This will stop the device from being classified as a Router and successfully discovered as a Printer.

![](/sys_attachment.do?sys_id=75a93b691b950950d018c8ca234bcbc0)
