---
title: "Our HR Interaction records aren't being scoped correctly"
aliases:
  - KB0867709
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0867709
kb_number: KB0867709
last_modified: 2025-09-03
---

## Our HR Interaction records aren't being scoped correctly

  

### Issue

Interactions with topics from 'Human Resources Scoped App: Virtual Agent Conversations (com.sn\_hr\_virtual\_agent)' plugin are set in Global scope.

### Resolution

The product team was able to review this behavior. Please see their notes below about how to properly configure the HRSD topics:  
  
Interactions which are generated from portal will initially be created in Global scope only.  
However, for HR VA conversations once the interaction is closed they are moved to correct scope. This will happen only if the interaction context has 'liveagent\_hr\_topic\_id' variable set to sys\_id(from sys\_cb\_topic table) of HR VA scoped topic.  
  
Steps to make sure that 'liveagent\_hr\_topic\_id' is set for HR VA topics :  
1\. Open the HR VA scoped Virtual Agent topic flow.  
2\. In the Topic properties, click on pencil icon of Live Agent variables.  
3\. Choose 'LiveAgent\_hr\_topic\_id' from Available options & move it to selected.  
4\. Save  
5\. Go to Edit topic Flow  
6\. From the bottom left Activate "Show Live Agent Variables"  
7\. Click on "LiveAgent\_hr\_topic\_id"  
8\. In the Default Value enter the sys\_id (from sys\_cb\_topic table) of this particular topic.  
9\. Save.  
10\. Save & Publish the topic.  
  
Please note that if the VA conversations is closed without choosing any HR VA scoped topic or if the choosen topic do not have 'LiveAgent\_hr\_topic\_id' variable properly set, the interaction will continue to be in global scope.
