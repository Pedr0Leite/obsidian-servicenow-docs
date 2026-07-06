---
title: "After user's password has been updated on user record, user is unable to login to instance"
aliases:
  - KB0744254
tags:
  - servicenow
  - support-kb
  - ldap
  - authentication
  - password
  - login
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744254
kb_number: KB0744254
last_modified: 2024-01-28
---

## After user's password has been updated on user record, user is unable to login to instance

  

### Issue

# Symptoms

-   After admin user updates a password of a user, user is unable to login to the instance.
-   Could observe below error in node log while reproducing the login issue for user whose password was updated by admin user, 

```
2019-03-04 02:49:30 (981) Default-thread-6 F1AB1DACDBC0BF00EFD1F7461D961905 txid=80cc1160db04 WARNING *** WARNING *** LDAP: No user information found in ldap for Shawn_Pillay2019-03-04 02:49:30 (982) Default-thread-6 F1AB1DACDBC0BF00EFD1F7461D961905 txid=80cc1160db04 WARNING *** WARNING *** LDAP: No DN returned for <UserName>2019-03-04 02:49:30 (985) Default-thread-6 F1AB1DACDBC0BF00EFD1F7461D961905 txid=80cc1160db04 Logging event: SNC.Auth.LDAP.Login.Failed with parm1: user_name=<UserName> and parm2: ldapconfigsysid=xxxxxxxxxxxxxxxxxxxxx
```

# Release

Any supported release. 

# Cause

-   LDAP integration was set up on the affected instance
-   Thus when the user authenticates, the system also tries to authenticate at the LDAP level and it fails there since the sys\_user record password was updated only at the instance level.
-   Hence updating the password of the sys\_user record in the instance is not enough.

# Resolution

When you change the password for a user in ServiceNow instance, also update it on LDAP server as well.

# Additional Information

[LDAP Integration](https://docs.servicenow.com/csh?topicname=c_LDAPIntegration.html&version=latest "LDAP Integration")

[User Administration](https://docs.servicenow.com/csh?topicname=c_UserAdministration.html&version=latest "User Administration")

## Related

- [[KB0728437 - User unable to login to Servicenow after administrator has updated user's password in ServiceNow instance]] - duplicate/near-identical LDAP password issue
- [[c_LDAPIntegration]] - official docs on LDAP integration
- [[c_LDAPIntegrationTroubleshooting]] - official LDAP integration troubleshooting guide
