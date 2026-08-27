---
title: "HR Case Creation Search is not returning results (irrespective of whether testing is done through the Platform UI or HR Agent Workspace)"
aliases:
  - KB0954953
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0954953
kb_number: KB0954953
last_modified: 2025-09-03
---

## HR Case Creation Search is not returning results (irrespective of whether testing is done through the Platform UI or HR Agent Workspace)

  

A very detailed Community article on HR search was provided to the user on the topic of **HR Case Creation Search**:

-   [https://community.servicenow.com/community?id=community\_article&sys\_id=3b592ed1dbd908941cd8a345ca961943](https://community.servicenow.com/community?id=community_article&sys_id=3b592ed1dbd908941cd8a345ca961943)  
    

The user was then directed, as per the article, to check to ensure the table and fields searched were indexed properly. Navigating to a record list for sys\_user or sn\_hr\_core\_profile can quickly show if the table is text searchable by checking if the user can search "for text". If "for text" is not shown, then the table is not text indexed. If "for text" is shown, but no search results are found for a search then there is an issue with the text indexing for the field being searched or the field is not readable.

After trying this, the user found that the tables were not indexed properly. Indexing them resolved the issue, and the Employee Search for HR Case Creation in both the Platform UI and HR Agent Workspace worked as expected.

\---

**Note:** It is highly recommended that for any HR Case Creation Search issues the above article be referenced before creating a case with Support, as many of these common issues can be resolved via the article.
