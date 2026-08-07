---
title: "CMDB Identification Error: In payload invalid data source [Manual Entry] exist"
aliases:
  - KB0720501
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720501
kb_number: KB0720501
last_modified: 2025-04-08
---

## Issue

# Symptoms

* * *

CMDB Identification Error: In payload invalid data source \[Manual Entry\] exist 

# Release

* * *

ALL

# Cause

* * *

The Dictionary Entry (Discovery Source), doesn't have Manual Entry in Choices 

# Resolution

* * *

Go to Dictionary table: sys\_dictionary and look for dictionary record using these details:

Table = cmdb\_ci

Column name = discovery\_Source

Open this record and add Manual Entry in Choices related list, like shown in the screenshot: 

![](/sys_attachment.do?sys_id=7e296caedb02b450e515c223059619a1) 

  

NOTE: You might see different source instead of "Manual Entry" so you need to replace the one with that. Also make sure that data source is valid one.

#
