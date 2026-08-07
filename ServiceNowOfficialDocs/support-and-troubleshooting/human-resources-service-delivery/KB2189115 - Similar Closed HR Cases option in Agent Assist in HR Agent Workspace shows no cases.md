---
title: "Similar Closed HR Cases option in Agent Assist in HR Agent Workspace shows no cases"
aliases:
  - KB2189115
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2189115
kb_number: KB2189115
last_modified: 2025-09-03
---

## Similar Closed HR Cases option in Agent Assist in HR Agent Workspace shows no cases

  

### Issue

The 'Similar Closed HR Cases' option in Agent Assist in HR Agent Workspace is not displaying any cases.  
1\. Open HR Agent Workspace   
2\. Search for any of the HR Cases   
3\. Open Agent Assist on the right side.  
4\. Select Similar Closed HR Cases from dropdown.

### Release

all releases

### Resolution

1\. Update the ML by removing the Description field from the Solution.  
2\. Retrain the ML after updating it.  
3\. The suggested solution, updating the OOB version by removing the description as a feature, can be shared as a new update set or solution. In this way, the existing OOB solution will be in the instance.  
4\. Retrain the model in prod again to make it work in prod.  
5\. You will be able to see similar closed HR cases once ML is updated and retrained.  
7\. Increase the number of records to have a more diverse set of predictions.
