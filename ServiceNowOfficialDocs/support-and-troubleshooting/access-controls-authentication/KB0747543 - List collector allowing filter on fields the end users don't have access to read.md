---
title: "List collector allowing filter on fields the end users don't have access to read"
aliases:
  - KB0747543
tags:
  - servicenow
  - support-kb
  - acl
  - field-level-acl
  - list-collector
  - text-search
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747543
kb_number: KB0747543
last_modified: 2024-04-07
---

## List collector allowing filter on fields the end users don't have access to read

  

### Issue

# Symptoms

List collector and table list allowing filter on fields the end users don't have access to read

# Release

All releases

# Cause

Expected behavior

# Resolution

This behavior is addressed in PRB1259457 - ACLs do not apply to the search in the list view and in the global text search. Though the PRB address this issue in List. Our development team has deemed this PRB as "working as expected" with the following reason. "Field-level ACLs are evaluated for the display of content, but do not have any impact on the actual text search. Fields with sensitive content can be excluded from being indexed." 

# Additional Information

In the screenshot below. ITIL user is not able to see the value in the SSN field but is able to search and return a value.

![](/sys_attachment.do?sys_id=de0d6062db82b450e515c22305961924)

## Related

- [[KB0727211 - FAQ Can an ACL work on the list view and be bypassed on the related list (or vice versa)]]
- [[KB0749174 - Customization considerations for Access Controls (ACLs)]]
- [[acl-function-fields]] - official docs on field-level ACL behavior

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0712001 - ACL Security Flaw when defining field level ACL, when condition depends on that field while utilizing REST|ACL Security Flaw when defining field level ACL, when condition depends on that field while utilizing REST]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688916 - When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form|When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688981 - Certain users are unable to sc_cat_item_producer records in Service Portal|Certain users are unable to sc_cat_item_producer records in Service Portal ]]
