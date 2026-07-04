---
title: "Exception Rule for \"Microsoft Visual Studio Community\" (non-licensable edition) does not work as expected"
aliases:
  - KB2066246
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2066246
kb_number: KB2066246
last_modified: 2026-03-27
---

## Exception Rule for "Microsoft Visual Studio Community" (non-licensable edition) does not work as expected

  

### Issue

The exception Rule for the "Microsoft Visual Studio Community" (non-licensable edition) does not work as expected.

/samp\_prod\_lic\_excep\_rules\_list.do?sysparm\_query=product.prod\_nameSTARTSWITHVisual%5EeditionSTARTSWITHComm&sysparm\_view=  
  
If you find the same issue with any other non-licensable edition of software, you can implement the same solution.

### Symptoms

The non-licensable edition is considered for reconciliation even when the product exception rule is present in the instance.

Check the SAM Workspace for Microsoft, you will see "Microsoft Visual Studio Community" listed.

### Release

All releases after Vancouver cause that is when samp\_custom\_lic\_exception\_rules is added as a feature.

### Cause

The norm\_product and norm\_publisher were still present for the software installations. They should be empty.

### Resolution

**Solution Proposed:**  
  
1\. Run the below script to clear the entire table "**samp\_prod\_lic\_excep\_rules**":  
\====  
`var gr = new GlideRecord("samp_prod_lic_excep_rules");`   
`gr.setWorkflow(false); // Bypass business rules and workflows`   
`gr.deleteMultiple();`  
\====  
  
2\. Pull content data by clearing the last\_updated\_on and by executing the scheduled job. (Only 'Maint' users can clear the last\_updated\_on field, hence request ServiceNow support to perform this step)  
Download Software content: Product License Exception Rules  
/nav\_to.do?uri=cds\_client\_schedule.do?sys\_id=8363e97210dc3910f877dded22d92362   
  
3\. Then execute SAM - Apply latest content changes   
/nav\_to.do?uri=sysauto\_script.do?sys\_id=26f6310bdb8773004fbf75868c961988   
  
This should bring back all the records on samp\_prod\_lic\_excep\_rules table.  
  
3\. Make sure that the "License Under Management" (LUM) Flag for that software model is disabled.  
  
4\. Ran reconciliation to verify the resolution.  
  
Note: If you find the same issue with any other non-licensable edition of any software product, you can implement the same solution.
