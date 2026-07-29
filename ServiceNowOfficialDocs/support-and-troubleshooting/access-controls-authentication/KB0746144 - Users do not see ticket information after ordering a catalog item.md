---
title: "Users do not see ticket information after ordering a catalog item"
aliases:
  - KB0746144
tags:
  - servicenow
  - support-kb
  - acl
  - business-rule
  - service-catalog
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746144
kb_number: KB0746144
last_modified: 2024-04-07
---

## Users do not see ticket information after ordering a catalog item

  

### Issue

# Symptoms

Users do not see ticket information on the ticket page after ordering a catalog item

# Release

All Supported Releases

# Cause

The user does not have access to the record created. The access can be restricted by a Business Rule or ACL

# Resolution

Find ACL or Business Rule restricting access to the record, Disable or change criteria to provide proper access.

## Related

- [[KB0748114 - Users see a No Matches Found on catalog item variable]]
- [[KB0749174 - Customization considerations for Access Controls (ACLs)]]
- [[c_BusinessRules]] - official docs on business rules

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0748114 - Users see a No Matches Found on catalog item variable|Users see a \"No Matches Found\" on catalog item variable]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688916 - When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form|When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688981 - Certain users are unable to sc_cat_item_producer records in Service Portal|Certain users are unable to sc_cat_item_producer records in Service Portal ]]
