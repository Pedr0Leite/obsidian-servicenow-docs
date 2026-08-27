---
title: "Workflow not working for \"Awaiting Acceptance\" on HR cases."
aliases:
  - KB0858332
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0858332
kb_number: KB0858332
last_modified: 2025-09-03
---

## Issue

When a HR  case is changed to state "Awaiting Acceptance" the OOTB workflow, "HRI Case User Acceptance" is getting triggered even though the condition to exclude the HR Service is configured.

A new workflow which is a copy of "HRI Case User Acceptance" has been created, which ideally should have been triggered instead of the OOTB one.

## Resolution

**There is a BR : Trigger Awaiting Acceptance Workflow**  
In this BR, the condition is like - if state is "Awaiting Acceptance", it will trigger the workflow : HRI Case User Acceptance(OOB)  
Now if you want to define workflows like  
  

1.  HRI Case User Acceptance :  
    Condition : state is "Awaiting Acceptance" and HR Service is not "your HR service"
2.  HRI Case User Acceptance(PHD)  
    Condition : state is "Awaiting Acceptance" and HR Service is "your HR service"

  
You can follow these steps :  
  

1.  COE(In which you have defined new HR service"your HR service ) and table which is mentioned in the workflow should be same.
2.  While defining workflow condition you need to select "Run as always" because if it is none :- The workflow is not automatically started by the workflow engine. To run this workflow, you need to write a script to start the workflow.
3.  You can disable the BR "Trigger Awaiting Acceptance Workflow" because it is triggering the workflow "HRI Case User Acceptance", that time it will not consider the condition which we mentioned in workflow.
