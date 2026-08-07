---
title: "LDAP Group Import pulling in Users instead of Groups / LDAP Users Import pulling in Groups instead of Users"
aliases:
  - KB0692033
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692033
kb_number: KB0692033
last_modified: 2026-05-04
---

## LDAP Group Import pulling in Users instead of Groups / LDAP Users Import pulling in Groups instead of Users

  

### Issue

A Group or User LDAP import may not populate the correct data into the respective import set tables, e.g. a Group import imports User data or a User import imports Group data to the import set table.

The LDAP OUs all look correct and the data source setup looks correct, but the instance ends up with the wrong data in the import set table defined in the data source.

For example if using a MID Server with the LDAP, after the Group import you may see the User OU filter being applied when the MID Server has the property glide.ldap.debug=true in the agent log:

07/03/18 13:41:30 (669) Worker-Standard:LDAPProbe Worker starting: LDAPProbe source: 1f03694edb03d30079ba5eea4b961966&#13;

07/03/18 13:41:31 (684) Worker-Standard:LDAPProbe LDAP API - LDAPLogger : LDAP Processing RDN OU=Domain Users and range &#13;

07/03/18 13:41:31 (684) Worker-Standard:LDAPProbe DEBUG: LDAP API - LDAP : Requesting attributes : null&#13;

07/03/18 13:41:31 (684) Worker-Standard:LDAPProbe DEBUG: LDAP API - LDAP : Getting results from LDAP server ..&#13;

07/03/18 13:41:31 (700) Worker-Standard:LDAPProbe DEBUG: LDAP API - LDAP : Using RDN : OU=Domain Users,DC=SNC,DC=local and search filter : (&amp;(objectClass=person)(sn=\*)(!(objectClass=computer)))&#13;

07/03/18 13:41:31 (700) Worker-Standard:LDAPProbe DEBUG: LDAP API - LDAP : LDAP paging enabled with 1000 on a page&#13;

07/03/18 13:41:31 (700) Worker-Standard:LDAPProbe DEBUG: LDAP API - LDAP : Using filter : (&amp;(objectClass=person)(sn=\*)(!(objectClass=computer)))&#13;

07/03/18 13:41:32 (184) Worker-Standard:LDAPProbe DEBUG: LDAP API - LDAP : Received results from LDAP server &#13;

07/03/18 13:41:32 (184) Worker-Standard:LDAPProbe DEBUG: LDAP API - LDAPLogger : Recieved LDAP record from server with DN: CN=User\\, User,OU=Domain Users,DC=usr,DC=local&#13;

07/03/18 13:41:32 (184) Worker-Standard:LDAPProbe DEBUG: LDAP API - LDAPLogger : Recieved LDAP record from server with DN: CN=User\\, User,OU=Domain Users,DC=usr,DC=local&#13;  
  

It is expected for the above logging to show the Group OU filter instead, since you are doing a Group import.

### Release

All releases

### Cause

There is a Read ACL on the sys\_data\_source.\* table and the mid server user (or the user running the import if a mid server is not used) does not have the needed Role to have that ACL provide access.

You can see if this is the case by impersonating the importing user in the UI and going to the list view of sys\_data\_source, if you see x number of rows, but no data in any of those rows this is the cause of the issue.

### Resolution

Add the ACL required role to the user doing the import, or create a new Read ACL on sys\_data\_source.\* that has a Role possessed by the importing user.
