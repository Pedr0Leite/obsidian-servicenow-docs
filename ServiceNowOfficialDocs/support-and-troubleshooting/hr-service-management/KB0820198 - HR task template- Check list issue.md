---
title: "HR task template- Check list issue"
aliases:
  - KB0820198
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820198
kb_number: KB0820198
last_modified: 2024-04-08
---

## Issue

For HR Task Templates, when tried to add items under Checklist 'Item Undefined' error is thrown  
  
Steps:  
1\. Navigate to Lifecycle Events -> Manage HR task Templates  
2\. Choose a template  
3\. Change the "acknowledgment type" to 'Checklist' in Classic UI or choose "HR Task Type" to checklist in New UI  
4\. Add an item under checklist and save the record  
5\. Observe 'Item undefined' error is thrown

## Resolution

After filling an item under the checklist, we should hit "Enter" to apply it to the list. Only then, the list will be saved.
