---
title: "SAMP Reconciliation: Certain software installs are not being considered for reconciliation"
aliases:
  - KB0829074
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0829074
kb_number: KB0829074
last_modified: 2024-04-08
---

## SAMP Reconciliation: Certain software installs are not being considered for reconciliation

  

### Issue

When running reconciliation, certain software install records do not seem to be counted against reconciliation, even though there are no filters that would filter out these installations

### Cause

The "Normalized Product" (norm\_product) and "Normalized Publisher" (norm\_publisher) fields on the software installs are empty although the norm\_publisher and norm\_product on discovery model associated with those installs are set correctly.

### Resolution

The script below can be used to fix the install records:   
\=================================================================  
var rec = new GlideRecord("cmdb\_sam\_sw\_install");  
rec.addQuery("software\_model", "<sys\_id of the model record associated with the installs>");  
rec.setValue("norm\_product", "<sys\_id of the normalized product>");  
rec.setValue("norm\_publisher", "<sys\_id of the normalized publisher>");  
rec.setValue("normalized\_version", "14.0.7015.1000"); //replace example with string value for normalized version  
rec.setValue("normalized\_publisher", "Microsoft"); //replace example with string value for normalized publisher  
rec.setValue("normalized\_display\_name", "Microsoft Visio Standard 2010"); //replace example with string value for normalized display name  
rec.setValue("is\_normalized", true);  
rec.updateMultiple();  
\=================================================================  
  
\*note\* Please run this script first on a sub-production instance and if there are any questions, reach out to Technical Support for further assistance
