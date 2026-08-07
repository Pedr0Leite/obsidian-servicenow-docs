---
title: "HR Surveys are not triggering "
aliases:
  - KB0813879
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813879
kb_number: KB0813879
last_modified: 2024-04-08
---

## HR Surveys are not triggering

  

### Issue

HR Surveys are not getting triggered based on the 30days rule.

### Resolution

  
  
There is a BR `"**Task survey events**"`,by default OOB, this BR will not send a survey to the user if a survey is already pending with a user.This BR was customised and causing the issue.  
  

Solution will be to :

Either revert this BR to OOB.If you are going ahead with this solution, make sure "this BR will not send a survey to the user if a survey is already pending with a user."

  
OR

If you want to ahead with your customised BR , please review the code
