---
title: "Service Mapping: \"Error on server request getServiceTreeData. Unknown error.\" occurs when viewing a Business Service map"
aliases:
  - KB0683861
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0683861
kb_number: KB0683861
last_modified: 2024-04-07
---

## Service Mapping: "Error on server request getServiceTreeData. Unknown error." occurs when viewing a Business Service map

  

### Issue

Service Mapping: "Error on server request getServiceTreeData. Unknown error." occurs when viewing a Business Service map

  
  

# Overview

* * *

The error "Error on server request getServiceTreeData. Unknown error." occurs when viewing a Business Service map.

# Root Cause

* * *

The "All" group is missing from cmdb\_ci\_service\_group. The "All" service group is a default group added by Service Mapping. This group is required in order for the service tree to appear on the map because it is by default the root of all groups.

# Solution

* * *

Restore the missing cmdb\_ci\_service\_group record.
