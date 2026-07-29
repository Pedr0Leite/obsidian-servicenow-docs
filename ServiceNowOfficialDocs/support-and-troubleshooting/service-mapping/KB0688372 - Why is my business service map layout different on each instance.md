---
title: "Why is my business service map layout different on each instance?"
aliases:
  - KB0688372
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688372
kb_number: KB0688372
last_modified: 2024-04-07
---

## Why is my business service map layout different on each instance?

  

### Issue

It may be noticed that a business service maps does not have the CIs arranged in the same order when compared between production and development instances. The layout may differ from instance to instance.

### Cause

This behavior is expected. The nodes of a business service map are sorted by their corresponding CI sys\_ids before the map is rendered. Therefore, every time a user views a map in the structure will remain more or less constant in the same environment. However, the order of the nodes will not be the same across different instances, as the nodes are sorted by sys\_ids and sys\_ids will not be the same across different environments.
