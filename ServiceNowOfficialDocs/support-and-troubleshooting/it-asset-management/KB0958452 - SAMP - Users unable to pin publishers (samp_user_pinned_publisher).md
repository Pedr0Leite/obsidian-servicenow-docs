---
title: "SAMP - Users unable to pin publishers (samp_user_pinned_publisher)"
aliases:
  - KB0958452
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0958452
kb_number: KB0958452
last_modified: 2024-03-01
---

## Issue

Identifying some inconsistency results when attempting to pin publishers (samp\_user\_pinned\_publisher) in license workbench.

The expectation is that clicking the pin icon next to a publisher name while in the license workbench will result in that publisher showing on the 'pinned publishers' tab of the license workbench. Which we are finding it this isn't the case. 

## Resolution

To resolve this is to rename the group to something other than 'global'.  
After that, cleanup the records from the pinned publisher table that points to this user group record  
  
Now you should see the pinning functionality work as expected.
