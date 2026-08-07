---
title: "HR Record Producer is not populating template values"
aliases:
  - KB0829085
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0829085
kb_number: KB0829085
last_modified: 2025-09-03
---

## HR Record Producer is not populating template values

  

### Issue

The user had a HR Record Producer which was not updating template values as specified in the selected HR Service on submission. They wanted to know why.

### Resolution

The reason the templated values were not being filled in per the HR Service's template configuration is that the user had customized the Script Include (_hrServicesUtil_) mentioned within the Record Producer's script section which reads:  
  
`new sn_hr_core.hr_ServicesUtil(current, gs).createCaseFromProducer(producer, cat_item.sys_id);`  
  
The script section in the HR Record Producer is what is responsible for populating template values set in a HR Service. So, because that Script Include which was mentioned had been modified/customized, it broke the system's ability to fill in the values per the user's expectation. Reverting the Script Include back to Out of Box (OOB) resolved the issue immediately.
