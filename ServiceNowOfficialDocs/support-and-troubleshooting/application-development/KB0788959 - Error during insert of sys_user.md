---
title: "Error during insert of sys_user "
aliases:
  - KB0788959
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788959
kb_number: KB0788959
last_modified: 2024-04-08
---

## Error during insert of sys\_user

  

### Issue

What is causing the error of importing sys\_user record? The user is active in AD but still showing False in ServiceNow.

### Release

All

### Cause

1.   The sys\_user record already exist in ServiceNow.
2.  When importing the sys\_user record from AD it will be Coalesced by the objectGUID.  The objectGUID (Global Unique Identifier) is a 128 bit hexadecimal value, that helps uniquely identify an object in a forest.
3.  If you look at the objectGUID for the import it will be different from that on the existing sys\_user objectGUID.
4.  Since the objectGUID are different the record will try to be inserted into ServiceNow.  This insert will fail because ServiceNow sys\_user (user\_name) needs to be unique.
5.  ServiceNow will prevent the insertion of the record because the SAMACCOUNTNAME is mapped to the ServiceNow user\_name.  ServiceNow does not allow  duplicate username in sys\_user record.

### Resolution

You can copy the new objectGUID to the existing sys\_user record, or delete the existing sys\_user record.  The next time the AD import runs it will because to create/update the record successfully.
