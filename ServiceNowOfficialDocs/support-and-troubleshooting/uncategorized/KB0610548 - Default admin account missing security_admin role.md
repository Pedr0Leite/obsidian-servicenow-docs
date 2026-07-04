---
title: "Default admin account missing security_admin role"
aliases:
  - KB0610548
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0610548
kb_number: KB0610548
last_modified: 2026-03-23
---

## Issue

Restoring a missing security\_admin role or system admin user.

## Resolution

### Restoring a missing security\_admin role from your default admin account

This procedure describes how to check how and when the role was deleted and how to recover the role into your instance.

1.  Log on to your instance as an admin user.
2.  Navigate to **Module System Definition** > **Deleted Records**.
3.  Search in deleted records with the following filter:  
    -   Table name = sys\_user\_has\_role
    -   Payload Contains security\_admin
4.  Open the record.
5.  Click the Payload XML to verify that the user is the default system admin user.
6.  Click **Undelete Record**.

This restores the security\_admin role to the default system admin account.

### Restoring a missing default system admin user

1.  Log on to your instance as an admin user.
2.  Navigate to **Module System Definition** > **Deleted Records**.
3.  Search in deleted records with this filter:  
    -   Table name = sys\_user
    -   Document key = 6816f79cc0a8016401c5a33be04be441
4.  Open the record and undelete the Admin user.
    -   This will recover the user but not all of the cascade deletions.
5.  To recover these deletions, use the following filter:
    -   Payload contains 6816f79cc0a8016401c5a33be04be441
6.  Select all and click **Undelete Records**.

This restores all roles, references, and the system admin user in your instance.

## Additional Information

[Security\_admin role](https://docs.servicenow.com/csh?topicname=security-admin-role.html&version=latest)
