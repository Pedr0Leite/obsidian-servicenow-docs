---
title: "Sam Reconciliation result shows partially completed, when version and edition is missing on the software models"
aliases:
  - KB3136892
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3136892
kb_number: KB3136892
last_modified: 2026-07-03
---

## Sam Reconciliation result shows partially completed, when version and edition is missing on the software models

  

### Issue

Sam Reconciliation result shows partially completed, when version and edition is missing on the software models

### Symptoms

The recon is failing with the error below:  
2026-06-29 14:16:27  
TypeError: Cannot convert null to an object.  
  
92  
2026-06-29 14:16:27  
at sys\_script\_include.ff2261966dfc4eb6b7a089030cb932a5.script:156  
at sys\_script\_include.ff2261966dfc4eb6b7a089030cb932a5.script:98  
at sys\_script\_include.ff2261966dfc4eb6b7a089030cb932a5.script:44 (insertSoftwareModel)  
at sys\_script\_include.ff2261966dfc4eb6b7a089030cb932a5.script:21 (buildTree)  
at sys\_script\_include.ff2261966dfc4eb6b7a089030cb932a5.script:15 (initialize)  
at sys\_script\_include.d22e7bdbc0a8016500a18e024bfc9aa3.script:11  
at sys\_script\_include.6f45a5263dbe4f3ea66a0733a6942e4b.script:131 (stampExistingSoftwareModels)  
at sys\_script\_include.6f45a5263dbe4f3ea66a0733a6942e4b.script:48 (tagSoftwareModelForUnlicensedInstall)  
at sys\_script\_include.6f45a5263dbe4f3ea66a0733a6942e4b.script:525 (createSMRforUnlicensedInstall)  
at sys\_script\_include.6f45a5263dbe4f3ea66a0733a6942e4b.script:485 (createSMRforUnlicensedObjects)  
at sys\_script\_include.f0f47ca6939b4948962959b7c522d08c.script:817 (publisherWrapup)  
at sys\_script\_include.f08a5362c3274daa8d6d4f11094c1e36.script:58 (publisherWrapup)  
at sys\_script\_include.d0e05c902b4744bb940b1ab2c636b0fb.script:729 (runReconTask)  
at sys\_script\_include.d0e05c902b4744bb940b1ab2c636b0fb.script:559 (processReconTasks)  
at sys\_script\_include.d0e05c902b4744bb940b1ab2c636b0fb.script:66 (run)  
at in the schedule record:1  
  
93  
2026-06-29 14:16:27  
Reconciliation Failed

### Release

Any Version

### Cause

It's because version and edition empty on the software model record and reconciliation logic is failing 

### Resolution

-   Please open the URL below on your instance, and if you find a software model with an empty version and edition,  
    [/cmdb\_software\_product\_model\_list.do?sysparm\_nostack=true&sysparm\_query=product.product\_type%3Dlicensable%5Eversion%3DNULL%5Eversion\_operator!%3Dis\_anything%5EORversion\_operator%3DNULL](https://exytedev.service-now.com/cmdb_software_product_model_list.do?sysparm_nostack=true&sysparm_query=product.product_type%3Dlicensable%5Eversion%3DNULL%5Eversion_operator!%3Dis_anything%5EORversion_operator%3DNULL)
-   Please add a version or delete this software model; the issue will be resolved.
