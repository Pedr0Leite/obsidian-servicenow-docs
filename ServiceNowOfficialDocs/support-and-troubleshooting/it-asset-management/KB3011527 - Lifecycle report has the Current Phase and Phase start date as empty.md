---
title: "Lifecycle report has the Current Phase and Phase start date as empty"
aliases:
  - KB3011527
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3011527
kb_number: KB3011527
last_modified: 2026-06-18
---

## Lifecycle report has the Current Phase and Phase start date as empty

  

### Issue

On the Software Lifecycle Report, we can see the Phase information is missing for most of the records. 

### Release

Any

### Cause

The Phase information and the dates come from the Content Library. One of the reason could be there are no Lifecycles available for the Products in the Software Product Lifecycle table (sam\_sw\_product\_lifecycle)

### Resolution

\- You will have to reach out to Content Team via Catalog Request([KB0790305](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790305)) to get the Lifecycles added in the sam\_sw\_product\_lifecycle table.

\- Apply the below filter on the 'sam\_sw\_product\_lifecycle\_report' table and share an xml export to the Content team as it would help to provide a faster resolution by addressing only what is relevant from a lifecycle coverage standpoint. 

(Add your instance name in the below link or refer to screenshot for filters)

[https://<instance-name>.service-now.com/sam\_sw\_product\_lifecycle\_report\_list.do?sysparm\_query=norm\_versionISNOTEMPTY%5Enorm\_product.product\_type%3Dlicensable%5EORnorm\_product.product\_type%3Dnot%20licensable%5Ega\_start\_dateISEMPTY%5Ega\_lifecycle.lifecycle\_codeISEMPTY%5Eeoes\_start\_dateISEMPTY%5Eeoes\_lifecycle.lifecycle\_codeISEMPTY%5Eeol\_start\_dateISEMPTY%5Eeol\_lifecycle.lifecycle\_codeISEMPTY%5Eeos\_start\_dateISEMPTY%5Eeos\_lifecycle.lifecycle\_codeISEMPTY&sysparm\_view=](https://\<instance-name\>.service-now.com/sam_sw_product_lifecycle_report_list.do?sysparm_query=norm_versionISNOTEMPTY%5Enorm_product.product_type%3Dlicensable%5EORnorm_product.product_type%3Dnot%20licensable%5Ega_start_dateISEMPTY%5Ega_lifecycle.lifecycle_codeISEMPTY%5Eeoes_start_dateISEMPTY%5Eeoes_lifecycle.lifecycle_codeISEMPTY%5Eeol_start_dateISEMPTY%5Eeol_lifecycle.lifecycle_codeISEMPTY%5Eeos_start_dateISEMPTY%5Eeos_lifecycle.lifecycle_codeISEMPTY&sysparm_view=)

![](/sys_attachment.do?sys_id=b5defc2d47b8835077b5ab29736d4376)
