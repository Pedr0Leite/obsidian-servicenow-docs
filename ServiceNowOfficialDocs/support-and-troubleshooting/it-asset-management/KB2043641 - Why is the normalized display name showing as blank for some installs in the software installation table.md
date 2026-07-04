---
title: "Why is the normalized display name showing as blank for some installs in the software installation table?"
aliases:
  - KB2043641
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2043641
kb_number: KB2043641
last_modified: 2026-03-27
---

## Issue

Why is the normalized display name showing as blank for some installs in the software installation table?

## Resolution

1\. As per the business rule "Create a Software Normalisation", the Normalised display name (normalized\_display\_name) is set only for installations that meet specific criteria. These installations are those that will be processed by reconciliation, meaning they are subject to license management and reconciliation processes. The criteria for this are that the product must be licensable and the 'ignore installs' field must be set to false. This ensures that the Normalised display name is accurately populated for installations that require reconciliation, while avoiding unnecessary population for installations that are not subject to reconciliation.

https://instancename.service-now.com/sys\_script.do?sys\_id=9ec2b34d37101000deeabfc8bcbe5d43

This is the reference code that populates it:  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

current.discovery\_model = gr.sys\_id;

if (!gs.nil(gr.norm\_product)

&& gr.norm\_type.toString() === 'licensable'.       <<====

&& !gr.norm\_product.ignore\_installs) {.               <<====

var display = SAMPremiumUtils.calculateNormDisplayName(gr);

current.setValue('norm\_product', gr.getValue('norm\_product'));

current.setValue('norm\_publisher', gr.getValue('norm\_publisher'));

current.setValue('normalized\_display\_name', display);

} else {

SAMPremiumUtils.clearNormFieldsForInstallGr(current);

}

  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

2\. Check the Software Product table (samp\_sw\_product) to verify if a product is licensable and ignore installs = false. If not, expect an empty Normalised display name.
