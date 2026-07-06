---
title: "When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation"
aliases:
  - KB0686244
tags:
  - servicenow
  - support-kb
  - acl
  - impersonation
  - rest-api
  - roles
  - security
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0686244
kb_number: KB0686244
last_modified: 2025-03-11
---

## When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation

  

### Issue

When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation

### Release

All releases

### Cause

Missing a required role, snc\_internal, for the RESTAPIProcessor Access Control (ACL) record.

### Resolution

1\. Go to System Security > Access Control (ACL)

2\. Filter for Name is RESTAPIProcessor

3\. Open the matching record

4\. Under the Requires Role related list, if you see a role that has a blank Sys user role, double click the blank value and in the suggestions popup, find and select the snc\_internal role. Click the green checkmark to save the change.

5\. Save the ACL record.

After performing these steps, you should be able to impersonate other users and re-impersonate yourself without getting the error.

## Related

- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]]
- [[KB0691976 - The users with SOAP role not able to view the incident table data even though the ACLs return true.]] - another role-driven API access-control gap
- [[debugging-rest-queries]] - official docs on debugging REST queries and ACL failures
