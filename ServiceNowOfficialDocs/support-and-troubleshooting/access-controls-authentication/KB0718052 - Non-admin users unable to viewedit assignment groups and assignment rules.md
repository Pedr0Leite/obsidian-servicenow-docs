---
title: "Non-admin users unable to view/edit assignment groups and assignment rules "
aliases:
  - KB0718052
tags:
  - servicenow
  - support-kb
  - acl
  - assignment-group
  - assignment-rule
  - plugin
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718052
kb_number: KB0718052
last_modified: 2023-08-25
---

## Non-admin users unable to view/edit assignment groups and assignment rules

  

### Issue

# Symptoms

* * *

Non-admin users are not able to view/edit assignment groups and assignment rules as expected .

# Release

* * *

ALL

#   

# Cause

* * *

One of the identified causes of the issue is the use of the plugin SolarWinds Alert Integration which adds some ACLs to the assignment group and assignment rules tables which can impact the behavior of some OOB features.

# Resolution

* * *

If you are facing the symptoms mentioned above, double check if you have the plugin SolarWinds Alert Integration installed in the instance. If so, review all the ACLs added by this plugin in relation to the weird behavior that you are encountering.

## Related

- [[KB0713093 - Assignment Rule is not working - incidents are created without an assignment group]]
- [[KB0749174 - Customization considerations for Access Controls (ACLs)]]
- [[access-control-rules]] - official docs on ACL rule evaluation

#

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688916 - When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form|When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688981 - Certain users are unable to sc_cat_item_producer records in Service Portal|Certain users are unable to sc_cat_item_producer records in Service Portal ]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691976 - The users with SOAP role not able to view the incident table data even though the ACLs return true.|The users with SOAP role not able to view the incident table data even though the ACLs return true.]]
