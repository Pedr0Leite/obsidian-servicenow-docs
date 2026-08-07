---
title: "LDAP Import of Users or Groups With a Large Number of Records (~100k) May not Return All Records Even If the Filter and LDAP Browse Returns Missing Users/Groups"
aliases:
  - KB0781719
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781719
kb_number: KB0781719
last_modified: 2024-04-08
---

## LDAP Import of Users or Groups With a Large Number of Records (~100k) May not Return All Records Even If the Filter and LDAP Browse Returns Missing Users/Groups

  

### Issue

LDAP import of users or groups with a large number of records (~100k) may not return all records even if the filter and LDAP browse returns the missing Users/Groups when executed from the LDAP server browser.

The LDAP import will complete without errors or warning and appears to be complete from the point of view of the instance.

### Release

Applies to any release.

### Cause

The LDAP server has an LDAP query limit.  See "LDAP query limits" here: [LDAP Integration Requirements](https://docs.servicenow.com/csh?topicname=r_LDAPIntegrationRequirements.html&version=latest "LDAP Integration Requirements")

### Resolution

Setup paging on the LDAP server, see: [Define An LDAP Server](https://docs.servicenow.com/csh?topicname=t_DefineAnLDAPServer.html&version=latest "Define An LDAP Server")

Select the "Paging" check box on the LDAP server record and save the change.
