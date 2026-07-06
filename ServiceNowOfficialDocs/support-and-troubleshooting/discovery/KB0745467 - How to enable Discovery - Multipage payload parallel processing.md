---
title: "How to enable Discovery - Multipage payload parallel processing"
aliases:
  - KB0745467
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745467
kb_number: KB0745467
last_modified: 2024-04-07
---

## Issue

# Description

1) In the Discovery schedules involving large routers and switches, we will observe that the payloads are processed by the Discovery - Multipage Sensors.

2) Due to Serial Processing of multiple payload pages, the worker nodes will be in use for a long amount of time.

3) In the case where we have multiple scheduled discoveries, it is a possibility that all the workers will be in use, thereby causing performance issues.

4) This article will provide information on how to enable multipage payload parallel processing in order to avoid the above mentioned issues

# Procedure

1) Navigate to sys\_properties Table

2) Search for the property : **glide.discovery.multi\_page\_serial\_mode**

3) If the property is present, set the value to false.  

4) Otherwise, add the property and set the value to false

# Applicable Versions

Kp11, London patch 3, Madrid
