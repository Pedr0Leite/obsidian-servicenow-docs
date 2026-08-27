---
title: "How can we avoid having the lifecycle from the generalized software model apply to the underlying models that are associated to the generic software model."
aliases:
  - KB0963948
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0963948
kb_number: KB0963948
last_modified: 2025-01-02
---

## How can we avoid having the lifecycle from the generalized software model apply to the underlying models that are associated to the generic software model.

  

### Summary

While Reconciliation is run and the automatic software model creation property is enabled i.e [com.snc.samp.automaticsmrcreation](https://empadartq.service-now.com/sys_properties.do?sys_id=3d4cbdfd67e313003b4687cb5685ef32&sysparm_record_target=sys_properties&sysparm_record_row=2&sysparm_record_rows=4&sysparm_record_list=nameCONTAINSautomatic%5EORDERBYname) the system creates software models.  
In most cases we see a generic software model being created for the product with no version, edition etc. Because of which it qualifies for condition as anything for all the attributes.  
Because the condition is set to have version,edition anything all the other different version software models are going to be associated with this model.  
And when there is a lifecycle added to this model it is confusing because this life cycle will be applied to all the underlying models which will cause confusion.

### Release

All

### Instructions

This Behavior is expected OOTB and to avoid confusion it is recommended not to add the lifecycle to this generic model.  
If it is already added please delete this lifecycle 

The software model lifecycle of that generic software model will be indeed applied to those underlying software models. If you don't want that lifecycle to apply to all the underlying software models then you should delete that lifecycle record from the generic software model. Instead, you should put the lifecycle into the specific software models.
