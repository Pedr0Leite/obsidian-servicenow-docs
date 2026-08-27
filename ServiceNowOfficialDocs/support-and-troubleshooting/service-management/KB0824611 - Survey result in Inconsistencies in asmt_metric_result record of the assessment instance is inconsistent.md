---
title: "Survey result in Inconsistencies in asmt_metric_result record of the assessment instance is inconsistent"
aliases:
  - KB0824611
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824611
kb_number: KB0824611
last_modified: 2024-04-08
---

## Survey result in Inconsistencies in asmt\_metric\_result record of the assessment instance is inconsistent

  

### Issue

For multi-select questions all results come back as "N/A" (where the expected result would be a metric result for each selected option)

### Release

All

### Cause

Customized assessment\_take2 UI page. 

### Resolution

Revert assessment\_take2 UI page to OOB version with sys\_id 012918babfb001007a6d257b3f073996

https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_ui\_page.do?sys\_id=012918babfb001007a6d257b3f073996
