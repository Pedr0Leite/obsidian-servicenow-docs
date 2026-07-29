---
title: "Unable to add roles, Insert new a row does not exist."
aliases:
  - KB0749023
tags:
  - servicenow
  - support-kb
  - sys_user_preference
  - list-edit
  - roles
  - acl
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749023
kb_number: KB0749023
last_modified: 2024-04-20
---

## Issue

# Symptoms

Unable to add roles, Insert new a row does not exist.

# Release

All

# Environment

Admin or any users who should be able to create ACL's.

# Cause

User Preference - \[list\_edit\_enable\] set to False 

In the sys\_user\_preference table, for that particular user, **list\_edit\_enable** preference set to **false**

# Resolution

Set this User Preference - \[list\_edit\_enable\] to True or delete.

## Related

- [[KB0743902 - Unable to view all sys_user_preferences records as an Admin, seeing security constraints message]]
- [[KB0749174 - Customization considerations for Access Controls (ACLs)]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691989 - Ui ActionButton does not display for a user even when the ACLs and the UI action conditions grant the access to that use|Ui Action/Button does not display for a user even when the ACLs and the UI action conditions grant the access to that user]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0728016 - A user with a specific role does not have access to a table even when an ACL grants that role the required access|A user with a specific role does not have access to a table even when an ACL grants that role the required access]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0743902 - Unable to view all sys_user_preferences records as an Admin, seeing security constraints message|Unable to view all sys_user_preferences records as an Admin, seeing security constraints message]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0753001 - Some roles are not visible and cannot be exported from the [sys_user_role] list table|Some roles are not  visible and cannot be exported from the [sys_user_role] list table]]
