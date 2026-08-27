---
title: "SAMP | Custom Software Product's Class Changed to Software Product"
aliases:
  - KB2491416
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2491416
kb_number: KB2491416
last_modified: 2026-05-12
---

## SAMP | Custom Software Product's Class Changed to Software Product

  

### Issue

Custom Software Product \[samp\_custom\_sw\_product\] record's Class \[sys\_class\_name\] changed to Software Product \[samp\_sw\_product\]

### Symptoms

-   Attempting to reclassify these records back to Custom Software Product \[samp\_custom\_sw\_product\] records the Software Product \[samp\_sw\_product\] table fails.

### Facts

-   There are no OOB ACLs on the Custom Software Product \[samp\_custom\_sw\_product\] to prevent customers from accidentally updating the Class \[sys\_class\_name\] field.
-   The Software Product \[samp\_sw\_product\] table however does have an OOB ACLs that 'Nobody' can Update any field on samp\_sw\_product records.

### Release

All Releases

### Cause

Custom Software Product \[samp\_custom\_sw\_product\] unintentionally updated by a User.

### Resolution

**Follow below procedures to reclassify the samp\_sw\_product record back to samp\_custom\_sw\_product**

\* You'll need to elevate your role to Security Admin in production instances for the steps involving ACLs below.

**I. First the OOB ACL for samp\_sw\_product.\* needs to be copied as a new record with Admin Overrides set to true.**

1\. Navigate to the **Access Controls \[sys\_access\_control\]** table.

2\. Filter the list where **Name = samp\_sw\_product.\*** and **Operation = Write**.

3\. **Open** the ACL Record.

4\. **Check** the **Admin Overrides** check box.

5\. **Right Click** the form header and select **Insert with Roles** to create the new record.

**II. Next follow the procedure below to run a background script to reclassify the records.**

1\. **Copy** the **Sys ID** of the record that needs to be reclassified back to Custom Software Product.

2\. **Paste** the **Sys ID** into **Line 4** in the script.

3\. **Run** the script.

```
// Background Script to Update Class back to samp_custom_sw_product //
// Start
// Step 1. Enter Sys ID of the SW Product to be updated on below line.
var customSwProd = "<Sys ID of Custom SW Product>";  // Example: var customSwProd = "1c671e1e47f7a2d004aa6305f16d439d";

// Step 2. Click [Run Script] in 'global' scope
// End

///////////////////////////////////////////////////////////////////////////////////////////////////////
updateSysClassName(customSwProd);
function updateSysClassName(customSwProd){
var gr = new GlideRecord('samp_sw_product');
gr.addQuery('sys_id', customSwProd);
gr.query();
while(gr.next()){
gr.setValue('sys_class_name','samp_custom_sw_product');
gr.update();
}
}
///////////////////////////////////////////////////////////////////////////////////////////////////////
```

**III. Delete the copied samp\_sw\_product.\* ACL record with Admin Overrides set to true that was created in section I above.**

1\. Navigate to the **Access Controls \[sys\_access\_control\]** table.

2\. Filter the list where **Name = samp\_sw\_product.\*** and **Operation = Write.**

3\. Confirm the copied ACL that was just created with **Admin = True** and **Delete** the record.
