---
title: "Oracle Named User Plus metric doesn't work for non-DB software. cmdb_sam_sw_install records are left as unlicensed install after reconciliation."
aliases:
  - KB0953148
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0953148
kb_number: KB0953148
last_modified: 2024-01-12
---

## Issue

Oracle Named User Plus metric doesn't work for non-DB software, for example:

-   Oracle Business Intelligence Foundation Suite - Named User Plus Perpetual
-   Oracle Hyperion Interactive Reporting Web Client 

cmdb\_sam\_sw\_install records are left as unlicensed install after reconciliation.

## Resolution

Workaround:

1> Under menu Custom License Metrics, create a new metric "CustomNamedUserPlus"  
  
  
\> Allocation type is Device  
\> Script is below:  
  
getRightsForDevice();  
function getRightsForDevice(){  
var rightsForDevice = -1;  
  
var installs = new SampRecord('cmdb\_sam\_sw\_install');  
installs.addEncodedQuery(encoded\_query\_for\_installs);  
installs.query();  
if (installs.next()) {  
  
var softwareModel = installs.getValue('software\_model');  
var inferredSuite = installs.getValue('inferred\_suite');  
var calSM;  
  
if (!gs.nil(inferredSuite)) {  
calSM = inferredSuite;  
} else {  
calSM = softwareModel;  
}  
  
//gs.log('SAM SM:' + calSM);  
  
var calRecord = new SampRecord('samp\_sw\_client\_access');  
calRecord.addQuery('software\_model', calSM);  
calRecord.addQuery('u\_device', entity);  
calRecord.query();  
if(calRecord.next()){  
rightsForDevice = calRecord.getValue('user\_count');  
}  
}  
return rightsForDevice;  
}  
  
  
2> On dictionary of Client Access (samp\_sw\_client\_access) table, create a new column:  
Type: Reference  
Column Label: Device  
Column Name: u\_device  
Reference: Configuration Item  

  
3> On the non-DB software model:

3.1) Add Client Access keys

\--only need to fill in total user count and device fields

\--one Client Access key for each computer

3.2) On the associated entitlement, change Metric Group type to Custom and picked License Metric 'CustomNamedUserPlus'  
  
3.3) - Optional: Add suite components if needed
