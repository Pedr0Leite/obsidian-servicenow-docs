---
title: "Lag in loading the Knowledge Base - Returns incorrect information "
aliases:
  - KB0752515
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752515
kb_number: KB0752515
last_modified: 2024-01-28
---

## Lag in loading the Knowledge Base - Returns incorrect information

  

### Issue

Incorrect Knowledge article Search results are showing up on a selection of categories and subcategories in knowledge page. When we select respective categories and subcategories with a time of 2 sec, it gives a correct result. Doing the same operation quickly gives incorrect incorrect Knowledge article Search results

### Cause

User customizes the system property which makes the query to run Async which results in the actual KB search result to get overridden.

### Resolution

1.  Check the Property on the 'glide.knowman.search.articles\_per\_page', it should not be customised
2.  Revert the property back to OOTB value which is 20
3.  After that query will be processed quickly and synchronously.   
      
    For more details please find the below document:   
    [Knowledge properties](https://docs.servicenow.com/csh?topicname=r_KnowledgeProperties.html&version=latest "Knowledge properties")
