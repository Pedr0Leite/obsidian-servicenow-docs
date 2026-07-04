---
title: "Software Asset Analytics widgets show \"No data available\" when SAM PA scheduled jobs are inactive or missing Run as user"
aliases:
  - KB2711630
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2711630
kb_number: KB2711630
last_modified: 2026-01-11
---

## Issue

→ In Software Asset Analytics, OOB visualizations/widgets do not populate and display “No data available” for indicators

## Resolution

**Validate the scheduled jobs**

→ Job SAM Data Collection  
→ https://<instance\_name>.service-now.com/nav\_to.do?uri=sysauto.do?sys\_id=24e64a6d534103008235258beec58708  
→ Indicators for this job  
→ https://<instance\_name>.service-now.com/pa\_job\_indicators\_list.do?sysparm\_query=job%3D24e64a6d534103008235258beec58708%5E&sysparm\_view=

 **Job SAM - Daily Job**  
→ https://<instance\_name>.service-now.com/nav\_to.do?uri=sysauto.do?sys\_id=ffc55a94dbfb22003fc57bfdae9619d9  
→ Indicators for this job  
→ https://<instance\_name>.service-now.com/pa\_job\_indicators\_list.do?sysparm\_query=job%3Dffc55a94dbfb22003fc57bfdae9619d9%5E&sysparm\_view=

 **Restore OOB configuration**  
→ Set both jobs to Active true  
→ Set Run as user to SAM PA Jobs Scheduler

 **Fix scheduler user state if needed**  
→ If SAM PA Jobs Scheduler user is locked or disabled unlock or correct the user so it can run scheduled jobs

 **Recalculate indicator scores**  
→ Run both jobs or allow them to run on schedule to generate PA scores

 **Validate**  
→ Refresh Software Asset Analytics  
→ https://<instance\_name>.service-now.com/now/softwareasset/analytics  
→ Confirm widgets populate and the message no data available no longer appears
