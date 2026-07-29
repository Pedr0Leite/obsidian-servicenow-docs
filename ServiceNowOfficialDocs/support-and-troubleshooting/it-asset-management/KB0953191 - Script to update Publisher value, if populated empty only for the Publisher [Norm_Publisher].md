---
title: "Script to update Publisher value, if populated <empty> only for the Publisher [Norm_Publisher]"
aliases:
  - KB0953191
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0953191
kb_number: KB0953191
last_modified: 2024-05-08
---

## Issue

Use Case where the publisher (norm\_publisher) is <empty> and while performing "Revert Normalization" to enter the value manually throws an error (Publisher not defined) as show in the screenshot below and unable to populate the 'Norm\_publisher' value.

![](/sys_attachment.do?sys_id=455b9fea1becf454a59033f2cd4bcbf9)

## Resolution

1\. Initially change the normalization status of these records to New and nullified the version, publisher, product.

Below is the sample fix script for Product 'Think-Cell' and run it as Fix Script: \[Note:- Backup the records before making any changes\]

  

runIt();

function runIt() {

    var grSDM = new GlideRecord('cmdb\_sam\_sw\_discovery\_model');  
    grSDM.addEncodedQuery("primary\_display\_nameSTARTSWITH**think**\-c^norm\_publisher=NULL^status=normalized^norm\_product=<Sys\_ID of the product>");  
    grSDM.setLimit(25);  
    grSDM.query();  
    gs.log("Count - " + grSDM.getRowCount());  
    while (grSDM.next()) {  
        // grSDM.status = 'new';  
        grSDM.setValue('status', 'new');  
        grSDM.setValue('norm\_product', '');  
        grSDM.setValue('norm\_publisher', '');  
        grSDM.setValue('norm\_version', '');  
        grSDM.update();  
    }  
}

  
  
2\. Now make sure all these records are updated with status as New and publisher, product and version are empty.  
  
3\. Now run the discovery model normalization job as below:

SAM - Discovery Model Normalization  
https://<INSTANCE>.service-now.com/nav\_to.do?uri=sysauto.do?sys\_id=f114f2667f622200fa0d328c4efa91da
