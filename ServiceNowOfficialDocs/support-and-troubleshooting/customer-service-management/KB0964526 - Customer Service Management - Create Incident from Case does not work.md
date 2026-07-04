---
title: "Customer Service Management  - Create Incident from Case does not work"
aliases:
  - KB0964526
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0964526
kb_number: KB0964526
last_modified: 2026-06-24
---

## Customer Service Management - Create Incident from Case does not work

  

### Issue

  
You have reported an issue with Customer Service Management OOTB function not working:  
  
You are trying to create an incident from a case.  
  
An agent can create an incident from a case by selecting the Create Incident item from the Additional Actions menu.  
  
Incorrect Behavior: Incident is Created but not saved and associated to the Case.  
  
Below Error is seen on Incident record  
Data Policy Exception: The following fields are mandatory: Caller, Assignment group, Description  
  
Expected Behavior:  
1\. When the incident is created:  
2\. The state of the incident is New.  
3\. The incident number is added to the Incident field in the Related Records form section on the Case form.  
4\. An update with the incident record number is added to the Work notes field on the Case form.  
5\. The domain of the incident is mapped to the domain of the case.

### Release

Any

### Cause

  
MOST PROBABLE CAUSE:  
The Incident record cannot be saved to the database as you have mandatory fields (Assignment group, Description) which are mapped OOB to be populated when created from Case.  
  
  
1\. OOB only the below fields are mapped from Case to Incident  
  
Case to Incident field mapping  
Case fields Incident fields  
Short description Short description  
Default impact Impact  
Urgency Urgency  
Contact Caller  
Configuration item (if available) Configuration item  
https://docs.servicenow.com/bundle/quebec-customer-service-management/page/product/customer-service-management/reference/csm-integration-sm-incident.html  
  
2\. The UI action references the below Script Include  
/nav\_to.do?uri=sys\_script\_include.do?sys\_id=0785387187b313003c1c8467a7cb0bc6  
line 48 - 61  
  
createIncidentFromCase: function(caseGr, uiActionHandler) {  
var incGr = new GlideRecord("incident");  
var ep = new GlideScriptedExtensionPoint().getExtensions(ServiceManagementIntegrationConstants.CASE\_INC\_EXTENSION\_POINT);  
//If there is any other new extension instance other than the OOB one, concat them together  
//The extension instance with higher order number would overwrite the one with lower order number  
for(var i = 0; i < ep.length; i ++){  
var point = ep\[i\];  
point.copyFieldsFromCaseToIncident(incGr, caseGr);  
}  
  
var incSysId = incGr.insert();  
caseGr.incident = incSysId;  
caseGr.update();  
gs.addInfoMessage(gs.getMessage("Incident {0} created", incGr.number));  
  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
Line 55 should copy the relevant fields from case to Incident.  
  
However the insert does not happen on line 58 successfully as a result of mandatory fields set at data level "Data Policy Exception:", which means the Incident cannot be saved and associated to the Case record.

### Resolution

  
To resolve your issue  
  
If it is a business requirement to have the fields (Assignment group, Description) as Mandatory on Incident, you will need to ensure you configure the mapping from Case to Incident for these additional fields which need to be populated and saved when Incident is created.  
  
Please reference the documentation below  
\--> https://docs.servicenow.com/bundle/quebec-customer-service-management/page/product/customer-service-management/reference/csm-integration-sm-incident.html  
Using an extension point to map the Incident field  
Customers can create the logic for mapping the Incident field by using the sn\_cs\_sm.CSMIncidentIntegrations extension point.  
  
\--> https://docs.servicenow.com/bundle/quebec-application-development/page/build/applications/concept/extension-points.html
