---
title: "Issue publishing Knowledge Articles"
aliases:
  - KB0786311
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786311
kb_number: KB0786311
last_modified: 2025-04-01
---

## Issue publishing Knowledge Articles

  

### Issue

You have an issue publishing Knowledge Articles  
  
You are unable to publish imported knowledge articles.  
The review and publish functionality is not working.

### Cause

Knowledgebase 'IT' which is defined to use the workflow 'Knowledge - Approval Publish' has no Owner or Manager associated to it.  
  
  
For ''Knowledge - Approval Publish' workflow, it requires a review by approval users who are the Owner or Manager on the knowledgebase record.  
As there were no Owner or Manager associated to the knowledgebase, the workflow 'Approval User' step was going to delete.  
  
TESTING:  
  
As a test I created a Knowledgebase, added an owner and manager.  
  
I created a new Article in this knowledgebase  
  
I clicked the 'publish' ui action, we can see that it is working properly as it is in the 'review' state with 2 Approval Users.  
  
I have further approved one of the approval records and now the Article is in state 'Published'

### Resolution

  
To resolve this issue, in your knowledegbase record, ensure you add an owner and Manager that will approve the records.
