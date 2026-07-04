---
title: "Widget \"HRJ Task Take Survey\" allows non assignees to submit a Survey task"
aliases:
  - KB2534115
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2534115
kb_number: KB2534115
last_modified: 2025-10-13
---

## Issue

The Subject User for a Journey can view and complete survey for an HR Task not assigned to them

## Resolution

Fixed by: PRB1945511

Workaround: Remove the following lines from the "HRJ Task Take Survey" widget’s server script (lines 35–36):  
  
data.link\_text = data.task.survey.name;  
data.link = "?id=take\_survey&type\_id=" + data.task.survey.id;

## Additional Information

Product doc: [https://docs.servicenow.com/bundle/xanadu-employee-service-management/page/product/human-resources/task/jny-dsgnr-employee-journey-tasks.html](https://docs.servicenow.com/bundle/xanadu-employee-service-management/page/product/human-resources/task/jny-dsgnr-employee-journey-tasks.html)
