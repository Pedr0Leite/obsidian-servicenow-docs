---
title: "Service Mapping issue - Update Application Service Failed"
aliases:
  - KB0715364
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715364
kb_number: KB0715364
last_modified: 2024-04-07
---

## Service Mapping issue - Update Application Service Failed

  

### Issue

# Symptoms

* * *

Unable to add an EntryPoint to a Business Service.  You will receive "Update application service failed" message when this error occurs. 

# Release

* * *

All

# Cause

* * *

This is cause by the discovery\_source choice list for Service-now, ServiceNow, and ServiceWatch are being set as inactive as true.

# Resolution

* * *

1.  Go to Choice List in the "Filter Navigator" 
2.  Element is discovery\_source
3.  Check to see if ServiceWatch, ServiceNow, and Service-now Value exist
4.  Check to see if Inactive is set to false for those Value
