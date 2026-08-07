---
title: "The asset is excluded from licensed hardware asset features."
aliases:
  - KB2660728
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2660728
kb_number: KB2660728
last_modified: 2025-12-01
---

## The asset is excluded from licensed hardware asset features.

  

### Issue

A message stating 'The asset is excluded from licensed hardware asset features.' appears when opening a Hardware Asset \[alm\_hardware\] record that is excluded from HAM.

<excluded\_from\_ham>true</excluded\_from\_ham>

### Release

This is not release specific.

### Cause

1\. The message appears because the Hardware Asset is excluded from HAM by the value of the exclude\_from\_ham field.  
2\. The field may have been set to true by a user or the opt-in status of the HAM category.

### Resolution

1\. Verify the category opt-in status in the HAM Resource Category list and opt-in, if not yet. The Opt-in jobs will execute, after which the message will no longer appear, and the CI will be available for HAM features.

https://instance.service-now.com/sn\_hamp\_resource\_category\_list.do

2\. If the category is opt-in already, the field can be directly updated to remove the exclusion.
