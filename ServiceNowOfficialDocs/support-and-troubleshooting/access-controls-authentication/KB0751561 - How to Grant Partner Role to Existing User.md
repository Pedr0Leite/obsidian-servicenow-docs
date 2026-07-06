---
title: "How to Grant \"Partner\" Role to Existing User"
aliases:
  - KB0751561
tags:
  - servicenow
  - support-kb
  - roles
  - partner-role
  - hi-service-portal
  - user-administration
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0751561
kb_number: KB0751561
last_modified: 2025-07-15
---

## Issue

This article provides information on giving an existing user the "Partner" role

##### Pre-check:

-   The user must be listed and active in the account to which you are granting access.
-   The administrator with the function partner\_admin may give the partner role.

## Resolution

As member Admin follow the below steps;

1.  Log in to Hi service portal
2.  Click on Manage Accounts
3.  Go to Users List
4.  Search for a user
5.  Once the user finds, click on the user
6.  Go to Roles click on (…) then we can find the Edit roles option, Click on it.
7.  Then you will be navigated to roles list
8.  Select the role "partner" Under collection field and click on (>) then, partner role will be assigned to Roles list.
9.  Click on Save.

**NOTE:** The above process is the same for partner\_admin

The user must be tagged and active in that specific account and submit the request for the partner\_admin role as either the primary contact or the current admin in the partner portal

**NOTE:** Any problems with accessing the partner portal should be reported through email to [partnerops@servicenow.com](mailto:partnerops@servicenow.com)

## Related

- [[KB0753001 - Some roles are not  visible and cannot be exported from the [sys_user_role] list table]] — related role visibility/administration issue on sys_user_role
- [[add-role-to-user]] — official docs on assigning roles to a user record

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0687701 - Admin user is being asked to elevate to admin role after logging in|Admin user is being asked to elevate to \"admin\" role after logging in]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691989 - Ui ActionButton does not display for a user even when the ACLs and the UI action conditions grant the access to that use|Ui Action/Button does not display for a user even when the ACLs and the UI action conditions grant the access to that user]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0694783 - User granted with the list_updater role but can't see the 'Update selected' and 'Update all' Context menu in list|User granted with the list_updater role but can't see the 'Update selected' and 'Update all' Context menu in list]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0715670 - Does not have access to performance_dashboards_main.do blank|Does not have access to performance_dashboards_main.do blank]]
