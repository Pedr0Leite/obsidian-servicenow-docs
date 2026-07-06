---
title: "Configuring LDAP Server URL(Primary/Secondary)"
aliases:
  - KB0748771
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748771
kb_number: KB0748771
last_modified: 2024-04-07
---

## Configuring LDAP Server URL(Primary/Secondary)

  

### Issue

# Question

URLs mentioned in the LDAP Server URL work as  'primary server' and a 'backup' server?

# Solution

Yes! The Server URL field, the valid URLs of all servers appear separated by a space. Servers are first ordered by operational status, with servers that are Up listed first, then ordered by the Order value that you specify. The first server listed is the primary LDAP server. The others are redundant servers.

#### **Note :** There is a slight delay between the change in the actual operational status and the display.

#### Alternatively, you can add a redundant LDAP server by navigating to an existing LDAP server record and inserting a row in the LDAP Server URLs embedded list.
