---
title: "Non-licensable products in license position report"
aliases:
  - KB2216134
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2216134
kb_number: KB2216134
last_modified: 2025-08-18
---

## Issue

Non-licensable products like child patches and drivers are getting populated in the license position report.  
  
  
  

## Resolution

Run the below script in the background script to fix the records:

This script finds all software install records that have been normalized to a product that is NOT licensable and then removes the normalization by clearing the norm\_product and norm\_publisher fields — essentially "de-normalizing" them — without triggering workflows.  
  
**IMPACT OF THE SCRIPT**: Once you run this, those installs will appear as un-normalized in SAM, and you may lose reporting/licensing data linked to them. If this was meant as a cleanup step, make sure you back up or export the affected records first.  
  
\======== **SCRIPT** ========  
var gr = new GlideRecord('cmdb\_sam\_sw\_install');  
gr.addEncodedQuery('norm\_productISNOTEMPTY^norm\_product.product\_type!=licensable');  
gr.query();  
var count = 0;  
while (gr.next()) {  
gr.setValue('norm\_product', '');  
gr.setValue('norm\_publisher', '');  
gr.setWorkflow(false);  
gr.update();  
count++;  
}  
gs.print('Updated installs: ' + count);

Next steps: Run reconciliation to verify results  
  

**IMP NOTE**: Please test this in **DEV or TEST** thoroughly before proceeding in the actual production instance.
