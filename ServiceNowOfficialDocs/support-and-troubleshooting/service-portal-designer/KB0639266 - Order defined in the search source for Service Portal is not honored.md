---
title: "Order defined in the search source for Service Portal is not honored"
aliases:
  - KB0639266
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0639266
kb_number: KB0639266
last_modified: 2025-06-10
---

## Order defined in the search source for Service Portal is not honored

  

### Issue

The Order field defined in the search source is not used to order the search results displayed in the TypeAhead search widget or Search Page widget. It is only used to sort the search source selection **Search Nav widget** in the search page as shown in the following image.

![](sys_attachment.do?sys_id=2dad83a147ca6a1077748d01426d43d5)

### Ordering the search based on relevancy

Service Portal search functionality is similar to the search inside the platform. To get more relevant search results, use document scoring. 

See these knowledge articles:

For document scoring: [Zing computes document scores using three components](https://docs.servicenow.com/csh?topicname=c_DocumentScoring.html&version=latest)

For Zing text search: [Set the relative weight of a field](https://docs.servicenow.com/csh?topicname=t_ControlMatchRelevanceByField.html&version=latest)

Add the **ts\_weight** attribute to the dictionary entry of the relevant field to display on the top. The maximum value given is 255. 

Re-index the table to display the changes.
