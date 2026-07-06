---
title: "LDAP group members are not being added even addMembers function existing onAfter transform script"
aliases:
  - KB0792443
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792443
kb_number: KB0792443
last_modified: 2026-06-29
---

## LDAP group members are not being added even addMembers function existing onAfter transform script

  

### Issue

LDAP group members are not being added even if addMembers function exists in the **onAfter** transform script.

### Release

All releases.

### Cause

The group members are not being added with LDAP import even if below checklist is followed for transform scripts :

-   On the Transform map, at least there shall be a field mapping for "sAMAccountName" and "source".
-   The transform script "onStart" with the script of:

gs.include("LDAPUtils");  
var ldapUtils = new LDAPUtils();  
ldapUtils.setLog(log);

-   The transform script "onAfter" script of:

ldapUtils.addMembers(source, target);

### Resolution

Add below function in the transform script , onAfter to make the transform map process all the group members in the group which is being imported:

processgroupmembers();

### Related Links

Please ensure all testing is done on sub-production instances before implemented on a production instance
