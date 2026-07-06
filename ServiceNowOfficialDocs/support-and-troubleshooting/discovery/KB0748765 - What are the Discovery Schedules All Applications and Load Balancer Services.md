---
title: "What are the Discovery Schedules \"All Applications\" and \"Load Balancer Services\""
aliases:
  - KB0748765
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748765
kb_number: KB0748765
last_modified: 2024-04-07
---

## What are the Discovery Schedules "All Applications" and "Load Balancer Services"

  

### Issue

# Overview

Usually Discovery Schedules are created and configured by users. However there are two Discovery Schedules that may be created on OOTB instance:

1.  All Applications
2.  Load Balancer Services

These two Discovery Schedules are OOTB and come with Service Mapping plugin. They were introduced since Jakarta version.  
  
They can be used to routinely discover/refresh business applications and services for Service Mapping. 

# Impact 

By default, they are set as inactive since Kingston version and can be activated by users. There is no impact if you disable them or don't use them.
