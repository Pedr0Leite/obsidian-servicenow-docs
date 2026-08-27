---
title: "Microsoft AZURE provisioning only targets sys_user and optionally sys_group tables"
aliases:
  - KB0655991
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0655991
kb_number: KB0655991
last_modified: 2026-05-04
---

## Microsoft AZURE provisioning only targets sys\_user and optionally sys\_group tables

  

### Issue

Microsoft AZURE does not create records in ServiceNow tables other than sys\_user, or optionally sys\_group. You might want to map other tables like location, company, etc.

### Release

All releases

### Cause

The provisioning service does resolve references between sys\_user records and other ServiceNow tables, but it does not create records in other tables like cmn\_location.

### Resolution

Microsoft Azure provisioning is not a ServiceNow product. Please contact Microsoft for specific questions.  
  
The typical Azure user provisioning flow is as follows:

1.  Azure AD sync service looks up assigned users in scope for provisioning in Azure AD.
2.  If new users have been assigned or otherwise added to the scope since the last sync, the Azure AD sync service queries ServiceNow to see if those users exist.
3.  If a user does not exist in ServiceNow, a new user is created in the sys\_user table.
4.  If a user does exist, then it is updated with any user attributes found to be out of sync.
5.  After the steps above have been completed, the Azure AD sync service queries for any ServiceNow reference attributes specified in the Azure AD sync attribute mappings.
6.  The Azure AD sync service then updates the user record with the reference attribute values.  
       
    If location is configured as one of the target attributes to sync to in the attribute mappings, the sync service should be updating that field.  
       
    The provisioning service does resolve references between a sys\_user record and other ServiceNow tables, but it does not create records in other tables like cmn\_location. 

 **Warning:** When dynamic creation is enabled, entering a nonexistent value in a reference field creates a new record on the referenced table instead of returning an error.
