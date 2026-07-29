---
title: "Multiple Splunk alerts create security incidents with the same short description"
aliases:
  - KB0746818
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746818
kb_number: KB0746818
last_modified: 2023-09-08
---

## Multiple Splunk alerts create security incidents with the same short description

  

### Issue

After downloading and configuring the Splunk app ServiceNow Security Operations Addon, when multiple alerts are triggered in Splunk, multiple security incidents are created on the instance. The multiple security incidents have a short description and/or description that matches the first alert even though in Splunk the values of the fields that map to the short description and/or description are different.

### Release

All releases.

### Cause

On the Splunk app, it's possible that static values are being sent to the ServiceNow instance through the When triggered form, the Correlation Search > Search field, or through the Title and/or Description fields of the Adaptive Response Actions > Create Multiple ServiceNow Security Incidents.

### Resolution

You can enter static default values in the When triggered form.

But, for multiple-incident creation, don't use the When triggered form to do the mapping.  
For dynamic data that you want to map to ServiceNow for multiple security incidents, do the mapping inside the Search field under Correlation Search, using eval.

![](/sys_attachment.do?sys_id=174ba46adb42b450e515c223059619bf)

Sample Search field value:

index=\*  
| eval description=  
"time: " + \_time + "  
date: " + short\_description + "  
subject: " + description + "  
sender: " + host  
| table description

The left side of the assignment operator '=' should match the field name on the ServiceNow staging table, also called the import table. The right side of the assignment operator '=' should be the Splunk field name.

Also, in the Create Multiple ServiceNow Security Incidents section under Adaptive Response Actions, make sure that the Title or Description fields do not have values. If these fields have values, the multiple security incidents on the ServiceNow instance will have a short description (Title) and/or Description matching the first alert.

  

![](/sys_attachment.do?sys_id=9f4ba46adb42b450e515c223059619d0)
