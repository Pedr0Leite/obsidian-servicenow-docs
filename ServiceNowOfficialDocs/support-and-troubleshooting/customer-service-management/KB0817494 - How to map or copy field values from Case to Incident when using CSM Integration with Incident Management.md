---
title: "How to map or copy field values from Case to Incident when using CSM Integration with Incident Management"
aliases:
  - KB0817494
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0817494
kb_number: KB0817494
last_modified: 2024-08-06
---

## How to map or copy field values from Case to Incident when using CSM Integration with Incident Management

  

### Issue

When creating a Incident from a Case by clicking on the 'Create Incident' UI action from the context menu, only certain fields are copied across from incident to case, how do you copy across Description and Service (business\_service)

**Steps to Reproduce**

Pre-requisite: Activate the Customer Service with Service Management (com.sn\_cs\_sm') plugin.

1.  Log in to an OOB Instance as SysAdmin.
2.  Create a new Case (sn\_customerservice\_case)  
    -   Populate mandatory fields using any valid contact and account
    -   Populate the Service (business\_service) field with any value.
3.  Save the case  
    -   Use the UI action from the form menu, '**Create Incident**'
4.  Note that the description and Service(business\_service) fields have not copied over

### Cause

This is expected behavior as documented below and is reproducible in OOB Instance [CSM integration with Incident Management](https://docs.servicenow.com/csh?topicname=csm-integration-sm-incident.html&version=latest "CSM integration with Incident Management")

Only the following fields are mapped by default

<table id="csm-integration-sm-incident__table_vvs_g4g_5fb" style="width: 373px; height: 78px;"><tbody><tr style="height: 13px;"><td style="width: 196px; height: 13px;" headers="csm-integration-sm-incident__table_vvs_g4g_5fb__entry__1 "><strong>CASE</strong></td><td style="width: 161px; height: 13px;" headers="csm-integration-sm-incident__table_vvs_g4g_5fb__entry__2 "><strong>INCIDENT</strong></td></tr><tr style="height: 13px;"><td style="width: 196px; height: 13px;" headers="csm-integration-sm-incident__table_vvs_g4g_5fb__entry__1 ">Short description</td><td style="width: 161px; height: 13px;" headers="csm-integration-sm-incident__table_vvs_g4g_5fb__entry__2 ">Short description</td></tr><tr style="height: 13px;"><td style="width: 196px; height: 13px;" headers="csm-integration-sm-incident__table_vvs_g4g_5fb__entry__1 ">Default impact</td><td style="width: 161px; height: 13px;" headers="csm-integration-sm-incident__table_vvs_g4g_5fb__entry__2 ">Impact</td></tr><tr style="height: 13px;"><td style="width: 196px; height: 13px;" headers="csm-integration-sm-incident__table_vvs_g4g_5fb__entry__1 ">Urgency</td><td style="width: 161px; height: 13px;" headers="csm-integration-sm-incident__table_vvs_g4g_5fb__entry__2 ">Urgency</td></tr><tr style="height: 13px;"><td style="width: 196px; height: 13px;" headers="csm-integration-sm-incident__table_vvs_g4g_5fb__entry__1 ">Contact</td><td style="width: 161px; height: 13px;" headers="csm-integration-sm-incident__table_vvs_g4g_5fb__entry__2 ">Caller</td></tr><tr style="height: 13px;"><td style="width: 196px; height: 13px;">Configuration item (if available)</td><td style="width: 161px; height: 13px;">Configuration item</td></tr></tbody></table>

### Resolution

The behavior that you are seeing where Business Service and Description field values from Case are not getting copied across to newly created Incident is expected behavior.

Reproducible on an OOB instance, but you can map the case fields to incident fields within the script includes CSMIncidentIntegrations.

To map the Service (business\_service) and Description field from Case to Incident, do the following:

1.  Log in as Admin, open the 'CSMIncidentIntegrations' script includes file: /nav\_to.do?uri=sys\_script\_include.do?sys\_id=8c5aa43187b313003c1c8467a7cb0b31
2.  Locate the following function within the script includes (roughly line 22):  
    copyFieldsFromCaseToIncident
3.  Scroll to the bottom of the function and add the following 2 lines:  
    
    incGr.business\_service = caseGr.business\_service;  
    incGr.description = caseGr.description; 
    
    What we have done is mapped business\_service and description fields FROM Case to business\_service and description fields TO Incident.
    
4.  Save the record, clear cache if required and test again.

In order to **override** the **Read Only Script Include** as per above, you must edit the **Extension Point** as below:

1.  Open the **Extension Point:**
    1.  https://<instanceName>.service-now.com/nav\_to.do?uri=sys\_extension\_point.do?sys\_id=5e0aa43187b313003c1c8467a7cb0b0f
2.  Override the **Method** as mentioned in the **Above Instructions**
3.  Click the **"Create Implementation" Related Link**
4.  See a **New Script Include** is created which will **override** the **Out Of Box** functionality. Please ensure this is **thoroughly tested** before moving to **Production**.
