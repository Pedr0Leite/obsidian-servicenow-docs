---
title: "Entitlements created with invalid data"
aliases:
  - KB2930030
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2930030
kb_number: KB2930030
last_modified: 2026-05-20
---

## Entitlements created with invalid data

  

### Issue

When loading Software entitlements and using the out-of-the-box (ootb) functionality "Import bulk entitlements in SAM Workspace," the data is often loaded with an invalid publisher assigned. Additionally, the software model is created with either an incorrect publisher or the system is switching the publisher to the wrong value during the import process.

If the Publisher field is left empty or not provided, the system should prevent the creation of any invalid records rather than allowing entries with missing or incorrect publisher information to be generated.

### Symptoms

1\. Create a custom software product with the same product name but different records (for example one OOB Software Product and one Custom Software Product). Or navaigate to the below OOB records  
[https://instance.service-now.com/samp\_sw\_product\_list.do?sysparm\_query=prod\_nameSTARTSWITHInDesign%5Eprod\_name%3DInDesign&sysparm\_first\_row=1&sysparm\_view=workspace](https://instance.service-now.com/samp_sw_product_list.do?sysparm_query=prod_nameSTARTSWITHInDesign%5Eprod_name%3DInDesign&sysparm_first_row=1&sysparm_view=workspace)

2\. Ensure that corresponding Software Models exist for both products.  
[https://instance.service-now.com/cmdb\_software\_product\_model\_list.do?sysparm\_query=product%3D40209c060b3022002d6c650d37673a89&sysparm\_first\_row=1&sysparm\_view=](https://emprkuppay.service-now.com/cmdb_software_product_model_list.do?sysparm_query=product%3D40209c060b3022002d6c650d37673a89&sysparm_first_row=1&sysparm_view=)

3\. Prepare an entitlement import file where:  
    \* Publisher Part Number (PPN) is empty  
    \* Publisher field may be empty or incorrect(random)  
    \* Product name is provided.

4\. Import the attachment via Bulk Import into Entitlement from SAM Workspace.(If duplicate exists, delete that and import again)  
5\. Observe that the record is successfully processed and an entitlement is created in the alm\_license table.  
6\. Verify that the entitlement may reference one of the available Software Models, without validating the Publisher or raising an error.

### Release

Any

### Cause

The entitlement import process was analyzed in the SAMPEntitlementUtil Script Include, particularly the createEntitlementFromImport() function.

\* Entitlement creation proceeds when either Publisher Part Number (PPN) OR Software Model is present, as seen in the condition:  
if (!gs.nil(ppn) || !gs.nil(importGR.getValue('software\_model')))

  
\* If the Software Model is already populated, the system does not attempt to re-validate Publisher or Product fields before creating the entitlement.

### Resolution

The behavior is a confirmed bug (PRB2006846) and explains the root cause: the system incorrectly defaults to the first matching product by name when the publisher is invalid, leading to incorrect software model association.

Workaround: Ensure the publisher field is correctly set in the import spreadsheet.

### Related Links

PRB2006846

[https://support.servicenow.com/nav\_to.do?uri=problem.do?sys\_id=330d45fa93fb72183a68b56d6cba1029](https://support.servicenow.com/nav_to.do?uri=problem.do?sys_id=330d45fa93fb72183a68b56d6cba1029)
