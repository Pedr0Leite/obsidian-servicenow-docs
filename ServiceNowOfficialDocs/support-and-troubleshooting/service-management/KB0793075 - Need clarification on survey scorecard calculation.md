---
title: "Need clarification on survey scorecard calculation"
aliases:
  - KB0793075
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793075
kb_number: KB0793075
last_modified: 2024-04-07
---

## Need clarification on survey scorecard calculation

  

### Issue

How to calculate the scorecard and how does it works  
What formula does it use for displaying the results?  
How are the current and different sections calculated?

### Resolution

We are calculating the scorecard result specific to the assessment group. e: g list of category result and metric result with specific to the assessment group.  
For example the metric "XYZ" . If you see total 6 metric results are there. However, only two of them are having valid assessment group. So the formula calculates on the basis of  
(sum of normalized value/total number of assessment group \*100)/100 . ((1.67+1.67)/2 \*100)/100 which is 1.67 in the year 2019. Records without the assessment group are not taking into consideration.
