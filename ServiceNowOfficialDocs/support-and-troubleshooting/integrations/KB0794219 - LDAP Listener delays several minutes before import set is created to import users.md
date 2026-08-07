---
title: "LDAP Listener delays several minutes before import set is created to import users"
aliases:
  - KB0794219
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0794219
kb_number: KB0794219
last_modified: 2024-04-07
---

## LDAP Listener delays several minutes before import set is created to import users

  

### Issue

-   An LDAP Server is configured to use an LDAP Listener
-   The LDAP Listener picks up changes from AD within a few seconds but it is observed that there might be delays of up to 5 minutes between the listener identifying the change and an import set being created

### Cause

-   This duration is controlled by the "Listen interval" (value in minutes) on the LDAP Server record

### Resolution

This duration is normal based on the instance default settings

Changing this value would change the time it takes for records to be imported by the listener

The lower this value, the faster the records brought in by the listener are transformed into the target table.

### Related Links

For more information on the "Listen interval (value in minutes)" property, see our Product Documentation [Define an LDAP Server](https://docs.servicenow.com/csh?topicname=t_DefineAnLDAPServer.html&version=latest "Define an LDAP Server")

Reminder: Please ensure all testing is done on sub-production instances before implementations are done in the Production instance
