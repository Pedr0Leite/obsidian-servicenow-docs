---
title: "Service Portal: How to handle performance degradation in a Knowledge Category containing large number of articles"
aliases:
  - KB0639109
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0639109
kb_number: KB0639109
last_modified: 2025-05-21
---

## Service Portal: How to handle performance degradation in a Knowledge Category containing large number of articles

  

### Issue

Performance degradation occurs in a Knowledge Category that contains a large number of articles.  

### Cause

In Service Portal, performance degradation can occur when a knowledge category contains a large number of articles in the **kb\_category** page. This occurs because this page loads all the articles at once, not on demand, and there is no way out of the box (OOB) to control this behavior. Here are some ways to work around it.

Problem Ticket PRB1194786 has already been raised to load the articles on demand.

### Resolution

#### Solution 1: Limit the number of articles

Limiting the number articles loaded on to the page, during testing 250 articles load on to the page in less than a second. Follow these steps:

1.  Navigate to **Service Portal > Widgets** 
2.  Search for **KB Category Page** widget. This is the widget that loads the articles. 
3.  Clone the widget 
4.  Modify the piece of code in the newly cloned widget: 
    -   **Server Script** Modify line number 14 from  
        data.items = $sp.getKBCategoryArticleSummaries(data.category, 0, 250);   
        To   
        data.items = $sp.getKBCategoryArticleSummaries(data.category, 250, 250); 
    -   **Explanation**   
        getKBCategoryArticleSummaries(<category sys\_id>, <article limit>, <char count for description>) 
5.  Add it back to the page using widget instance 
6.  Navigate to [https://yourinstance.service-now.com/sp\_instance.do?sys\_id=b6f5c370d7000200a9ad1e173e24d498](https://yourInstance.service-now.com/sp_instance.do?sys_id=b6f5c370d7000200a9ad1e173e24d498) 
7.  In the widget tab widget field, change KB Category Page to **Cloned Widget** 

#### Solution 2: Using Knowledge Management Service Portal 

Knowledge Management Service Portal is a newly available plugin to work around some of the drawbacks with stock Service Portal like support for multiple knowledge bases. This plugin introduces a new search page **kb\_search**, which loads articles on demand and could apply different filters to it. 

[https://docs.servicenow.com/csh?topicname=knowledge-management-service-portal.html&version=latest](https://docs.servicenow.com/csh?topicname=knowledge-management-service-portal.html&version=latest "https://docs.servicenow.com/csh?topicname=knowledge-management-service-portal.html&version=latest")
