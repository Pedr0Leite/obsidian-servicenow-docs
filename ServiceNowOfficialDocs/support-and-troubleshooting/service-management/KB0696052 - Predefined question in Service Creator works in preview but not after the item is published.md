---
title: "Predefined question in Service Creator works in preview but not after the item is published"
aliases:
  - KB0696052
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696052
kb_number: KB0696052
last_modified: 2024-04-07
---

## Predefined question in Service Creator works in preview but not after the item is published

  

### Issue

Predefined question in Service Creator works in preview, but not after item is published

  

#   

### Cause

Single Quotes in the reference qualifier.

### Resolution

The predefined question has a reference qualifier, 

u\_store\_status='O' 

  

Notice that the value is mentioned in single quotes (''). The value should not be within the quotes and this caused the issue. 

Instead, simply use u\_store\_status=O^EQ 

  

EQ specifies the End. 

  

Please refer to the section "Advance Reference Qualifier" in this link for more details on reference qualifier, 

[https://docs.servicenow.com/csh?topicname=c\_ReferenceQualifiers.html&version=latest](https://docs.servicenow.com/csh?topicname=c_ReferenceQualifiers.html&version=latest)
