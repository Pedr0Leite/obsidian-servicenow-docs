---
title: "Users can not edit On-Call shifts"
aliases:
  - KB0783335
tags:
  - servicenow
  - support-kb
  - acl
  - express-acl
  - on-call
  - on-call-scheduling
  - rota
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783335
kb_number: KB0783335
last_modified: 2024-04-20
---

## Issue

A user that had both _rota\_manager_ and _rota\_admin_ can not edit the shift members. On the modal popup to edit the members, no user is listed.

## Resolution

In some rare cases we do see conflicting issues with Express ACLs. These are denoted by the field '**Express security**' set to true. You can safely disable this ACL to resolve the behavior.

## Related

- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] — general ACL evaluation background
- [[KB0861944 - On-Call users using default system schedules can cause SLA issues]] — another On-Call scheduling issue
- [[c_OnCallScheduling]] — official docs on On-Call Scheduling configuration and rota roles

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688916 - When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form|When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688981 - Certain users are unable to sc_cat_item_producer records in Service Portal|Certain users are unable to sc_cat_item_producer records in Service Portal ]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691976 - The users with SOAP role not able to view the incident table data even though the ACLs return true.|The users with SOAP role not able to view the incident table data even though the ACLs return true.]]
