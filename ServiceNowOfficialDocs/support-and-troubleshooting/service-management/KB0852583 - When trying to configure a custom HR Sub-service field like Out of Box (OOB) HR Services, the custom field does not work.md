---
title: "When trying to configure a custom \"HR Sub-service\" field like Out of Box (OOB) HR Services, the custom field does not work when set as a \"Drop-down\" type"
aliases:
  - KB0852583
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852583
kb_number: KB0852583
last_modified: 2025-09-03
---

## When trying to configure a custom "HR Sub-service" field like Out of Box (OOB) HR Services, the custom field does not work when set as a "Drop-down" type

  

### Issue

The user was trying to configure their custom field to allow the selection of a HR sub-service under the HR Service field. They wanted to know how to make it function like the Out of Box (OOB) HR Service field does, as their attempt to make the field a "Drop-down" type field did not work (when clicking on the field on the HR form, only the "-- None --" option displayed).

### Resolution

It was found that the user needed to configure their custom "HR Sub-service" field to be of type "Reference" like the OOB HR Service field.  
  
Once this was modified on the corresponding sys\_dictionary record, results appeared per the user's expectation.
