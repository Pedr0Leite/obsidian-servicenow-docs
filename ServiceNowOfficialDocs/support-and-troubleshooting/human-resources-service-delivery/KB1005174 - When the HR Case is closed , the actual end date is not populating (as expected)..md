---
title: "When the HR Case is closed , the \"actual end date\" is not populating (as expected)."
aliases:
  - KB1005174
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1005174
kb_number: KB1005174
last_modified: 2025-09-03
---

## When the HR Case is closed , the "actual end date" is not populating (as expected).

  

### Issue

On the HR Cases, the Actual end date is not populating after the case is closed. The stop time is getting updated in the Task SLA's related list but not showing/populating in the field.  
It is populating only for some cases but not to all.

### Resolution

we set work\_start in ''Start Work' UI Action, but we don't set the work\_end neither on on the 'Close Complete' UI Action nor on the 'HRI Case User Acceptance' workflow  
However, we set work\_end on the 'close Incomplete' UI action...  
This is working as per current product design.
