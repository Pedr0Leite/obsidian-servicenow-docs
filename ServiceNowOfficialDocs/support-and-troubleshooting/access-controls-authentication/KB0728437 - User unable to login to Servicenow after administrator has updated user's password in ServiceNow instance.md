---
title: "User unable to login to Servicenow after administrator has updated user's password in ServiceNow instance"
aliases:
  - KB0728437
tags:
  - servicenow
  - support-kb
  - ldap
  - authentication
  - password
  - login
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0728437
kb_number: KB0728437
last_modified: 2024-01-28
---

## Issue

# Symptoms

* * *

After administrator has updated user's password in Servicenow, user is unable to login to Servicenow instance with his new password.

Could observe below error in node log while reproducing the login issue for affected user,

```
2019-03-04 02:49:30 (981) Default-thread-6 F1AB1DACDBC0BF00EFD1F7461D961905 txid=80cc1160db04 WARNING *** WARNING *** LDAP: No user information found in ldap for xxxxxxx2019-03-04 02:49:30 (982) Default-thread-6 F1AB1DACDBC0BF00EFD1F7461D961905 txid=80cc1160db04 WARNING *** WARNING *** LDAP: No DN returned for xxxxxxx2019-03-04 02:49:30 (985) Default-thread-6 F1AB1DACDBC0BF00EFD1F7461D961905 txid=80cc1160db04 Logging event: SNC.Auth.LDAP.Login.Failed with parm1: user_name=xxxxxxx and parm2: ldapconfigsysid=yyyyyyyyyyyyyyyyy
```

# Release

* * *

Any supported release.

# Cause

* * *

There was a LDAP integration set up with sys\_user record and hence source field on the sys\_user record contained LDAP details of the user record. Due to this, updating, the password only in ServiceNow's sys\_user record is not enough, also it should be updated in the corresponding user record in LDAP server.

# Resolution

* * *

When an administrator updates the password in the sys\_user record, he/she needs to update the corresponding user record's password in LDAP server as well.

# Additional Information

* * *

[User Administration](https://docs.servicenow.com/csh?topicname=c_UserAdministration.html&version=latest "User Administration")

## Related

- [[KB0744254 - After user's password has been updated on user record, user is unable to login to instance]] - duplicate/near-identical LDAP password issue
- [[c_LDAPIntegration]] - official docs on LDAP integration
- [[c_LDAPIntegrationTroubleshooting]] - official LDAP integration troubleshooting guide

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0744254 - After user's password has been updated on user record, user is unable to login to instance|After user's password has been updated on user record, user is unable to login to instance]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538787 - Determining if SAML or LDAP is being used in the instance|Determining if SAML or LDAP is being used in the instance]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0715664 - Page not found when logging in through side_door.do|Page not found when logging in through side_door.do]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538763 - Determining if the SAML certificate is incorrect|Determining if the SAML certificate is incorrect]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538765 - Determining if ADFS is receiving a signed request| Determining if ADFS is receiving a signed request]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538768 - Determining if the properties from the source were copied over a target|Determining if the properties from the source were copied over a target]]
