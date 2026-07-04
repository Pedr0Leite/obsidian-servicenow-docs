---
title: "How to Capture incident ticket details along with Survey Response in Survey_response table"
aliases:
  - KB0830143
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830143
kb_number: KB0830143
last_modified: 2024-04-08
---

## How to Capture incident ticket details along with Survey Response in Survey\_response table

  

### Issue

There is query on how we can get the details of the survey along with the task record for which that survey is submitted on a report for survey\_response table. But the above report is giving only survey responses but also needed the field for which ticket the response is given

### Cause

There is a table which stores the task number and as well as the survey responses with question and value which satisfies the requirement to build a report which will have the task id and as well as the survey responses

### Resolution

There are two ways where your requirement of having both the task id and the survey responses:  
1.Create a database view with left join to tables 'survey\_response' and 'asmt\_assessment\_instance' where the task id is present in the assessment table  
2.There is an existing table 'task\_survey\_detail' is having the question response and the task as well
