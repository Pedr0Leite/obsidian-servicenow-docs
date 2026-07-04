---
title: "\"Marking an article as helpful\" information does not get carried over to the newer versions of the article on portal."
aliases:
  - KB0820165
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820165
kb_number: KB0820165
last_modified: 2024-04-08
---

## "Marking an article as helpful" information does not get carried over to the newer versions of the article on portal.

  

### Issue

In the hrpotal, employees have the option to mark knowledge articles as being helpful or not. When the corresponding knowledge articles are visited, it will show the percentage of feedback However, if the article is being checked-out and new version being published, this information no more appears against the article which is a loss of valuable information. How to fix this?

### Resolution

Cause of this issue was usage of custom widget for showing knowledge Article helpful details.  
Using **OOB** widget `"Knowledge Article Helpful"` fixed the issue.
