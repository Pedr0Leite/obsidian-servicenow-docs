---
title: "Survey triggered from HR Activities are not visible in my_survey page in Portal"
aliases:
  - KB1895889
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1895889
kb_number: KB1895889
last_modified: 2026-03-04
---

## Survey triggered from HR Activities are not visible in my\_survey page in Portal

  

### Issue

We may have HR activities which are type of Surveys. When those are triggered, and assessment\_instances are created, the surveys are not visible on the OOTB my\_survey page. 

### Release

This is not release or environment specific

### Cause

This behaviour is as expected. FilterHrTaskSurveys script include hides all survey instances associated with sn\_hr\_core\_task to prevent any type of duplicate count.

### Resolution

  
 This behaviour is as expected. 

1\. We have implemented global.FilterSurveys extension point in sn\_hr\_core.FilterHrTaskSurveys script include.

2\. This script include hides all survey instances associated with sn\_hr\_core\_task.

3\. You can find the script include here and consider deactivating it if your business needs require to see them:  
Script Include - FilterHrTaskSurveys

https://<instance>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=dd4d5ce70f723010176e008c07767ea5

4\. This behaviour was only to prevent any type of duplicate count. This can be safely disabled to meet your business requirements.  
  

NOTE: Please test first in a sub-production instance before moving it to a production instance.
