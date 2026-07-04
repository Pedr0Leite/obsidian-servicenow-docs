---
title: "Assessment Metric change empties Assessment Metric Definitions"
aliases:
  - KB0779982
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779982
kb_number: KB0779982
last_modified: 2024-04-08
---

## Assessment Metric change empties Assessment Metric Definitions

  

### Issue

An update to the Assessment Metric record affects the related list 'Assessment Metric Definitions'. The string value in the Display column is replaced by the numeric value in the Value column.

Steps to Reproduce:

1\. Navigate to Assessments > Metric definitions > Metrics  
2\. Select a Metric that has Assessment Metric with data type numeric scale  
3\. Make an update to the Metric record such as updating the Description on the General tab  
4\. Click Update  
5\. Observe that in the Assessment Metric Definitions related list, the Display is now the same as the Value

### Cause

Known Error in:

PRB1320939 'The survey scorecard is showing responses as "empty".'

The issue can be reproduced when a survey contains survey question which is “numeric scale” type. Scorecard is displayed by grouping Metric Definition field in Metric Results table. This column is a reference field. When a survey instance is completed, Metric Definition field gets corresponding value. Now, if there is update to the survey question, e.g. change name of this numeric scale question, the value of Metric Definition field is wiped out for the completed survey instances. When the survey question gets updated/changed, the existing metric definitions are deleted and new ones get created. So the reference in metric result is lost and in scorecard it shows as “empty” result.

  
For other question types like choice, if user manually deletes a metric definition, the reference in metric result is also lost.

### Resolution

PRB1320939 is fixed in the New York release. There is no known workaround.
