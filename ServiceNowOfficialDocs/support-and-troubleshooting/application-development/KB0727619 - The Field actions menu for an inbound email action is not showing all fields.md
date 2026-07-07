---
title: "The Field actions menu for an inbound email action is not showing all fields"
aliases:
  - KB0727619
tags:
  - servicenow
  - support-kb
  - inbound-email-actions
  - access-control-acl
  - admin-overrides
  - save_as_template
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727619
kb_number: KB0727619
last_modified: 2024-12-05
---

## The Field actions menu for an inbound email action is not showing all fields

  

### Issue

The menu for Field actions in the Action section of an inbound email action is not showing all the expected fields.

  

#   

### Cause

The ACL record for the target table, operation save\_as\_template, does not have the Admin overrides checkbox checked.

### Resolution

1\. Take note of the Target table name for the inbound email action.  
2\. Elevate to the security\_admin role.  
3\. Go to System Security > Access Control (ACL)  
4\. Filter for Name is <targetTableName>.\* and for Operation is save\_as\_template  
<targetTableName> is the system name of the table. For example, if the Target table is Request \[sc\_request\], filter for Name is sc\_request.\*  
5\. Open the matching record.  
6\. If the Admin overrides checkbox is not checked, check it and save the record.

#

## Related

- [[KB0685046 - How the Admin overrides option works in an access control (ACL) rule]] - explains the Admin overrides checkbox referenced in the resolution
- [[KB0696894 - Field actions field is not displaying all available fields to select when incident table is selected as Target table for]] - same symptom, different target table
- [[KB0727612 - Copy inbound email into the Work Notes or Additional Comments field of a target record]] - inbound email action scripting

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0725108 - Facilities Management Nonexistent users replying to emails is not working|Facilities Management: Nonexistent users replying to emails is not working]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0753001 - Some roles are not visible and cannot be exported from the [sys_user_role] list table|Some roles are not  visible and cannot be exported from the [sys_user_role] list table]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0782082 - When 'Admin Overrides' is unchecked and the requirement is to allow a specific roled users (but not admin) to access a f|When 'Admin Overrides' is unchecked and the requirement is to allow a specific roled users (but not admin) to access a field, need to make to use of ACL script.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0816018 - Admin role does not pass an ACL when Admin Overrides is selected|Admin role does not pass an ACL when Admin Overrides is selected]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0696894 - Field actions field is not displaying all available fields to select when incident table is selected as Target table for|Field actions field is not displaying all available fields to select when incident table is selected as Target table for Inbound Email Actions]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0727612 - Copy inbound email into the Work Notes or Additional Comments field of a target record|Copy inbound email into the Work Notes or Additional Comments field of a target record]]
