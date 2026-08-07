---
title: "The \"To:\" line on quick messages created in the Employee Relations COE does not auto-populate with the subject person's email like it does in other COEs.  Is this expected behavior due to enhanced security on the Employee Relations COE?"
aliases:
  - KB2920631
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2920631
kb_number: KB2920631
last_modified: 2026-03-27
---

## The "To:" line on quick messages created in the Employee Relations COE does not auto-populate with the subject person's email like it does in other COEs. Is this expected behavior due to enhanced security on the Employee Relations COE?

  

### Summary

**Issue** : The "To:" line on quick messages created in the Employee Relations COE does not auto-populate with the subject person's email like it does in other COEs.  

**Most Probable Cause**: "To" field was not set on email template record. 

**Resolution**:  
\-"To" field not set on email template record. 

\-Email template for sn\_hr\_core\_case\_workforce\_admin, "TO" field is set to - javascript:new sn\_hr\_agent\_ws.hr\_EmailUIBUtils(current.getTableName(), current.sys\_id).getToValue()

\-Link to email template for workforce cases  
 https://<Instance\_Name>.service-now.com/nav\_to.do?uri=sys\_email\_client\_template.do?sys\_id=79c910af530230102a09ddeeff7b1277

\-Email template for Employee relations case, "TO" field is empty.

\-After adding the same line in "TO" same as workforce email template, issue should be resolved  
https://<Instance\_name>.service-now.com/nav\_to.do?uri=sys\_email\_client\_template.do?sys\_id=61fcef851be0b05067b0657ce54bcb3e

Please review the following points before applying this solution:

1) Ensure that these changes do not impact any other functionality that uses the same email template, as it is hardcoded.  
2) Implement this solution in the sub-production instance first and test it thoroughly before moving it to PROD instance.

### Release

Zurich
