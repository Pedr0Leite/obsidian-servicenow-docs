---
title: "Determining if the LDAP OU definition has changed"
aliases:
  - KB0538642
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538642
kb_number: KB0538642
last_modified: 2024-05-01
---

## Determining if the LDAP OU definition has changed

  

### Issue

Determining if the LDAP OU definition has changed

Problem

* * *

The instance is available but users cannot log in.  

Symptoms

* * *

-   The user or users are unable to log in.
-   The login screen shows an invalid user name or password.

Cause

* * *

If a recent update is made to the configured LDAP OU definition, this may result in an incorrect Full-RDN request, which can exclude users.  

  
Resolution

* * *

1.  Go to the associated LDAP server for the affected user records.
2.  Locate the LDAP OU definition associated with the user.
3.  Consult the LDAP administrator to confirm the value within the RDN column. The value in the RDN can be blank if confirmed that the user DN returns information in the LDAP browser on the instance.
