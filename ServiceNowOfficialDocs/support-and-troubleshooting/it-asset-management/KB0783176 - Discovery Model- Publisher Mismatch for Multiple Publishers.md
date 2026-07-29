---
title: "Discovery Model- Publisher Mismatch for Multiple Publishers"
aliases:
  - KB0783176
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783176
kb_number: KB0783176
last_modified: 2024-07-31
---

## Issue

The discovered publisher Oracle is showing the publisher as Red Hat in software discovery models.

Go to Software Asset ->Discovery ->Discovery Models.

In the filter, provide discovered publisher is Oracle and publisher is Red Hat.

      ![](sys_attachment.do?sys_id=ebf1b1f91b9af890ccc253da234bcb68)

## Resolution

In order to correct the Publisher value of the discovered publishers, follow below steps.

**Step1** :  
     Copy the sys\_id of the record to be corrected the publisher name. Example take 10 records sys\_ids.

**Step2:**  
paste the sys\_id's in the below script  
  

```
var installGr;var counter=0;var discoveryModelSysIds=['f26136791bd7bf00a027dceacd4bcb87', //replace sys_id'f9a95468db9b3700419e8384059619de',//replace sys_id'fe93d8641b17b700a027dceacd4bcb9b',//replace sys_id'3a93d8641b17b700a027dceacd4bcb82',//replace sys_id'3a93d8641b17b700a027dceacd4bcb84',//replace sys_id'3e93d8641b17b700a027dceacd4bcb53',//replace sys_id'7293d8641b17b700a027dceacd4bcb86',//replace sys_id'7293d8641b17b700a027dceacd4bcb96',//replace sys_id'7a93d8641b17b700a027dceacd4bcb72',//replace sys_id'b293d8641b17b700a027dceacd4bcb6f'//sys_id 10];var dm = new GlideRecord('cmdb_sam_sw_discovery_model');dm.addQuery('sys_id',discoveryModelSysIds);dm.addQuery('status','normalized');dm.query();while (dm.next()) {    //clear out discovery model    dm.setValue("norm_publisher", "");     dm.setValue("norm_product", "");     dm.setValue("norm_type", "");    dm.setValue("norm_version", "");    dm.setValue("norm_edition", "");    dm.setValue("norm_full_version", "");    dm.setValue("norm_platform", "anything");    dm.setValue("norm_language", "832bec5493212200caef14f1b47ffb56");    dm.setValue("normalize_date", "");    dm.setValue("status", "missed");        dm.update();    counter++;    // clear out install table    installGr = new GlideRecord('cmdb_sam_sw_install');    installGr.addQuery('discovery_model', dm.getUniqueValue());    installGr.query();    while (installGr.next()) {        installGr.setValue('norm_product', "");        installGr.setValue('norm_publisher', "");        installGr.update();    }}gs.log('Count of Discovery Models updated: ' + counter);
```

**Step3 :**  
Go to script -background  
https://<instancename>.service-now.com/nav\_to.do?uri=%2Fsys.scripts.do  
  
**Step 4**:  
Paste the modified script in the step 2  
**Steps 5**:  
Run the Script.  
**Steps6**:  
Open all the records ->Click Normalization action.
