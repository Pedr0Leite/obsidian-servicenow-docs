---
title: "There are some entries with value \"-1\" in asmt_metric_result table for the survey.  "
aliases:
  - KB0822959
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0822959
kb_number: KB0822959
last_modified: 2024-11-13
---

## There are some entries with value "-1" in asmt\_metric\_result table for the survey.

  

### Issue

" asmt\_metric\_result " table does not seem to display/capture the correct string/actual value from asmt\_assessment\_instance\_question table.

The asmt\_assessment\_instance\_question table shows "Like / 10" as String/Actual Value but asmt\_metric\_result table showed "N/A / -1". 

### Release

New York

### Cause

Expected behavior

### Resolution

According to the documentation, the value of the "Actual Value" field on the asmt\_metric\_result table depends on the type of the metric.  
  
For Date, Date/Time, or String types, the actual value is -1 to indicate that these data types do not contribute to category result calculations.  
  
  
  
  

### Related Links

More details can be found:

[View a metric result](https://docs.servicenow.com/csh?topicname=t_ViewAMetricResult.html&version=latest "View a metric result")
