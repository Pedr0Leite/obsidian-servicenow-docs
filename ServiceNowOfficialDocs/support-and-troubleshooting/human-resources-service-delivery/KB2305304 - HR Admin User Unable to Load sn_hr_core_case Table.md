---
title: "HR Admin User Unable to Load sn_hr_core_case Table"
aliases:
  - KB2305304
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2305304
kb_number: KB2305304
last_modified: 2025-09-03
---

## HR Admin User Unable to Load sn\_hr\_core\_case Table

  

### Issue

The HR admin user is unable to load data from the HR case (sn\_hr\_core\_case) table. When the user attempts to open the table with all cases, the system times out. However, the user can open the table when using very restrictive filters.   
  

### Release

Washington

### Cause

Corrupted User preference record

### Resolution

1\. Identify the misconfigured user preference record for the impacted user. The record is named 'sn\_hr\_core\_case.db.order' with a value of 'variables.XXXXXXXXX'.  
2\. Remove the identified user preference record from the system. This can be done by accessing the user preference table for the impacted user and deleting the record.  
3\. Verify that the removal of the user preference record resolves the issue by checking the load time for the HR case list.  
  
  

Below is an example of the user preference record with a proper value configured:

![UserPreferenceRecord](/sys_attachment.do?sys_id=a44b0d1d4736ead0f64de825126d43de "User Preference record")
