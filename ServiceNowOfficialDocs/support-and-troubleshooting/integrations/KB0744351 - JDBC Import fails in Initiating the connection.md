---
title: "JDBC Import fails in Initiating the connection"
aliases:
  - KB0744351
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744351
kb_number: KB0744351
last_modified: 2024-01-28
---

## JDBC Import fails in Initiating the connection

  

### Issue

# Symptoms

JDBC Import fails with below Error:

**MID Server reported error: Failed to init the JDBC connection. Check configuration**

# Release

All versions

# Environment

Set up a JDBC Data Source via MID Server with or without specific Application scope which has Application Administration as Active.

# Cause

Configuration issue of scope where it has Application Administration set to true on the sys\_scope record and the ACL issue sys\_data\_source table.

# Resolution

Deactivate 'Application administration' on the sys\_scope record.

OR

If 'Application administration' is required to be Active. We will need to ensure that the READ ACLs against the 'sys\_data\_source' table has the role defined - 'x\_<scope\_name>.user' i.e. whatever is configured on the Application details so that the mid server user can access the sys\_data\_source table.

# Additional Information

Ref Doc: [Access control rules in application administration apps](https://docs.servicenow.com/csh?topicname=ACL-access-checks.html&version=latest "Access control rules in application administration apps")

Check system property: **glide.security.scoped\_administration.honor\_global\_acl** If no scoped ACL rules are defined, application administration apps can inherit global ACL rules. By default, this property is enabled for new and upgraded instances.
