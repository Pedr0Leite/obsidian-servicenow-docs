---
title: "EMC Isilon discovery pattern fails with error \"java.lang.String cannot be cast to java.util.List\" when device is not configured with smb shares"
aliases:
  - KB0725195
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725195
kb_number: KB0725195
last_modified: 2024-04-07
---

## Issue

# Cause

* * *

At step "adding zone name to smb shares", the transform table operation will fail with the below error if the smb shares are not configured on the device.

java.lang.String cannot be cast to java.util.List

If the device is not configured with smb shares, the smb\_shares variable retain to be string rather than an array and hence the transform table operation fails.  

# Resolution

* * *

The attached script is a customization to the pattern where a check is made to see if the $smb\_shares variable in step 70 is an array or string before we perform a transform table operation on it.
