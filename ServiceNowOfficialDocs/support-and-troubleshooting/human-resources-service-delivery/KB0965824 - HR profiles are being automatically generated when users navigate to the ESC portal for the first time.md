---
title: "HR profiles are being automatically generated when users navigate to the ESC portal for the first time"
aliases:
  - KB0965824
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0965824
kb_number: KB0965824
last_modified: 2026-06-26
---

## HR profiles are being automatically generated when users navigate to the ESC portal for the first time

  

### Issue

HR profiles are being automatically generated when users navigate to the ESC portal for the first time.

### Symptoms

-   An HR profile is created automatically for a user the first time they open the ESC portal.
-   The user did not have an existing HR profile before visiting the portal.

### Release

All releases

### Cause

This is the expected behavior for instances created before the Rome release. Each time a user without an HR profile opens the ESC portal for the first time, an HR profile is created for them. 

The logic responsible for this is in the Header | Footer widget ESC Header: 

[https://<instance-name>.service-now.com/sp\_header\_footer.do?sys\_id=bda7abc623882300fb0c949e27bf6544](https://instance_name.service-now.com/sp_header_footer.do?sys_id=bda7abc623882300fb0c949e27bf6544)   
  
\---

if(new GlidePluginManager().isActive("com.sn\_hr\_core")) {  
data.isHrCoreActive = true;  
  
// HR Profile  
var hrProfileGr = new GlideRecord('sn\_hr\_core\_profile');  
hrProfileGr.addQuery('user', gs.getUserID());  
hrProfileGr.setLimit(1);  
hrProfileGr.query();  
if (!hrProfileGr.next()) {  
hrProfileGr.setValue('user', gs.getUserID());  
hrProfileGr.insert();  
}  
}  
  

### Resolution

Beginning with the Rome release, a new system property is available that controls whether HR profiles are created automatically on the first ESC portal visit. Note that this property is not created automatically on instances that upgrade to Rome or later releases — you must import it manually using the steps below. 

To change this behavior on pre-Rome releases: 

1\. Import the attached system property XML for `sn_hr_core.esc.create_hrprofile.override` and confirm it is set to `false`. Use the following URL to navigate to the property after importing it: [https://<instance-name>.service-now.com/sys\_properties.do?sys\_id=7c7b3883eb172010c7296d3eb552286](https://instance_name.service-now.com/sys_properties.do?sys_id=7c7b3883eb172010c7296d3eb5522863) 

2\. Confirm that the Header | Footer widget ESC Header is at the base system version and is on the latest version: [https://<instance-name>.service-now.com/sp\_header\_footer.do?sys\_id=bda7abc623882300fb0c949e27bf6544](https://instance_name.service-now.com/sp_header_footer.do?sys_id=bda7abc623882300fb0c949e27bf6544) 

3\. Review your Restricted Caller Access (RCA) records and move any invalidated records to the Allowed state: [https://<instance-name>.service-now.com/sys\_restricted\_caller\_access\_list.do?sysparm\_query=status!%3D2%5EORstatus%3DNULL&sysparm\_view=](https://instance_name.service-now.com/sys_restricted_caller_access_list.do?sysparm_query=status!%3D2%5EORstatus%3DNULL&sysparm_view=)
