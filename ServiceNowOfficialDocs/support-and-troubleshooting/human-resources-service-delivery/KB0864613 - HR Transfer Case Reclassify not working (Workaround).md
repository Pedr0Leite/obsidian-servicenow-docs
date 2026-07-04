---
title: "HR Transfer Case Reclassify not working (Workaround)"
aliases:
  - KB0864613
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0864613
kb_number: KB0864613
last_modified: 2025-01-03
---

## HR Transfer Case Reclassify not working (Workaround)

  

### Issue

At ServiceNow we have "Unique" checked on the task table since we want to prevent duplicate numbers. This results in the Reclassify option not working. The "swapNumber"-function (in the hr\_TransferCase script include) of ServiceNow calls the "setNumber"-function twice: - Once to set the new record number on the original record - the second to set the original number on the new record During the execution of this at one time the number is not unique and the unique check prevents this. Doing so results in the improper execution of the swapNumber function. 

Note: This issue is fixed in Quebec.  You can consider the following workaround if you are on releases prior to Quebec.  Test thoroughly in dev/test instance before applying to production.

### Resolution

For a workaround the customer can edit the \`ReclassifyCaseTransfer\` and \`hr\_TransferCase\` to use a temporary number while transferring and avoid a duplicate key issue.  
  
They can add a function \`setNumber\` in \`hr\_TransferCase\`:  
  
setNumber: function (record, value) {  
var lePluginActive = GlidePluginManager.isActive("com.sn\_hr\_lifecycle\_events");  
var leUtils = lePluginActive ? new sn\_hr\_le.hr\_LETransferUtils() : '';  
  
if (lePluginActive && leUtils.isLECase(record))  
leUtils.setNumber(record, value);  
else  
record.number = value;  
},  
  
and call that in \`ReclassifyTransferCase\`, replacing lines 71-87 with:  
  
var originalNumber = String(grCase.number);  
transferUtils.setNumber(grCase, String(newRecord.number));  
  
// Use a temporary number to avoid unique key violation  
var tempNumber = "TEMP00000000";  
transferUtils.setNumber(newRecord, tempNumber);  
newRecord.update();  
  
// Copy transfer-specific fields  
newRecord.transferred\_from = originalRecordSysId;  
grCase.transferred\_to = newRecord.getUniqueValue();  
  
// Cancel original case  
grCase.state = 7;  
  
if (!grCase.update()) {  
gs.addErrorMessage(gs.getMessage("Failed to close original case"));  
return;  
}  
  
// Copy original creation date & number  
newRecord.sys\_created\_on = grCase.sys\_created\_on;  
newRecord.number = originalNumber;  
newRecord.update();
