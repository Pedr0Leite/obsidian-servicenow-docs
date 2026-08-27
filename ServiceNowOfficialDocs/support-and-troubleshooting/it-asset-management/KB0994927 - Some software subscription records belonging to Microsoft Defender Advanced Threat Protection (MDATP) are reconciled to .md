---
title: "Some software subscription records belonging to \"Microsoft Defender Advanced Threat Protection (MDATP)\" are reconciled to \"Defender for Office 365\" product"
aliases:
  - KB0994927
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0994927
kb_number: KB0994927
last_modified: 2024-07-27
---

## Issue

From License Workbench or historical result of reconciliation, you might encounter situation where software subscription records belonging to "Microsoft Defender Advanced Threat Protection (MDATP)" are reconciled to "Defender for Office 365" product.  
Subscription Identifier "WIN\_DEF\_ATP" should be map to MDATP product.

## Resolution

1.  From the menu (System Maintenance --> Scripts-Background) run script to remove all subscriptions with identifier WIN\_DEF\_ATP. Example:  
    \======  
    var gr = new GlideRecord('samp\_sw\_subscription');  
    gr.addQuery('subscription\_identifier', 'WIN\_DEF\_ATP');  
    gr.setWorkflow(false);  
    gr.deleteMultiple();  
    \======
2.  Run "SAM - Import User Subscriptions" schedule job to re-import Microsoft subscriptions.
3.  Run reconciliation for Microsoft and all WIN\_DEF\_ATP subscription records are reconciled into MDATP product only.

## Additional Information

The correct way is to update same content (PPN) by using the stage entitlement definition. Whenever content changes the stage column, logic will run some handler scripts to update all the subscription records.  
Since the content is not updated, rather a new content record gets added for WIN\_DEF\_ATP, new subscription records are linked to new product (MDATP). The old one is not updated and still linked to Defender for Office 365.
