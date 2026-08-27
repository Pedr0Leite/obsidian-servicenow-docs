---
title: "Business rules are missing with Skills Management (com.snc.skill_determination) plugin"
aliases:
  - KB0868312
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0868312
kb_number: KB0868312
last_modified: 2024-10-12
---

## Issue

By following the below document: [Using rules to identify skills for work items](https://docs.servicenow.com/bundle/orlando-servicenow-platform/page/product/customer-service-management/concept/skills-based-routing.html "Using rules to identify skills for work items:")

-     
    

The above document mentioned 'com.snc.skill\_determination' plugin will activates 3 business rules when installed:  
1\. "Skill determination for case", 2."Skill determination for work order task" and 3. "Skill determination for interaction"  
  
  
But when installing 'com.snc.skill\_determination' plugin, the "Skill determination for case" and " Skill determination for work order task" Business Rules not present, only the Business rule "Skill determination for interaction" Business Rule is present.  
  
Steps to reproduce:  
1\. System Definitions >> Business Rules >> check and notice that Business rules which are in mentioned in the document not present  
\[Make sure 'com.snc.skill\_determination' plugin is installed\]  

## Resolution

For 'Skill determination for case' has dependency on Customer Service plugin (com.sn\_customerservice).  
Similarly for the business rule - 'Skill determination for work order task' has dependency on Field Service Management (com.snc.work\_management) plugin.  
  
Since both of these plugins are not installed in customer's instance and above 2 business rules work on cases and work order tasks, the skill determination plugin doesn't install them when it is activated.  
  
In order to get both of these business rules, please install 'Customer Service' (com.sn\_customerservice) and 'Field Service Management' (com.snc.work\_management) plugins.
