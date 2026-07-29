---
title: "Certain users are unable to sc_cat_item_producer records in Service Portal "
aliases:
  - KB0688981
tags:
  - servicenow
  - support-kb
  - acl
  - access-control
  - service-portal
  - catalog-item
  - debug-security
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688981
kb_number: KB0688981
last_modified: 2024-04-07
---

## Certain users are unable to sc\_cat\_item\_producer records in Service Portal

  

### Issue

# Symptoms

* * *

Some users are unable to sc\_cat\_item\_producer records in Service Portal 

# Release

* * *

All the available releases

# Cause

* * *

Issue is most likely caused as a result of failing ACLs

# Resolution

* * *

-   Reproduce the issue in sc\_cat\_item\_producer list view with Debug Security turned on
-   View the ACL debug data and check the table level read ACLs that are failing for the sc\_cat\_item\_producer table
-   Re-configure any failing ACLs that are causing this issue to resolve the field visibility

# Additional Information

* * *

[https://docs.servicenow.com/csh?topicname=c\_SessionDebug.html&version=latest](https://docs.servicenow.com/csh?topicname=c_SessionDebug.html&version=latest)

## Related

- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]]
- [[KB0688916 - When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form]] - similar failing-ACL diagnosis pattern
- [[c_AccessControlRulesDebug]] - official docs on debugging ACL rules
- [[access-control-rules]] - official docs on access control rules

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688916 - When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form|When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691976 - The users with SOAP role not able to view the incident table data even though the ACLs return true.|The users with SOAP role not able to view the incident table data even though the ACLs return true.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691989 - Ui ActionButton does not display for a user even when the ACLs and the UI action conditions grant the access to that use|Ui Action/Button does not display for a user even when the ACLs and the UI action conditions grant the access to that user]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0692741 - How to grant or restrict access to the users for the Pop-up view in schedule page (show_schedule.do)|How to grant or restrict access to the users for the Pop-up view in schedule page (show_schedule.do)?]]
