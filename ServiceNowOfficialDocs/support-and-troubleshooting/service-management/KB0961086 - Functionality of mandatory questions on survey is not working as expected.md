---
title: "Functionality of mandatory questions on survey is not working as expected"
aliases:
  - KB0961086
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961086
kb_number: KB0961086
last_modified: 2025-10-27
---

## Functionality of mandatory questions on survey is not working as expected

  

### Issue

When user tries to submit the survey without filling the mandatory fields it is throwing error only for few questions inspite of all questions being configured as mandatory.

Steps To Replicate:  
\> Open a survey link  
\> There are total 5(suppose) mandatory questions to be filled but when user clicks on Submit without filling any of the field  
 Expected behavior- Error Message should be shown: " There are 5 questions that do not have a valid response. Please correct these and re-submit "  
 Actual behavior- " Error MessageThere are 2 questions that do not have a valid response. Please correct these and re-submit "

Observation- Questions of type Multiple Selection has the issue (not showing error for these questions).  

### Release

All

### Cause

UI page was customised - https://<instance\_name>.service-now.com/sys\_ui\_page.do?sys\_id=012918babfb001007a6d257b3f073996

### Resolution

Reverting the UI page "assessment\_take2" to OOTB version fixes the issue.

### Related Links

Assessments

[https://docs.servicenow.com/bundle/quebec-servicenow-platform/page/administer/assessments/reference/r\_Assessments.html](https://docs.servicenow.com/bundle/quebec-servicenow-platform/page/administer/assessments/reference/r_Assessments.html)
