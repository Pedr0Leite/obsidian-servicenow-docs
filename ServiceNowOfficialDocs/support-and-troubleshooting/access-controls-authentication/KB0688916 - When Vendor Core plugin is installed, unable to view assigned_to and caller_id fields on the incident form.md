---
title: "When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form"
aliases:
  - KB0688916
tags:
  - servicenow
  - support-kb
  - acl
  - access-control
  - sys_user
  - incident-management
  - vendor-core
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688916
kb_number: KB0688916
last_modified: 2024-04-07
---

## When Vendor Core plugin is installed, unable to view assigned\_to and caller\_id fields on the incident form

  

### Issue

When Vendor Core plugin is installed, unable to view assigned\_to and caller\_id fields on the incident form or any fields that have reference to a sys\_user record.

### Release

All releases

### Cause

When the Vendor Core plugin is installed, it creates a read ACL on the sys\_user table that enables users with the vendor\_contact role to access the records. If the user does not have any ACL that overrides this one, all the other users (except admins) will not have read access to the sys\_user records.  
  

https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_security\_acl.do?sys\_id=7c1241eaeb2222009403a638a206fe4c

### Resolution

The user will have to either modify the ACL by adding roles or editing the script or deactivate the ACL for other users to see the sys\_user records.

## Related

- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] - field-level ACL evaluation order (table.field vs table.*)
- [[KB0688981 - Certain users are unable to sc_cat_item_producer records in Service Portal ]] - similar plugin-installed ACL regression pattern
- [[access-control-rules]] - official docs on access control rules

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691976 - The users with SOAP role not able to view the incident table data even though the ACLs return true.|The users with SOAP role not able to view the incident table data even though the ACLs return true.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688981 - Certain users are unable to sc_cat_item_producer records in Service Portal|Certain users are unable to sc_cat_item_producer records in Service Portal ]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691989 - Ui ActionButton does not display for a user even when the ACLs and the UI action conditions grant the access to that use|Ui Action/Button does not display for a user even when the ACLs and the UI action conditions grant the access to that user]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0692741 - How to grant or restrict access to the users for the Pop-up view in schedule page (show_schedule.do)|How to grant or restrict access to the users for the Pop-up view in schedule page (show_schedule.do)?]]
