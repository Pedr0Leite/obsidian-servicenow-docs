---
title: "Risks of using an LDAP user for MID Server authentication"
aliases:
  - KB0746247
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746247
kb_number: KB0746247
last_modified: 2026-02-06
---

## Risks of using an LDAP user for MID Server authentication

  

### Issue

Learn about the risks of using an LDAP-synchronized user for MID Server authentication and why this configuration can cause unplanned outages. This article also explains why MID Server passwords must be updated manually and cannot be changed from the instance.

### Release

All supported releases

### Resolution

### How MID Server authentication works

The MID Server initiates a connection with the instance. Only after that connection is established does the MID Server communicate with the instance. This process is similar to an inbound REST or SOAP integration.

The user name and password for the MID Server service account are stored in the `config.xml` file on the MID Server host. These credentials are set during initial installation or updated manually afterward. This is the only way to set the MID Server login password.

The password cannot be updated from the instance because the change would only work if the MID Server were up and communicating with the instance at the time of the change, which is not guaranteed.

### Risks of using LDAP users

Although there is no technical restriction preventing an LDAP-synchronized user from being used for the MID Server, this configuration has caused problems resulting in MID Servers suddenly being unable to authenticate with the instance. When authentication fails, the MID Server immediately goes down.

Common issues include:

**Account lockout or deactivation**

The account may become locked out or inactive in LDAP for reasons unrelated to the MID Server. For example:

-   Another system using the same user name caused a lockout due to too many failed attempts.
-   The password was not reset before a password policy deadline.
-   The User must change password at next logon setting was enabled due to Active Directory password complexity requirements.

**Password changes in LDAP**

When the account password is changed in LDAP, the change is imported to the User \[sys\_user\] table in the instance. However, the MID Server continues to use the password from the `config.xml` file, causing authentication to fail.

This commonly occurs when a user name is shared between multiple integrations, and the MID Servers are forgotten when the password is changed.

**LDAP authentication dependency**

If LDAP authentication is enabled for the MID Server user (in addition to LDAP import for user details), a problem with the LDAP server causes the MID Server to fail authentication and go down—even if there is no issue with the ServiceNow instance, MID Server, or the connection between them.

### How to prevent unplanned MID Server outages

To prevent unplanned MID Server outages that affect integrations, Discovery, and Event Management:

**Create the user directly in the instance**

-   Create the service account in the User \[sys\_user\] table directly and set the password at that time.
-   To verify an existing user was created directly, confirm that the Source field on the user record is empty.

**Avoid LDAP-synchronized users**

-   Do not use an external user that is synchronized to the instance through LDAP.
-   If security requirements mandate using an LDAP password, implement a manual or automated password synchronization tool such as CyberArk. For information about automating the MID Server-side update, see the Related Links section.

**Avoid LDAP authentication for the MID Server user**

-   An LDAP outage causes a MID Server outage.

**Dedicate the user account to MID Server use only**

-   Do not use this user for anything else.
-   Use a user name that clearly indicates it is for MID Server use.
-   Do not allow users to log in from a browser with this user name.
-   Do not run scheduled jobs such as imports as this user.

**Assign only the mid\_server role**

-   Assign only the mid\_server role to this user.
-   Do not assign the admin role. The MID Server user does not require admin privileges.
-   If assigning admin appears to resolve an issue, this is a workaround. The underlying ACL rules should be corrected instead.

**Consider separate users for each MID Server**

-   MID Servers do not have to share the same user.
-   For improved auditing and troubleshooting, and to limit the impact of a single user issue, consider creating a separate user for each MID Server or for each region or MID Server cluster.

### Related Links

[How to update a MID Server password](https://support.servicenow.com/kb_view.do?sysparm_article=KB0746702)
