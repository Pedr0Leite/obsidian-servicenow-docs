---
title: "Service Now Synchronization Issues with Azure attributes - Department field"
aliases:
  - KB0789085
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789085
kb_number: KB0789085
last_modified: 2024-04-08
---

## Service Now Synchronization Issues with Azure attributes - Department field

  

### Issue

After setting up synchronization of user accounts on service now with our Azure Tenant, the sync process is working as expected. provisioning of accounts on service now side is syncing fine, however, some attributes fields on service now side is not Updated. The "department" field of a user on service now side for a user is not getting updated based on attribute mapping on azure provisioning.

### Release

NA

### Cause

\->Actual cause of the issue from Azure perspective :

Tried to create an reference type AAD attribute – failed because reference type attribute no supported in the Azure AD  
  
PS C:\\windows\\system32> New-AzureADApplicationExtensionProperty -ObjectId $MyApp -Name "servicenow-department" -DataType "Reference" -TargetObjects "User"  
  
New-AzureADApplicationExtensionProperty : Error occurred while executing NewApplicationExtensionProperty  
  
Code: Request\_BadRequest  
  
Message: Invalid value specified for property 'dataType' of resource 'ExtensionProperty'.  
  
RequestId: 6773fc59-e189-4410-9afa-322b07730efc  
  
DateTimeStamp: Tue, 19 Nov 2019 06:11:36 GMT  
  
Details: PropertyName - dataType, PropertyErrorCode - InvalidValue  
  
  
1\. Tried to use cref expression function to convert string to reference – failed due to Cref expression function no supported in the Azure AD user provisioning  
  
\[cid:image001.png@01D59EE5.E0B33D00\]  
  
  
Technically speaking, this is not an real issue, it is totally data structure mismatch. As you know, in the ServiceNow side that the department attribute type is reference, in the Azure AD side that the extension attribute is string.  
  
From Microsoft perspective, we recommend to use the same data structure to pass the value.

### Resolution

  
\->Create a column (string) on ServiceNow instance on User table name 'u\_orgunit' . (column name can be anything)

\->Map the column with the attribute on Azure end as below.

![](sys_attachment.do?sys_id=ceced04ddb04b8d066e0a345ca9619ef)

\->Run the full sync from Azure end to see if the values are being populated at ServiceNow end on the OrgUnit column of User's table.

![](sys_attachment.do?sys_id=46ced04ddb04b8d066e0a345ca9619f1)

\->You can see that the data from Azure is sent into User's table and the Department data that Azure is sent to ServiceNow is now populated on orgUnit column of User's table.

  
  
\-> Run the below background script on the users table to sync the data between orgUnit and Dept ( This script is written when there is already some data in DEPT and to sync the data between orgUnit and Dept)

  
var gr1 = new GlideRecord("sys\_user");  
//gr1.addEncodedQuery("orgunitISNOTEMPTY");  
  
//gr1.addEncodedQuery("u\_orgunitISNOTEMPTY");  
  
//gr1.addQuery("name", "value");  
gr1.query();  
gs.print("count : "+gr1.getRowCount());  
while (gr1.next()) {  
  
  
var gr = new GlideRecord('cmn\_department'); //u\_affiliates refers to table name  
gr.addQuery('name',gr1.u\_orgunit.toString());  
gr.query();  
if(gr.next()){  
gr1.department=gr.sys\_id;  
}  
else{  
gr.initialize();  
gr.name=gr1.u\_orgunit.toString();  
gr1.department=gr.insert();  
}  
gs.print(gr1.user\_name);  
gr1.update();  
  
}

  
2) Create an onBefore Business Rule so that any further update on sys\_user table can run the below script from now on: (auto Sync between the columns OrgUnit and DEPT)

\*\*\*\*\*On every update/insert of the record on User's table)\*\*\*\*\*\*  
  
  
(function executeRule(current, previous /\*null when async\*/) {  
  
  
var gr = new GlideRecord('cmn\_department'); //u\_affiliates refers to table name  
gr.addQuery('name',current.u\_orgunit.toString());  
gr.query();  
if(gr.next()){  
current.department=gr.sys\_id;  
}  
else{  
gr.initialize();  
gr.name=current.u\_orgunit.toString();  
current.department=gr.insert();  
  
}  
  
})(current, previous);  
  
  
  
  
  

### Related Links

NA
