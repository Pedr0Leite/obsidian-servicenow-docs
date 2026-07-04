---
title: "Assessment not displaying Source name in portal when there is only source in the assessment instance"
aliases:
  - KB0818535
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818535
kb_number: KB0818535
last_modified: 2024-04-08
---

## Assessment not displaying Source name in portal when there is only source in the assessment instance

  

### Issue

Assessment not displaying Source name in portal when there is only source in the assessment instance

### Release

NewYork

### Cause

For the 'Assessment metric type' the field 'Pagination setting for service portal view' is set as 'none'

### Resolution

  
For the 'Assessment metric type' the field 'Pagination setting for service portal view' is set as 'none' and therefore the name of the source (assessable record) is not shown.

  
The name will be visible if the value is changed to either 'question' or 'category'
