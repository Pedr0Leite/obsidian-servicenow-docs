---
title: "Cannot Revert Hardware Model Normalization"
aliases:
  - KB2584278
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2584278
kb_number: KB2584278
last_modified: 2025-10-24
---

## Cannot Revert Hardware Model Normalization

  

### Issue

Cannot revert normalization for records in the cmdb\_hardware\_product\_model table once they have been reverted once.

### Symptoms

There will be no "Revert normalization" button on the hardware model.

### Release

All releases

### Resolution

Once a hardware model has its normalization reverted once, it cannot be normalized OOB again with that same normalization rule.

This is because when a normalization is reverted, it is assumed that the customer will proceed with their own normalization rule to handle the normalization of the model. Thus, we disable the rule so that the model doesn't constantly revert to the normalization rule established via our Content Library.  
  
Once a normalization is reverted on a particular hardware model, then when normalizing the model again, you will no longer see a "Normalized" normalization status when all of the normalization fields are filled when using that particular normalization rule. Instead, a normalization status of "Manually normalized" can be achieved instead. As long as this manually normalized model maps to the correct model that we have in content, you will still receive all updates to the model from the Content Library.  
  
Thus, as a result of the above-mentioned points, once you revert normalization once, the hardware model cannot have its normalization reverted again for the same normalization rule.  
  
Reviewing the documentation "Revert normalization of hardware and consumable models":  
[https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/hardware-asset-management/task/revert-norm-ham.html](https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/hardware-asset-management/task/revert-norm-ham.html)  
  
It explicitly states that, after the revert normalization process is complete, the following changes take place:  
\[-\] All the normalized fields present in the model are reverted and the normalization status changes to Match not Found.  
\[-\] Fields are reset to their original values and any rule associated with the model is deactivated.  
\[-\] After deactivation of the rule, revert normalization is run on all models that were normalized using that rule before.  
\[-\] The deactivated rule can no longer normalize any more models. The deactivated rule can't be reactivated. It's a one-time procedure.  
\[-\] The Revert Normalization option on the model record is replaced with the Normalize option.
